from typing import Tuple, List

from ib_tasks.adapters.auth_service import InvalidProjectIdsException, UserIsNotInProject
from ib_tasks.constants.enum import Status
from ib_tasks.exceptions.filter_exceptions import \
    FieldIdsNotBelongsToTemplateId, UserNotHaveAccessToFields, \
    InvalidFilterId, \
    UserNotHaveAccessToFilter, InvalidProjectId
from ib_tasks.interactors.filter_dtos import FilterCompleteDetailsDTO, \
    CreateConditionDTO, CreateFilterDTO, FilterDTO, ConditionDTO, \
    UpdateFilterDTO
from ib_tasks.interactors.mixins.validation_mixin import ValidationMixin
from ib_tasks.interactors.presenter_interfaces.filter_presenter_interface \
    import \
    FilterPresenterInterface
from ib_tasks.interactors.storage_interfaces.fields_storage_interface import FieldsStorageInterface
from ib_tasks.interactors.storage_interfaces.filter_storage_interface \
    import FilterStorageInterface


class FilterInteractor(ValidationMixin):

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
            return self.presenter.get_response_for_invalid_field_ids(error=error)
        except InvalidProjectIdsException as err:
            return self.presenter.get_response_for_invalid_project_id(err=err)
        except UserIsNotInProject:
            return self.presenter.get_response_for_user_not_in_project()
        except UserNotHaveAccessToFields:
            return self.presenter.get_response_for_user_not_have_access_to_fields()
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
            return self.presenter.get_response_for_user_not_have_access_to_update_filter()
        except InvalidTemplateID:
            return self.presenter.get_response_for_invalid_task_template_id()
        except FieldIdsNotBelongsToTemplateId as error:
            return self.presenter.get_response_for_invalid_field_ids(
                error=error)
        except UserNotHaveAccessToFields:
            return self.presenter.get_response_for_user_not_have_access_to_fields()
        return self.presenter.get_response_for_update_filter(
            filter_dto=filter_dto,
            condition_dtos=condition_dtos
        )

    def update_filter(
            self, filter_dto: UpdateFilterDTO,
            condition_dtos: List[CreateConditionDTO]):
        filter_id = filter_dto.filter_id
        user_id = filter_dto.user_id
        self._validate_filter_id(
            filter_id=filter_id
        )
        self._validate_user_with_filter_id(
            filter_id=filter_id, user_id=user_id
        )
        self._validate_filter_data(
            filter_dto=filter_dto,
            condition_dtos=condition_dtos
        )
        filter_dto, condition_dtos = self.filter_storage.update_filter(
            filter_dto=filter_dto, condition_dtos=condition_dtos
        )
        return filter_dto, condition_dtos
        pass

    def delete_filter_wrapper(self, filter_id: int, user_id: str):
        try:
            self.delete_filter(filter_id=filter_id, user_id=user_id)
        except InvalidFilterId:
            return self.presenter.get_response_for_invalid_filter_id()
        except UserNotHaveAccessToFilter:
            return self.presenter.get_response_for_user_not_have_access_to_delete_filter()

    def delete_filter(self, filter_id: int, user_id: str):
        self._validate_filter_id(
            filter_id=filter_id
        )
        self._validate_user_with_filter_id(
            filter_id=filter_id, user_id=user_id
        )
        self.filter_storage.delete_filter(
            filter_id=filter_id, user_id=user_id
        )

    def get_filters_details_wrapper(self, user_id: str, project_id: str):

        try:
            filter_details = self._get_filters_details(
                user_id=user_id, project_id=project_id
            )
        except InvalidProjectIdsException as err:
            return self.presenter.get_response_for_invalid_project_id(err=err)
        except UserIsNotInProject:
            return self.presenter.get_response_for_user_not_in_project()
        return self.presenter.get_response_for_get_filters_details(
            filter_complete_details=filter_details
        )

    def _get_filters_details(self, user_id: str, project_id: str):

        self._validate_project_data(project_id=project_id, user_id=user_id)
        filters_dto = self.filter_storage.get_filters_dto_to_user(
            user_id=user_id, project_id=project_id
        )
        filter_ids = self._get_filter_ids(filters_dto)
        conditions_dto = \
            self.filter_storage.get_conditions_to_filters(filter_ids=filter_ids)
        filter_complete_details_dto = FilterCompleteDetailsDTO(
            filters_dto=filters_dto,
            conditions_dto=conditions_dto
        )
        return filter_complete_details_dto

    def update_filter_select_status_wrapper(
            self, user_id: str, filter_id: int, is_selected: Status):
        from ib_tasks.exceptions.filter_exceptions import InvalidFilterId
        from ib_tasks.exceptions.filter_exceptions \
            import UserNotHaveAccessToFilter
        try:
            response = self.update_filter_select_status(
                user_id=user_id, filter_id=filter_id, is_selected=is_selected
            )
        except InvalidFilterId:
            return self.presenter.get_response_for_invalid_filter_id()
        except UserNotHaveAccessToFilter:
            return self.presenter \
                .get_response_for_invalid_user_to_update_filter_status()
        return self.presenter.get_response_for_update_filter_status(
            filter_id=filter_id, is_selected=response
        )

    def update_filter_select_status(
            self, user_id: str, filter_id: int, is_selected: Status):

        self._validate_filter_id(filter_id=filter_id)
        self._validate_user_with_filter_id(
            user_id=user_id, filter_id=filter_id
        )
        response = self.filter_storage.update_filter_status(
            filter_id=filter_id, is_selected=is_selected
        )
        return response

    def _validate_filter_data(
            self, filter_dto: CreateFilterDTO,
            condition_dtos: List[CreateConditionDTO]):
        template_id = filter_dto.template_id
        field_ids = [condition_dto.field_id for condition_dto in condition_dtos]
        self.filter_storage.validate_template_id(
            template_id=filter_dto.template_id
        )
        valid_field_ids = self.filter_storage.get_field_ids_for_task_template(
            template_id=template_id, field_ids=field_ids
        )
        invalid_field_ids = [
            invalid_field_id for invalid_field_id in field_ids
            if invalid_field_id not in valid_field_ids
        ]
        if invalid_field_ids:
            raise FieldIdsNotBelongsToTemplateId(field_ids=field_ids)
        from ib_tasks.adapters.service_adapter import get_service_adapter
        service_adapter = get_service_adapter()
        user_roles = service_adapter.roles_service.get_user_role_ids(
            user_id=filter_dto.user_id
        )
        self.filter_storage.validate_user_roles_with_field_ids_roles(
            user_roles=user_roles, field_ids=field_ids
        )

    @staticmethod
    def _get_filter_ids(filters_dto: List[FilterDTO]):

        return [
            filter_dto.filter_id
            for filter_dto in filters_dto
        ]

    def _validate_filter_id(self, filter_id: int):
        self.filter_storage.validate_filter_id(
            filter_id=filter_id
        )

    def _validate_user_with_filter_id(self, user_id: str, filter_id: int):
        self.filter_storage.validate_user_with_filter_id(
            user_id=user_id, filter_id=filter_id
        )
