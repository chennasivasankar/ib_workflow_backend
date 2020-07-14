from typing import List


class RolesService:

    @property
    def interface(self):
        # from ib_iam.app_interfaces import ServiceInterface
        # return ServiceInterface()
        pass

    def get_all_valid_read_permission_roles(self) -> List[str]:
        valid_read_permission_roles = \
            self.interface.get_all_valid_read_permission_roles()
        return valid_read_permission_roles

    def get_all_valid_write_permission_roles(self) -> List[str]:
        valid_write_permission_roles = \
            self.interface.get_all_valid_write_permission_roles()
        return valid_write_permission_roles

    def check_read_permission_roles_and_return_invalid_roles(
            self, read_permission_roles: List[str]
    ) -> List[str]:
        invalid_read_permission_roles = \
            self.interface.check_read_permission_roles_and_return_invalid_roles(
                read_permission_roles=read_permission_roles
            )
        return invalid_read_permission_roles

    def check_write_permission_roles_and_return_invalid_roles(
            self, write_permission_roles: List[str]
    ) -> List[str]:
        invalid_write_permission_roles = \
            self.interface.check_read_permission_roles_and_return_invalid_roles(
                write_permission_roles=write_permission_roles
            )
        return invalid_write_permission_roles
