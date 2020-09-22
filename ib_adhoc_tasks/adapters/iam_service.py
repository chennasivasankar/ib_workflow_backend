from typing import List


class IamService:

    @property
    def interface(self):
        from ib_iam.app_interfaces.service_interface import ServiceInterface
        return ServiceInterface()

    def get_valid_project_ids(self, project_ids: List[str]) -> List[str]:
        pass

    @staticmethod
    def get_user_role_ids_based_on_project(
            user_id: str, project_id: str
    ) -> List[str]:
        pass
