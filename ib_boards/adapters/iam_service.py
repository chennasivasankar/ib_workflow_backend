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
       return True

    def validate_project_ids(self, project_ids: List[str]) -> \
            List[str]:
        #TODO validate project ids
       return project_ids