from typing import List

from ib_tasks.interactors.presenter_interfaces.dtos import TaskCompleteDetailsDTO, AllTasksOverviewDetailsDTO
from ib_tasks.interactors.storage_interfaces.get_task_dtos import TaskDetailsDTO


class GetUserActOnTaskResponse:

    def get_user_act_on_task_response(
            self, task_dto: TaskDetailsDTO, task_id: int,
            stage_ids: List[str], project_id: str
    ):
        self._create_or_update_task_in_elasticsearch(
            task_dto=task_dto, task_id=task_id, stage_ids=stage_ids
        )
        task_complete_details_dto = self._get_task_current_board_complete_details(
            task_id=task_id, stage_ids=stage_ids, project_id=project_id
        )
        task_current_stage_details_dto = \
            self._get_task_current_stage_details(task_id=task_id)
        all_tasks_overview_details_dto = self._get_tasks_overview_for_users(
            task_id=task_id, project_id=project_id
        )
        return (
            task_complete_details_dto, task_current_stage_details_dto,
            all_tasks_overview_details_dto
        )

    def _create_or_update_task_in_elasticsearch(
            self, task_dto: TaskDetailsDTO, stage_ids: List[str],
            task_id: int):
        from ib_tasks.interactors \
            .create_or_update_data_in_elasticsearch_interactor import \
            CreateOrUpdateDataInElasticSearchInteractor
        elasticsearch_interactor = CreateOrUpdateDataInElasticSearchInteractor(
            elasticsearch_storage=self.elasticsearch_storage,
            field_storage=self.field_storage,
            task_storage=self.task_storage
        )
        elasticsearch_interactor.create_or_update_task_in_elasticsearch(
            task_dto=task_dto, stage_ids=stage_ids, task_id=task_id
        )

    def _get_task_current_board_complete_details(
            self, task_id: int, stage_ids: List[str], project_id: str
    ) -> TaskCompleteDetailsDTO:
        from ib_tasks.interactors.user_action_on_task \
            .get_task_current_board_complete_details_interactor \
            import GetTaskCurrentBoardCompleteDetailsInteractor
        interactor = GetTaskCurrentBoardCompleteDetailsInteractor(
            task_stage_storage=self.task_stage_storage,
            user_id=self.user_id,
            board_id=self.board_id,
            field_storage=self.field_storage,
            stage_storage=self.stage_storage,
            task_storage=self.task_storage,
            action_storage=self.action_storage,
            view_type=self.view_type,
            project_id=project_id
        )
        return interactor.get_task_current_board_complete_details(
            task_id=task_id, stage_ids=stage_ids)

    def _get_task_current_stage_details(self, task_id: int):
        from ib_tasks.interactors.get_task_current_stages_interactor import \
            GetTaskCurrentStagesInteractor
        get_task_current_stages_interactor = GetTaskCurrentStagesInteractor(
            task_stage_storage=self.task_stage_storage)
        task_current_stage_details_dto = \
            get_task_current_stages_interactor.get_task_current_stages_details(
                task_id=task_id, user_id=self.user_id)
        return task_current_stage_details_dto

    def _get_tasks_overview_for_users(
            self, task_id: int, project_id: str
    ) -> AllTasksOverviewDetailsDTO:
        from ib_tasks.interactors.get_all_task_overview_with_filters_and_searches_for_user \
            import GetTasksOverviewForUserInteractor
        task_overview_interactor = GetTasksOverviewForUserInteractor(
            stage_storage=self.stage_storage, task_storage=self.task_storage,
            field_storage=self.field_storage,
            action_storage=self.action_storage,
            task_stage_storage=self.task_stage_storage,
            template_storage=self.task_template_storage
        )
        all_tasks_overview_details_dto = \
            task_overview_interactor.get_filtered_tasks_overview_for_user(
                user_id=self.user_id, task_ids=[task_id],
                view_type=self.view_type,
                project_id=project_id)
        return all_tasks_overview_details_dto
