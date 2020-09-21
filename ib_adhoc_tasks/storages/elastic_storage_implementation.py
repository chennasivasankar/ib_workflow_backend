from typing import List

from elasticsearch_dsl import Q, Search

from ib_adhoc_tasks.interactors.dtos import TaskIdsAndCountDTO, \
    TaskIdsForGroupsParameterDTO
from ib_adhoc_tasks.interactors.storage_interfaces \
    .elastic_storage_interface import ElasticStorageInterface


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
        query = Q('term',
                  project_id__keyword=task_ids_for_groups_parameter_dto.project_id) \
                & Q('term',
                    template_id__keyword=task_ids_for_groups_parameter_dto.template_id) \
                & Q('terms', stages__stage_id__keyword=stage_ids)
        for groupby_dto in task_ids_for_groups_parameter_dto.groupby_value_dtos:
            from ib_adhoc_tasks.constants.enum import GroupByType
            if groupby_dto.group_by_display_name == GroupByType.ASSIGNEE.value:
                query &= Q(
                    'term',
                    assignees__assignee_id__keyword=groupby_dto.group_by_value
                )
            elif groupby_dto.group_by_display_name == GroupByType.STAGE.value:
                query &= Q(
                    'term',
                    stages__stage_id__keyword=groupby_dto.group_by_value
                )
            else:
                attribute = groupby_dto.group_by_display_name + '.keyword'
                query &= Q('term', **{attribute: groupby_dto.group_by_value})

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
