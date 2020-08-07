from ib_tasks.interactors.task_template_dtos import \
    CreateTemplateDTO


class PopulateTemplate:

    @staticmethod
    def _populate_template_in_db(create_template_dto: CreateTemplateDTO):
        from ib_tasks.storages.task_template_storage_implementation import \
            TaskTemplateStorageImplementation
        task_template_storage = TaskTemplateStorageImplementation()

        from ib_tasks.interactors.create_template_interactor import \
            CreateTemplateInteractor
        interactor = CreateTemplateInteractor(
            task_template_storage=task_template_storage)

        interactor.create_template(
            create_template_dto=create_template_dto
        )
