from typing import List


class ServiceInterface:
    @staticmethod
    def get_valid_role_ids_in_given_role_ids(role_ids: List[str]):
        return ["ALL_ROLES", "Payment Requester", "Payment POC"]


class RolesService:

    @property
    def interface(self):
        # TODO: should import the interface from ib_iam app for roles
        #  validation from ib_iam.app_interfaces import ServiceInterface
        return ServiceInterface()

    def get_valid_role_ids_in_given_role_ids(
            self, role_ids: List[str]
    ) -> List[str]:
        valid_roles = \
            self.interface.get_valid_role_ids_in_given_role_ids(role_ids)
        return valid_roles
