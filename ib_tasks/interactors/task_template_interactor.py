from ib_tasks.interactors.storage_interfaces.task_storage_interface \
    import TaskStorageInterface
from ib_tasks.interactors.dtos import CreateTaskTemplateDTO


class TaskTemplateInteractor:
    def __init__(self, task_storage: TaskStorageInterface):
        self.task_storage = task_storage

    def create_task_template_wrapper(
            self, create_task_template_dto: CreateTaskTemplateDTO):
        self.create_task_template(
            create_task_template_dto=create_task_template_dto
        )

    def create_task_template(
            self, create_task_template_dto: CreateTaskTemplateDTO):
        self._make_validations(
            create_task_template_dto=create_task_template_dto
        )
        is_template_exists = self.task_storage.check_is_template_exists(
            template_id=create_task_template_dto.template_id
        )
        is_template_not_exists = not is_template_exists
        if is_template_not_exists:
            self.task_storage.create_task_template(
                template_id=create_task_template_dto.template_id,
                template_name=create_task_template_dto.template_name
            )
        return

    def _make_validations(
            self, create_task_template_dto: CreateTaskTemplateDTO):
        self._validate_field_values_of_create_task_template_dto(
            create_task_template_dto=create_task_template_dto
        )

    def _validate_field_values_of_create_task_template_dto(
            self, create_task_template_dto: CreateTaskTemplateDTO):
        template_name = create_task_template_dto.template_name
        template_id = create_task_template_dto.template_id

        self._validate_template_name(template_name=template_name)
        self._validate_template_id(template_id=template_id)

    @staticmethod
    def _validate_template_name(template_name: str):
        template_name_after_strip = template_name.strip()
        is_template_name_empty = not template_name_after_strip
        from ib_tasks.exceptions.custom_exceptions import InvalidValueForField
        if is_template_name_empty:
            raise InvalidValueForField("template_name")

    @staticmethod
    def _validate_template_id(template_id: str):
        template_id_after_strip = template_id.strip()
        is_template_id_empty = not template_id_after_strip
        from ib_tasks.exceptions.custom_exceptions import InvalidValueForField
        if is_template_id_empty:
            raise InvalidValueForField("template_id")
