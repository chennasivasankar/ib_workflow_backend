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

    def get_projects_config(self):
        return self.interface.get_projects_task_assignee_config()

    def get_project_prefix(self, project_id: str):
        from ib_iam.exceptions.custom_exceptions import \
            InvalidProjectIdException
        try:
            project_prefix = \
                self.interface.get_project_prefix(project_id=project_id)
        except InvalidProjectIdException as err:
            from ib_tasks.exceptions.custom_exceptions import \
                    InvalidProjectId
            raise InvalidProjectId(err.project_id)

        return project_prefix
