from typing import List, Dict
from ib_tasks.interactors.presenter_interfaces. \
    get_task_templates_presenter_interface import \
    GetTaskTemplatesPresenterInterface, CompleteTaskTemplatesDTO
from ib_tasks.interactors.storage_interfaces.actions_dtos import \
    ActionsOfTemplateDTO
from ib_tasks.interactors.storage_interfaces.fields_dtos import \
    FieldWithPermissionsDTO
from ib_tasks.interactors.storage_interfaces.gof_dtos import GoFDTO, \
    GoFToTaskTemplateDTO
from ib_tasks.interactors.storage_interfaces.task_templates_dtos import \
    TaskTemplateDTO
from ib_tasks.exceptions.task_custom_exceptions import \
    TaskTemplatesDoesNotExists


class GetTaskTemplatesPresenterImplementation(
    GetTaskTemplatesPresenterInterface):

    def raise_task_templates_does_not_exists_exception(
            self, err: TaskTemplatesDoesNotExists):
        import json
        from django.http import response
        from ib_tasks.constants.exception_messages import \
            TASK_TEMPLATES_DOES_NOT_EXISTS

        data = json.dumps({
            "response": TASK_TEMPLATES_DOES_NOT_EXISTS[0],
            "http_status_code": 404,
            "res_status": TASK_TEMPLATES_DOES_NOT_EXISTS[1]
        })
        response_object = response.HttpResponse(data, status=404)
        return response_object

    def get_task_templates_response(
            self, complete_task_templates_dto: CompleteTaskTemplatesDTO):
        task_templates_dicts = self._get_task_templates_in_dicts(
            task_templates_dtos=complete_task_templates_dto.task_template_dtos
        )
        actions_of_templates_dict = self.get_actions_of_templates_dict(
            actions_of_templates_dtos=complete_task_templates_dto.actions_of_templates_dtos
        )
        gofs_of_templates_dict = self._get_gofs_of_templates_dict(
            gofs_to_task_templates_dtos=complete_task_templates_dto.gofs_to_task_templates_dtos,
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

    def get_actions_of_templates_dict(
            self, actions_of_templates_dtos: List[ActionsOfTemplateDTO]
    ) -> Dict:
        actions_of_templates_dicts_list = \
            self._convert_action_dtos_into_list_of_dicts(
                actions_of_template_dtos=actions_of_templates_dtos
            )

        import collections
        actions_group_by_template_id_dict = collections.defaultdict(list)
        for action_dict in actions_of_templates_dicts_list:
            actions_group_by_template_id_dict[action_dict['template_id']]. \
                append(action_dict)

        actions_of_templates_dict = collections.defaultdict(list)
        for template_id, action_dicts_list in actions_group_by_template_id_dict.items():
            action_dicts_list_with_out_template_id = \
                self._get_action_dicts_list_without_template_id(
                    action_dicts_list=action_dicts_list
                )
            actions_of_templates_dict[template_id] = \
                action_dicts_list_with_out_template_id
        return actions_of_templates_dict

    def _get_gofs_of_templates_dict(
            self, gofs_to_task_templates_dtos: List[GoFToTaskTemplateDTO],
            gof_dtos: List[GoFDTO]):
        gof_details_dto_dict = self._get_gof_dto_dict(gof_dtos=gof_dtos)
        gof_details_dicts = \
            self.get_complete_gofs_details_dicts(
                gofs_to_task_templates_dtos=gofs_to_task_templates_dtos,
                gof_details_dto_dict=gof_details_dto_dict
            )

        import collections
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
            self, field_with_permissions_dtos: List[FieldWithPermissionsDTO]):
        field_dicts = self._get_fields_details_dicts(
            field_with_permissions_dtos=field_with_permissions_dtos
        )

        import collections
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
            self, field_with_permissions_dtos: List[FieldWithPermissionsDTO]
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
    def get_complete_gofs_details_dicts(
            gofs_to_task_templates_dtos: List[GoFToTaskTemplateDTO],
            gof_details_dto_dict: Dict) -> List[Dict]:
        gofs_to_task_templates_dicts_list = []
        for gofs_to_task_templates_dto in gofs_to_task_templates_dtos:
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
    def _convert_action_dtos_into_list_of_dicts(
            actions_of_template_dtos: List[ActionsOfTemplateDTO]
    ) -> List[Dict]:
        actions_of_templates_dicts_list = []
        for action_dto in actions_of_template_dtos:
            action_dict = {
                "template_id": action_dto.template_id,
                "action_id": action_dto.action_id,
                "button_text": action_dto.button_text,
                "button_color": action_dto.button_color
            }
            actions_of_templates_dicts_list.append(action_dict)
        return actions_of_templates_dicts_list

    @staticmethod
    def _get_field_details_as_dict(
            field_with_permissions_dto: FieldWithPermissionsDTO) -> Dict:
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
            "is_field_readable": field_with_permissions_dto.is_field_readable,
            "is_field_writable": field_with_permissions_dto.is_field_writable
        }
        return field_dict

    @staticmethod
    def _get_action_dicts_list_without_template_id(
            action_dicts_list: List[Dict]) -> List[Dict]:
        for action_dict in action_dicts_list:
            action_dict.pop('template_id')
        return action_dicts_list

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
