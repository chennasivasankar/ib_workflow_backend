import collections
from typing import List, Dict

from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_tasks.interactors.presenter_interfaces. \
    get_task_templates_presenter_interface import \
    GetTaskTemplatesPresenterInterface, CompleteTaskTemplatesDTO
from ib_tasks.interactors.storage_interfaces.actions_dtos import \
    ActionWithStageIdDTO
from ib_tasks.interactors.storage_interfaces.fields_dtos import \
    FieldPermissionDTO
from ib_tasks.interactors.storage_interfaces.gof_dtos import GoFDTO, \
    GoFToTaskTemplateDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import \
    StageIdWithTemplateIdDTO, StageGoFWithTemplateIdDTO
from ib_tasks.interactors.storage_interfaces.task_templates_dtos import \
    TemplateDTO, ProjectIdWithTaskTemplateIdDTO


class GetTaskTemplatesPresenterImplementation(
        GetTaskTemplatesPresenterInterface, HTTPResponseMixin):

    def raise_task_templates_does_not_exists_exception(self):

        from ib_tasks.constants.exception_messages import \
            TASK_TEMPLATES_DOES_NOT_EXISTS
        response_dict = ({
            "response": TASK_TEMPLATES_DOES_NOT_EXISTS[0],
            "http_status_code": 404,
            "res_status": TASK_TEMPLATES_DOES_NOT_EXISTS[1]
        })
        return self.prepare_404_not_found_response(response_dict)

    def get_task_templates_response(
            self, complete_task_templates_dto: CompleteTaskTemplatesDTO):
        task_templates_dicts = self._get_task_templates_in_dicts(
            task_templates_dtos=complete_task_templates_dto.task_template_dtos)
        actions_of_templates_dict = self._get_actions_of_templates_dict(
            action_with_stage_id_dtos=
            complete_task_templates_dto.action_with_stage_id_dtos,
            stage_id_with_template_id_dtos=
            complete_task_templates_dto.initial_stage_id_with_template_id_dtos)
        gofs_of_templates_dict = self._get_gofs_of_templates_dict(
            gofs_of_task_templates_dtos=
            complete_task_templates_dto.gofs_of_task_templates_dtos,
            gof_dtos=complete_task_templates_dto.gof_dtos)
        fields_of_gofs_dict = self._get_fields_of_gofs_dict(
            field_with_permissions_dtos=
            complete_task_templates_dto.field_with_permissions_dtos)
        complete_gof_details_dicts = self._merge_gofs_with_fields(
            gofs_of_templates_dict, fields_of_gofs_dict)
        task_creation_gof_ids_of_templates_dict = \
            self._get_task_creation_gof_ids_for_each_task_template(
                initial_stage_id_with_template_id_dtos=
                complete_task_templates_dto.
                initial_stage_id_with_template_id_dtos,
                stage_gof_with_template_id_dtos=
                complete_task_templates_dto.stage_gof_with_template_id_dtos
            )
        stage_gofs_dict_of_templates_dict = \
            self._get_stage_gofs_for_each_task_template(
                initial_stage_id_with_template_id_dtos=
                complete_task_templates_dto.
                initial_stage_id_with_template_id_dtos,
                stage_gof_with_template_id_dtos=
                complete_task_templates_dto.stage_gof_with_template_id_dtos
            )
        for task_template in task_templates_dicts:
            task_template_id = task_template['template_id']
            task_template['actions'] = actions_of_templates_dict[
                task_template_id]
            task_template['group_of_fields'] = complete_gof_details_dicts[
                task_template_id]
            task_template['task_creation_gof_ids'] = \
                task_creation_gof_ids_of_templates_dict[task_template_id]
            task_template["stage_gofs"] = \
                stage_gofs_dict_of_templates_dict[task_template_id]

        # ToDo optimize project id in task templates logic
        project_id_with_task_template_id_dtos = \
            complete_task_templates_dto.project_id_with_task_template_id_dtos
        task_templates_with_project_id_details_list = \
            self._merge_task_templates_with_project_ids(
                task_templates_dicts=task_templates_dicts,
                project_id_with_task_template_id_dtos=
                project_id_with_task_template_id_dtos)

        return self.prepare_200_success_response(
            task_templates_with_project_id_details_list
        )

    def _merge_task_templates_with_project_ids(
            self, task_templates_dicts: List[Dict],
            project_id_with_task_template_id_dtos:
            List[ProjectIdWithTaskTemplateIdDTO]) -> List[Dict]:

        task_templates_details_dict = self._make_task_templates_details_dict(
            task_templates_dicts=task_templates_dicts)
        task_templates_with_project_id_details_list = []
        for project_id_with_task_template_id_dto in \
                project_id_with_task_template_id_dtos:
            task_template_id_of_project = \
                project_id_with_task_template_id_dto.task_template_id
            task_template_of_project = \
                task_templates_details_dict[task_template_id_of_project]
            task_template_of_project['project_id'] = \
                project_id_with_task_template_id_dto.project_id
            task_templates_with_project_id_details_list.append(
                task_template_of_project)
        task_template_ids = self._get_task_templates_ids(
            task_templates_dicts=task_templates_dicts
        )
        task_template_ids_of_projects = \
            self._get_task_template_ids_of_projects(
                project_id_with_task_template_id_dtos=
                project_id_with_task_template_id_dtos)
        independent_task_template_ids = [
            task_template_id
            for task_template_id in task_template_ids
            if task_template_id not in task_template_ids_of_projects
        ]
        for task_template_id in independent_task_template_ids:
            task_template_details = \
                task_templates_details_dict[task_template_id]
            task_template_details['project_id'] = None
            task_templates_with_project_id_details_list.append(
                task_template_details
            )
        return task_templates_with_project_id_details_list

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
        for template_id, gof_details_dicts in \
                gofs_details_group_by_template_id_dict.items():
            gofs_details_dicts_without_template_id = \
                self._get_gof_details_dicts_without_template_id(
                    gof_details_dicts=gof_details_dicts
                )
            gofs_details_of_templates_dict[template_id] = \
                gofs_details_dicts_without_template_id
        return gofs_details_of_templates_dict

    def _get_fields_of_gofs_dict(
            self,
            field_with_permissions_dtos: List[FieldPermissionDTO]):
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
            field_with_permissions_dtos: List[FieldPermissionDTO]
    ) -> List[Dict]:
        field_dicts = []
        for field_with_permissions_dto in field_with_permissions_dtos:
            field_dict = self._get_field_details_as_dict(
                field_with_permissions_dto=field_with_permissions_dto
            )
            field_dicts.append(field_dict)
        return field_dicts

    def _get_task_creation_gof_ids_for_each_task_template(
            self, initial_stage_id_with_template_id_dtos:
            List[StageIdWithTemplateIdDTO],
            stage_gof_with_template_id_dtos: List[StageGoFWithTemplateIdDTO]
    ) -> Dict:

        initial_stage_ids = self._get_stage_ids(
            stage_id_with_template_id_dtos=
            initial_stage_id_with_template_id_dtos)

        stage_gof_with_template_id_dtos_for_initial_stages = [
            stage_gof_with_template_id_dto
            for stage_gof_with_template_id_dto in
            stage_gof_with_template_id_dtos
            if stage_gof_with_template_id_dto.stage_id in initial_stage_ids
        ]

        stage_gof_ids_dict = self._get_stage_gof_ids_dict(
            stage_gof_with_template_id_dtos=
            stage_gof_with_template_id_dtos_for_initial_stages
        )

        task_creation_gof_ids_of_templates_dict = {}
        for initial_stage_id_with_template_id_dto in \
                initial_stage_id_with_template_id_dtos:
            task_creation_gof_ids_of_templates_dict[
                initial_stage_id_with_template_id_dto.template_id] = \
                stage_gof_ids_dict[
                    initial_stage_id_with_template_id_dto.stage_id]

        return task_creation_gof_ids_of_templates_dict

    def _get_stage_gofs_for_each_task_template(
            self, initial_stage_id_with_template_id_dtos:
            List[StageIdWithTemplateIdDTO],
            stage_gof_with_template_id_dtos: List[StageGoFWithTemplateIdDTO]
    ) -> Dict:

        initial_stage_ids = self._get_stage_ids(
            stage_id_with_template_id_dtos=
            initial_stage_id_with_template_id_dtos)

        stage_gof_with_template_id_dtos_without_initial_stages = [
            stage_gof_with_template_id_dto
            for stage_gof_with_template_id_dto in
            stage_gof_with_template_id_dtos
            if stage_gof_with_template_id_dto.stage_id not in initial_stage_ids
        ]

        stage_gof_ids_dict = self._get_stage_gof_ids_dict(
            stage_gof_with_template_id_dtos=
            stage_gof_with_template_id_dtos_without_initial_stages
        )

        stage_id_task_template_dict = self._make_stage_id_task_template_dict(
            stage_gof_with_template_id_dtos=
            stage_gof_with_template_id_dtos_without_initial_stages
        )

        stage_gof_ids_of_templates_dict = collections.defaultdict(list)
        for stage_id, gof_ids in stage_gof_ids_dict.items():
            task_template_id = stage_id_task_template_dict[stage_id]
            stage_gof_ids_of_templates_dict[task_template_id].append(
                {
                    "stage_id": stage_id,
                    "gof_ids": gof_ids
                }
            )

        return stage_gof_ids_of_templates_dict

    @staticmethod
    def _get_task_templates_in_dicts(
            task_templates_dtos: List[TemplateDTO]) -> List[Dict]:
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
                'enable_add_another':
                    gofs_to_task_templates_dto.enable_add_another,
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
                "button_color": action_with_stage_id_dto.button_color,
                "action_type": action_with_stage_id_dto.action_type,
                "transition_template_id":
                    action_with_stage_id_dto.transition_template_id
            }
            action_dicts_list.append(action_dict)
        return action_dicts_list

    @staticmethod
    def _get_field_details_as_dict(
            field_with_permissions_dto: FieldPermissionDTO) -> Dict:
        field_dto = field_with_permissions_dto.field_dto
        # TODO change order attribute to gof_order
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
            "is_field_writable": field_with_permissions_dto.is_field_writable,
            "field_order": field_dto.order
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

    @staticmethod
    def _make_task_templates_details_dict(
            task_templates_dicts: List[Dict]) -> Dict:
        task_templates_details_dict = {
            task_templates_dict['template_id']: task_templates_dict
            for task_templates_dict in task_templates_dicts
        }

        return task_templates_details_dict

    @staticmethod
    def _get_task_templates_ids(
            task_templates_dicts: List[Dict]) -> List[str]:
        task_template_ids = [
            task_templates_dict['template_id']
            for task_templates_dict in task_templates_dicts
        ]
        return task_template_ids

    @staticmethod
    def _get_task_template_ids_of_projects(
            project_id_with_task_template_id_dtos:
            List[ProjectIdWithTaskTemplateIdDTO]) -> List[str]:
        task_template_ids = [
            project_id_with_task_template_id_dto.task_template_id
            for project_id_with_task_template_id_dto in
            project_id_with_task_template_id_dtos
        ]
        return task_template_ids

    @staticmethod
    def _get_stage_ids(
            stage_id_with_template_id_dtos: List[StageIdWithTemplateIdDTO]
    ) -> List[int]:
        stage_ids = [
            stage_id_with_template_id_dto.stage_id
            for stage_id_with_template_id_dto in stage_id_with_template_id_dtos
        ]
        return stage_ids

    @staticmethod
    def _get_stage_gof_ids_dict(
            stage_gof_with_template_id_dtos: List[StageGoFWithTemplateIdDTO]
    ) -> Dict:
        stage_gofs_dict = collections.defaultdict(list)

        for stage_gof_with_template_id_dto in stage_gof_with_template_id_dtos:
            stage_gofs_dict[stage_gof_with_template_id_dto.stage_id].append(
                stage_gof_with_template_id_dto.gof_id
            )

        return stage_gofs_dict

    @staticmethod
    def _make_stage_id_task_template_dict(
            stage_gof_with_template_id_dtos: List[StageGoFWithTemplateIdDTO]
    ) -> Dict:
        stage_id_task_template_dict = {
            stage_gof_with_template_id_dto.stage_id:
                stage_gof_with_template_id_dto.task_template_id
            for stage_gof_with_template_id_dto in
            stage_gof_with_template_id_dtos
        }
        return stage_id_task_template_dict
