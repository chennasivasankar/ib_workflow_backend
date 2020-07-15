from typing import List

class ServiceInterface:
    def get_all_valid_read_permission_roles(self):
        pass

    def get_all_valid_write_permission_roles(self):
        pass


class RolesService:

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
