"""
Created on: 04/09/20
Author: Pavankumar Pamuru

"""
from dataclasses import dataclass

from ib_boards.constants.enum import DisplayStatus
from ib_boards.interactors.presenter_interfaces.presenter_interface import \
    FieldsDisplayStatusPresenterInterface
from ib_boards.interactors.storage_interfaces.storage_interface import \
    StorageInterface


@dataclass
class ChangeFieldsOrderParameter:
    user_id: str
    column_id: str
    field_id: str
    display_status: DisplayStatus


class ChangeFieldsDisplayStatus:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def change_field_display_status_wrapper(
            self, field_order_parameter: ChangeFieldsOrderParameter,
            presenter: FieldsDisplayStatusPresenterInterface):
        from ib_boards.exceptions.custom_exceptions import \
            FieldNotBelongsToColumn, UserDoNotHaveAccessToColumn, InvalidColumnId
        try:
            self.change_field_display_status(
                field_order_parameter=field_order_parameter
            )
        except InvalidColumnId:
            return presenter.get_response_for_the_invalid_column_id()
        except UserDoNotHaveAccessToColumn:
            return presenter.get_response_for_user_have_no_access_for_column()
        except FieldNotBelongsToColumn:
            return presenter.get_response_for_field_not_belongs_to_column()

    def change_field_display_status(
            self, field_order_parameter: ChangeFieldsOrderParameter):
        self.storage.validate_column_id(
            column_id=field_order_parameter.column_id
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
        self.storage.validate_field_id_with_column_id(
            column_id=field_order_parameter.column_id,
            field_id=field_order_parameter.field_id
        )
        self.storage.change_display_status_of_field(
            column_id=field_order_parameter.column_id,
            user_id=field_order_parameter.user_id,
            field_id=field_order_parameter.field_id
        )
