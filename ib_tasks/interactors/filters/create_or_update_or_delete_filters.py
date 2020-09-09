"""
Created on: 03/09/20
Author: Pavankumar Pamuru

"""
from typing import Tuple, List

from ib_tasks.constants.enum import FieldTypes
from ib_tasks.exceptions.adapter_exceptions import InvalidProjectIdsException, \
    UserIsNotInProjectException
from ib_tasks.exceptions.filter_exceptions import \
    FieldIdsNotBelongsToTemplateId, UserNotHaveAccessToFields, \
    InvalidFilterId, \
    UserNotHaveAccessToFilter, InvalidFilterCondition
from ib_tasks.interactors.filter_dtos import CreateConditionDTO, \
    CreateFilterDTO, FilterDTO, ConditionDTO, \
    UpdateFilterDTO
from ib_tasks.interactors.mixins.validation_mixin import ValidationMixin
from ib_tasks.interactors.presenter_interfaces.filter_presenter_interface \
    import \
    FilterPresenterInterface
from ib_tasks.interactors.storage_interfaces.fields_storage_interface import \
    FieldsStorageInterface
from ib_tasks.interactors.storage_interfaces.filter_storage_interface \
    import FilterStorageInterface


class CreateOrUpdateOrDeleteFiltersInteractor(ValidationMixin):

    def __init__(
            self, filter_storage: FilterStorageInterface,
            field_storage: FieldsStorageInterface,
            presenter: FilterPresenterInterface):
        self.presenter = presenter
        self.field_storage = field_storage
        self.filter_storage = filter_storage

    def create_filter_wrapper(
            self, filter_dto: CreateFilterDTO,
            condition_dtos: List[CreateConditionDTO]):
        from ib_tasks.exceptions.filter_exceptions import InvalidTemplateID
        try:
            filter_dto, condition_dtos = self.create_filter(
                filter_dto=filter_dto,
                condition_dtos=condition_dtos
            )
        except InvalidTemplateID:
            return self.presenter.get_response_for_invalid_task_template_id()
        except FieldIdsNotBelongsToTemplateId as error:
            return self.presenter.get_response_for_invalid_field_ids(
                error=error)
        except InvalidProjectIdsException as err:
            return self.presenter.get_response_for_invalid_project_id(err=err)
        except UserIsNotInProjectException:
            return self.presenter.get_response_for_user_not_in_project()
        except InvalidFilterCondition as error:
            return self.presenter.get_response_for_invalid_filter_condition(error=error)
        except UserNotHaveAccessToFields:
            return \
                self.presenter.get_response_for_user_not_have_access_to_fields()
        return self.presenter.get_response_for_create_filter(
            filter_dto=filter_dto,
            condition_dtos=condition_dtos
        )

    def create_filter(
            self, filter_dto: CreateFilterDTO,
            condition_dtos: List[CreateConditionDTO]) \
            -> Tuple[FilterDTO, List[ConditionDTO]]:
        project_id = filter_dto.project_id
        user_id = filter_dto.user_id
        self._validate_project_data(project_id=project_id, user_id=user_id)
        self._validate_filter_data(
            filter_dto=filter_dto,
            condition_dtos=condition_dtos
        )
        field_ids = [condition_dto.field_id for condition_dto in
                     condition_dtos]
        self._validate_user_fields_permission(
            user_id=user_id, project_id=project_id, field_ids=field_ids
        )
        filter_dto, condition_dtos = self.filter_storage.create_filter(
            filter_dto=filter_dto, condition_dtos=condition_dtos
        )
        return filter_dto, condition_dtos

    def _validate_project_data(self, project_id: str, user_id: str):

        self.validate_given_project_ids(project_ids=[project_id])
        self.validate_if_user_is_in_project(
            project_id=project_id, user_id=user_id
        )

    def update_filter_wrapper(
            self, filter_dto: UpdateFilterDTO,
            condition_dtos: List[CreateConditionDTO]):
        from ib_tasks.exceptions.filter_exceptions import InvalidTemplateID
        try:
            filter_dto, condition_dtos = self.update_filter(
                filter_dto=filter_dto,
                condition_dtos=condition_dtos
            )
        except InvalidFilterId:
            return self.presenter.get_response_for_invalid_filter_id()
        except UserNotHaveAccessToFilter:
            return \
                self.presenter.get_response_for_user_not_have_access_to_update_filter()
        except InvalidTemplateID:
            return self.presenter.get_response_for_invalid_task_template_id()
        except FieldIdsNotBelongsToTemplateId as error:
            return self.presenter.get_response_for_invalid_field_ids(
                error=error)
        except InvalidFilterCondition as error:
            return self.presenter.get_response_for_invalid_filter_condition(error=error)
        except UserNotHaveAccessToFields:
            return \
                self.presenter.get_response_for_user_not_have_access_to_fields()
        return self.presenter.get_response_for_update_filter(
            filter_dto=filter_dto,
            condition_dtos=condition_dtos
        )

    def update_filter(
            self, filter_dto: UpdateFilterDTO,
            condition_dtos: List[CreateConditionDTO]):
        filter_id = filter_dto.filter_id
        user_id = filter_dto.user_id
        self.validate_filter_id(filter_id=filter_id)
        self.validate_user_with_filter_id(filter_id=filter_id, user_id=user_id)
        self._validate_filter_data(
            filter_dto=filter_dto,
            condition_dtos=condition_dtos
        )
        project_id = self.filter_storage.get_project_id_to_filter(
            filter_id=filter_id
        )
        field_ids = [condition_dto.field_id for condition_dto in
                     condition_dtos]
        self._validate_user_fields_permission(
            user_id=user_id, project_id=project_id, field_ids=field_ids
        )
        filter_dto, condition_dtos = self.filter_storage.update_filter(
            filter_dto=filter_dto, condition_dtos=condition_dtos
        )
        return filter_dto, condition_dtos

    def delete_filter_wrapper(self, filter_id: int, user_id: str):
        try:
            self.delete_filter(filter_id=filter_id, user_id=user_id)
        except InvalidFilterId:
            return self.presenter.get_response_for_invalid_filter_id()
        except UserNotHaveAccessToFilter:
            return \
                self.presenter.get_response_for_user_not_have_access_to_delete_filter()

    def delete_filter(self, filter_id: int, user_id: str):
        self.validate_filter_id(filter_id=filter_id)
        self.validate_user_with_filter_id(filter_id=filter_id, user_id=user_id)
        self.filter_storage.delete_filter(filter_id=filter_id, user_id=user_id)

    def _validate_filter_data(
            self, filter_dto: CreateFilterDTO,
            condition_dtos: List[CreateConditionDTO]):
        template_id = filter_dto.template_id
        field_ids = [condition_dto.field_id for condition_dto in
                     condition_dtos]

        self.filter_storage.validate_template_id(
            template_id=filter_dto.template_id
        )
        self._validate_conditions_for_values(condition_dtos=condition_dtos)
        valid_field_ids = self.filter_storage.get_field_ids_for_task_template(
            template_id=template_id, field_ids=field_ids
        )
        invalid_field_ids = [
            invalid_field_id for invalid_field_id in field_ids
            if invalid_field_id not in valid_field_ids
        ]
        if invalid_field_ids:
            raise FieldIdsNotBelongsToTemplateId(field_ids=field_ids)

    def _validate_user_fields_permission(self, user_id: str,
                                         field_ids: List[str],
                                         project_id: str):
        from ib_tasks.adapters.service_adapter import get_service_adapter
        service_adapter = get_service_adapter()
        user_roles = service_adapter.roles_service.get_user_role_ids_based_on_project(
            user_id=user_id, project_id=project_id
        )
        self.filter_storage.validate_user_roles_with_field_ids_roles(
            user_roles=user_roles, field_ids=field_ids
        )

    def _validate_conditions_for_values(self, condition_dtos: List[CreateConditionDTO]):
        field_ids = [condition_dto.field_id for condition_dto in
                     condition_dtos]
        field_type_dtos = self.field_storage.get_field_type_dtos(
            field_ids=field_ids)

        field_types_map = {}
        for field_type_dto in field_type_dtos:
            field_types_map[field_type_dto.field_id] = field_type_dto.field_type
        from ib_tasks.constants.constants import NUMERIC_OPERATORS, STRING_OPERATORS
        for condition_dto in condition_dtos:
            field_type = field_types_map[condition_dto.field_id]
            is_invalid_filter_string = field_type != FieldTypes.NUMBER.value \
                                and field_type != FieldTypes.FLOAT.value \
                                and condition_dto.operator in NUMERIC_OPERATORS
            is_invalid_filter = (field_type == FieldTypes.NUMBER.value \
                                or field_type == FieldTypes.FLOAT.value) \
                                and condition_dto.operator in STRING_OPERATORS
            if is_invalid_filter or is_invalid_filter_string:
                raise InvalidFilterCondition(condition=condition_dto.operator)
