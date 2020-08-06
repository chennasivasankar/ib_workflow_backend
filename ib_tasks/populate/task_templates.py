class PopulateTaskTemplates:

    def populate_task_templates(self):
        from ib_tasks.utils.get_google_sheet import get_google_sheet
        from ib_tasks.constants.constants import GOOGLE_SHEET_NAME
        sheet = get_google_sheet(sheet_name=GOOGLE_SHEET_NAME)

        from ib_tasks.constants.constants import TASK_TEMPLATE_SUB_SHEET_TITLE
        task_templates_dicts = \
            sheet.worksheet(TASK_TEMPLATE_SUB_SHEET_TITLE).get_all_records()

        for task_templates_dict in task_templates_dicts:
            self._populate_task_template_in_db(
                template_id=task_templates_dict['Template ID'].strip(),
                template_name=task_templates_dict['Template Name'].strip()
            )

    @staticmethod
    def _populate_task_template_in_db(template_id: str, template_name: str):
        from ib_tasks.storages.task_template_storage_implementation import \
            TaskTemplateStorageImplementation
        task_template_storage = TaskTemplateStorageImplementation()

        from ib_tasks.interactors.create_task_template_interactor import \
            CreateTaskTemplateInteractor
        interactor = CreateTaskTemplateInteractor(
            task_template_storage=task_template_storage)

        from ib_tasks.interactors.task_template_dtos import \
            CreateTaskTemplateDTO
        create_task_template_dto = CreateTaskTemplateDTO(
            template_id=template_id, template_name=template_name
        )
        interactor.create_task_template(
            create_task_template_dto=create_task_template_dto
        )
