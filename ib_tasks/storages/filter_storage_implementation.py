from typing import List
from django.db.models import F
from ib_tasks.interactors.filter_dtos import FilterDTO, ConditionDTO
from ib_tasks.interactors.storage_interfaces.filter_storage_interface \
    import FilterStorageInterface
from ib_tasks.models import Filter, TaskTemplate, FilterCondition


class FilterStorageImplementation(FilterStorageInterface):

    def get_conditions_to_filters(
            self, filter_ids: List[int]) -> List[ConditionDTO]:
        condition_objs = FilterCondition.objects.filter(filter_id__in=filter_ids)\
            .annotate(field_name=F('field__display_name'))
        return [
            ConditionDTO(
                filter_id=condition_obj.filter_id,
                condition_id=condition_obj.id,
                field_id=condition_obj.field_id,
                field_name=condition_obj.field_name,
                operator=condition_obj.operator,
                value=condition_obj.value
            )
            for condition_obj in condition_objs
        ]

    def get_filters_dto_to_user(self, user_id: str) -> List[FilterDTO]:
        filter_objs = Filter.objects.filter(created_by=user_id)\
            .annotate(template_name=F('template__name'))
        return [
            FilterDTO(
                filter_id=filter_obj.id,
                filter_name=filter_obj.name,
                user_id=filter_obj.created_by,
                is_selected=filter_obj.is_selected,
                template_id=filter_obj.template_id,
                template_name=filter_obj.template_name
            )
            for filter_obj in filter_objs
        ]