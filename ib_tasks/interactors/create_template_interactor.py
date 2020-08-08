from ib_tasks.interactors.storage_interfaces.task_template_storage_interface \
    import \
    TaskTemplateStorageInterface
from ib_tasks.interactors.task_template_dtos import CreateTemplateDTO


class CreateTemplateInteractor:
    def __init__(self, task_template_storage: TaskTemplateStorageInterface):
        self.task_template_storage = task_template_storage

    def create_template_wrapper(
            self, create_template_dto: CreateTemplateDTO):
        self.create_template(create_template_dto=create_template_dto)

    def create_template(self, create_template_dto: CreateTemplateDTO):
        template_id = create_template_dto.template_id
        template_name = create_template_dto.template_name
        is_transition_template = create_template_dto.is_transition_template

        self._make_validations(
            template_id=template_id, template_name=template_name
        )
        is_template_exists = \
            self.task_template_storage.check_is_template_exists(
                template_id=template_id
            )
        if is_template_exists:
            self.task_template_storage.update_template(
                template_id=template_id, template_name=template_name,
                is_transition_template=is_transition_template
            )
            return

        self.task_template_storage.create_template(
            template_id=template_id, template_name=template_name,
            is_transition_template=is_transition_template
        )

    def _make_validations(
            self, template_id: str, template_name: str):
        self._validate_template_name(template_name=template_name)
        self._validate_template_id(template_id=template_id)

    @staticmethod
    def _validate_template_name(template_name: str):
        template_name_after_strip = template_name.strip()
        is_template_name_empty = not template_name_after_strip
        from ib_tasks.exceptions.fields_custom_exceptions import \
            InvalidValueForField
        from ib_tasks.constants.exception_messages import \
            INVALID_VALUE_FOR_TEMPLATE_NAME
        if is_template_name_empty:
            message = INVALID_VALUE_FOR_TEMPLATE_NAME
            raise InvalidValueForField(message)

    @staticmethod
    def _validate_template_id(template_id: str):
        template_id_after_strip = template_id.strip()
        is_template_id_empty = not template_id_after_strip
        from ib_tasks.exceptions.fields_custom_exceptions import \
            InvalidValueForField
        from ib_tasks.constants.exception_messages import \
            INVALID_VALUE_FOR_TEMPLATE_ID
        if is_template_id_empty:
            message = INVALID_VALUE_FOR_TEMPLATE_ID
            raise InvalidValueForField(message)