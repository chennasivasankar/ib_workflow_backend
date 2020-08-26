from typing import List


class ProjectService:

    @property
    def interface(self):
        from ib_iam.app_interfaces.service_interface import ServiceInterface
        return ServiceInterface()

    def get_valid_project_ids(self, project_ids: List[str]) -> List[str]:
        valid_project_ids = \
            self.interface.get_valid_project_ids(project_ids=project_ids)
        return valid_project_ids
