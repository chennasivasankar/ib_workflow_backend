
from collections import defaultdict
from typing import List
from ib_tasks.interactors.storage_interfaces.storage_interface \
    import StorageInterface
from ib_tasks.interactors.dtos import TaskTemplateStageActionDTO
from ib_tasks.interactors.mixins\
    .stage_actions_validation_mixin \
    import StageActionsAndTasksValidationMixin


class CreateUpdateTasksInteractor(StageActionsAndTasksValidationMixin):

    def __init__(self, storage: StorageInterface,
                 tasks_dto: List[TaskTemplateStageActionDTO]):
        super().__init__(storage=storage)
        self.tasks_dto = tasks_dto

    def create_update_tasks(self):
        tasks_dto = self.tasks_dto
        stage_ids = self._get_stage_ids(tasks_dto)
        self.validations_for_stage_ids(stage_ids=stage_ids)
        self.validations_for_stage_roles(tasks_dto)
        self.validations_for_empty_stage_display_logic(tasks_dto)
        self.validations_for_empty_button_texts(tasks_dto)
        self.validations_for_button_texts(tasks_dto)
        self.validations_for_duplicate_stage_actions(tasks_dto)
        self._create_update_tasks(tasks_dto)

    def _create_update_tasks(
            self, tasks_dto: List[TaskTemplateStageActionDTO]):
        stage_ids = self._get_stage_ids(tasks_dto)
        db_stage_tasks_dto = self.storage \
            .get_stage_action_names(stage_ids=stage_ids)
        is_db_stage_actions_empty = not db_stage_tasks_dto
        if is_db_stage_actions_empty:
            self.storage\
                .create_task_template_stage_actions(tasks_dto=tasks_dto)
        stage_actions = self._get_stage_actions(tasks_dto)
        self._create_or_update_tasks(db_stage_tasks_dto, stage_actions)

    @staticmethod
    def _get_stage_actions(tasks_dto):
        stage_actions = defaultdict(list)
        for task_dto in tasks_dto:
            stage_actions[task_dto.stage_id].append(task_dto)
        return stage_actions

    def _create_or_update_tasks(
            self, db_stage_actions_dto, stage_actions):
        create_stage_actions, update_stage_actions = [], []
        for stage_task_dto in db_stage_actions_dto:
            db_action_names = stage_task_dto.action_names
            stage_tasks_dto = stage_actions[stage_task_dto.stage_id]
            self._append_create_and_update_stage_dto(
                db_action_names, stage_tasks_dto,
                create_stage_actions, update_stage_actions
            )

        is_create_actions_present = create_stage_actions
        if is_create_actions_present:
            self.storage.create_task_template_stage_actions(
                tasks_dto=create_stage_actions
            )
        is_update_actions_present = update_stage_actions
        if is_update_actions_present:
            self.storage.update_task_template_stage_actions(
                tasks_dto=update_stage_actions
            )

    @staticmethod
    def _append_create_and_update_stage_dto(
            db_action_names, stage_tasks_dto,
            create_stage_actions, update_stage_actions):
        for stage_task_dto in stage_tasks_dto:
            if stage_task_dto.action_name not in db_action_names:
                create_stage_actions.append(stage_task_dto)
            elif stage_task_dto.action_name in db_action_names:
                update_stage_actions.append(stage_task_dto)


