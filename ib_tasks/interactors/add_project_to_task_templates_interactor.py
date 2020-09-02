from typing import List
from ib_tasks.interactors.storage_interfaces.task_template_storage_interface \
    import TaskTemplateStorageInterface


class AddProjectToTaskTemplatesInteractor:

    def __init__(self, task_template_storage: TaskTemplateStorageInterface):
        self.task_template_storage = task_template_storage

    def add_project_to_task_templates_interactor(
            self, project_id, task_template_ids: List[str]
    ):
        self._make_validations(
            project_id=project_id, task_template_ids=task_template_ids)

        existing_task_template_ids_of_project = self.task_template_storage.\
            get_existing_task_template_ids_of_project_task_templates(
                task_template_ids=task_template_ids, project_id=project_id)
        task_template_ids_to_create = [
            task_template_id
            for task_template_id in task_template_ids
            if task_template_id not in existing_task_template_ids_of_project
        ]

        self.task_template_storage.add_project_to_task_templates(
            project_id=project_id,
            task_template_ids=task_template_ids_to_create)

    def _make_validations(self, project_id: str, task_template_ids: List[str]):
        self._validate_task_template_ids(task_template_ids=task_template_ids)

        from ib_tasks.adapters.service_adapter import ServiceAdapter
        service_adapter = ServiceAdapter()
        project_id_list = [project_id]
        valid_project_ids = \
            service_adapter.project_service.get_valid_project_ids(
                project_ids=project_id_list)
        is_invalid_project = not valid_project_ids
        if is_invalid_project:
            from ib_tasks.exceptions.custom_exceptions import \
                InvalidProjectId
            raise InvalidProjectId(project_id)

    def _validate_task_template_ids(self, task_template_ids: List[str]):

        import collections
        task_template_ids_counter = collections.Counter(task_template_ids)
        duplicate_task_template_ids = [
            task_template_id
            for task_template_id, count in task_template_ids_counter.items()
            if count > 1
        ]

        if duplicate_task_template_ids:
            from ib_tasks.exceptions.custom_exceptions import \
                DuplicateTaskTemplateIdsGivenToAProject
            raise DuplicateTaskTemplateIdsGivenToAProject(
                duplicate_task_template_ids)

        valid_task_template_ids = self.task_template_storage. \
            get_valid_task_template_ids_in_given_task_template_ids(
                template_ids=task_template_ids)
        invalid_task_template_ids = [
            task_template_id for task_template_id in task_template_ids
            if task_template_id not in valid_task_template_ids
        ]

        if invalid_task_template_ids:
            from ib_tasks.exceptions.task_custom_exceptions import \
                InvalidTaskTemplateIds
            raise InvalidTaskTemplateIds(invalid_task_template_ids)
