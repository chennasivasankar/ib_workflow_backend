from typing import List

from django.db.models import F, Q

from ib_tasks.interactors.stages_dtos import StagesActionDTO
from ib_tasks.interactors.storage_interfaces.action_storage_interface import \
    ActionStorageInterface
from ib_tasks.interactors.storage_interfaces.stage_dtos import StageActionNamesDTO
from ib_tasks.models import StageAction, Stage, ActionPermittedRoles


class ActionsStorageImplementation(ActionStorageInterface):

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

    def create_stage_actions(self, stage_actions: List[StagesActionDTO]):
        list_of_actions = []
        list_of_permitted_roles = []
        names_list = [stage.action_name for stage in stage_actions]
        stage_ids = [stage.stage_id for stage in stage_actions]
        stages = Stage.objects.filter(stage_id__in=stage_ids).values('stage_id', 'id')

        list_of_stages = {}
        for item in stages:
            list_of_stages[item['stage_id']] = item['id']

        list_of_actions = self._get_list_of_action_objs_to_create(
            list_of_stages, stage_actions)

        StageAction.objects.bulk_create(list_of_actions)
        q = None
        for counter, item in enumerate(stage_actions):
            current_queue = Q(stage_id__stage_id=item.stage_id, name=item.action_name)
            if counter == 0:
                q = current_queue
            else:
                q = q | current_queue

        action_objs = StageAction.objects.filter(q)

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
                button_text=stage_action.button_text,
                button_color=stage_action.button_color
            ))
        return list_of_actions

    def update_stage_actions(self, stage_actions: List[StagesActionDTO]):
        # TODO: Optimize db hits
        for stage_action in stage_actions:
            StageAction.objects.filter(stage__stage_id=stage_action.stage_id,
                                       name=stage_action.action_name)\
                .update(
                logic=stage_action.logic,
                py_function_import_path=stage_action.function_path,
                button_text=stage_action.button_text,
                button_color=stage_action.button_color
            )
        action_objs = []
        for stage_action in stage_actions:
            action_objs.append(
                StageAction.objects.get(
                    name=stage_action.action_name, stage__stage_id=stage_action.stage_id))

        list_of_permitted_roles = self._get_list_of_permitted_roles_objs(
            action_objs, stage_actions)

        ActionPermittedRoles.objects.bulk_create(list_of_permitted_roles)

    @staticmethod
    def _get_list_of_permitted_roles_objs(action_objs,
                                          stage_actions):

        list_of_permitted_roles = []
        for action_obj in action_objs:
            for stage in stage_actions:
                if action_obj.name == stage.action_name:
                    for role in stage.roles:
                        list_of_permitted_roles.append(
                            ActionPermittedRoles(action_id=action_obj.id, role_id=role))
        return list_of_permitted_roles

    def delete_stage_actions(self, stage_actions: List[StageActionNamesDTO]):
        stage_actions_dict = [{'stage_id': stage.stage_id,
                               'action_names': stage.action_names}
                              for stage in stage_actions]
        q = None
        for counter, item in enumerate(stage_actions_dict):
            current_queue = Q(stage_id__stage_id=item['stage_id'], name__in=item["action_names"])
            if counter == 0:
                q = current_queue
            else:
                q = q | current_queue

        StageAction.objects.filter(q).delete()

