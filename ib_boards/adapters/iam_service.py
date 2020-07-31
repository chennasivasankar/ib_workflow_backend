"""
Created on: 24/07/20
Author: Pavankumar Pamuru

"""
from typing import List


class IamService:
    @property
    def interface(self):
        from ib_iam.app_interfaces.service_interface import ServiceInterface
        return ServiceInterface()

    def get_user_roles(self, user_id: str):
        pass

    def get_valid_user_role_ids(self, user_roles: List[str]):
        valid_role_ids = self.interface.get_valid_role_ids(
            role_ids=user_roles
        )
        return valid_role_ids
