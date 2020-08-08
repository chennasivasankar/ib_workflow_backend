from typing import List


class RolesService:

    @property
    def interface(self):
        from ib_iam.app_interfaces.service_interface import ServiceInterface
        return ServiceInterface()

    def get_db_roles(self):
        # TODO: call service interface
        return ['FIN_PAYMENT_APPROVER', 'FIN_FINANCE_RP',
                'FIN_ACCOUNTS_LEVEL4_VERIFIER', 'FIN_PAYMENTS_RP']

    def get_user_roles(self, user_id):
        pass

    def get_valid_role_ids_in_given_role_ids(
            self, role_ids: List[str]
    ) -> List[str]:
        valid_roles = \
            self.interface.get_valid_role_ids(role_ids)
        return valid_roles

    def get_user_role_ids(self, user_id) -> List[str]:
        return ['ALL_ROLES', 'FIN_PAYMENT_REQUESTER', 'FIN_PAYMENT_POC',
                'FIN_PAYMENT_APPROVER', 'FIN_COMPLIANCE_VERIFIER',
                'FIN_COMPLIANCE_APPROVER', 'FIN_PAYMENTS_LEVEL1_VERIFIER',
                'FIN_PAYMENTS_LEVEL2_VERIFIER', 'FIN_PAYMENTS_LEVEL3_VERIFIER',
                'FIN_PAYMENTS_RP', 'FIN_FINANCE_RP',
                'FIN_ACCOUNTS_LEVEL1_VERIFIER', 'FIN_ACCOUNTS_LEVEL2_VERIFIER',
                'FIN_ACCOUNTS_LEVEL5_VERIFIER']
        user_role_ids = self.interface.get_user_role_ids(user_id=user_id)
        return user_role_ids
