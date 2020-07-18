from typing import List
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
        template_id = create_task_template_dto.template_id
        template_name = create_task_template_dto.template_name

        self._make_validations(
            template_id=template_id, template_name=template_name
        )
        is_template_exists = self.task_storage.check_is_template_exists(
            template_id=template_id
        )
        if is_template_exists:
            existing_template_name = self.task_storage.get_task_template_name(
                template_id=template_id
            )
            is_template_names_are_equal = \
                existing_template_name == template_name
            is_template_names_are_not_equal = not is_template_names_are_equal

            if is_template_names_are_not_equal:
                self.task_storage.update_task_template(
                    template_id=template_id, template_name=template_name
                )
            return

        self.task_storage.create_task_template(
            template_id=template_id, template_name=template_name
        )

    def _make_validations(
            self, template_id: str, template_name: str):
        self._validate_template_name(template_name=template_name)
        self._validate_template_id(template_id=template_id)

    @staticmethod
    def _validate_template_name(template_name: str):
        template_name_after_strip = template_name.strip()
        is_template_name_empty = not template_name_after_strip
        from ib_tasks.exceptions.custom_exceptions import InvalidValueForField
        from ib_tasks.constants.exception_messages import \
            INVALID_VALUE_FOR_TEMPLATE_NAME
        if is_template_name_empty:
            err_msg = INVALID_VALUE_FOR_TEMPLATE_NAME
            raise InvalidValueForField(err_msg)

    @staticmethod
    def _validate_template_id(template_id: str):
        template_id_after_strip = template_id.strip()
        is_template_id_empty = not template_id_after_strip
        from ib_tasks.exceptions.custom_exceptions import InvalidValueForField
        from ib_tasks.constants.exception_messages import \
            INVALID_VALUE_FOR_TEMPLATE_ID
        if is_template_id_empty:
            err_msg = INVALID_VALUE_FOR_TEMPLATE_ID
            raise InvalidValueForField(err_msg)
