from typing import List


class UserRoleValidationInteractor:
    def user_role_validation(self, user_id: str, role_ids: List[str]) -> bool:

        from ib_tasks.constants.constants import all_roles_id
        if all_roles_id in role_ids:
            return True

        user_role_ids = self._get_user_role_ids(user_id)
        for user_role_id in user_role_ids:
            if user_role_id in role_ids:
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
