from typing import List

from ib_tasks.interactors.storage_interfaces.stages_storage_interface import \
    StageStorageInterface
from ib_tasks.interactors.storage_interfaces.task_template_storage_interface \
    import TaskTemplateStorageInterface


class ProjectTaskTemplateValidationInteractor:

    def __init__(self, task_template_storage: TaskTemplateStorageInterface):
        self.task_template_storage = task_template_storage

    def get_task_template_stages_for_project(
            self, project_id: str, stage_storage: StageStorageInterface
    ) -> List[str]:
        self._validate_project_id(project_id=project_id)

        task_templates_of_project = \
            self.task_template_storage.get_project_templates(
                project_id=project_id
            )
        common_task_template_ids = self.get_common_task_templates()

        task_templates_of_project_with_common_task_template_ids = \
            task_templates_of_project + common_task_template_ids

        stage_ids = stage_storage.get_stage_ids_of_templates(
            template_ids=
            task_templates_of_project_with_common_task_template_ids)
        return stage_ids

    def get_common_task_templates(self):
        task_template_ids = self.task_template_storage.get_task_template_ids()
        project_task_template_ids = \
            self.task_template_storage.get_task_template_ids_of_project_task_templates()

        common_task_template_ids = [
            task_template_id
            for task_template_id in task_template_ids
            if task_template_id not in project_task_template_ids
        ]
        return common_task_template_ids

    @staticmethod
    def _validate_project_id(project_id: str):
        from ib_tasks.adapters.project_service import ProjectService
        project_service = ProjectService()

        project_id_list = [project_id]
        valid_project_ids = \
            project_service.get_valid_project_ids(project_ids=project_id_list)

        is_invalid_project_id = project_id not in valid_project_ids
        if is_invalid_project_id:
            from ib_tasks.exceptions.custom_exceptions import InvalidProjectId
            raise InvalidProjectId(project_id=project_id)
