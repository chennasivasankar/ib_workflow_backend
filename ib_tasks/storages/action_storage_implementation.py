from typing import List

from django.db.models import F

from ib_tasks.interactors.dtos import StagesActionDTO
from ib_tasks.interactors.storage_interfaces.action_storage_interface import \
    ActionStorageInterface
from ib_tasks.interactors.storage_interfaces.dtos import StageActionNamesDTO
from ib_tasks.models import StageAction, Stage, ActionPermittedRoles


class ActionsStorageImplementation(ActionStorageInterface):

    def get_stage_action_names(
            self, stage_ids: List[str]) -> List[StageActionNamesDTO]:
        stages = (StageAction.objects
                  .filter(stage__stage_id__in=stage_ids)
                  .annotate(stage_value_id=F('stage__stage_id'))
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

        for stage_action in stage_actions:
            list_of_actions.append(StageAction(
                stage_id=list_of_stages[stage_action.stage_id],
                name=stage_action.action_name,
                logic=stage_action.logic,
                py_function_import_path=stage_action.function_path,
                button_text=stage_action.button_text,
                button_color=stage_action.button_color
            ))

        StageAction.objects.bulk_create(list_of_actions)
        action_objs = StageAction.objects.filter(name__in=names_list)

        for action_obj in action_objs:
            for stage in stage_actions:
                if action_obj.name == stage.action_name:
                    list_of_permitted_roles.append(
                        ActionPermittedRoles(action_id=action_obj, role_id=stage_action.roles))

        ActionPermittedRoles.objects.bulk_create(list_of_permitted_roles)

    def update_stage_actions(self, stage_actions: List[StagesActionDTO]):
        pass

    def delete_stage_actions(self, stage_actions: List[StageActionNamesDTO]):
        pass
