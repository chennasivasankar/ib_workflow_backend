from typing import List

from elasticsearch_dsl import Q, Search, A

from ib_adhoc_tasks.constants.config import TASK_INDEX_NAME
from ib_adhoc_tasks.interactors.dtos.dtos import GroupByDTO, \
    TaskOffsetAndLimitValuesDTO, TaskIdsForGroupsParameterDTO, \
    TaskIdsAndCountDTO, GroupByValueDTO
from ib_adhoc_tasks.interactors.storage_interfaces.dtos import GroupDetailsDTO, \
    GroupCountDTO, ChildGroupCountDTO
from ib_adhoc_tasks.interactors.storage_interfaces.elastic_storage_interface import \
    ElasticStorageInterface


class ElasticStorageImplementation(ElasticStorageInterface):

    def get_task_ids_and_count_dto_based_on_given_groupby_and_pagination_detail(
            self,
            task_ids_for_groups_parameter_dto: TaskIdsForGroupsParameterDTO,
            stage_ids: List[str]
    ) -> TaskIdsAndCountDTO:
        from elasticsearch_dsl import connections
        from django.conf import settings
        connections.create_connection(
            hosts=[settings.ELASTICSEARCH_ENDPOINT], timeout=20
        )
        from ib_adhoc_tasks.constants.config import TASK_INDEX_NAME
        search = Search(index=TASK_INDEX_NAME)
        query = self._get_query_for_project_template_and_stage_ids(
            stage_ids=stage_ids,
            task_ids_for_groups_parameter_dto=task_ids_for_groups_parameter_dto
        )
        for groupby_dto in task_ids_for_groups_parameter_dto.groupby_value_dtos:
            query &= self._get_query_for_given_groupby_field(
                groupby_value_dto=groupby_dto
            )

        task_objects = search.filter(query)
        total_tasks_count = task_objects.count()
        offset = task_ids_for_groups_parameter_dto.offset
        limit = task_ids_for_groups_parameter_dto.limit
        task_ids = [
            task_object.task_id
            for task_object in task_objects[offset: offset + limit]
        ]
        return TaskIdsAndCountDTO(
            task_ids=task_ids,
            total_tasks_count=total_tasks_count
        )

    def _get_query_for_given_groupby_field(
            self, groupby_value_dto: GroupByValueDTO
    ):
        from ib_adhoc_tasks.constants.enum import GroupByType
        if groupby_value_dto.group_by_display_name == GroupByType.ASSIGNEE.value:
            return Q(
                'term',
                assignees__assignee_id__keyword=groupby_value_dto.group_by_value
            )
        elif groupby_value_dto.group_by_display_name == GroupByType.STAGE.value:
            return Q(
                'term',
                stages__stage_id__keyword=groupby_value_dto.group_by_value
            )
        else:
            attribute = groupby_value_dto.group_by_display_name + '.keyword'
            return Q('term', **{attribute: groupby_value_dto.group_by_value})

    def _get_query_for_project_template_and_stage_ids(
            self,
            stage_ids: List[str],
            task_ids_for_groups_parameter_dto: TaskIdsForGroupsParameterDTO
    ):
        query = \
            Q('term',
              project_id__keyword=task_ids_for_groups_parameter_dto.project_id) \
            & Q('term',
                template_id__keyword=task_ids_for_groups_parameter_dto.template_id) \
            & Q('terms', stages__stage_id__keyword=stage_ids)
        return query

    def get_group_details_of_project(
            self, project_id: str, adhoc_template_id: str,
            group_by_dtos: List[GroupByDTO], stage_ids: List[str],
            task_offset_and_limit_values_dto: TaskOffsetAndLimitValuesDTO
    ):
        from elasticsearch_dsl import connections
        from django.conf import settings
        connections.create_connection(hosts=[settings.ELASTICSEARCH_ENDPOINT],
                                      timeout=20)

        query = Q("term", project_id__keyword=project_id) \
                & Q('term', template_id__keyword=adhoc_template_id) \
                & Q('terms', stages__stage_id__keyword=stage_ids)

        search = Search(index=TASK_INDEX_NAME)

        is_grouping_for_order_one = False
        is_grouping_for_order_two = False

        group_agg = ""
        child_agg = ""
        group_by_order_one_dto = ""
        group_by_order_two_dto = ""

        for group_by_dto in group_by_dtos:
            if group_by_dto.order == 1:
                is_grouping_for_order_one = not is_grouping_for_order_one
                group_by_order_one_dto = group_by_dto
                group_agg = self._prepare_aggregation(group_by_dto=group_by_dto)

        for group_by_dto in group_by_dtos:
            if group_by_dto.order == 2:
                is_grouping_for_order_two = not is_grouping_for_order_two
                group_by_order_two_dto = group_by_dto
                child_agg = self._prepare_aggregation(group_by_dto=group_by_dto)

        is_no_group_by_dtos = not group_by_dtos
        if is_no_group_by_dtos:
            group_details_dtos = self._prepare_group_details_dto_for_no_grouping(
                query=query, search=search,
                task_offset_and_limit_values_dto=task_offset_and_limit_values_dto
            )
            return group_details_dtos, [], []

        is_grouping_for_only_order_one = not is_grouping_for_order_two
        if is_grouping_for_only_order_one:
            group_details_dtos, group_count_dto = \
                self._prepare_group_details_dto_for_first_order_grouping(
                    query=query, search=search, group_agg=group_agg,
                    task_offset_and_limit_values_dto=task_offset_and_limit_values_dto,
                    group_by_order_one_dto=group_by_order_one_dto
                )
            return group_details_dtos, group_count_dto, []

        if is_grouping_for_order_two:
            group_details_dtos, group_count_dto, child_group_count_dtos = \
                self._prepare_group_details_dto_for_second_order_grouping(
                    query=query, search=search, group_agg=group_agg,
                    child_agg=child_agg,
                    task_offset_and_limit_values_dto=task_offset_and_limit_values_dto,
                    group_by_order_one_dto=group_by_order_one_dto,
                    group_by_order_two_dto=group_by_order_two_dto
                )
            return group_details_dtos, group_count_dto, child_group_count_dtos
        return

    @staticmethod
    def _prepare_aggregation(group_by_dto: GroupByDTO):
        from ib_adhoc_tasks.constants.enum import GroupByEnum
        group_by_value = group_by_dto.group_by_value
        is_group_by_value_stage = group_by_value == GroupByEnum.STAGE.value
        is_group_by_value_assignee = group_by_value == GroupByEnum.ASSIGNEE.value
        is_group_by_value_other_than_stage_and_assignee = \
            (group_by_value != GroupByEnum.STAGE.value) and (
                    group_by_value != GroupByEnum.STAGE.value)
        group_agg = ""
        if is_group_by_value_stage:
            group_agg = A('terms', field='stages.stage_id.keyword')
        if is_group_by_value_assignee:
            group_agg = A('terms', field='assignees.assignee_id.keyword')
        if is_group_by_value_other_than_stage_and_assignee:
            attribute = group_by_dto.group_by_value + '.keyword'
            group_agg = A('terms', field=attribute)
        return group_agg

    @staticmethod
    def _prepare_group_details_dto_for_no_grouping(
            query, search,
            task_offset_and_limit_values_dto: TaskOffsetAndLimitValuesDTO
    ):
        task_objects = search.filter(query)
        task_ids = []
        offset = task_offset_and_limit_values_dto.offset
        limit = task_offset_and_limit_values_dto.limit
        for task in task_objects[offset: offset + limit]:
            task_ids.append(task.task_id)
        group_details_dto = GroupDetailsDTO(
            task_ids=task_ids,
            total_tasks=task_objects.count()
        )
        group_details_dtos = [group_details_dto]
        return group_details_dtos

    @staticmethod
    def _prepare_group_details_dto_for_first_order_grouping(
            query, search, group_agg,
            task_offset_and_limit_values_dto: TaskOffsetAndLimitValuesDTO,
            group_by_order_one_dto: GroupByDTO
    ):
        tasks_data = A('top_hits')
        search = search.filter(query)
        search.aggs.bucket('groups', group_agg).bucket('tasks', tasks_data)
        response = search.execute()

        total_groups_count = len(response.aggregations.groups.buckets)

        group_offset = group_by_order_one_dto.offset
        group_limit = group_by_order_one_dto.limit
        task_offset = task_offset_and_limit_values_dto.offset
        task_limit = task_offset_and_limit_values_dto.limit

        group_details_dtos = []
        for group in response.aggregations.groups.buckets[
                     group_offset: group_offset + group_limit]:
            task_ids = []

            for task in group.tasks[task_offset: task_offset + task_limit]:
                task_ids.append(task.task_id)

            group_details_dto = GroupDetailsDTO(
                task_ids=task_ids,
                total_tasks=group.doc_count
            )
            group_details_dto.group_by_value = group.key
            group_details_dto.group_by_display_name = group.key
            group_details_dtos.append(group_details_dto)

        return group_details_dtos, total_groups_count

    @staticmethod
    def _prepare_group_details_dto_for_second_order_grouping(
            query, search, group_agg, child_agg,
            task_offset_and_limit_values_dto,
            group_by_order_one_dto, group_by_order_two_dto
    ):
        tasks_data = A('top_hits')
        search.filter(query)
        search.aggs.bucket('groups', group_agg).bucket(
            'child_groups', child_agg
        ).bucket('tasks', tasks_data)
        response = search.execute()
        total_groups_count = len(response.aggregations.groups.buckets)

        task_offset = task_offset_and_limit_values_dto.offset
        task_limit = task_offset_and_limit_values_dto.limit

        group_offset = group_by_order_one_dto.offset
        group_limit = group_by_order_one_dto.limit

        child_group_offset = group_by_order_two_dto.offset
        child_group_limit = group_by_order_two_dto.limit

        child_group_count_dtos = []

        group_details_dtos = []
        for group in response.aggregations.groups.buckets[
                     group_offset: group_offset + group_limit]:
            child_group_count_dto = ChildGroupCountDTO(
                group_by_value=group.key,
                total_child_groups=len(group.child_groups)
            )

            for child_group in group.child_groups[
                               child_group_offset: child_group_offset + child_group_limit]:

                child_group_count_dtos.append(child_group_count_dto)

                task_ids = []
                for task in child_group.tasks[
                            task_offset: task_offset + task_limit]:
                    task_ids.append(task.task_id)
                group_details_dto = GroupDetailsDTO(
                    task_ids=task_ids,
                    total_tasks=child_group.doc_count
                )

                group_details_dto.group_by_value = group.key
                group_details_dto.group_by_display_name = group.key

                group_details_dto.child_group_by_value = child_group.key
                group_details_dto.child_group_by_display_name = child_group.key

                group_details_dtos.append(group_details_dto)

        return group_details_dtos, total_groups_count, child_group_count_dtos
