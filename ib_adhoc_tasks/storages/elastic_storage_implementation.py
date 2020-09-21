from typing import List

from elasticsearch_dsl import Q, Search, A

from ib_adhoc_tasks.constants.config import TASK_INDEX_NAME
from ib_adhoc_tasks.interactors.dtos.dtos import GroupByDTO, \
    TaskOffsetAndLimitValuesDTO
from ib_adhoc_tasks.interactors.storage_interfaces.dtos import GroupDetailsDTO
from ib_adhoc_tasks.interactors.storage_interfaces.elastic_storage_interface import \
    ElasticStorageInterface


class ElasticStorageImplementation(ElasticStorageInterface):

    def get_group_details_of_project(
            self, project_id: str, adhoc_template_id: str,
            group_by_dtos: List[GroupByDTO],
            task_offset_and_limit_values_dto: TaskOffsetAndLimitValuesDTO
    ) -> List[GroupDetailsDTO]:
        # TODO: if group_by_dtos empty return all tasks

        from elasticsearch_dsl import connections
        from django.conf import settings
        connections.create_connection(hosts=[settings.ELASTICSEARCH_ENDPOINT],
                                      timeout=20)

        query = Q("term", project_id__keyword=project_id) \
                & Q('term', template_id__keyword=adhoc_template_id)

        search = Search(index=TASK_INDEX_NAME)

        is_grouping_for_order_one = False
        is_grouping_for_order_two = False

        for group_by_dto in group_by_dtos:
            is_grouping_for_order_one = True
            if group_by_dto.order == 1:
                group_by_order_one_dto = group_by_dto
                group_agg = self._prepare_aggregation(group_by_dto=group_by_dto)

        for group_by_dto in group_by_dtos:
            is_grouping_for_order_two = True
            if group_by_dto.order == 2:
                group_by_order_two_dto = group_by_dto
                child_agg = self._prepare_aggregation(group_by_dto=group_by_dto)

        tasks_data = A('top_hits')
        is_no_group_by_dtos = not group_by_dtos
        if is_no_group_by_dtos:
            group_details_dto = self._prepare_group_details_dto_for_no_grouping(
                query=query, search=search,
                task_offset_and_limit_values_dto=task_offset_and_limit_values_dto
            )

        is_grouping_for_only_order_one = not is_grouping_for_order_two
        if is_grouping_for_order_one:
            group_details_dto = self._prepare_group_details_dto_for_first_order_grouping(
                query=query, search=search, group_agg=group_agg,
                task_offset_and_limit_values_dto=task_offset_and_limit_values_dto,
                group_by_order_one_dto=group_by_order_one_dto
            )

        search.aggs.bucket('groups', group_agg).bucket('child_groups',
                                                       child_agg).bucket(
            'tasks', tasks_data)

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
        return group_details_dto

    def _prepare_group_details_dto_for_first_order_grouping(
            self, query, search, group_agg,
            task_offset_and_limit_values_dto: TaskOffsetAndLimitValuesDTO,
            group_by_order_one_dto: GroupByDTO
    ):
        tasks_data = A('top_hits')
        search.filter(query)
        search.buckets('groups', group_agg).bucket('tasks', tasks_data)
        response = search.execute()
        from ib_adhoc_tasks.constants.enum import GroupByEnum
        group_by_value = group_by_order_one_dto.group_by_value
        is_group_by_value_is_field = (GroupByEnum.STAGE != group_by_value) and (GroupByEnum.STAGE != group_by_value)
        total_groups_count = len(response.aggregations.groups.buckets)

        group_offset = group_by_order_one_dto.offset
        group_limit = group_by_order_one_dto.limit
        task_offset = task_offset_and_limit_values_dto.offset
        task_limit = task_offset_and_limit_values_dto.limit
        group_details_dtos = []
        for group in response.aggregations.groups.buckets[group_offset: group_offset+group_limit]:
            task_ids = []
            for task in group.tasks[task_offset: task_offset+task_limit]:
                task_ids.append(task.task_id)
            group_details_dto = GroupDetailsDTO(
                task_ids=task_ids,
                total_tasks=group.doc_count
            )
            group_details_dto.group_by_value =
            if is_group_by_value_is_field:
                group_details_dto.group_by_display_name = group.key

