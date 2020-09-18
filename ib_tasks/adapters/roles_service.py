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

    def get_project_roles(self, project_id: str):

        from ib_iam.exceptions.custom_exceptions import InvalidProjectId
        try:
            project_roles = self.interface.get_project_role_ids(
                project_id=project_id
            )
        except InvalidProjectId:
            from ib_tasks.exceptions.adapter_exceptions import InvalidProjectIdsException
            raise InvalidProjectIdsException(invalid_project_ids=[project_id])

        return project_roles

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
