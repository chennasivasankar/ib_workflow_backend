
from typing import List


class ServiceInterface:
    def get_all_valid_read_permission_roles(self) -> List[str]:
        pass

    def get_all_valid_write_permission_roles(self) -> List[str]:
        pass

    def get_user_role_ids(self, user_id) -> List[str]:
        pass



class RolesService:

    def get_db_roles(self):
        pass

    def get_user_roles(self, user_id):
        pass

    @property
    def interface(self):
        # TODO: should import the interface from ib_iam app for roles validation
        # from ib_iam.app_interfaces import ServiceInterface
        return ServiceInterface()

    def get_all_valid_read_permission_roles(self) -> List[str]:
        valid_read_permission_roles = \
            self.interface.get_all_valid_read_permission_roles()
        return valid_read_permission_roles

    def get_all_valid_write_permission_roles(self) -> List[str]:
        valid_write_permission_roles = \
            self.interface.get_all_valid_write_permission_roles()
        return valid_write_permission_roles

    def get_user_role_ids(self, user_id) -> List[str]:
        user_role_ids = self.interface.get_user_role_ids(user_id)
        return user_role_ids




