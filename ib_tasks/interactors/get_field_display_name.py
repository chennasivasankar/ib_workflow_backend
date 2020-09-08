"""
Created on: 07/09/20
Author: Pavankumar Pamuru

"""
from typing import List

from ib_tasks.interactors.mixins.validation_mixin import ValidationMixin
from ib_tasks.interactors.storage_interfaces.fields_dtos import \
    FieldDisplayNameDTO
from ib_tasks.interactors.storage_interfaces.fields_storage_interface import \
    FieldsStorageInterface


class GetFieldDisplayNamesInteractor(ValidationMixin):
    def __init__(self, field_storage: FieldsStorageInterface):
        self.field_storage = field_storage

    def get_field_display_names(
            self, user_id: str, project_id: str,
            field_ids: List[str]) -> List[FieldDisplayNameDTO]:
        self.validate_given_project_ids(project_ids=[project_id])
        self.validate_if_user_is_in_project(
            project_id=project_id, user_id=user_id
        )
        self.validate_if_user_is_in_project(user_id=user_id,
                                            project_id=project_id)
        self._validate_user_fields_permission(
            user_id=user_id,
            project_id=project_id,
            field_ids=field_ids
        )
        display_name_dtos = self.field_storage.get_field_display_names(
            field_ids=field_ids
        )
        return display_name_dtos

    def _validate_user_fields_permission(self, user_id: str,
                                         field_ids: List[str],
                                         project_id: str):
        from ib_tasks.adapters.service_adapter import get_service_adapter
        service_adapter = get_service_adapter()
        user_roles = service_adapter.roles_service.get_user_role_ids_based_on_project(
            user_id=user_id, project_id=project_id
        )
        self.field_storage.validate_user_roles_with_field_ids_roles(
            user_roles=user_roles, field_ids=field_ids
        )
