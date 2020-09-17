from typing import List, Optional, Dict

from django.db.models import F, Q

from ib_tasks.constants.constants import ALL_ROLES_ID
from ib_tasks.constants.enum import ActionTypes
from ib_tasks.exceptions.action_custom_exceptions import InvalidActionException
from ib_tasks.exceptions.stage_custom_exceptions import \
    (TransitionTemplateIsNotRelatedToGivenStageAction, InvalidStageId)
from ib_tasks.interactors.stages_dtos import (TemplateStageDTO,
                                              StageActionDTO,
                                              StageActionLogicDTO)
from ib_tasks.interactors.storage_interfaces.action_storage_interface import \
    ActionStorageInterface
from ib_tasks.interactors.storage_interfaces.actions_dtos import \
    StageActionDetailsDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import \
    StageActionNamesDTO, StageIdActionNameDTO, StageActionIdDTO
from ib_tasks.interactors.storage_interfaces.task_dtos import \
    TaskProjectRolesDTO
from ib_tasks.models import (StageAction, Stage, ActionPermittedRoles,
                             TaskTemplateInitialStage)


class ActionsStorageImplementation(ActionStorageInterface):

    def get_action_roles(self, action_id: int) -> List[str]:

        action_permitted_role_objs = \
            ActionPermittedRoles.objects.filter(action_id=action_id)

        return [
            obj.role_id for obj in action_permitted_role_objs
        ]

    def get_path_name_to_action(self, action_id: int) -> str:

        action_obj = StageAction.objects.get(id=action_id)
        return action_obj.py_function_import_path

    def validate_action_id(
            self, action_id) -> Optional[InvalidActionException]:
        try:
            StageAction.objects.get(id=action_id)
        except StageAction.DoesNotExist:
            raise InvalidActionException(action_id)
        return

    def validate_stage_id(self, stage_id) -> Optional[InvalidStageId]:
        try:
            Stage.objects.get(id=stage_id)
        except Stage.DoesNotExist:
            raise InvalidStageId(stage_id)
        return

    def validate_transition_template_id_is_related_to_given_stage_action(
            self, transition_checklist_template_id, action_id, stage_id
    ) -> Optional[TransitionTemplateIsNotRelatedToGivenStageAction]:
        transition_checklist_template_is_related_to_given_stage_action = \
            StageAction.objects.filter(
                transition_template_id=transition_checklist_template_id,
                stage_id=stage_id, id=action_id
            )
        if not transition_checklist_template_is_related_to_given_stage_action:
            raise TransitionTemplateIsNotRelatedToGivenStageAction(
                transition_checklist_template_id, action_id, stage_id
            )
        return

    def get_action_type_for_given_action_id(self,
                                            action_id: int) -> ActionTypes:
        action_type = StageAction.objects.get(id=action_id).action_type
        return action_type

    def get_stage_action_names(
            self, stage_ids: List[str]) -> List[StageActionNamesDTO]:
        stages = (StageAction.objects
                  .filter(stage_id__stage_id__in=stage_ids)
                  .annotate(stage_value_id=F('stage_id__stage_id'))
                  .values('stage_value_id', 'name'))

        from collections import defaultdict
        list_of_actions = defaultdict(list)
        for item in stages:
            list_of_actions[item['stage_value_id']].append(item['name'])

        list_of_dtos = self._convert_to_actions_dtos(list_of_actions)
        return list_of_dtos

    @staticmethod
    def _convert_to_actions_dtos(list_of_actions):
        list_of_dtos = []
        for key, value in list_of_actions.items():
            list_of_dtos.append(StageActionNamesDTO(
                stage_id=key,
                action_names=value
            ))
        return list_of_dtos

    def create_stage_actions(self, stage_actions: List[StageActionDTO]):
        stage_ids = [stage.stage_id for stage in stage_actions]
        stages = Stage.objects.filter(stage_id__in=stage_ids).values(
            'stage_id', 'id')

        list_of_stages = {}
        for item in stages:
            list_of_stages[item['stage_id']] = item['id']

        list_of_actions = self._get_list_of_action_objs_to_create(
            list_of_stages, stage_actions)

        StageAction.objects.bulk_create(list_of_actions)
        q = None
        for counter, item in enumerate(stage_actions):
            current_queue = Q(stage_id__stage_id=item.stage_id,
                              name=item.action_name)
            if counter == 0:
                q = current_queue
            else:
                q = q | current_queue

        action_objs = StageAction.objects.filter(q) \
            .annotate(normal_stage=F('stage__stage_id'))

        list_of_permitted_roles = self._get_list_of_permitted_roles_objs(
            action_objs, stage_actions)

        ActionPermittedRoles.objects.bulk_create(list_of_permitted_roles)

    @staticmethod
    def _get_list_of_action_objs_to_create(list_of_stages, stage_actions):
        list_of_actions = []
        for stage_action in stage_actions:
            list_of_actions.append(StageAction(
                stage_id=list_of_stages[stage_action.stage_id],
                name=stage_action.action_name,
                logic=stage_action.logic,
                py_function_import_path=stage_action.function_path,
                action_type=stage_action.action_type,
                transition_template_id=stage_action.transition_template_id,
                button_text=stage_action.button_text,
                button_color=stage_action.button_color
            ))
        return list_of_actions

    @staticmethod
    def _get_stage_action_dto_map(
            action_dtos: List[StageActionDTO]
    ) -> Dict[str, StageActionDTO]:

        return {
            action_dto.stage_id + action_dto.action_name: action_dto
            for action_dto in action_dtos
        }

    def update_stage_actions(self, stage_actions: List[StageActionDTO]):

        stage_action_dto_map = self._get_stage_action_dto_map(stage_actions)
        q = None
        for counter, item in enumerate(stage_actions):
            current_queue = Q(stage_id__stage_id=item.stage_id,
                              name=item.action_name)
            if counter == 0:
                q = current_queue
            else:
                q = q | current_queue
        action_objs = StageAction.objects.filter(q) \
            .annotate(normal_stage=F('stage__stage_id'))

        ActionPermittedRoles.objects.filter(action__in=action_objs).delete()

        list_of_permitted_roles = self._get_list_of_permitted_roles_objs(
            action_objs, stage_actions)

        ActionPermittedRoles.objects.bulk_create(list_of_permitted_roles)

        for action_obj in action_objs:
            key = action_obj.normal_stage + action_obj.name
            action_dto = stage_action_dto_map[key]
            action_obj.logic = action_dto.logic
            action_obj.py_function_import_path = action_dto.function_path
            action_obj.button_text = action_dto.button_text
            action_obj.action_type = action_dto.action_type
            action_obj.transition_template_id = \
                action_dto.transition_template_id
            action_obj.button_color = action_dto.button_color
        attributes = [
            "logic", "py_function_import_path", "button_text",
            "action_type", "transition_template_id", "button_color"
        ]
        StageAction.objects.bulk_update(action_objs, attributes)

    def _get_list_of_permitted_roles_objs(self, action_objs,
                                          stage_actions: List[StageActionDTO]):

        stage_id_action_name_roles_map = \
            self._get_stage_id_action_name_roles(stage_actions)

        action_roles = []
        for action_obj in action_objs:
            key = action_obj.normal_stage + action_obj.name
            roles = stage_id_action_name_roles_map[key]
            self._append_roles_to_permitted_roles(action_obj, roles,
                                                  action_roles)
        return action_roles

    @staticmethod
    def _append_roles_to_permitted_roles(
            action_obj, roles: List[str], action_roles
    ):
        for role in roles:
            action_roles.append(
                ActionPermittedRoles(
                    action_id=action_obj.id,
                    role_id=role
                )
            )

    @staticmethod
    def _get_stage_id_action_name_roles(
            stage_actions: List[StageActionDTO]):

        from collections import defaultdict
        stage_id_action_name_map = defaultdict()
        for stage_action in stage_actions:
            stage_id = stage_action.stage_id
            action_name = stage_action.action_name
            key = stage_id + action_name
            stage_id_action_name_map[key] = stage_action.roles
        return stage_id_action_name_map

    def delete_stage_actions(self, stage_actions: List[StageActionNamesDTO]):
        stage_actions_dict = [{'stage_id': stage.stage_id,
                               'action_names': stage.action_names}
                              for stage in stage_actions]
        q = None
        for counter, item in enumerate(stage_actions_dict):
            current_queue = Q(stage_id__stage_id=item['stage_id'],
                              name__in=item["action_names"])
            if counter == 0:
                q = current_queue
            else:
                q = q | current_queue

        StageAction.objects.filter(q).delete()

    def get_or_create_initial_stage_to_task_template(
            self, task_template_stage_dtos: List[TemplateStageDTO]):
        stage_ids = [stage.stage_id for stage in task_template_stage_dtos]
        stages = Stage.objects.filter(stage_id__in=stage_ids).values(
            'stage_id',
            'id')

        list_of_stages = {}
        for item in stages:
            list_of_stages[item['stage_id']] = item['id']

        for task in task_template_stage_dtos:
            TaskTemplateInitialStage.objects.get_or_create(
                task_template_id=task.task_template_id,
                stage_id=list_of_stages[task.stage_id]
            )

    def get_valid_task_template_ids(self, task_template_ids: List[str]):
        from ib_tasks.models.task_template import TaskTemplate
        valid_template_ids = list(
            TaskTemplate.objects.filter(pk__in=task_template_ids).
                values_list("template_id", flat=True)
        )
        return valid_template_ids

    def get_valid_stage_ids(self, stage_ids: List[str]) -> Optional[List[str]]:
        valid_stage_ids = Stage.objects.filter(
            stage_id__in=stage_ids
        ).values_list('stage_id', flat=True)

        return list(valid_stage_ids)

    def get_actions_details(self,
                            action_ids: List[int]) -> \
            List[StageActionDetailsDTO]:
        action_objs = (StageAction.objects
                       .filter(id__in=action_ids))
        unique_action_objs = list(set(action_objs))
        action_dtos = self._convert_action_objs_to_dtos(unique_action_objs)
        return action_dtos

    @staticmethod
    def _convert_action_objs_to_dtos(action_objs):
        action_dtos = []
        for action in action_objs:
            action_dtos.append(
                StageActionDetailsDTO(
                    action_id=action.id,
                    name=action.name,
                    stage_id=action.stage.stage_id,
                    button_text=action.button_text,
                    button_color=action.button_color,
                    action_type=action.action_type,
                    transition_template_id=action.transition_template_id
                )
            )
        return action_dtos

    def validate_action(self, action_id: int) -> bool:
        return StageAction.objects.filter(id=action_id).exists()

    def get_permitted_action_ids_given_stage_ids(self, user_roles: List[str],
                                                 stage_ids: List[str]) -> List[
        int]:
        action_ids = ActionPermittedRoles.objects.filter(
            Q(action__stage__stage_id__in=stage_ids),
            Q(role_id__in=user_roles) | Q(role_id=ALL_ROLES_ID)
        ).values_list('action_id', flat=True)
        return sorted(list(set(action_ids)))

    def get_stage_ids_having_actions(self, db_stage_ids: List[int]) \
            -> List[int]:
        db_stage_ids = \
            list(StageAction.objects.filter(
                stage_id__in=db_stage_ids).values_list(
                'stage_id', flat=True))
        return db_stage_ids

    def get_database_stage_actions(self) -> List[StageActionLogicDTO]:

        action_objs = StageAction.objects.all().annotate(
            stage_name=F('stage__stage_id'))
        return [
            StageActionLogicDTO(
                action_id=action_obj.id,
                stage_id=action_obj.stage_name,
                action_logic=action_obj.logic,
                action_name=action_obj.name,
                py_function_import_path=action_obj.py_function_import_path
            )
            for action_obj in action_objs
        ]

    def get_permitted_action_ids_for_given_task_stages(
            self, user_project_roles: List[TaskProjectRolesDTO],
            stage_ids):

        q = None
        for counter, item in enumerate(user_project_roles):
            current_queue = Q(role_id__in=item.roles) | Q(
                role_id=ALL_ROLES_ID) & \
                            Q(
                                action__stage__currenttaskstage__task=item.task_id) & \
                            Q(action__stage__stage_id__in=stage_ids)
            if counter == 0:
                q = current_queue
            else:
                q = q | current_queue
        if q is None:
            return []

        action_ids = (ActionPermittedRoles.objects.filter(
            q)
                      .values_list('action_id', flat=True))
        return list(set(action_ids))

    def get_stage_id_for_given_action_id(self, action_id: int) -> int:
        obj = StageAction.objects.get(id=action_id)
        return obj.stage_id

    def get_user_permitted_action_ids_given_stage_ids(
            self, user_roles: List[str],
            stage_ids: List[int]
    ) -> List[int]:
        action_ids = ActionPermittedRoles.objects.filter(
            action__stage_id__in=stage_ids
        ).filter(
            Q(role_id__in=user_roles) | Q(role_id=ALL_ROLES_ID)
        ).values_list('action_id', flat=True)
        return sorted(list(set(action_ids)))

    def get_action_ids_given_stage_ids(
            self, stage_ids: List[int]) -> List[int]:
        action_ids = StageAction.objects \
            .filter(stage_id__in=stage_ids) \
            .values_list('id', flat=True)
        return sorted(list(set(action_ids)))

    def get_stage_action_name_dtos(
            self, stage_id_action_dtos: List[StageIdActionNameDTO]
    ) -> List[StageActionIdDTO]:

        q = None
        for counter, item in enumerate(stage_id_action_dtos):
            current_queue = Q(stage__stage_id=item.stage_id,
                              name=item.action_name)
            if counter == 0:
                q = current_queue
            else:
                q = q | current_queue
        if q is None:
            q = []
        action_objs = StageAction.objects.filter(q) \
            .annotate(normal_stage_id=F('stage__stage_id'))

        return [
            StageActionIdDTO(
                stage_id=action_obj.normal_stage_id,
                action_id=action_obj.id,
                action_name=action_obj.name
            )
            for action_obj in action_objs
        ]

    def get_task_present_stage_actions(self, task_id: int):

        from ib_tasks.models import CurrentTaskStage
        task_stage_ids = CurrentTaskStage.objects.filter(task_id=task_id) \
            .values_list('stage_id', flat=True)
        action_ids = StageAction.objects.filter(stage_id__in=task_stage_ids) \
            .values_list('id', flat=True)
        return action_ids