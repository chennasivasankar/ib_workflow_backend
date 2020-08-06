from ib_tasks.interactors.storage_interfaces\
    .create_or_update_task_storage_interface \
    import CreateOrUpdateTaskStorageInterface
from ib_tasks.interactors.storage_interfaces.get_task_dtos \
    import TaskDetailsDTO


class GetTaskBaseInteractor:

    def __init__(self, storage: CreateOrUpdateTaskStorageInterface):
        self.storage = storage

    def get_task(self, task_id: int):
        template_id = self.storage.validate_task_id(task_id)
        task_gof_dtos = self.storage.get_task_gof_dtos(task_id)
        task_gof_ids = [
            task_gof_dto.task_gof_id
            for task_gof_dto in task_gof_dtos
        ]
        task_gof_field_dtos = self.storage.get_task_gof_field_dtos(
            task_gof_ids
        )
        task_details_dto = TaskDetailsDTO(
            template_id=template_id,
            task_gof_dtos=task_gof_dtos,
            task_gof_field_dtos=task_gof_field_dtos
        )
        return task_details_dto
