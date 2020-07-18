from typing import List


class ServiceInterface:
    @staticmethod
    def get_all_valid_read_permission_roles():
        return ["ALL_ROLES"]

    @staticmethod
    def get_all_valid_write_permission_roles():
        return ["ALL_ROLES"]


class RolesService:

    @property
    def interface(self):
        # TODO: should import the interface from ib_iam app for roles
        #  validation from ib_iam.app_interfaces import ServiceInterface
        return ServiceInterface()

    def get_all_valid_read_permission_roles(self) -> List[str]:
        valid_read_permission_roles = \
            self.interface.get_all_valid_read_permission_roles()
        return valid_read_permission_roles

    def get_all_valid_write_permission_roles(self) -> List[str]:
        valid_write_permission_roles = \
            self.interface.get_all_valid_write_permission_roles()
        return valid_write_permission_roles
