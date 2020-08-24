from typing import List


class ProjectService:

    @property
    def interface(self):
        from ib_iam.app_interfaces.service_interface import ServiceInterface
        return ServiceInterface()

    @staticmethod
    def check_is_project_id_exists(project_id: str) -> bool:
        return True
        # TODO: call service interface
        return True
