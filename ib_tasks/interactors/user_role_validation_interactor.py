from typing import List

from ib_tasks.interactors.storage_interfaces.fields_storage_interface import \
    FieldsStorageInterface
from ib_tasks.interactors.storage_interfaces.gof_storage_interface import \
    GoFStorageInterface


class UserRoleValidationInteractor:
    def does_user_has_required_permission(self, user_id: str,
                                          role_ids: List[str]) -> bool:

        from ib_tasks.constants.constants import ALL_ROLES_ID
        if ALL_ROLES_ID in role_ids:
            return True

        user_role_ids = self._get_user_role_ids(user_id)
        if set(user_role_ids).intersection(set(role_ids)):
            return True
        return False

    def get_gof_ids_having_read_permission_for_user(
            self, user_id: str, gof_ids: List[str],
            gof_storage: GoFStorageInterface) -> List[str]:

        user_role_ids = self._get_user_role_ids(user_id)
        gof_ids_of_user_with_read_permission = \
            gof_storage.get_gof_ids_having_read_permission_for_user(
                user_roles=user_role_ids, gof_ids=gof_ids)

        return gof_ids_of_user_with_read_permission

    def get_gof_ids_having_write_permission_for_user(
            self, user_id: str, gof_ids: List[str],
            gof_storage: GoFStorageInterface) -> List[str]:

        user_role_ids = self._get_user_role_ids(user_id)
        gof_ids_of_user_with_write_permission = \
            gof_storage.get_gof_ids_having_write_permission_for_user(
                user_roles=user_role_ids, gof_ids=gof_ids)

        return gof_ids_of_user_with_write_permission

    def get_field_ids_having_read_permission_for_user(
            self, user_id: str, field_ids: List[str],
            field_storage: FieldsStorageInterface) -> List[str]:

        user_role_ids = self._get_user_role_ids(user_id)
        field_ids_having_read_permission_for_user = \
            field_storage.get_field_ids_having_read_permission_for_user(
                user_roles=user_role_ids, field_ids=field_ids)

        return field_ids_having_read_permission_for_user

    def get_field_ids_having_write_permission_for_user(
            self, user_id: str, field_ids: List[str],
            field_storage: FieldsStorageInterface) -> List[str]:

        user_role_ids = self._get_user_role_ids(user_id)
        field_ids_having_write_permission_for_user = \
            field_storage.get_field_ids_having_write_permission_for_user(
                user_roles=user_role_ids, field_ids=field_ids)

        return field_ids_having_write_permission_for_user

    def check_is_user_has_read_permission_for_field(
            self, user_id: str, field_id: str,
            field_storage: FieldsStorageInterface) -> bool:

        user_role_ids = self._get_user_role_ids(user_id)
        is_user_has_read_permission = \
            field_storage.check_is_user_has_read_permission_for_field(
                field_id=field_id, user_roles=user_role_ids)
        return is_user_has_read_permission

    def check_is_user_has_write_permission_for_field(
            self, user_id: str, field_id: str,
            field_storage: FieldsStorageInterface) -> bool:

        user_role_ids = self._get_user_role_ids(user_id)
        is_user_has_write_permission = \
            field_storage.check_is_user_has_write_permission_for_field(
                field_id=field_id, user_roles=user_role_ids)
        return is_user_has_write_permission

    @staticmethod
    def _get_user_role_ids(user_id: str) -> List[str]:
        from ib_tasks.adapters.roles_service_adapter import \
            get_roles_service_adapter
        roles_service_adapter = get_roles_service_adapter()
        roles_service = roles_service_adapter.roles_service
        user_role_ids = \
            roles_service.get_user_role_ids(user_id=user_id)
        return user_role_ids
