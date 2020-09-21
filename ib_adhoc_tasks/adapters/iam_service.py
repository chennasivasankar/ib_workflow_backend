from typing import List


class InvalidUserId(Exception):
    pass


class InvalidProjectId(Exception):
    pass


class InvalidUserForProject(Exception):
    pass


class IamService:

    @property
    def interface(self):
        from ib_iam.app_interfaces.service_interface import ServiceInterface
        return ServiceInterface()

    def get_user_role_ids_based_on_project(
            self, user_id: str, project_id: str) -> List[str]:
        from ib_iam.interactors.project_role_interactor import \
            UserNotAMemberOfAProject
        try:
            user_role_ids = self.interface.get_user_role_ids_based_on_project(
                user_id=user_id, project_id=project_id
            )
        except InvalidProjectId:
            raise InvalidProjectId
        except UserNotAMemberOfAProject:
            raise InvalidUserForProject
        return user_role_ids

    def get_valid_project_ids(self, project_ids: List[str]):
        valid_project_ids = self.interface.get_valid_project_ids(
            project_ids=project_ids
        )
        return valid_project_ids

    def is_valid_user_id_for_given_project(self, user_id: str, project_id: str):
        try:
            response = self.interface.is_valid_user_id_for_given_project(
                user_id=user_id, project_id=project_id
            )
        except InvalidUserId:
            raise InvalidUserId
        except InvalidProjectId:
            raise InvalidProjectId
        if response:
            raise InvalidUserForProject
