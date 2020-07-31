from typing import List


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

    @staticmethod
    def _get_user_role_ids(user_id: str) -> List[str]:
        from ib_tasks.adapters.roles_service_adapter import \
            get_roles_service_adapter
        roles_service_adapter = get_roles_service_adapter()
        roles_service = roles_service_adapter.roles_service
        user_role_ids = \
            roles_service.get_user_role_ids(user_id=user_id)
        return user_role_ids
