import collections
from typing import List, Dict

from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_tasks.exceptions.task_custom_exceptions import \
    TransitionTemplateDoesNotExist
from ib_tasks.interactors.presenter_interfaces. \
    get_transition_template_presenter_interface import \
    CompleteTransitionTemplateDTO, GetTransitionTemplatePresenterInterface
from ib_tasks.interactors.storage_interfaces.fields_dtos import \
    FieldDTO
from ib_tasks.interactors.storage_interfaces.gof_dtos import GoFDTO, \
    GoFToTaskTemplateDTO


class GetTransitionTemplatePresenterImplementation(
        GetTransitionTemplatePresenterInterface, HTTPResponseMixin):

    def raise_transition_template_does_not_exists_exception(
            self, err: TransitionTemplateDoesNotExist):
        from ib_tasks.constants.exception_messages import \
            TRANSITION_TEMPLATE_DOES_NOT_EXISTS

        response_dict = ({
            "response": TRANSITION_TEMPLATE_DOES_NOT_EXISTS[0].format(
                err.transition_template_id
            ),
            "http_status_code": 404,
            "res_status": TRANSITION_TEMPLATE_DOES_NOT_EXISTS[1]
        })
        return self.prepare_404_not_found_response(response_dict)

    def get_transition_template_response(
            self,
            complete_transition_template_dto: CompleteTransitionTemplateDTO):

        transition_template_dto = \
            complete_transition_template_dto.transition_template_dto
        gof_dtos = complete_transition_template_dto.gof_dtos
        gofs_of_transition_template_dtos = \
            complete_transition_template_dto.gofs_of_transition_template_dtos
        field_dtos = complete_transition_template_dto.field_dtos

        gofs_of_template_dicts = self._get_gofs_of_template_dicts(
            gofs_of_template_dtos=gofs_of_transition_template_dtos,
            gof_dtos=gof_dtos
        )
        fields_of_gofs_dict = self._get_fields_of_gofs_dict(
            field_dtos=field_dtos
        )
        complete_gof_details_dicts = self._merge_gofs_with_fields(
            gofs_of_template_dicts, fields_of_gofs_dict
        )
        complete_transition_template_dict = {
            'transition_template_id': transition_template_dto.template_id,
            "transition_template_name": transition_template_dto.template_name,
            "group_of_fields": complete_gof_details_dicts
        }

        return self.prepare_200_success_response(
            complete_transition_template_dict)

    def _get_gofs_of_template_dicts(
            self, gofs_of_template_dtos: List[GoFToTaskTemplateDTO],
            gof_dtos: List[GoFDTO]) -> List[Dict]:
        gof_details_dto_dict = self._get_gof_dto_dict(gof_dtos=gof_dtos)
        gof_details_dicts = \
            self._get_complete_gofs_details_dicts(
                gofs_of_template_dtos=gofs_of_template_dtos,
                gof_details_dto_dict=gof_details_dto_dict
            )
        return gof_details_dicts

    def _get_fields_of_gofs_dict(self, field_dtos: List[FieldDTO]) -> Dict:
        field_dicts = self._get_fields_details_dicts(field_dtos=field_dtos)
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
            self, field_dtos: List[FieldDTO]) -> List[Dict]:
        field_dicts = []
        for field_dto in field_dtos:
            field_dict = self._get_field_details_as_dict(field_dto=field_dto)
            field_dicts.append(field_dict)
        return field_dicts

    @staticmethod
    def _get_gof_dto_dict(gof_dtos: List[GoFDTO]):
        gof_dto_dict = {gof_dto.gof_id: gof_dto for gof_dto in gof_dtos}
        return gof_dto_dict

    @staticmethod
    def _get_complete_gofs_details_dicts(
            gofs_of_template_dtos: List[GoFToTaskTemplateDTO],
            gof_details_dto_dict: Dict) -> List[Dict]:
        gofs_to_template_dicts_list = []
        for gofs_to_task_templates_dto in gofs_of_template_dtos:
            gof_id = gofs_to_task_templates_dto.gof_id
            complete_gof_details_dict = {
                'gof_id': gof_id,
                'order': gofs_to_task_templates_dto.order,
                'enable_add_another':
                    gofs_to_task_templates_dto.enable_add_another,
                'gof_display_name': gof_details_dto_dict[
                    gof_id].gof_display_name,
                'max_columns': gof_details_dto_dict[gof_id].max_columns
            }
            gofs_to_template_dicts_list.append(complete_gof_details_dict)
        return gofs_to_template_dicts_list

    @staticmethod
    def _get_field_details_as_dict(field_dto: FieldDTO) -> Dict:
        # ToDo Remove is_field_readable in fields details
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
            "is_field_writable": True,
            "order": field_dto.order
        }
        return field_dict

    @staticmethod
    def _get_field_dicts_without_gof_id(field_dicts: List[Dict]) -> List[Dict]:
        for field_dict in field_dicts:
            field_dict.pop('gof_id')
        return field_dicts

    @staticmethod
    def _merge_gofs_with_fields(
            gofs_of_template_dicts: List[Dict],
            fields_of_gofs_dict: Dict) -> List[Dict]:
        for gof_details_dict in gofs_of_template_dicts:
            gof_details_dict['fields'] = \
                fields_of_gofs_dict[gof_details_dict['gof_id']]

        return gofs_of_template_dicts
