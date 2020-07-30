from typing import List, Optional

from django.db.models import Q

from ib_tasks.interactors.stages_dtos import TemplateStageDTO
from ib_tasks.interactors.storage_interfaces.actions_dtos import ActionDetailsDTO
from ib_tasks.interactors.storage_interfaces.fields_dtos import FieldDetailsDTO, StageTaskFieldsDTO, \
    TaskTemplateStageFieldsDTO, TaskAndFieldsDTO
from ib_tasks.interactors.storage_interfaces.fields_storage_interface import FieldsStorageInterface
from ib_tasks.interactors.storage_interfaces.stage_dtos import GetTaskStageCompleteDetailsDTO, TaskTemplateStageDTO
from ib_tasks.interactors.task_dtos import GetTaskDetailsDTO
from ib_tasks.models import TaskStage, StageAction, Stage, Field
from ib_tasks.models.task import Task
from ib_tasks.models.task_gof_field import TaskGoFField


class FieldsStorageImplementation(FieldsStorageInterface):
    def get_stage_details(self, task_dtos: List[GetTaskDetailsDTO]) -> \
            List[TaskTemplateStageDTO]:
        task_ids = [task.task_id for task in task_dtos]
        task_objs = Task.objects.filter(id__in=task_ids
                                        ).values('id', 'template_id')
        template_stage_ids_list = []
        task_stages_dict = {}
        for item in task_dtos:
            task_stages_dict[item.task_id] = item.stage_id
        for task in task_objs:
            template_stage_ids_list.append(
                TaskTemplateStageDTO(
                    task_id=task['id'],
                    task_template_id=task['template_id'],
                    stage_id=task_stages_dict[task['id']]
                )
            )
        return template_stage_ids_list

    def get_actions_details(self,
                            stage_ids: List[str]) -> \
            List[ActionDetailsDTO]:
        action_objs = StageAction.objects.filter(stage__stage_id__in=stage_ids)
        action_dtos = self._convert_action_objs_to_dtos(action_objs)
        return action_dtos

    @staticmethod
    def _convert_action_objs_to_dtos(action_objs):
        action_dtos = []
        for action in action_objs:
            action_dtos.append(
                ActionDetailsDTO(
                    action_id=action.id,
                    name=action.name,
                    stage_id=action.stage.stage_id,
                    button_text=action.button_text,
                    button_color=action.button_color
                )
            )
        return action_dtos

    def get_fields_details(self, task_fields_dtos: List[StageTaskFieldsDTO]) -> \
            List[FieldDetailsDTO]:
        q = None
        for counter, item in enumerate(task_fields_dtos):
            current_queue = Q(task_gof__task_id=item.task_id, field_id__in=item.field_ids)
            if counter == 0:
                q = current_queue
            else:
                q = q | current_queue

        field_objs = TaskGoFField.objects.filter(q).select_related(
            'field', 'task_gof'
        )
        task_fields_dtos = self._convert_field_objs_to_dtos(field_objs)
        return task_fields_dtos

    @staticmethod
    def _convert_field_objs_to_dtos(field_objs):
        task_fields_dtos = []
        for field in field_objs:
            task_fields_dtos.append(
                FieldDetailsDTO(
                    field_id=field.field_id,
                    value=field.field_response,
                    key=field.field.display_name,
                    field_type=field.field.field_type
                )
            )
        return task_fields_dtos

    def get_valid_task_ids(self, task_ids: List[str]) -> Optional[List[str]]:
        valid_task_ids = Task.objects.filter(id__in=task_ids).values_list('id', flat=True)
        return list(valid_task_ids)

    def get_field_ids(self, task_dtos: List[TaskTemplateStageDTO]) -> \
            List[TaskTemplateStageFieldsDTO]:
        print(Stage.objects.all().values())
        task_stages_dict = {}
        for item in task_dtos:
            task_stages_dict[item.stage_id] = item.task_id

        q = None
        for counter, item in enumerate(task_dtos):
            current_queue = Q(stage_id=item.stage_id, task_template_id=item.task_template_id)
            if counter == 0:
                q = current_queue
            else:
                q = q | current_queue
        stage_objs = Stage.objects.filter(q)
        task_fields_dtos = self._convert_stage_objs_to_dtos(stage_objs, task_stages_dict)
        return task_fields_dtos

    @staticmethod
    def _convert_stage_objs_to_dtos(stage_objs, task_stages_dict):
        task_fields_dtos = []
        import json
        for stage in stage_objs:
            fields = stage.field_display_config
            field_ids = json.loads(fields)
            task_fields_dtos.append(
                TaskTemplateStageFieldsDTO(
                    task_template_id=stage.task_template_id,
                    task_id=task_stages_dict[stage.stage_id],
                    stage_id=stage.stage_id,
                    field_ids=field_ids
                )
            )
        return task_fields_dtos

    def validate_task_related_stage_ids(self,
                                        task_dtos: List[GetTaskDetailsDTO]) -> \
            List[GetTaskDetailsDTO]:
        q = None
        for counter, item in enumerate(task_dtos):
            current_queue = Q(stage__stage_id=item.stage_id, task_id=item.task_id)
            if counter == 0:
                q = current_queue
            else:
                q = q | current_queue
        task_objs = TaskStage.objects.filter(q).values('task_id', 'stage__stage_id')
        task_stage_dtos = self._convert_task_objs_to_dtos(task_objs)
        return task_stage_dtos

    def _convert_task_objs_to_dtos(self, task_objs):
        valid_task_stages_dtos = [
            GetTaskDetailsDTO(
                task_id=task_obj['task_id'],
                stage_id=task_obj['stage__stage_id']
            )
            for task_obj in task_objs
        ]
        return valid_task_stages_dtos
