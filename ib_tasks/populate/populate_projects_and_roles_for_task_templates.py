from typing import Dict, List

from ib_tasks.interactors.\
    add_project_and_roles_to_task_templates_interactor import \
    AddProjectAndRolesToTaskTemplatesInteractor
from ib_tasks.interactors.task_template_dtos import TaskTemplateRolesDTO
from ib_tasks.storages.task_template_storage_implementation import \
    TaskTemplateStorageImplementation


class PopulateProjectsAndRolesForTaskTemplates:

    @property
    def data_sheet(self):
        from ib_tasks.populate.get_data_from_sheet import GetDataFromSheet
        return GetDataFromSheet()

    def populate_projects_and_roles_for_task_template(
            self, spread_sheet_name: str):
        template_ids_group_by_project_id_dict, task_template_role_dtos = \
            self._get_template_ids_group_by_project_id_and_roles_of_templates(
                spread_sheet_name=spread_sheet_name)

        self._populate_projects_for_task_templates(
            template_ids_group_by_project_id_dict=
            template_ids_group_by_project_id_dict)

        self._populate_roles_for_task_templates(
            task_template_role_dtos=task_template_role_dtos)

    def _get_template_ids_group_by_project_id_and_roles_of_templates(
            self, spread_sheet_name: str) -> (
            Dict, List[TaskTemplateRolesDTO]):

        from ib_tasks.constants.constants import \
            PROJECT_FOR_TASK_TEMPLATES_SUB_SHEET
        field_records = self.data_sheet.get_data_from_sub_sheet(
            spread_sheet_name=spread_sheet_name,
            sub_sheet_name=PROJECT_FOR_TASK_TEMPLATES_SUB_SHEET)

        import collections
        template_ids_group_by_project_id_dict = collections.defaultdict(list)
        task_template_role_dtos = []

        for item in field_records:
            template_ids_group_by_project_id_dict[item['Project ID'].strip()].\
                append(item['Task Template ID'].strip())

            role_ids = item["Roles"].split("\n")
            task_template_role_dtos.append(
                TaskTemplateRolesDTO(
                    task_template_id=item['Task Template ID'].strip(),
                    role_ids=role_ids
                ))

        return template_ids_group_by_project_id_dict, task_template_role_dtos

    @staticmethod
    def _populate_projects_for_task_templates(
            template_ids_group_by_project_id_dict: Dict):
        task_template_storage = TaskTemplateStorageImplementation()

        add_project_to_task_templates_interactor = \
            AddProjectAndRolesToTaskTemplatesInteractor(
                task_template_storage=task_template_storage)

        from ib_tasks.exceptions.task_custom_exceptions import \
            InvalidTaskTemplateIds
        from ib_tasks.exceptions.custom_exceptions import InvalidProjectId
        from ib_tasks.constants.exception_messages import \
            INVALID_TASK_TEMPLATE_IDS, INVALID_PROJECT_ID

        for project_id, task_template_ids in \
                template_ids_group_by_project_id_dict.items():
            try:
                add_project_to_task_templates_interactor.\
                    add_project_to_task_templates_interactor(
                        project_id=project_id,
                        task_template_ids=task_template_ids)
            except InvalidTaskTemplateIds as err:
                return INVALID_TASK_TEMPLATE_IDS[0].format(
                    err.invalid_task_template_ids)
            except InvalidProjectId as err:
                return INVALID_PROJECT_ID[0].format(err.project_id)

    @staticmethod
    def _populate_roles_for_task_templates(
            task_template_role_dtos: List[TaskTemplateRolesDTO]):
        task_template_storage = TaskTemplateStorageImplementation()

        add_project_to_task_templates_interactor = \
            AddProjectAndRolesToTaskTemplatesInteractor(
                task_template_storage=task_template_storage)

        from ib_tasks.exceptions.task_custom_exceptions import \
            InvalidTaskTemplateIds
        from ib_tasks.exceptions.custom_exceptions import \
            DuplicateRoleIdsGivenToATaskTemplate
        from ib_tasks.exceptions.roles_custom_exceptions import \
            InvalidRoleIdsException

        from ib_tasks.constants.exception_messages import \
            DUPLICATE_ROLE_IDS_GIVEN_TO_TASK_TEMPLATE, INVALID_ROLE_IDS, \
            INVALID_TASK_TEMPLATE_IDS

        try:
            add_project_to_task_templates_interactor.\
                add_roles_to_task_templates(
                    task_template_role_dtos=task_template_role_dtos)
        except DuplicateRoleIdsGivenToATaskTemplate as err:
            return DUPLICATE_ROLE_IDS_GIVEN_TO_TASK_TEMPLATE[0].format(
                err.role_ids, err.task_template_id)
        except InvalidRoleIdsException as err:
            return INVALID_ROLE_IDS[0].format(err.role_ids)
        except InvalidTaskTemplateIds as err:
            return INVALID_TASK_TEMPLATE_IDS[0].format(
                err.invalid_task_template_ids)
