"""
Created on: 24/07/20
Author: Pavankumar Pamuru

"""
from typing import List


class InvalidProjectIdsException(Exception):
    def __init__(self, invalid_project_ids: List[str]):
        self.invalid_project_ids = invalid_project_ids


class UserIsNotInProjectException(Exception):
    pass


class IamService:
    @property
    def interface(self):
        from ib_iam.app_interfaces.service_interface import ServiceInterface
        return ServiceInterface()

    def get_user_roles(self, user_id: str):
        user_roles = self.interface.get_user_role_ids(
            user_id=user_id
        )
        return user_roles

    def get_valid_user_role_ids(self, user_roles: List[str]):
        valid_role_ids = self.interface.get_valid_role_ids(
            role_ids=user_roles
        )
        return valid_role_ids

    def validate_if_user_is_in_project(self, user_id: str, project_id: str):
        is_in_project = self.interface.is_valid_user_id_for_given_project(
            user_id=user_id, project_id=project_id)
        return is_in_project

    def validate_project_ids(self, project_ids: List[str]) -> \
            List[str]:
        valid_project_ids = self.interface.get_valid_project_ids(project_ids)
        return valid_project_ids

    def get_user_role_ids_based_on_project(
            self, user_id, project_id: str) -> List[str]:
        role_ids = self.interface.get_user_role_ids_based_on_project(
            user_id=user_id, project_id=project_id)
        return role_ids
