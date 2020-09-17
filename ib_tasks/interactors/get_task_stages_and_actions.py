from collections import defaultdict
from typing import List

from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskIdException
from ib_tasks.interactors.storage_interfaces.action_storage_interface import \
    ActionStorageInterface
from ib_tasks.interactors.storage_interfaces.fields_storage_interface import \
    FieldsStorageInterface
from ib_tasks.interactors.storage_interfaces.stages_storage_interface import \
    StageStorageInterface
from ib_tasks.interactors.storage_interfaces.storage_interface import \
    StorageInterface
from ib_tasks.interactors.storage_interfaces.task_storage_interface import TaskStorageInterface
from ib_tasks.interactors.task_dtos import StageAndActionsDetailsDTO
from ib_tasks.interactors.user_role_validation_interactor import \
    UserRoleValidationInteractor


class GetTaskStagesAndActions:
    def __init__(self, field_storage: FieldsStorageInterface,
                 storage: StorageInterface,
                 task_storage: TaskStorageInterface,
                 stage_storage: StageStorageInterface,
                 action_storage: ActionStorageInterface,
                 ):
        self.field_storage = field_storage
        self.task_storage = task_storage
        self.storage = storage
        self.stage_storage = stage_storage
        self.action_storage = action_storage

    def get_task_stages_and_actions(self, task_id: int, user_id: str) -> \
            List[StageAndActionsDetailsDTO]:

        is_valid = self.task_storage.check_is_task_exists(task_id)
        is_invalid = not is_valid
        if is_invalid:
            raise InvalidTaskIdException(task_id)

        project_id = self.task_storage.get_task_project_id(task_id)
        user_roles_interactor = UserRoleValidationInteractor()
        stage_ids = self.field_storage.get_task_stages(task_id)
        permitted_stage_ids = \
            user_roles_interactor.get_permitted_stage_ids_for_stages(
                user_id=user_id, project_id=project_id, stage_ids=stage_ids,
                stage_storage=self.stage_storage)
        stage_details_dtos = self.field_storage.get_stage_complete_details(
                permitted_stage_ids)

        permitted_action_ids = user_roles_interactor. \
            get_permitted_action_ids_for_given_user_id(
                action_storage=self.action_storage, user_id=user_id,
                stage_ids=permitted_stage_ids, project_id=project_id)

        stage_actions_dtos = self.action_storage.get_actions_details(
            permitted_action_ids)

        stage_actions_dtos = self._convert_to_task_complete_details_dto(
                stage_details_dtos, stage_actions_dtos, permitted_stage_ids)
        return stage_actions_dtos

    def _convert_to_task_complete_details_dto(self, stage_details_dtos,
                                              stage_actions_dtos,
                                              stage_ids):
        stages_dtos = {}
        for stage in stage_details_dtos:
            stages_dtos[stage.stage_id] = stage

        list_of_actions = defaultdict(list)
        for item in stage_actions_dtos:
            list_of_actions[item.stage_id].append(item)

        list_of_stage_actions = []
        for stage in stage_ids:
            stage_dto = stages_dtos[stage]
            list_of_stage_actions.append(self._get_stage_actions_dto(
                    list_of_actions[stage], stage_dto))

        return list_of_stage_actions

    @staticmethod
    def _get_stage_actions_dto(actions_dtos, stage_dto):
        return StageAndActionsDetailsDTO(
                stage_id=stage_dto.stage_id,
                name=stage_dto.name,
                db_stage_id=stage_dto.db_stage_id,
                actions_dtos=actions_dtos,
                color=stage_dto.color
        )
