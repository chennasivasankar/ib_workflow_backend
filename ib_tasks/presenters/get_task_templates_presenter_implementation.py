import collections
from typing import List, Dict
from ib_tasks.interactors.presenter_interfaces. \
    get_task_templates_presenter_interface import \
    GetTaskTemplatesPresenterInterface, CompleteTaskTemplatesDTO
from ib_tasks.interactors.storage_interfaces.actions_dtos import \
    ActionWithStageIdDTO
from ib_tasks.interactors.storage_interfaces.fields_dtos import \
    FieldWithWritePermissionDTO
from ib_tasks.interactors.storage_interfaces.gof_dtos import GoFDTO, \
    GoFToTaskTemplateDTO
from ib_tasks.interactors.storage_interfaces.task_templates_dtos import \
    TaskTemplateDTO
from ib_tasks.exceptions.task_custom_exceptions import \
    TaskTemplatesDoesNotExists
from ib_tasks.interactors.storage_interfaces.stage_dtos import \
    StageIdWithTemplateIdDTO


class GetTaskTemplatesPresenterImplementation(
        GetTaskTemplatesPresenterInterface):

    def raise_task_templates_does_not_exists_exception(
            self, err: TaskTemplatesDoesNotExists):
        import json
        from django.http import response

        data = json.dumps({
            "response": err.message[0],
            "http_status_code": 404,
            "res_status": err.message[1]
        })
        response_object = response.HttpResponse(data, status=404)
        return response_object

    def get_task_templates_response(
            self, complete_task_templates_dto: CompleteTaskTemplatesDTO):
        task_templates_dicts = self._get_task_templates_in_dicts(
            task_templates_dtos=complete_task_templates_dto.task_template_dtos
        )
        actions_of_templates_dict = self._get_actions_of_templates_dict(
            action_with_stage_id_dtos=complete_task_templates_dto.action_with_stage_id_dtos,
            stage_id_with_template_id_dtos=complete_task_templates_dto.stage_id_with_template_id_dtos
        )
        gofs_of_templates_dict = self._get_gofs_of_templates_dict(
            gofs_of_task_templates_dtos=complete_task_templates_dto.gofs_of_task_templates_dtos,
            gof_dtos=complete_task_templates_dto.gof_dtos
        )
        fields_of_gofs_dict = self._get_fields_of_gofs_dict(
            field_with_permissions_dtos=complete_task_templates_dto.field_with_permissions_dtos
        )
        complete_gof_details_dicts = self._merge_gofs_with_fields(
            gofs_of_templates_dict, fields_of_gofs_dict
        )
        for task_template in task_templates_dicts:
            task_template_id = task_template['template_id']
            task_template['actions'] = actions_of_templates_dict[
                task_template_id]
            task_template['group_of_fields'] = complete_gof_details_dicts[
                task_template_id]

        import json
        from django.http import response
        data = json.dumps({"task_templates": task_templates_dicts})
        response_object = response.HttpResponse(data, status=200)
        return response_object

    def _get_actions_of_templates_dict(
            self, action_with_stage_id_dtos: List[ActionWithStageIdDTO],
            stage_id_with_template_id_dtos: List[StageIdWithTemplateIdDTO]
    ) -> Dict:

        stage_ids_group_by_template_id_dict = collections.defaultdict(list)
        for stage_id_with_template_id_dto in stage_id_with_template_id_dtos:
            stage_ids_group_by_template_id_dict[
                stage_id_with_template_id_dto.template_id].append(
                stage_id_with_template_id_dto.stage_id
            )
        actions_with_stage_id_dto_dict = \
            self._convert_action_dtos_into_dict(
                action_with_stage_id_dtos=action_with_stage_id_dtos,
            )

        actions_of_templates_dict = collections.defaultdict(list)
        for template_id, stage_ids in stage_ids_group_by_template_id_dict.items():
            for stage_id in stage_ids:
                action_dicts_list = \
                    self._convert_action_dtos_into_action_details_dict(
                        action_with_stage_id_dtos=
                        actions_with_stage_id_dto_dict[stage_id]
                    )
                actions_of_templates_dict[template_id] += action_dicts_list
        return actions_of_templates_dict

    def _get_gofs_of_templates_dict(
            self, gofs_of_task_templates_dtos: List[GoFToTaskTemplateDTO],
            gof_dtos: List[GoFDTO]) -> Dict:
        gof_details_dto_dict = self._get_gof_dto_dict(gof_dtos=gof_dtos)
        gof_details_dicts = \
            self._get_complete_gofs_details_dicts(
                gofs_of_task_templates_dtos=gofs_of_task_templates_dtos,
                gof_details_dto_dict=gof_details_dto_dict
            )
        gofs_details_group_by_template_id_dict = collections.defaultdict(list)
        for gof_details_dict in gof_details_dicts:
            gofs_details_group_by_template_id_dict[
                gof_details_dict['template_id']]. \
                append(gof_details_dict)
        gofs_details_of_templates_dict = collections.defaultdict(list)
        for template_id, gof_details_dicts in gofs_details_group_by_template_id_dict.items():
            gofs_details_dicts_without_template_id = \
                self._get_gof_details_dicts_without_template_id(
                    gof_details_dicts=gof_details_dicts
                )
            gofs_details_of_templates_dict[template_id] = \
                gofs_details_dicts_without_template_id
        return gofs_details_of_templates_dict

    def _get_fields_of_gofs_dict(
            self,
            field_with_permissions_dtos: List[FieldWithWritePermissionDTO]):
        field_dicts = self._get_fields_details_dicts(
            field_with_permissions_dtos=field_with_permissions_dtos
        )
        fields_group_by_gof_id_dict = collections.defaultdict(list)
        for field_dict in field_dicts:
            fields_group_by_gof_id_dict[field_dict['gof_id']].append(
                field_dict)
        fields_of_gofs_dict = collections.defaultdict(list)
        for gof_id, field_dicts in fields_group_by_gof_id_dict.items():
            field_dicts_without_gof_id = \
                self._get_field_dicts_without_gof_id(field_dicts=field_dicts)
            fields_of_gofs_dict[gof_id] = field_dicts_without_gof_id
        return fields_of_gofs_dict

    def _get_fields_details_dicts(
            self,
            field_with_permissions_dtos: List[FieldWithWritePermissionDTO]
    ) -> List[Dict]:
        field_dicts = []
        for field_with_permissions_dto in field_with_permissions_dtos:
            field_dict = self._get_field_details_as_dict(
                field_with_permissions_dto=field_with_permissions_dto
            )
            field_dicts.append(field_dict)
        return field_dicts

    @staticmethod
    def _get_task_templates_in_dicts(
            task_templates_dtos: List[TaskTemplateDTO]) -> List[Dict]:
        task_templates_dicts_list = []
        for task_template_dto in task_templates_dtos:
            task_template_details = {
                "template_id": task_template_dto.template_id,
                "template_name": task_template_dto.template_name
            }
            task_templates_dicts_list.append(task_template_details)
        return task_templates_dicts_list

    @staticmethod
    def _get_gof_dto_dict(gof_dtos: List[GoFDTO]):
        gof_dto_dict = {gof_dto.gof_id: gof_dto for gof_dto in gof_dtos}
        return gof_dto_dict

    @staticmethod
    def _get_complete_gofs_details_dicts(
            gofs_of_task_templates_dtos: List[GoFToTaskTemplateDTO],
            gof_details_dto_dict: Dict) -> List[Dict]:
        gofs_to_task_templates_dicts_list = []
        for gofs_to_task_templates_dto in gofs_of_task_templates_dtos:
            gof_id = gofs_to_task_templates_dto.gof_id
            complete_gof_details_dict = {
                'gof_id': gof_id,
                'template_id': gofs_to_task_templates_dto.template_id,
                'order': gofs_to_task_templates_dto.order,
                'enable_add_another': gofs_to_task_templates_dto.enable_add_another,
                'gof_display_name': gof_details_dto_dict[
                    gof_id].gof_display_name,
                'max_columns': gof_details_dto_dict[gof_id].max_columns
            }
            gofs_to_task_templates_dicts_list.append(complete_gof_details_dict)
        return gofs_to_task_templates_dicts_list

    @staticmethod
    def _convert_action_dtos_into_action_details_dict(
            action_with_stage_id_dtos: List[ActionWithStageIdDTO]
    ) -> List[Dict]:
        action_dicts_list = []
        for action_with_stage_id_dto in action_with_stage_id_dtos:
            action_dict = {
                "action_id": action_with_stage_id_dto.action_id,
                "button_text": action_with_stage_id_dto.button_text,
                "button_color": action_with_stage_id_dto.button_color
            }
            action_dicts_list.append(action_dict)
        return action_dicts_list

    @staticmethod
    def _get_field_details_as_dict(
            field_with_permissions_dto: FieldWithWritePermissionDTO) -> Dict:
        field_dto = field_with_permissions_dto.field_dto
        field_dict = {
            "field_id": field_dto.field_id,
            'gof_id': field_dto.gof_id,
            "field_type": field_dto.field_type,
            "display_name": field_dto.field_display_name,
            "is_field_required": field_dto.required,
            "field_values": field_dto.field_values,
            "allowed_formats": field_dto.allowed_formats,
            "validation_regex": field_dto.validation_regex,
            "error_msg": field_dto.error_message,
            "tooltip": field_dto.tooltip,
            "help_text": field_dto.help_text,
            "placeholder_text": field_dto.placeholder_text,
            "is_field_writable": field_with_permissions_dto.is_field_writable
        }
        return field_dict

    @staticmethod
    def _get_gof_details_dicts_without_template_id(
            gof_details_dicts: List[Dict]) -> List[Dict]:
        for gof_details_dict in gof_details_dicts:
            gof_details_dict.pop('template_id')
        return gof_details_dicts

    @staticmethod
    def _get_field_dicts_without_gof_id(field_dicts: List[Dict]) -> List[Dict]:
        for field_dict in field_dicts:
            field_dict.pop('gof_id')
        return field_dicts

    @staticmethod
    def _merge_gofs_with_fields(
            gofs_details_of_templates_dict: Dict,
            fields_of_gofs_dict: Dict) -> Dict:
        for gof_details_dicts in gofs_details_of_templates_dict.values():
            for gof_details_dict in gof_details_dicts:
                gof_details_dict['fields'] = \
                    fields_of_gofs_dict[gof_details_dict['gof_id']]
        return gofs_details_of_templates_dict

    @staticmethod
    def _convert_action_dtos_into_dict(
            action_with_stage_id_dtos: List[ActionWithStageIdDTO]) -> Dict:
        actions_with_stage_id_dict = collections.defaultdict(list)
        for action_with_stage_id_dto in action_with_stage_id_dtos:
            actions_with_stage_id_dict[
                action_with_stage_id_dto.stage_id].append(
                action_with_stage_id_dto)
        return actions_with_stage_id_dict
