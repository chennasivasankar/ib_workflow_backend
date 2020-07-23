class PopulateTaskTemplates:

    def populate_task_templates(self):
        from ib_tasks.utils.get_google_sheet import get_google_sheet
        sheet = get_google_sheet()

        task_templates_dicts = \
            sheet.worksheet("Task Templates").get_all_records()

        for task_templates_dict in task_templates_dicts:
            self._populate_task_template_in_db(
                template_id=task_templates_dict['Template ID'],
                template_name=task_templates_dict['Template Name']
            )

    @staticmethod
    def _populate_task_template_in_db(template_id: str, template_name: str):

        from ib_tasks.storages.tasks_storage_implementation import \
            TasksStorageImplementation
        task_storage = TasksStorageImplementation()

        from ib_tasks.interactors.create_task_template_interactor import \
            CreateTaskTemplateInteractor
        interactor = CreateTaskTemplateInteractor(task_storage=task_storage)

        from ib_tasks.interactors.task_template_dtos import CreateTaskTemplateDTO
        create_task_template_dto = CreateTaskTemplateDTO(
            template_id=template_id, template_name=template_name
        )
        interactor.create_task_template(
            create_task_template_dto=create_task_template_dto
        )
