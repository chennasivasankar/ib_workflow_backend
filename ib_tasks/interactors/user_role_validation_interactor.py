from typing import List

from ib_tasks.interactors.storage_interfaces.action_storage_interface import \
    ActionStorageInterface
from ib_tasks.interactors.storage_interfaces.fields_storage_interface import \
    FieldsStorageInterface
from ib_tasks.interactors.storage_interfaces.gof_storage_interface import \
    GoFStorageInterface
from ib_tasks.interactors.storage_interfaces.stages_storage_interface import \
    StageStorageInterface


class UserRoleValidationInteractor:
    def does_user_has_required_permission(self, user_id: str,
                                          role_ids: List[str],
                                          project_id: str) -> bool:

        from ib_tasks.constants.constants import ALL_ROLES_ID
        if ALL_ROLES_ID in role_ids:
            return True

        user_role_ids = self._get_user_role_ids_based_on_project(
            user_id=user_id, project_id=project_id)
        if set(user_role_ids).intersection(set(role_ids)):
            return True
        return False

    @staticmethod
    def get_gof_ids_having_read_permission_for_user(
            user_roles: List[str], gof_ids: List[str],
            gof_storage: GoFStorageInterface) -> List[str]:

        gof_ids_of_user_with_read_permission = \
            gof_storage.get_gof_ids_having_read_permission_for_user(
                user_roles=user_roles, gof_ids=gof_ids)

        return gof_ids_of_user_with_read_permission

    @staticmethod
    def get_gof_ids_having_write_permission_for_user(
            user_roles: List[str], gof_ids: List[str],
            gof_storage: GoFStorageInterface) -> List[str]:

        gof_ids_of_user_with_write_permission = \
            gof_storage.get_gof_ids_having_write_permission_for_user(
                user_roles=user_roles, gof_ids=gof_ids)

        return gof_ids_of_user_with_write_permission

    @staticmethod
    def get_field_ids_having_read_permission_for_user(
            user_roles: List[str], field_ids: List[str],
            field_storage: FieldsStorageInterface) -> List[str]:

        field_ids_having_read_permission_for_user = \
            field_storage.get_field_ids_having_read_permission_for_user(
                user_roles=user_roles, field_ids=field_ids)

        return field_ids_having_read_permission_for_user

    @staticmethod
    def get_field_ids_having_write_permission_for_user(
            user_roles: List[str], field_ids: List[str],
            field_storage: FieldsStorageInterface) -> List[str]:

        field_ids_having_write_permission_for_user = \
            field_storage.get_field_ids_having_write_permission_for_user(
                user_roles=user_roles, field_ids=field_ids)

        return field_ids_having_write_permission_for_user

    @staticmethod
    def check_is_user_has_read_permission_for_field(
            user_roles: List[str], field_id: str,
            field_storage: FieldsStorageInterface) -> bool:

        is_user_has_read_permission = \
            field_storage.check_is_user_has_read_permission_for_field(
                field_id=field_id, user_roles=user_roles)
        return is_user_has_read_permission

    @staticmethod
    def check_is_user_has_write_permission_for_field(
            user_roles: List[str], field_id: str,
            field_storage: FieldsStorageInterface) -> bool:

        is_user_has_write_permission = \
            field_storage.check_is_user_has_write_permission_for_field(
                field_id=field_id, user_roles=user_roles)
        return is_user_has_write_permission

    def get_permitted_stage_ids_given_user_id(
            self, user_id: str,
            project_id: str,
            stage_storage: StageStorageInterface) -> List[str]:
        user_role_ids = self._get_user_role_ids(user_id)
        permitted_stage_ids = stage_storage.get_permitted_stage_ids(
            user_role_ids, project_id
        )
        return permitted_stage_ids

    def get_permitted_action_ids_for_given_user_id(
            self, stage_ids: List[str],
            user_id: str,
            action_storage: ActionStorageInterface) -> List[int]:
        user_role_ids = self._get_user_role_ids(user_id)
        permitted_action_ids = \
            action_storage.get_permitted_action_ids_given_stage_ids(
                user_role_ids, stage_ids)
        return permitted_action_ids

    @staticmethod
    def _get_user_role_ids(user_id: str) -> List[str]:
        from ib_tasks.adapters.roles_service_adapter import \
            get_roles_service_adapter
        roles_service_adapter = get_roles_service_adapter()
        roles_service = roles_service_adapter.roles_service
        user_role_ids = \
            roles_service.get_user_role_ids(user_id=user_id)
        return user_role_ids

    @staticmethod
    def _get_user_role_ids_based_on_project(
            user_id: str, project_id: str) -> List[str]:
        from ib_tasks.adapters.roles_service_adapter import \
            get_roles_service_adapter
        roles_service_adapter = get_roles_service_adapter()
        roles_service = roles_service_adapter.roles_service
        user_role_ids = \
            roles_service.get_user_role_ids_based_on_project(
                user_id=user_id, project_id=project_id)
        return user_role_ids
