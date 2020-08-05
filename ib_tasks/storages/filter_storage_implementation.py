from typing import List

from ib_tasks.interactors.filter_dtos import FilterDTO, ConditionDTO
from ib_tasks.interactors.storage_interfaces.filter_storage_interface \
    import FilterStorageInterface
from ib_tasks.models import Filter, TaskTemplate, FilterCondition


class FilterStorageImplementation(FilterStorageInterface):

    def get_conditions_to_filters(
            self, filter_ids: List[int]) -> List[ConditionDTO]:
        FilterCondition.objects.filter(filter_id__in=filter_ids)



    def get_filters_dto_to_user(self, user_id: str) -> List[FilterDTO]:
        filter_objs = Filter.objects.filter(created_by=user_id)
        template_ids = [
            filter_obj.template_id
            for filter_obj in filter_objs
        ]
        template_objs = TaskTemplate.objects\
            .filter(template_id__in=template_ids)
        template = {
            template_obj.template_id: template_obj.name
            for template_obj in template_objs
        }
        return [
            FilterDTO(
                filter_id=filter_obj.id,
                filter_name=filter_obj.name,
                user_id=filter_obj.created_by,
                is_selected=filter_obj.is_selected,
                template_id=filter_obj.template_id,
                template_name=template[filter_obj.template_id]
            )
            for filter_obj in filter_objs
        ]