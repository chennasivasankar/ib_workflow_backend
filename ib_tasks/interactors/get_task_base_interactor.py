from ib_tasks.adapters.dtos import ProjectDetailsDTO
from ib_tasks.interactors.storage_interfaces\
    .create_or_update_task_storage_interface \
    import CreateOrUpdateTaskStorageInterface
from ib_tasks.interactors.storage_interfaces.get_task_dtos \
    import TaskDetailsDTO


class GetTaskBaseInteractor:

    def __init__(self, storage: CreateOrUpdateTaskStorageInterface):
        self.storage = storage

    def get_task(self, task_id: int) -> TaskDetailsDTO:
        task_base_details_dto = self.storage.validate_task_id(task_id)
        project_id = task_base_details_dto.project_id
        # task_project_details_dto = self._get_task_project_details_dto(project_id)
        task_project_details_dto = None
        task_gof_dtos = self.storage.get_task_gof_dtos(task_id)
        task_gof_ids = [
            task_gof_dto.task_gof_id
            for task_gof_dto in task_gof_dtos
        ]
        task_gof_field_dtos = self.storage.get_task_gof_field_dtos(
            task_gof_ids
        )
        task_details_dto = TaskDetailsDTO(
            project_details_dto=task_project_details_dto,
            task_base_details_dto=task_base_details_dto,
            task_gof_dtos=task_gof_dtos,
            task_gof_field_dtos=task_gof_field_dtos
        )
        return task_details_dto

    @staticmethod
    def _get_task_project_details_dto(project_id: str) -> ProjectDetailsDTO:
        from ib_tasks.adapters.service_adapter import get_service_adapter
        service_adapter = get_service_adapter()
        task_project_details_dto = service_adapter.auth_service. \
            get_projects_info_for_given_ids(project_ids=[project_id])
        return task_project_details_dto


