from typing import List

from ib_tasks.constants.enum import ViewType
from ib_tasks.interactors.storage_interfaces.fields_dtos import TaskTemplateStageFieldsDTO, StageTaskFieldsDTO
from ib_tasks.interactors.storage_interfaces.fields_storage_interface \
    import FieldsStorageInterface
from ib_tasks.interactors.storage_interfaces.stage_dtos import TaskTemplateStageDTO
from ib_tasks.interactors.storage_interfaces.task_dtos import TaskProjectDTO
from ib_tasks.interactors.user_role_validation_interactor import UserRoleValidationInteractor


class GetTaskFieldsInteractor:
    def __init__(self, field_storage: FieldsStorageInterface):
        self.field_storage = field_storage

    def get_task_fields(self, task_stage_dtos: List[TaskTemplateStageDTO],
                        task_project_dtos: List[TaskProjectDTO],
                        user_id: str,
                        view_type: ViewType):
        user_roles_interactor = UserRoleValidationInteractor()
        stage_fields_dtos = self.field_storage.get_field_ids(task_stage_dtos, view_type)
        list_of_field_ids = self._get_field_ids(stage_fields_dtos)
        permitted_field_ids = user_roles_interactor. \
            get_field_ids_having_permission_for_user(
            task_project_dtos=task_project_dtos, user_id=user_id,
            field_ids=list_of_field_ids, field_storage=self.field_storage)

        task_fields_dtos = self._map_task_and_their_fields(
            stage_fields_dtos, task_stage_dtos, permitted_field_ids)
        field_dtos = self.field_storage.get_fields_details(
            task_fields_dtos)
        return field_dtos

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
                                  field_ids=valid_field_ids)
