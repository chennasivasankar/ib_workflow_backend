from ib_adhoc_tasks.interactors.dtos.dtos import GetSubtasksParameterDTO


class SubTasksInteractor:

    def get_subtasks_of_task_wrapper(
            self, get_subtasks_parameter_dto: GetSubtasksParameterDTO
    ):
        complete_subtasks_details_dto = self.get_subtasks_of_task(
            get_subtasks_parameter_dto=get_subtasks_parameter_dto
        )
        # todo add presenter interface here
        return presenter.get_response_for_get_subtasks_of_task(
            get_subtasks_parameter_dto=get_subtasks_parameter_dto
        )

    def get_subtasks_of_task(
            self, get_subtasks_parameter_dto: GetSubtasksParameterDTO
    ):
        from ib_adhoc_tasks.adapters.service_adapter import get_service_adapter
        service = get_service_adapter()
        project_id = service.task_service.get_project_id_based_on_task_id(
            task_id=get_subtasks_parameter_dto.task_id
        )
        subtask_ids = service.task_service.get_subtask_ids_for_task_id(
            task_id=get_subtasks_parameter_dto.task_id
        )
        # todo apply limit offset on subtasks
        from ib_adhoc_tasks.adapters.dtos import TasksDetailsInputDTO
        task_details_input_dto = TasksDetailsInputDTO(
            task_ids=subtask_ids,
            project_id=project_id,
            user_id=get_subtasks_parameter_dto.user_id,
            view_type=get_subtasks_parameter_dto.view_type
        )
        complete_subtasks_details_dto = service.get_task_complete_details_dto(
            task_details_input_dto=task_details_input_dto
        )
        return complete_subtasks_details_dto
