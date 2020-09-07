from typing import List

from ib_tasks.adapters.dtos import ProjectRolesDTO
from ib_tasks.exceptions.permission_custom_exceptions import \
    InvalidUserIdException


class UserNotAMemberOfAProjectException(Exception):
    pass


class RolesService:

    @property
    def interface(self):
        from ib_iam.app_interfaces.service_interface import ServiceInterface
        return ServiceInterface()

    def get_db_roles(self):
        # TODO: call service interface
        return ['FIN_PAYMENT_APPROVER', 'FIN_FINANCE_RP',
                'FIN_ACCOUNTS_LEVEL4_VERIFIER', 'FIN_PAYMENTS_RP',
                'FIN_COMPLIANCE_APPROVER', 'FIN_PAYMENTS_LEVEL3_VERIFIER',
                'FIN_PAYMENTS_LEVEL2_VERIFIER', 'FIN_PAYMENTS_LEVEL1_VERIFIER',
                'PR_PENDING_ACCOUNTS_LEVEL1_VERIFICATION',
                'FIN_ACCOUNTS_LEVEL1_VERIFIER', 'FIN_ACCOUNTS_LEVEL2_VERIFIER',
                'FIN_ACCOUNTS_LEVEL3_VERIFIER'
                ]

    def get_user_roles(self, user_id):
        pass

    def get_valid_role_ids_in_given_role_ids(
            self, role_ids: List[str]
    ) -> List[str]:
        valid_roles = self.interface.get_valid_role_ids(role_ids)
        return valid_roles

    def get_user_role_ids(self, user_id: str) -> List[str]:
        from ib_iam.exceptions.custom_exceptions import InvalidUserId
        try:
            user_role_ids = self.interface.get_user_role_ids(user_id=user_id)
        except InvalidUserId:
            raise InvalidUserIdException(user_id)
        return user_role_ids

    def get_user_role_ids_based_on_project(
            self, user_id, project_id: str) -> List[str]:
        from ib_iam.interactors.project_role_interactor import \
            UserNotAMemberOfAProject
        try:
            return self.interface.get_user_role_ids_based_on_project(
                user_id=user_id, project_id=project_id)
        except UserNotAMemberOfAProject:
            raise UserNotAMemberOfAProjectException()

    def get_user_role_ids_based_on_given_project_ids(
            self, user_id, project_ids: List[str]) -> \
            List[ProjectRolesDTO]:
        # raise NotImplementedError
        # TODO: Remove get roles from loop
        project_roles = [
            ProjectRolesDTO(
                project_id=project_id,
                roles=self.get_user_role_ids_based_on_project(
                    user_id, project_id)
            )
            for project_id in project_ids
        ]
        return project_roles
