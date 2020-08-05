
from typing import List, Dict

from ib_tasks.interactors.stages_dtos import TaskTemplateStageActionDTO, \
    StageActionDTO, TemplateStageDTO
from ib_tasks.interactors.storage_interfaces.action_storage_interface import \
    ActionStorageInterface


class InvalidTaskTemplateIdsException(Exception):
    def __init__(self, task_template_ids_dict: str):
        self.task_template_ids_dict = task_template_ids_dict


class ConfigureInitialTaskTemplateStageActions:

    def __init__(self, storage: ActionStorageInterface,
                 tasks_dto: List[TaskTemplateStageActionDTO]):
        self.storage = storage
        self.tasks_dto = tasks_dto

    def create_update_delete_stage_actions_to_task_template(self):

        tasks_dto = self.tasks_dto
        self._validations_for_initial_task_template_stages(tasks_dto)
        actions_dto = self._get_stage_actions_dto(tasks_dto)
        from ib_tasks.interactors.create_update_delete_stage_actions \
            import CreateUpdateDeleteStageActionsInteractor
        interactor_obj = CreateUpdateDeleteStageActionsInteractor(
            storage=self.storage, actions_dto=actions_dto
        )
        interactor_obj.create_update_delete_stage_actions()

        task_template_stage_dtos = \
            self._get_initial_stage_dto_to_tasks_templates(tasks_dto)
        self.storage.create_initial_stage_to_task_template(
            task_template_stage_dtos=task_template_stage_dtos
        )

    def _validations_for_initial_task_template_stages(
            self, tasks_dto: List[TaskTemplateStageActionDTO]):

        unique_task_templates = self.get_unique_task_template_ids(tasks_dto)
        self._validate_task_template_ids(unique_task_templates)
        self._validate_for_unique_task_template_stage(tasks_dto)

    def _validate_for_unique_task_template_stage(
            self, tasks_dto: List[TaskTemplateStageActionDTO]):
        from collections import defaultdict
        template_stage_dict = defaultdict(set)

        for task_dto in tasks_dto:
            template_id = task_dto.task_template_id
            stage_id = task_dto.stage_id
            template_stage_dict[template_id].add(stage_id)

        template_stages_dict = \
            self._get_task_template_stages_dict(template_stage_dict)

        is_not_template_stage_unique_present = template_stages_dict
        from ib_tasks.exceptions.task_custom_exceptions \
            import ManyStagesToInitialTaskTemplate
        if is_not_template_stage_unique_present:
            import json
            template_stages_dict = json.dumps(template_stages_dict)
            raise ManyStagesToInitialTaskTemplate(
                task_template_stages_dict=template_stages_dict
            )

    @staticmethod
    def _get_task_template_stages_dict(
        template_stage_dict: Dict[str, set]
    ) -> Dict[str, List[str]]:

        from collections import defaultdict
        template_stages_dict = defaultdict(list)
        for key, value in template_stage_dict.items():
            is_not_template_stage_unique = len(value) > 1
            if is_not_template_stage_unique:
                template_stages_dict[key] = sorted(value)
        return template_stages_dict

    def _validate_task_template_ids(self, task_template_ids: List[str]):
        valid_task_template_ids = self.storage.get_valid_task_template_ids(
            task_template_ids=task_template_ids)

        invalid_ids = []
        for task_template_id in task_template_ids:
            if task_template_id not in valid_task_template_ids:
                invalid_ids.append(task_template_id)

        is_invalid_task_template_ids_present = invalid_ids
        import json
        if is_invalid_task_template_ids_present:
            task_template_ids_dict = json.dumps(
                {"invalid_task_template_ids": invalid_ids})
            raise InvalidTaskTemplateIdsException(
                task_template_ids_dict=task_template_ids_dict)
        return

    @staticmethod
    def get_unique_task_template_ids(
            tasks_dto: List[TaskTemplateStageActionDTO]):

        return sorted(list({
            task_dto.task_template_id
            for task_dto in tasks_dto
        }))

    def _get_initial_stage_dto_to_tasks_templates(
            self,
            tasks_dto: List[TaskTemplateStageActionDTO]):

        task_template_stage_dtos = []
        unique_ids = []
        for task_dto in tasks_dto:
            task_template_id = task_dto.task_template_id
            if task_template_id not in unique_ids:
                unique_ids.append(task_template_id)
                task_template_stage_dtos.append(self._append_task_dto(task_dto))

        return task_template_stage_dtos

    @staticmethod
    def _append_task_dto(task_dto):

        return TemplateStageDTO(
            task_template_id=task_dto.task_template_id,
            stage_id=task_dto.stage_id
        )

    @staticmethod
    def _get_stage_actions_dto(tasks_dto: List[TaskTemplateStageActionDTO]):

        return [
            StageActionDTO(
                stage_id=task_dto.stage_id,
                action_name=task_dto.action_name,
                logic=task_dto.logic,
                roles=task_dto.roles,
                function_path=task_dto.function_path,
                button_text=task_dto.button_text,
                button_color=task_dto.button_color
            )
            for task_dto in tasks_dto
        ]
