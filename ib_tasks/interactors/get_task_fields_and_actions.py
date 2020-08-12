from typing import List

from ib_boards.interactors.dtos import StageActionDetailsDTO
from ib_tasks.adapters.roles_service_adapter import get_roles_service_adapter
from ib_tasks.constants.enum import ViewType
from ib_tasks.exceptions.stage_custom_exceptions import InvalidTaskStageIds
from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskIds
from ib_tasks.interactors.storage_interfaces.action_storage_interface import \
    ActionStorageInterface
from ib_tasks.interactors.storage_interfaces.actions_dtos import \
    ActionDetailsDTO
from ib_tasks.interactors.storage_interfaces.fields_dtos import \
    StageTaskFieldsDTO, FieldDetailsDTO, TaskTemplateStageFieldsDTO, \
    FieldDetailsDTOWithTaskId
from ib_tasks.interactors.storage_interfaces.fields_storage_interface import \
    FieldsStorageInterface
from ib_tasks.interactors.storage_interfaces.stage_dtos import \
    GetTaskStageCompleteDetailsDTO, TaskTemplateWithStageColorDTO, TaskTemplateStageDTO
from ib_tasks.interactors.storage_interfaces.stages_storage_interface import \
    StageStorageInterface
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface
from ib_tasks.interactors.task_dtos import GetTaskDetailsDTO
from ib_tasks.interactors.user_role_validation_interactor import UserRoleValidationInteractor


class GetTaskFieldsAndActionsInteractor:
    def __init__(self, task_storage: TaskStorageInterface,
                 field_storage: FieldsStorageInterface,
                 stage_storage: StageStorageInterface,
                 action_storage: ActionStorageInterface):
        self.field_storage = field_storage
        self.stage_storage = stage_storage
        self.task_storage = task_storage
        self.action_storage = action_storage

    def get_task_fields_and_action(self, task_dtos: List[GetTaskDetailsDTO],
                                   user_id: str, view_type: ViewType) -> \
            List[GetTaskStageCompleteDetailsDTO]:

        task_ids = [task.task_id for task in task_dtos]
        stage_ids = [task.stage_id for task in task_dtos]

        unique_task_ids = list(sorted(set(task_ids)))
        unique_stage_ids = list(sorted(set(stage_ids)))

        valid_task_ids = self.task_storage.get_valid_task_ids(unique_task_ids)
        self._validate_task_ids(unique_task_ids, valid_task_ids)

        stage_task_dtos = task_dtos
        valid_stage_ids = self.stage_storage.get_existing_stage_ids(
            unique_stage_ids)

        self._validate_stage_ids(unique_stage_ids, valid_stage_ids)
        valid_stage_and_tasks = self.task_storage.validate_task_related_stage_ids(
            task_dtos)
        self._validate_stage_and_tasks(valid_stage_and_tasks, task_dtos)

        task_stage_dtos = self.stage_storage.get_stage_details(stage_task_dtos)

        user_roles_interactor = UserRoleValidationInteractor()
        permitted_action_ids = user_roles_interactor. \
            get_permitted_action_ids_for_given_user_id(
            action_storage=self.action_storage, user_id=user_id, stage_ids=stage_ids)

        action_dtos = self.action_storage.get_actions_details(permitted_action_ids)

        stage_fields_dtos = self.field_storage.get_field_ids(task_stage_dtos, view_type)
        list_of_field_ids = self._get_field_ids(stage_fields_dtos)
        permitted_field_ids = user_roles_interactor.get_field_ids_having_write_permission_for_user(
            user_id=user_id, field_ids=list_of_field_ids, field_storage=self.field_storage
        )
        task_fields_dtos = self._map_task_and_their_fields(
            stage_fields_dtos, task_stage_dtos, permitted_field_ids)

        field_dtos = self.field_storage.get_fields_details(
            task_fields_dtos)

        task_details_dtos = self. \
            _map_fields_and_actions_based_on_their_stage_and_task_id(
            action_dtos, field_dtos, stage_fields_dtos)
        return task_details_dtos

    @staticmethod
    def _get_field_ids(stage_fields_dtos: List[TaskTemplateStageFieldsDTO]):
        field_ids_list = []
        for stage in stage_fields_dtos:
            field_ids_list += stage.field_ids

        return list(set(field_ids_list))

    def _map_task_and_their_fields(self, stage_fields_dtos: List[TaskTemplateStageFieldsDTO],
                                   task_stage_dtos: List[TaskTemplateStageDTO],
                                   permitted_field_ids: List[str]):
        list_of_stage_fields = []
        for task in task_stage_dtos:
            for stage in stage_fields_dtos:
                template_condition = stage.task_template_id == \
                                     task.task_template_id
                stage_condition = stage.stage_id == task.stage_id
                if task.task_id == stage.task_id and stage_condition and template_condition:
                    list_of_stage_fields.append(
                        self._get_task_fields(stage, task, permitted_field_ids))
        return list_of_stage_fields

    @staticmethod
    def _get_task_fields(stage, task, permitted_field_ids: List[str]):
        valid_field_ids = [field for field in stage.field_ids
                           if field in permitted_field_ids]

        return StageTaskFieldsDTO(task_id=task.task_id,
                                  stage_id=stage.stage_id,
                                  field_ids=list(valid_field_ids))

    @staticmethod
    def _validate_stage_ids(stage_ids, valid_stage_ids):
        invalid_stage_ids = [
            stage_id for stage_id in stage_ids
            if stage_id not in valid_stage_ids
        ]
        if invalid_stage_ids:
            from ib_tasks.exceptions.stage_custom_exceptions import \
                InvalidStageIdsListException
            raise InvalidStageIdsListException(invalid_stage_ids)
        return

    @staticmethod
    def _validate_task_ids(task_ids, valid_task_ids):
        invalid_task_ids = [
            task_id for task_id in task_ids if task_id not in valid_task_ids
        ]
        if invalid_task_ids:
            raise InvalidTaskIds(invalid_task_ids)
        return

    def _map_fields_and_actions_based_on_their_stage_and_task_id(
            self,
            action_dtos: List[ActionDetailsDTO],
            field_dtos: List[FieldDetailsDTOWithTaskId],
            stage_fields_dtos: List[TaskTemplateStageFieldsDTO]
    ):
        list_of_task_details_dtos = []
        for stage in stage_fields_dtos:
            list_of_field_dtos = self._get_list_of_fields_for_stage(
                field_dtos, stage)
            list_of_action_dtos = self._get_list_of_actions_dtos_for_stage(
                action_dtos, stage)
            task_stage_dtos = self._get_task_stage_details(
                list_of_action_dtos, list_of_field_dtos, stage)
            list_of_task_details_dtos.append(task_stage_dtos)

        return list_of_task_details_dtos

    @staticmethod
    def _get_task_stage_details(
            list_of_action_dtos: List[StageActionDetailsDTO],
            list_of_field_dtos: List[FieldDetailsDTOWithTaskId],
            stage
    ):
        fields_dtos = [
            FieldDetailsDTO(
                field_type=field.field_type,
                value=field.value,
                key=field.key,
                field_id=field.field_id
            )
            for field in list_of_field_dtos
        ]
        return GetTaskStageCompleteDetailsDTO(
            task_id=stage.task_id,
            stage_id=stage.stage_id,
            stage_color=stage.stage_color,
            field_dtos=fields_dtos,
            action_dtos=list_of_action_dtos
        )

    @staticmethod
    def _get_list_of_fields_for_stage(
            field_dtos: List[FieldDetailsDTOWithTaskId],
            stage: TaskTemplateStageFieldsDTO
    ):
        list_of_field_dtos = []
        if not field_dtos:
            return []
        for field in field_dtos:
            if field.field_id in stage.field_ids and field.task_id == stage.task_id:
                list_of_field_dtos.append(field)
        return list_of_field_dtos

    @staticmethod
    def _get_list_of_actions_dtos_for_stage(action_dtos, stage):
        list_of_action_dtos = []
        if action_dtos:
            for action in action_dtos:
                if action.stage_id == stage.stage_id:
                    list_of_action_dtos.append(action)
        return list_of_action_dtos

    @staticmethod
    def _validate_stage_and_tasks(valid_task_stage_ids, task_dtos):
        import copy
        invalid_task_stage_ids = copy.deepcopy(task_dtos)
        for task in task_dtos:
            for valid_task in valid_task_stage_ids:
                task_id_condition = task.task_id == valid_task.task_id
                stage_id_condition = task.stage_id == valid_task.stage_id
                if task_id_condition and stage_id_condition:
                    invalid_task_stage_ids.remove(task)
        if invalid_task_stage_ids:
            raise InvalidTaskStageIds(invalid_task_stage_ids)
        return
