from collections import defaultdict
from datetime import datetime
from typing import List, Optional, Dict, Union

from django.db.models import Q, Count

from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskDisplayId
from ib_tasks.interactors.global_constants_dtos import GlobalConstantsDTO
from ib_tasks.interactors.gofs_dtos import GoFWithOrderAndAddAnotherDTO
from ib_tasks.interactors.storage_interfaces.actions_dtos import \
    ActionDTO, ActionWithStageIdDTO
from ib_tasks.interactors.storage_interfaces.fields_dtos import \
    FieldDetailsDTO, FieldCompleteDetailsDTO
from ib_tasks.interactors.storage_interfaces.get_task_dtos import \
    TemplateFieldsDTO, TaskBaseDetailsDTO
from ib_tasks.interactors.storage_interfaces.gof_dtos import GoFDTO, \
    GoFToTaskTemplateDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import \
    GetTaskStageCompleteDetailsDTO, StageIdWithTemplateIdDTO, \
    TaskIdWithStageValueDTO, TaskStagesDTO, StageDTO
from ib_tasks.interactors.storage_interfaces.status_dtos import \
    TaskTemplateStatusDTO, StatusVariableDTO
from ib_tasks.interactors.storage_interfaces.task_dtos import \
    TaskDisplayIdDTO, TaskProjectDTO, TaskDueMissingDTO, SubTasksCountDTO, \
    SubTasksIdsDTO
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface
from ib_tasks.interactors.storage_interfaces.task_templates_dtos import \
    TemplateDTO
from ib_tasks.interactors.task_dtos import CreateTaskLogDTO, GetTaskDetailsDTO, \
    TaskDelayParametersDTO
from ib_tasks.models import Stage, TaskTemplate, CurrentTaskStage, \
    TaskTemplateStatusVariable, TaskStageHistory, TaskStatusVariable, SubTask
from ib_tasks.models.field import Field
from ib_tasks.models.stage_actions import StageAction
from ib_tasks.models.task import Task, ElasticSearchTask
from ib_tasks.models.task_gof_field import TaskGoFField
from ib_tasks.models.task_template_gofs import TaskTemplateGoFs


class TasksStorageImplementation(TaskStorageInterface):

    def add_sub_task(self, sub_task_id: int, parent_task_id: int):
        SubTask.objects.create(task_id=parent_task_id, sub_task_id=sub_task_id)

    def validate_task_display_id_and_return_task_id(
            self, task_display_id: str) -> Union[InvalidTaskDisplayId, int]:
        try:
            task_id = Task.objects.get(task_display_id=task_display_id).id
        except Task.DoesNotExist:
            raise InvalidTaskDisplayId(task_display_id)
        else:
            return task_id

    def update_status_variables_to_task(
            self, task_id: int, status_variables_dto: List[StatusVariableDTO]):

        status_variable_objs = TaskStatusVariable.objects \
            .filter(task_id=task_id)
        status_variable_dict = \
            self._get_status_variable_dict(status_variable_objs)
        for status_variable_dto in status_variables_dto:
            status_obj = \
                status_variable_dict[status_variable_dto.status_id]
            status_obj.variable = status_variable_dto.status_variable
            status_obj.value = status_variable_dto.value
            status_obj.save()

    @staticmethod
    def _get_status_variable_dict(status_variable_objs):

        status_variable_dict = {}

        for status_variable_obj in status_variable_objs:
            status_id = status_variable_obj.id
            status_variable_dict[status_id] = status_variable_obj
        return status_variable_dict

    def get_status_variables_to_task(
            self, task_id: int) -> List[StatusVariableDTO]:

        status_variable_objs = TaskStatusVariable.objects \
            .filter(task_id=task_id)

        return [
            StatusVariableDTO(
                status_id=status_variable_obj.id,
                status_variable=status_variable_obj.variable,
                value=status_variable_obj.value
            ) for status_variable_obj in status_variable_objs
        ]

    def get_project_id_for_task_display_id(self, task_display_id: str):
        from ib_tasks.models.task import Task
        project_id = Task.objects.filter(task_display_id=task_display_id). \
            values_list('project_id', flat=True)
        return project_id.first()

    def get_tasks_with_max_stage_value_dto(
            self) -> List[TaskIdWithStageValueDTO]:
        pass

    def create_elastic_task(self, task_id: int, elastic_task_id: str):

        ElasticSearchTask.objects.create(
            task_id=task_id, elasticsearch_id=elastic_task_id
        )

    def get_field_types_for_given_field_ids(self, field_ids: List[str]) -> \
            List[FieldCompleteDetailsDTO]:
        field_type_dicts = list(
            Field.objects.filter(field_id__in=field_ids). \
                values('field_id', 'field_type')
        )
        field_type_dtos = self._prepare_field_type_dtos(field_type_dicts)
        return field_type_dtos

    @staticmethod
    def _prepare_field_type_dtos(field_type_dicts: List[Dict]):
        field_type_dtos = [
            FieldCompleteDetailsDTO(field_id=field_type_dict['field_id'],
                                    field_type=field_type_dict['field_type'])
            for field_type_dict in field_type_dicts
        ]
        return field_type_dtos

    def get_task_template_name_if_exists(self, template_id: str) -> str:
        pass

    @staticmethod
    def _get_matching_gof_dto(gof_id: str,
                              gof_dtos: List[GoFDTO]) -> Optional[GoFDTO]:
        for gof_dto in gof_dtos:
            gof_id_matched = gof_id == gof_dto.gof_id
            if gof_id_matched:
                return gof_dto
        return

    def get_existing_field_ids(self, field_ids: List[str]) -> List[str]:
        from ib_tasks.models.field import Field
        existing_field_ids = list(
            Field.objects.filter(
                field_id__in=field_ids
            ).values_list("field_id", flat=True)
        )
        return existing_field_ids

    def create_status_for_tasks(
            self, create_status_for_tasks: List[TaskTemplateStatusDTO]):
        list_of_status_tasks = [
            TaskTemplateStatusVariable(
                variable=status.status_variable_id,
                task_template_id=status.task_template_id)
            for status in create_status_for_tasks
        ]

        TaskTemplateStatusVariable.objects.bulk_create(list_of_status_tasks)

    def get_initial_stage_ids_of_templates(self) -> List[int]:
        from ib_tasks.models.task_template_initial_stages import \
            TaskTemplateInitialStage
        templates_initial_stage_ids_queryset = \
            TaskTemplateInitialStage.objects.all(). \
                values_list('stage_id', flat=True)
        templates_initial_stage_ids = \
            list(templates_initial_stage_ids_queryset)
        return templates_initial_stage_ids

    def create_stages_with_given_information(self,
                                             stage_information: StageDTO):
        pass

    def validate_stage_ids(self, stage_ids) -> Optional[List[str]]:
        pass

    def update_stages_with_given_information(self,
                                             update_stages_information:
                                             StageDTO):
        pass

    def validate_stages_related_task_template_ids(self,
                                                  task_stages_dto:
                                                  TaskStagesDTO) -> \
            Optional[List[TaskStagesDTO]]:
        pass

    @staticmethod
    def _get_global_constant_names(
            global_constants_dtos: List[GlobalConstantsDTO]):
        global_constants_names = [
            global_constants_dto.constant_name
            for global_constants_dto in global_constants_dtos
        ]
        return global_constants_names

    @staticmethod
    def _make_global_constants_dict(
            global_constants_dtos: List[GlobalConstantsDTO]):
        global_constants_dict = {}
        for global_constants_dto in global_constants_dtos:
            global_constants_dict[global_constants_dto.constant_name] = \
                global_constants_dto
        return global_constants_dict

    @staticmethod
    def _get_gof_ids(gof_dtos: List[GoFWithOrderAndAddAnotherDTO]):
        gof_ids = [gof_dto.gof_id for gof_dto in gof_dtos]
        return gof_ids

    @staticmethod
    def _make_gofs_dict(gof_dtos: List[GoFWithOrderAndAddAnotherDTO]):
        gofs_dict = {}
        for gof_dto in gof_dtos:
            gofs_dict[gof_dto.gof_id] = gof_dto
        return gofs_dict

    def get_task_details(self, task_dtos: List[GetTaskDetailsDTO]) -> \
            GetTaskStageCompleteDetailsDTO:
        task_ids = [task.task_id for task in task_dtos]
        task_objs = Task.objects.filter(id__in=task_ids).values('id',
                                                                'template_id')

        task_template_and_stage_ids = self._get_task_tempalate_and_stage_ids(
            task_dtos, task_objs)
        q = None
        for counter, item in enumerate(task_template_and_stage_ids):
            current_queue = Q(task_template_id=item['template_id'],
                              stage_id=item['stage_id'])
            if counter == 0:
                q = current_queue
            else:
                q = q | current_queue

        stage_objs = Stage.objects.filter(q).values('field_display_config',
                                                    'stage_id')

        stage_actions = self._get_stage_action_objs(
            task_template_and_stage_ids)
        stage_fields_dtos = self._get_fields_details(stage_objs)
        stage_actions_dtos = self._convert_stage_actions_to_dtos(stage_actions)

        return GetTaskStageCompleteDetailsDTO(
            fields_dto=stage_fields_dtos,
            actions_dto=stage_actions_dtos
        )

    @staticmethod
    def _get_task_tempalate_and_stage_ids(task_dtos, task_objs):
        task_template_and_stage_ids = []
        for task in task_objs:
            for task_dto in task_dtos:
                if task['id'] == task_dto.task_display_id:
                    task_template_and_stage_ids.append(
                        {
                            "template_id": task['template_id'],
                            "stage_id": task_dto.stage_id
                        }
                    )
        return task_template_and_stage_ids

    @staticmethod
    def _get_stage_action_objs(task_template_and_stage_ids):
        q = None
        for counter, item in enumerate(task_template_and_stage_ids):
            current_queue = Q(stage__task_template_id=item['template_id'],
                              stage__stage_id=item['stage_id'])
            if counter == 0:
                q = current_queue
            else:
                q = q | current_queue
        stage_actions = StageAction.objects.filter(q).values(
            'id', 'stage__stage_id', 'name', 'button_text', 'button_color')

        return stage_actions

    def _get_fields_details(self, stage_objs):
        fields_ids = [stage['field_display_config'] for stage in stage_objs]
        field_objs = Field.objects.filter(field_id__in=fields_ids).values(
            'field_id', 'field_type')
        field_response_objs = TaskGoFField.objects.filter(
            field_id__in=fields_ids).values('field_id', 'field_response')
        field_values = {}
        for item in field_response_objs:
            field_values[item['field_id']] = item['field_response']
        fields_dtos = []
        for stage in stage_objs:
            for field in field_objs:
                if field['field_id'] in stage['field_display_config']:
                    field_id = field['field_id']
                    fields_dtos.append(
                        self.get_field_dto(field, field_id, field_values,
                                           stage)
                    )
        return fields_dtos

    @staticmethod
    def get_field_dto(field, field_id, field_values, stage):
        return FieldDetailsDTO(
            field_id=field_id,
            field_type=field['field_type'],
            key=field['display_name'],
            value=field_values[field_id]
        )

    @staticmethod
    def _convert_stage_actions_to_dtos(stage_actions):
        stage_actions_dtos = []
        for stage in stage_actions:
            stage_actions_dtos.append(
                ActionDTO(
                    action_id=stage['id'],
                    name=stage['name'],
                    stage_id=stage['stage__stage_id'],
                    button_color=stage['button_color'],
                    button_text=stage['button_text']
                )
            )
        return stage_actions_dtos

    def get_valid_task_ids(self, task_ids: List[str]) -> Optional[List[str]]:
        valid_task_ids = (
            Task.objects.filter(id__in=task_ids)
                .values_list('id', flat=True))
        return list(valid_task_ids)

    def get_valid_task_display_ids(self, task_display_ids: List[str]) -> \
            Optional[List[str]]:
        valid_task_ids = (
            Task.objects.filter(task_display_id__in=task_display_ids)
                .values_list('task_display_id', flat=True))
        return list(valid_task_ids)

    @staticmethod
    def _convert_task_templates_objs_to_dtos(
            task_template_objs: List[TaskTemplate]) -> List[TemplateDTO]:
        task_template_dtos = [
            TemplateDTO(
                template_id=task_template_obj.template_id,
                template_name=task_template_obj.name
            )
            for task_template_obj in task_template_objs
        ]
        return task_template_dtos

    @staticmethod
    def _convert_task_template_gofs_to_dtos(
            task_template_gofs) -> List[GoFToTaskTemplateDTO]:
        task_template_gof_dtos = [
            GoFToTaskTemplateDTO(
                template_id=task_template_gof.task_template_id,
                gof_id=task_template_gof.gof_id,
                order=task_template_gof.order,
                enable_add_another=task_template_gof.enable_add_another_gof

            )
            for task_template_gof in task_template_gofs
        ]
        return task_template_gof_dtos

    def get_user_task_and_max_stage_value_dto_based_on_given_stage_ids(
            self, user_id: str, stage_ids: List[str], limit: int,
            offset: int) -> List[TaskIdWithStageValueDTO]:
        from django.db.models import Max
        task_objs_with_max_stage_value = list(
            CurrentTaskStage.objects.filter(
                task__created_by=user_id,
                stage__stage_id__in=stage_ids).values("task_id").annotate(
                stage_value=Max("stage__value"))[offset:limit])
        task_id_with_max_stage_value_dtos = []
        for task_with_stage_value_item in task_objs_with_max_stage_value:
            task_id_with_max_stage_value_dtos.append(
                TaskIdWithStageValueDTO(
                    task_id=task_with_stage_value_item['task_id'],
                    stage_value=task_with_stage_value_item['stage_value']))
        return task_id_with_max_stage_value_dtos

    def get_field_ids_for_given_task_template_ids(self,
                                                  task_template_ids: List[
                                                      str]) -> List[
        TemplateFieldsDTO]:
        task_field_objs = TaskTemplateGoFs.objects.filter(
            task_template_id__in=task_template_ids).values('task_template_id',
                                                           'gof__field')
        task_fields_dtos = self._convert_task_template_fields_to_dtos(
            task_field_objs)
        return task_fields_dtos

    @staticmethod
    def _convert_task_template_fields_to_dtos(task_field_objs):
        task_fields_dict = defaultdict(list)
        for task in task_field_objs:
            task_fields_dict[task['task_template_id']].append(
                task['gof__field'])

        task_fields_dtos = []
        for template_id, field_ids in task_fields_dict.items():
            task_fields_dtos.append(
                TemplateFieldsDTO(
                    task_template_id=template_id,
                    field_ids=field_ids
                )
            )
        return task_fields_dtos

    def get_initial_stage_id_with_template_id_dtos(
            self) -> List[StageIdWithTemplateIdDTO]:

        from ib_tasks.models.task_template_initial_stages import \
            TaskTemplateInitialStage
        template_id_with_stage_id_dicts = \
            TaskTemplateInitialStage.objects.all().values(
                'stage_id', 'task_template_id')

        template_id_with_stage_id_dtos = \
            self._convert_template_id_with_stage_id_dicts_to_dtos(
                template_id_with_stage_id_dicts=template_id_with_stage_id_dicts
            )
        return template_id_with_stage_id_dtos

    @staticmethod
    def _convert_template_id_with_stage_id_dicts_to_dtos(
            template_id_with_stage_id_dicts: List[Dict]
    ) -> List[StageIdWithTemplateIdDTO]:
        template_id_with_stage_id_dtos = [
            StageIdWithTemplateIdDTO(
                template_id=template_id_with_stage_id_dict['task_template_id'],
                stage_id=template_id_with_stage_id_dict['stage_id']
            )
            for template_id_with_stage_id_dict in
            template_id_with_stage_id_dicts
        ]
        return template_id_with_stage_id_dtos

    @staticmethod
    def _convert_stage_actions_details_to_dtos(
            stage_action_details: List[Dict]) -> List[ActionWithStageIdDTO]:
        actions_of_template_dtos = [
            ActionWithStageIdDTO(
                action_id=stage_action['id'],
                stage_id=stage_action['stage_id'],
                button_color=stage_action['button_color'],
                button_text=stage_action['button_text'],
                action_type=stage_action['action_type'],
                transition_template_id=stage_action['transition_template_id']
            )
            for stage_action in stage_action_details
        ]
        return actions_of_template_dtos

    def get_actions_for_given_stage_ids_in_dtos(
            self, stage_ids: List[int]) -> List[ActionWithStageIdDTO]:
        stage_action_details = StageAction.objects.filter(
            stage_id__in=stage_ids
        ).values(
            'id', 'button_text', 'button_color', 'stage_id',
            'action_type', 'transition_template_id'
        )

        action_with_stage_id_dtos = \
            self._convert_stage_actions_details_to_dtos(
                stage_action_details=stage_action_details
            )
        return action_with_stage_id_dtos

    def check_is_task_exists(self, task_id: int) -> bool:
        is_task_exists = Task.objects.filter(id=task_id).exists()
        return is_task_exists

    def get_task_project_id(self, task_id: int) -> str:
        task = Task.objects.get(id=task_id)
        return task.project_id

    def create_task_log(self, create_task_log_dto: CreateTaskLogDTO):
        from ib_tasks.models.task_log import TaskLog
        TaskLog.objects.create(
            task_json=create_task_log_dto.task_json,
            action_id=create_task_log_dto.action_id,
            user_id=create_task_log_dto.user_id,
            task_id=create_task_log_dto.task_id
        )

    def validate_task_related_stage_ids(self,
                                        task_dtos: List[GetTaskDetailsDTO]
                                        ) -> List[GetTaskDetailsDTO]:
        q = None
        for counter, item in enumerate(task_dtos):
            current_queue = Q(stage__stage_id=item.stage_id,
                              task_id=item.task_id)
            if counter == 0:
                q = current_queue
            else:
                q = q | current_queue
        if q is None:
            return []
        task_objs = CurrentTaskStage.objects.filter(q).values('task_id',
                                                              'stage__stage_id')

        task_stage_dtos = self._convert_task_objs_to_dtos(task_objs)
        return task_stage_dtos

    @staticmethod
    def _convert_task_objs_to_dtos(task_objs):
        valid_task_stages_dtos = [
            GetTaskDetailsDTO(task_id=task_obj['task_id'],
                              stage_id=task_obj['stage__stage_id'])
            for task_obj in task_objs
        ]
        return valid_task_stages_dtos

    def get_user_task_ids_and_max_stage_value_dto_based_on_given_stage_ids(
            self, stage_ids: List[str], task_ids: List[int]) -> List[
        TaskIdWithStageValueDTO]:
        from django.db.models import Max
        task_objs_with_max_stage_value = list(
            CurrentTaskStage.objects.filter(
                stage__stage_id__in=stage_ids,
                task_id__in=task_ids
            ).values("task_id").annotate(
                stage_value=Max("stage__value")
            )
        )
        task_id_with_max_stage_value_dtos = self. \
            _prepare_task_id_with_max_stage_value_dtos(
            task_objs_with_max_stage_value)
        return task_id_with_max_stage_value_dtos

    @staticmethod
    def _prepare_task_id_with_max_stage_value_dtos(
            task_objs_with_max_stage_value) \
            -> List[TaskIdWithStageValueDTO]:
        task_id_with_max_stage_value_dtos = []
        for task_with_stage_value_item in task_objs_with_max_stage_value:
            task_id_with_max_stage_value_dtos.append(
                TaskIdWithStageValueDTO(
                    task_id=task_with_stage_value_item['task_id'],
                    stage_value=task_with_stage_value_item['stage_value']))
        return task_id_with_max_stage_value_dtos

    def check_is_valid_task_display_id(self, task_display_id: str) -> bool:
        is_task_exists = \
            Task.objects.filter(task_display_id=task_display_id).exists()
        return is_task_exists

    def get_task_id_for_task_display_id(self, task_display_id: str) -> int:
        task_id_queryset = Task.objects.filter(
            task_display_id=task_display_id).values_list('id', flat=True)
        task_id = task_id_queryset.first()
        return task_id

    def get_task_display_ids_dtos(self, task_ids: List[int]) -> List[
        TaskDisplayIdDTO]:
        task_ids = Task.objects.filter(
            id__in=task_ids
        ).values('id', 'task_display_id')

        return [
            TaskDisplayIdDTO(
                task_id=task_id['id'],
                display_id=task_id['task_display_id']
            )
            for task_id in task_ids
        ]

    def get_task_ids_given_task_display_ids(self, task_display_ids: List[
        str]) -> List[TaskDisplayIdDTO]:
        task_ids = Task.objects.filter(
            task_display_id__in=task_display_ids
        ).values('id', 'task_display_id')

        return [
            TaskDisplayIdDTO(
                task_id=task_id['id'],
                display_id=task_id['task_display_id']
            )
            for task_id in task_ids
        ]

    def get_project_id_for_the_task_id(self, task_id) -> str:
        return Task.objects.get(id=task_id).project_id

    def get_project_id_of_task(self, task_id: int) -> str:
        task_obj = Task.objects.get(id=task_id)
        return task_obj.project_id

    def get_team_id(self, stage_id: int, task_id: int) -> str:
        team_ids = TaskStageHistory.objects.filter(
            task_id=task_id, stage_id=stage_id
        ).values_list('team_id', flat=True).order_by('-id')
        return team_ids[0]

    def get_task_due_datetime(
            self, task_id: int) -> \
            Optional[datetime]:
        task_due_time = Task.objects.filter(
            id=task_id
        ).values_list('due_date', flat=True)
        if task_due_time:
            return task_due_time[0]
        return None

    def get_valid_task_ids_from_the_project(self, task_ids: List[int],
                                            project_id: str):
        task_ids = Task.objects.filter(
            project_id=project_id
        ).values_list('id', flat=True)
        return list(task_ids)

    def get_task_project_ids(self, task_ids: List[int]) -> \
            List[TaskProjectDTO]:
        tasks = Task.objects.filter(id__in=task_ids)
        task_project_dtos = [
            TaskProjectDTO(
                task_id=task.id,
                project_id=task.project_id
            )
            for task in tasks
        ]
        return task_project_dtos

    def get_task_display_id_for_task_id(self, task_id: int) -> str:
        task_display_id = Task.objects.get(id=task_id).task_display_id
        return task_display_id

    def get_global_constants_to_task(
            self, task_id: int) -> List[GlobalConstantsDTO]:

        from ib_tasks.models.task import Task
        task_obj = Task.objects.get(id=task_id)
        from ib_tasks.models import GlobalConstant
        global_constant_objs = GlobalConstant.objects \
            .filter(task_template_id=task_obj.template_id)
        return [
            GlobalConstantsDTO(
                constant_name=global_constant_obj.name,
                value=global_constant_obj.value
            )
            for global_constant_obj in global_constant_objs
        ]

    def get_task_due_details(self, task_id: int, stage_id: int) -> \
            List[TaskDueMissingDTO]:
        from ib_tasks.models import UserTaskDelayReason
        task_due_objects = (
            UserTaskDelayReason.objects.filter(
                task_id=task_id, stage_id=stage_id
            ).values('due_datetime', 'count', 'reason', 'user_id',
                     'task__task_display_id'))

        task_due_details_dtos = self._convert_task_due_details_objs_to_dtos(
            task_due_objects)
        return task_due_details_dtos

    @staticmethod
    def _convert_task_due_details_objs_to_dtos(task_due_objs):
        task_due_details_dtos = []
        for task in task_due_objs:
            task_due_details_dtos.append(
                TaskDueMissingDTO(
                    task_id=task['task__task_display_id'],
                    due_date_time=task['due_datetime'],
                    due_missed_count=task['count'],
                    reason=task['reason'],
                    user_id=task['user_id']
                )
            )
        return task_due_details_dtos

    def add_due_delay_details(self, due_details: TaskDelayParametersDTO):
        user_id = due_details.user_id
        task_id = due_details.task_id
        reason_id = due_details.reason_id
        stage_id = due_details.stage_id
        updated_due_datetime = due_details.due_date_time
        from ib_tasks.models import UserTaskDelayReason
        count = UserTaskDelayReason.objects.filter(
            task_id=task_id, user_id=user_id, stage_id=stage_id).count()

        UserTaskDelayReason.objects.create(user_id=user_id, task_id=task_id,
                                           due_datetime=updated_due_datetime,
                                           count=count + 1,
                                           reason_id=reason_id,
                                           stage_id=stage_id,
                                           reason=due_details.reason)

    def update_task_due_datetime(self, due_details: TaskDelayParametersDTO):
        task_id = due_details.task_id
        updated_due_datetime = due_details.due_date_time

        Task.objects.filter(pk=task_id).update(due_date=updated_due_datetime)

    def get_base_details_to_task_ids(
            self, task_ids: List[int]
    ) -> List[TaskBaseDetailsDTO]:

        task_objs = Task.objects.filter(id__in=task_ids)
        return [
            self._get_task_base_details_dto(task_obj=task_obj)
            for task_obj in task_objs
        ]

    @staticmethod
    def _get_task_base_details_dto(task_obj: Task) -> TaskBaseDetailsDTO:
        task_base_details_dto = TaskBaseDetailsDTO(
            template_id=task_obj.template_id,
            project_id=task_obj.project_id,
            task_display_id=task_obj.task_display_id,
            title=task_obj.title,
            description=task_obj.description,
            start_date=task_obj.start_date,
            due_date=task_obj.due_date,
            priority=task_obj.priority,
            task_id=task_obj.id
        )
        return task_base_details_dto

    def get_sub_tasks_count_to_tasks(
            self, task_ids: List[int]
    ) -> List[SubTasksCountDTO]:
        sub_task_dicts = SubTask.objects.filter(task_id__in=task_ids) \
            .values("task_id").annotate(sub_tasks_count=Count("sub_task_id"))

        from collections import defaultdict
        task_sub_task_counts_map = defaultdict(int)
        for sub_task_dict in sub_task_dicts:
            task_id = sub_task_dict["task_id"]
            sub_tasks_count = sub_task_dict["sub_tasks_count"]
            task_sub_task_counts_map[task_id] = sub_tasks_count

        return [
            SubTasksCountDTO(
                task_id=task_id,
                sub_tasks_count=task_sub_task_counts_map.get(task_id, 0)
            )
            for task_id in task_ids
        ]

    def get_sub_task_ids_to_tasks(
            self, task_ids: List[int]
    ) -> List[SubTasksIdsDTO]:

        sub_task_objs = SubTask.objects.filter(task_id__in=task_ids)

        from collections import defaultdict
        task_sub_task_ids_map = defaultdict(list)
        for sub_task_obj in sub_task_objs:
            task_id = sub_task_obj.task_id
            sub_task_id = sub_task_obj.sub_task_id
            task_sub_task_ids_map[task_id].append(sub_task_id)

        return [
            SubTasksIdsDTO(
                task_id=task_id,
                sub_task_ids=task_sub_task_ids_map.get(task_id, [])
            )
            for task_id in task_ids
        ]
