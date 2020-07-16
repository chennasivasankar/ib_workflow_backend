from typing import List

from ib_boards.interactors.storage_interfaces.dtos import TaskDTO
from ib_boards.tests.factories.storage_dtos import TaskActionsDTOFactory, TaskFieldsDTOFactory


def prepare_task_details_dtos(mocker, task_dtos: List[TaskDTO],
                          user_id: str):
    mock = mocker.patch(
        'ib_boards.adapters.tasks_service.TaskService.get_task_details_dtos'
    )

    actions_dto = [
        TaskActionsDTOFactory.create(
            task_id=task_dto.task_id
        ) for _index, task_dto in enumerate(task_dtos)
    ]

    fields_dto = [
        TaskFieldsDTOFactory.create(
            task_id=task_dto.task_id
        ) for _index, task_dto in enumerate(task_dtos)
    ]
    # actions_dto = TaskActionsDTOFactory.create_batch(size=0, task_id)
    # fields_dto = TaskFieldsDTOFactory.create_batch(size=3)
    mock.return_value = actions_dto, fields_dto
    return mock