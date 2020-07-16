from typing import List
from ib_boards.interactors.storage_interfaces.dtos import (
    TaskDTO, TaskFieldsDTO, TaskActionsDTO)


class TaskService:
    @property
    def interface(self):
        from ib_tasks.interactors.service_interface import ServiceInterface
        return ServiceInterface()

    def get_task_details_dtos(self, task_dtos: List[TaskDTO],
                                user_id: str):
        task_fields_dtos, task_actions_dtos = self.interface.get_task_details_dtos(
            task_dtos=task_dtos, user_id=user_id)

        fields_dtos = []
        actions_dtos = []
        for field_dto in task_fields_dtos:
            fields_dtos.append(TaskFieldsDTO(
                task_id=field_dto.task_id,
                field_type=field_dto.field_type,
                key=field_dto.key,
                value=field_dto.value
            ))

        for actions_dto in task_actions_dtos:
            actions_dtos.append(TaskActionsDTO(
                task_id=actions_dto.task_id,
                action_id=actions_dto.action_id,
                name=actions_dto.name,
                button_text=actions_dto.button_text,
                button_color=actions_dto.button_color
            ))

        return fields_dtos, actions_dtos
