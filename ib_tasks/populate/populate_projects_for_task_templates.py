from typing import Dict


class PopulateProjectsForTaskTemplates:

    @property
    def data_sheet(self):
        from ib_tasks.populate.get_data_from_sheet import GetDataFromSheet
        return GetDataFromSheet()

    def populate_projects_for_task_template(self, spread_sheet_name: str):
        template_ids_group_by_project_id_dict = \
            self._get_template_ids_group_by_project_id(
                spread_sheet_name=spread_sheet_name)

        from ib_tasks.interactors.add_project_to_task_templates_interactor \
            import AddProjectToTaskTemplatesInteractor
        from ib_tasks.storages.task_template_storage_implementation import \
            TaskTemplateStorageImplementation
        task_template_storage = TaskTemplateStorageImplementation()

        add_project_to_task_templates_interactor = \
            AddProjectToTaskTemplatesInteractor(
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

    def _get_template_ids_group_by_project_id(
            self, spread_sheet_name: str) -> Dict:
        from ib_tasks.constants.constants import \
            PROJECT_FOR_TASK_TEMPLATES_SUB_SHEET
        field_records = self.data_sheet.get_data_from_sub_sheet(
            spread_sheet_name=spread_sheet_name,
            sub_sheet_name=PROJECT_FOR_TASK_TEMPLATES_SUB_SHEET)

        import collections
        template_ids_group_by_project_id_dict = collections.defaultdict(list)
        for item in field_records:
            template_ids_group_by_project_id_dict[item['Project ID'].strip()].\
                append(item['Task Template ID'].strip())

        return template_ids_group_by_project_id_dict
