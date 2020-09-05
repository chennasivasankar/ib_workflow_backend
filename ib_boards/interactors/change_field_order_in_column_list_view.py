"""
Created on: 04/09/20
Author: Pavankumar Pamuru

"""

from ib_boards.interactors.dtos import ChangeFieldsOrderParameter
from ib_boards.interactors.presenter_interfaces.presenter_interface import \
    FieldsDisplayStatusPresenterInterface, FieldsDisplayOrderPresenterInterface
from ib_boards.interactors.storage_interfaces.storage_interface import \
    StorageInterface


class InvalidFieldDisplayOrder(Exception):
    pass


class ChangeFieldsDisplayOrder:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def change_field_display_order_wrapper(
            self, field_order_parameter: ChangeFieldsOrderParameter,
            presenter: FieldsDisplayOrderPresenterInterface):
        from ib_boards.exceptions.custom_exceptions import \
            FieldIdsNotBelongsToColumn, UserDoNotHaveAccessToColumn, InvalidColumnId
        try:
            field_display_name_dtos, field_display_order_dtos, field_display_status_dtos = \
                self.change_field_display_order(
                    field_order_parameter=field_order_parameter
                )
        except InvalidColumnId:
            return presenter.get_response_for_the_invalid_column_id()
        except UserDoNotHaveAccessToColumn:
            return presenter.get_response_for_user_have_no_access_for_column()
        except FieldIdsNotBelongsToColumn as error:
            return presenter.get_response_for_field_not_belongs_to_column(error=error)
        except InvalidFieldDisplayOrder:
            return presenter.get_response_for_the_invalid_display_order()
        return presenter.get_response_for_field_order_in_column(
            field_display_name_dtos, field_display_order_dtos,
            field_display_status_dtos
        )

    def change_field_display_order(
            self, field_order_parameter: ChangeFieldsOrderParameter):
        self._validate_given_data(field_order_parameter)
        self.storage.change_display_order_of_field(
            field_order_parameter=field_order_parameter
        )
        field_display_status_dtos = self.storage.get_field_display_status_dtos(
            column_id=field_order_parameter.column_id,
            user_id=field_order_parameter.user_id
        )
        field_display_order_dtos = self.storage.get_field_display_order_dtos(
            column_id=field_order_parameter.column_id,
            user_id=field_order_parameter.user_id
        )
        field_ids = [
            field_display_status_dto.field_id
            for field_display_status_dto in field_display_status_dtos
        ]
        from ib_boards.adapters.service_adapter import get_service_adapter
        service_adapter = get_service_adapter()
        field_display_name_dtos = service_adapter.task_service.get_field_display_name(
            field_ids=field_ids
        )
        return field_display_name_dtos, field_display_order_dtos, field_display_status_dtos

    def _validate_given_data(self, field_order_parameter: ChangeFieldsOrderParameter):
        self.storage.validate_column_id(
            column_id=field_order_parameter.column_id
        )
        self._validate_display_order(
            display_order=field_order_parameter.display_order
        )
        project_id = self.storage.get_project_id_for_given_column_id(
            field_order_parameter.column_id
        )
        from ib_boards.adapters.service_adapter import get_service_adapter
        service_adapter = get_service_adapter()
        user_id = field_order_parameter.user_id
        user_role = service_adapter.user_service.get_user_role_ids_based_on_project(
            user_id=user_id, project_id=project_id)
        self.storage.validate_user_role_with_column_roles(
            user_role=user_role,
            column_id=field_order_parameter.column_id
        )
        self._validate_field_ids(
            field_order_parameter=field_order_parameter
        )
        self.storage.validate_field_id_with_column_id(
            column_id=field_order_parameter.column_id,
            field_id=field_order_parameter.field_id
        )

    @staticmethod
    def _validate_display_order(display_order: int):
        if display_order < 0:
            raise InvalidFieldDisplayOrder

    def _validate_field_ids(self, field_order_parameter: ChangeFieldsOrderParameter):
        field_ids = field_order_parameter.field_ids
        if field_order_parameter.field_id not in field_ids:
            field_ids.append(field_order_parameter.field_id)
        valid_field_ids = self.storage.get_valid_field_ids(
            column_id=field_order_parameter.column_id,
            field_ids=field_order_parameter.field_ids
        )
        invalid_field_ids = [
            invalid_field_id
            for invalid_field_id in field_ids
            if invalid_field_id not in valid_field_ids
        ]
        if invalid_field_ids:
            from ib_boards.exceptions.custom_exceptions import \
                FieldIdsNotBelongsToColumn
            raise FieldIdsNotBelongsToColumn(
                invalid_field_ids=invalid_field_ids
            )