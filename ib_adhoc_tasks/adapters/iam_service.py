from dataclasses import dataclass
from typing import List

from ib_users.interactors.exceptions.user_profile import InvalidUserException


@dataclass
class UserIdAndNameDTO:
    user_id: str
    name: str


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
            is_user_not_in_a_project = not self.interface.is_valid_user_id_for_given_project(
                user_id=user_id, project_id=project_id
            )
        except InvalidUserId:
            raise InvalidUserId
        except InvalidProjectId:
            raise InvalidProjectId
        if is_user_not_in_a_project:
            raise InvalidUserForProject

    def get_user_details_bulk(self, user_ids: List[str]) -> \
            List[UserIdAndNameDTO]:
        try:
            user_profile_dtos = self.interface.get_user_details_bulk(
                user_ids=user_ids
            )
        except InvalidUserException:
            raise InvalidUserId
        user_id_and_name_dtos = self._prepare_user_id_and_name_dtos(
            user_profile_dtos=user_profile_dtos
        )
        return user_id_and_name_dtos

    def get_user_role_ids(self, user_id: str):
        user_role_ids = self.interface.get_user_role_ids(
            user_id=user_id
        )
        return user_role_ids

    def validate_user_id_for_given_project(
            self, user_id: str, project_id: str
    ):
        try:
            is_invalid_user_id_for_given_project = \
                not self.interface.is_valid_user_id_for_given_project(
                    user_id=user_id, project_id=project_id
                )
        except InvalidUserId:
            raise InvalidUserId
        except InvalidProjectId:
            raise InvalidProjectId

        if is_invalid_user_id_for_given_project:
            raise InvalidUserForProject

    @staticmethod
    def _prepare_user_id_and_name_dtos(user_profile_dtos):
        user_id_and_name_dtos = [
            UserIdAndNameDTO(
                user_id=user_profile_dto.user_id,
                name=user_profile_dto.name
            )
            for user_profile_dto in user_profile_dtos
        ]
        return user_id_and_name_dtos
