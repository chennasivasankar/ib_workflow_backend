from typing import Tuple, List

from ib_adhoc_tasks.adapters.dtos import TasksCompleteDetailsDTO
from ib_adhoc_tasks.interactors.dtos.dtos import GetSubtasksParameterDTO
from ib_adhoc_tasks.interactors.presenter_interfaces \
    .subtask_presenter_interface import GetSubTasksPresenterInterface


class SubTasksInteractor:

    def get_subtasks_of_task_wrapper(
            self, get_subtasks_parameter_dto: GetSubtasksParameterDTO,
            presenter: GetSubTasksPresenterInterface
    ):
        subtask_ids, complete_subtasks_details_dto = \
            self.get_subtasks_of_task(
                get_subtasks_parameter_dto=get_subtasks_parameter_dto
            )
        return presenter.get_response_for_get_subtasks_of_task(
            task_display_id=get_subtasks_parameter_dto.task_id,
            subtask_ids=subtask_ids,
            complete_subtasks_details_dto=complete_subtasks_details_dto
        )

    def get_subtasks_of_task(
            self, get_subtasks_parameter_dto: GetSubtasksParameterDTO
    ) -> Tuple[List[int], TasksCompleteDetailsDTO]:
        from ib_adhoc_tasks.adapters.service_adapter import get_service_adapter
        service = get_service_adapter()
        task_id = service.task_service.get_task_id(
            task_display_id=get_subtasks_parameter_dto.task_id
        )
        # get_subtasks_parameter_dto.task_id = task_id
        project_id = service.task_service.get_project_id_based_on_task_id(
            task_id=task_id
        )
        subtask_ids = service.task_service.get_subtask_ids_for_task_id(
            task_id=task_id
        )
        from ib_adhoc_tasks.adapters.dtos import TasksDetailsInputDTO
        task_details_input_dto = TasksDetailsInputDTO(
            task_ids=subtask_ids,
            project_id=project_id,
            user_id=get_subtasks_parameter_dto.user_id,
            view_type=get_subtasks_parameter_dto.view_type
        )
        complete_subtasks_details_dto = service.task_service.get_task_complete_details_dto(
            task_details_input_dto=task_details_input_dto
        )
        return subtask_ids, complete_subtasks_details_dto
