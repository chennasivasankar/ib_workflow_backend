from typing import List


class ServiceInterface:

    @staticmethod
    def get_valid_role_ids_in_given_role_ids(role_ids: List[str]):
        return [
            "ALL_ROLES", "FIN_PAYMENTS_RP", "FIN_ACCOUNTS_LEVEL1_VERIFIER",
            "FIN_FINANCE_RP", "FIN_PAYMENTS_LEVEL1_VERIFIER", "FIN_PAYMENTS_LEVEL2_VERIFIER",
            "FIN_PAYMENTS_LEVEL3_VERIFIER", "FIN_PAYMENTS_RP", "FIN_FINANCE_RP",
            "FIN_ACCOUNTS_LEVEL1_VERIFIER", "FIN_ACCOUNTS_LEVEL2_VERIFIER",
            "FIN_ACCOUNTS_LEVEL3_VERIFIER", "FIN_ACCOUNTS_LEVEL4_VERIFIER", "FIN_ACCOUNTS_LEVEL5_VERIFIER"
        ]

    def get_user_role_ids(self, user_id) -> List[str]:
        pass

class RolesService:

    @property
    def interface(self):
        # TODO: should import the interface from ib_iam app for roles validation
        # from ib_iam.app_interfaces import ServiceInterface
        return ServiceInterface()

    def get_db_roles(self):
        pass
        # TODO: should import the interface from ib_iam app for roles validation
        # from ib_iam.app_interfaces import ServiceInterface
        return ServiceInterface()

    def get_valid_role_ids_in_given_role_ids(self, role_ids: List[str]):
        valid_role_ids = self.interface.get_valid_role_ids_in_given_role_ids(role_ids)
        return valid_role_ids

    def get_user_role_ids(self, user_id) -> List[str]:
        user_role_ids = self.interface.get_user_role_ids(user_id)
        return user_role_ids


