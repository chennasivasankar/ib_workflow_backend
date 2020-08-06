from ib_tasks.interactors.gofs_dtos import GoFsWithTemplateIdDTO


class PopulateGoFsToTemplate:

    @staticmethod
    def populate_gofs_to_template(
            gofs_with_template_id_dto: GoFsWithTemplateIdDTO):
        from ib_tasks.storages.task_template_storage_implementation import \
            TaskTemplateStorageImplementation
        task_template_storage = TaskTemplateStorageImplementation()
        from ib_tasks.storages.gof_storage_implementation import \
            GoFStorageImplementation
        gof_storage = GoFStorageImplementation()

        from ib_tasks.interactors.add_gofs_to_template_interactor \
            import AddGoFsToTemplateInteractor
        interactor = \
            AddGoFsToTemplateInteractor(
                task_template_storage=task_template_storage,
                gof_storage=gof_storage
            )
        interactor.add_gofs_to_template_wrapper(
            gofs_with_template_id_dto=gofs_with_template_id_dto
        )
