
from typing import List


class ServiceInterface:
    def get_all_valid_read_permission_roles(self) -> List[str]:
        pass

    def get_all_valid_write_permission_roles(self) -> List[str]:
        pass

    def get_user_role_ids(self, user_id) -> List[str]:
        pass

class RolesService:

    @property
    def interface(self):
        # from ib_iam.interfaces.service_interface import ServiceInterface
        # return ServiceInterface()
        pass

    def get_db_roles(self):
        pass
        # TODO: should import the interface from ib_iam app for roles validation
        # from ib_iam.app_interfaces import ServiceInterface
        return ServiceInterface()

