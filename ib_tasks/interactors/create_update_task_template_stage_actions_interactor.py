from collections import defaultdict
from typing import List

from ib_tasks.interactors.mixins.get_stage_actions_details \
    import GetStageActionsDetailsMixin
from ib_tasks.interactors.storage_interfaces.storage_interface \
    import StorageInterface
from ib_tasks.interactors.dtos import TaskTemplateStageActionDTO


class CreateUpdateTaskTemplateStageActionsInteractor(
        GetStageActionsDetailsMixin):

    def __init__(self, storage: StorageInterface,
                 tasks_dto: List[TaskTemplateStageActionDTO]):
        self.storage = storage
        self.tasks_dto = tasks_dto

    def create_update_tasks(self):
        tasks_dto = self.tasks_dto
        task_template_ids = self._get_task_template_ids(tasks_dto=tasks_dto)
        self._validate_task_template_ids(task_template_ids)
        from ib_tasks.interactors.stage_actions_validation_interactor \
            import StageActionsAndTasksValidationInteractor
        interactor = StageActionsAndTasksValidationInteractor(
            storage=self.storage)
        interactor.validations_for_actions_dto(actions_dto=tasks_dto)

        self._create_update_tasks(tasks_dto)

    @staticmethod
    def _get_task_template_ids(tasks_dto: List[TaskTemplateStageActionDTO]):
        return [
            task_dto.task_template_id
            for task_dto in tasks_dto
        ]

    def _validate_task_template_ids(self, task_template_ids: List[str]):

        valid_task_template_ids = self.storage.get_valid_task_template_ids(
            task_template_ids=task_template_ids
        )
        invalid_task_template_ids = [
            task_template_id
            for task_template_id in task_template_ids
            if task_template_id not in valid_task_template_ids
        ]
        is_invalid_task_template_exist = invalid_task_template_ids
        import json
        from ib_tasks.exceptions.custom_exceptions \
            import InvalidTaskTemplateId
        if is_invalid_task_template_exist:
            print(invalid_task_template_ids)
            task_template_ids_dict = json.dumps(
                {"task_template_ids": invalid_task_template_ids})
            raise InvalidTaskTemplateId(
                task_template_ids_dict=task_template_ids_dict)

    def _create_update_tasks(
            self, tasks_dto: List[TaskTemplateStageActionDTO]):
        stage_ids = self.get_stage_ids(tasks_dto)
        db_stage_tasks_dto = self.storage \
            .get_stage_action_names(stage_ids=stage_ids)
        is_db_stage_actions_empty = not db_stage_tasks_dto
        if is_db_stage_actions_empty:
            self.storage \
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
