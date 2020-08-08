from typing import List, Tuple

from django.db.models import F

from ib_tasks.constants.enum import Status
from ib_tasks.exceptions.filter_exceptions import InvalidTemplateID, \
    InvalidFilterId, UserNotHaveAccessToFilter, UserNotHaveAccessToFields
from ib_tasks.interactors.filter_dtos import FilterDTO, ConditionDTO, \
    CreateFilterDTO, CreateConditionDTO, UpdateFilterDTO
from ib_tasks.interactors.storage_interfaces.filter_storage_interface \
    import FilterStorageInterface
from ib_tasks.models import Filter, TaskTemplate, FilterCondition, FieldRole, \
    TaskTemplateGoFs, Field


class FilterStorageImplementation(FilterStorageInterface):

    def enable_filter_status(self, filter_id: int) -> Status:

        filter_obj = Filter.objects.get(id=filter_id)
        filter_obj.is_selected = Status.ENABLED.value
        filter_obj.save()
        return filter_obj.is_selected

    def disable_filter_status(self, filter_id: int) -> Status:

        filter_obj = Filter.objects.get(id=filter_id)
        filter_obj.is_selected = Status.DISABLED.value
        filter_obj.save()
        return filter_obj.is_selected

    def get_conditions_to_filters(
            self, filter_ids: List[int]) -> List[ConditionDTO]:
        condition_objs = FilterCondition.objects.filter(
            filter_id__in=filter_ids) \
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
        filter_objs = Filter.objects.filter(created_by=user_id) \
            .annotate(template_name=F('template__name'))
        return self._get_filter_dtos(filter_objs=filter_objs)

    @staticmethod
    def _get_filter_dtos(filter_objs: List[Filter]) -> List[FilterDTO]:
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

    def validate_template_id(self, template_id: str):
        invalid_task_template_id = not TaskTemplate.objects.filter(
            template_id=template_id
        ).exists()
        if invalid_task_template_id:
            raise InvalidTemplateID

    def get_field_ids_for_task_template(
            self, template_id: str, field_ids: List[int]) -> List[int]:
        gof_ids = list(TaskTemplateGoFs.objects.filter(
            task_template_id=template_id
        ).values_list('gof_id', flat=True))

        valid_field_ids = Field.objects.filter(
            gof_id__in=gof_ids
        ).values_list('field_id', flat=True)
        return list(valid_field_ids)

    def validate_user_roles_with_field_ids_roles(
            self, user_roles, field_ids):
        fields_user_roles = FieldRole.objects.values_list(
            'role', flat=True
        ).filter(field_id__in=field_ids)
        user_roles = sorted(list(set(user_roles)))
        from ib_tasks.constants.constants import ALL_ROLES_ID
        updated_user_role = user_roles + [ALL_ROLES_ID]
        fields_user_roles = sorted(list(set(fields_user_roles)))
        invalid_user = not (updated_user_role == fields_user_roles \
                            or set(fields_user_roles).issubset(set(updated_user_role)))
        if invalid_user:
            raise UserNotHaveAccessToFields

    def create_filter(
            self, filter_dto: CreateFilterDTO,
            condition_dtos: List[CreateConditionDTO]) \
            -> Tuple[FilterDTO, List[ConditionDTO]]:
        filter_object = Filter.objects.create(
            created_by=filter_dto.user_id,
            name=filter_dto.filter_name,
            template_id=filter_dto.template_id
        )
        self._create_filter_conditions(
            condition_dtos=condition_dtos,
            filter_id=filter_object.id
        )
        filter_objects = Filter.objects.filter(id=filter_object.id) \
            .annotate(template_name=F('template__name'))
        filter_dto = self._get_filter_dtos(filter_objs=filter_objects)[0]
        condition_dtos = self.get_conditions_to_filters(
            filter_ids=[filter_object.id]
        )
        return filter_dto, condition_dtos

    def update_filter(
            self, filter_dto: UpdateFilterDTO,
            condition_dtos: List[CreateConditionDTO]) \
            -> Tuple[FilterDTO, List[ConditionDTO]]:
        filter_object = Filter.objects.get(id=filter_dto.filter_id)
        self._update_filter_object(
            filter_object=filter_object, filter_dto=filter_dto
        )
        self._update_filter_conditions(
            condition_dtos=condition_dtos, filter_id=filter_object.id
        )
        filter_objects = Filter.objects.filter(id=filter_object.id) \
            .annotate(template_name=F('template__name'))
        filter_dto = self._get_filter_dtos(filter_objs=filter_objects)[0]
        condition_dtos = self.get_conditions_to_filters(
            filter_ids=[filter_object.id]
        )
        return filter_dto, condition_dtos

    def validate_filter_id(self, filter_id: int):
        invalid_filter_id = not Filter.objects.filter(
            id=filter_id
        ).exists()
        if invalid_filter_id:
            raise InvalidFilterId()

    def validate_user_with_filter_id(self, user_id: str, filter_id: int):
        invalid_user = not Filter.objects.filter(
            id=filter_id, created_by=user_id
        ).exists()
        if invalid_user:
            raise UserNotHaveAccessToFilter()

    def delete_filter(self, filter_id: int, user_id: str):
        Filter.objects.get(id=filter_id).delete()

    @staticmethod
    def _create_filter_conditions(
            condition_dtos: List[CreateConditionDTO], filter_id: int):
        condition_objects = [
            FilterCondition(
                filter_id=filter_id,
                field_id=condition_dto.field_id,
                operator=condition_dto.operator,
                value=condition_dto.value
            )
            for condition_dto in condition_dtos
        ]
        FilterCondition.objects.bulk_create(condition_objects)

    @staticmethod
    def _update_filter_object(
            filter_object: Filter, filter_dto: UpdateFilterDTO):
        filter_object.name = filter_dto.filter_name
        filter_object.template_id = filter_dto.template_id
        filter_object.save()

    # TODO: need to update function with condition_id
    def _update_filter_conditions(
            self, condition_dtos: List[CreateConditionDTO], filter_id: int):
        condition_objects = FilterCondition.objects.filter(
            filter_id=filter_id
        ).delete()
        self._create_filter_conditions(
            condition_dtos=condition_dtos,
            filter_id=filter_id
        )
