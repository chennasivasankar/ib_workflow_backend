from typing import List
from ib_tasks.interactors.storage_interfaces.storage_interface \
    import StorageInterface, TaskGofAndStatusesDTO


class GetGroupOfFieldsAndStatusVariablesToTaskInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_gofs_and_status_variables_to_task(self, task_id: str):

        self._validate_task_id(task_id=task_id)
        group_of_fields_dto = \
            self.storage.get_task_group_of_fields_dto(task_id=task_id)
        group_of_field_ids = self._get_group_of_field_ids(
            group_of_fields_dto=group_of_fields_dto
        )
        fields_dto = self.storage.get_fields_to_group_of_field_ids(
            group_of_field_ids=group_of_field_ids
        )
        status_variable_dtos = \
            self.storage.get_status_variables_to_task(task_id=task_id)
        return TaskGofAndStatusesDTO(
            task_id=task_id, fields_dto=fields_dto,
            group_of_fields_dto=group_of_fields_dto,
            statuses_dto=status_variable_dtos
        )

    def _validate_task_id(self, task_id: str):

        valid_task = self.storage.validate_task_id(task_id=task_id)
        is_invalid_task = not valid_task
        if is_invalid_task:
            from ib_tasks.exceptions.custom_exceptions \
                import InvalidTaskIdException
            raise InvalidTaskIdException(task_id=task_id)

    @staticmethod
    def _get_group_of_field_ids(group_of_fields_dto) -> List[str]:

        return [
            group_of_field_dto.database_id
            for group_of_field_dto in group_of_fields_dto
        ]
