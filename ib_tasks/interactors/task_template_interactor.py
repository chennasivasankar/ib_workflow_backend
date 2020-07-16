from typing import List
from ib_tasks.interactors.storage_interfaces.task_storage_interface \
    import TaskStorageInterface
from ib_tasks.interactors.dtos import CreateTaskTemplateDTO, GoFIDAndOrderDTO


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
            self.task_storage.add_gofs_to_task_template(
                template_id=create_task_template_dto.template_id,
                gof_id_and_order_dtos=create_task_template_dto.gof_dtos
            )
            return

        self._check_existing_gofs_of_template_are_in_given_gofs(
            create_task_template_dto=create_task_template_dto
        )
        gof_id_and_order_dtos_to_add_to_template = \
            self._get_gof_dtos_to_add_to_template(
                create_task_template_dto=create_task_template_dto
            )
        if gof_id_and_order_dtos_to_add_to_template:
            self.task_storage.add_gofs_to_task_template(
                template_id=create_task_template_dto.template_id,
                gof_id_and_order_dtos=gof_id_and_order_dtos_to_add_to_template
            )

    def _make_validations(
            self, create_task_template_dto: CreateTaskTemplateDTO):
        self._validate_field_values_of_create_task_template_dto(
            create_task_template_dto=create_task_template_dto
        )
        gof_ids = self._get_gof_ids(
            gof_dtos=create_task_template_dto.gof_dtos
        )
        self._validate_uniqueness_in_gof_ids(gof_ids=gof_ids)

    def _validate_field_values_of_create_task_template_dto(
            self, create_task_template_dto: CreateTaskTemplateDTO):
        template_name = create_task_template_dto.template_name
        template_id = create_task_template_dto.template_id
        gof_dtos = create_task_template_dto.gof_dtos

        self._validate_template_name(template_name=template_name)
        self._validate_template_id(template_id=template_id)

        gof_ids = self._get_gof_ids(gof_dtos=gof_dtos)
        self._validate_gof_ids(gof_ids=gof_ids)
        self._validate_order_of_gof(gof_dtos=gof_dtos)

    def _validate_gof_ids(self, gof_ids: List[str]):
        for gof_id in gof_ids:
            self._validate_gof_id(gof_id=gof_id)

    def _get_gof_dtos_to_add_to_template(
            self, create_task_template_dto: CreateTaskTemplateDTO):
        existing_gof_ids = \
            self.task_storage.get_existing_gof_ids_of_template(
                template_id=create_task_template_dto.template_id,
            )
        gof_dtos = create_task_template_dto.gof_dtos
        gof_dtos_to_update = [
            gof_dto
            for gof_dto in gof_dtos
            if gof_dto.gof_id not in existing_gof_ids
        ]
        return gof_dtos_to_update

    def _validate_template_name_with_existing_name(
            self, template_id: str, template_name: str):
        from ib_tasks.exceptions.custom_exceptions \
            import DifferentTemplateName
        existing_template_name = \
            self.task_storage.get_task_template_name(template_id=template_id)

        is_same_template_name = existing_template_name == template_name
        is_different_template_name = not is_same_template_name
        if is_different_template_name:
            raise DifferentTemplateName(existing_template_name, template_name)

    def _check_existing_gofs_of_template_are_in_given_gofs(
            self, create_task_template_dto: CreateTaskTemplateDTO):
        existing_gof_ids = \
            self.task_storage.get_existing_gof_ids_of_template(
                template_id=create_task_template_dto.template_id,
            )
        given_gof_ids = self._get_gof_ids(
            gof_dtos=create_task_template_dto.gof_dtos
        )
        gof_of_template_not_in_given_gof = [
            gof_id
            for gof_id in existing_gof_ids
            if gof_id not in given_gof_ids
        ]
        from ib_tasks.exceptions.custom_exceptions import \
            ExistingGoFNotInGivenGoF
        if gof_of_template_not_in_given_gof:
            raise ExistingGoFNotInGivenGoF(
                gof_of_template_not_in_given_gof, given_gof_ids
            )

    @staticmethod
    def _validate_template_name(template_name: str):
        is_template_name_string = (type(template_name) == str)
        is_template_name_not_a_string = not is_template_name_string
        from ib_tasks.exceptions.custom_exceptions import InvalidValueForField
        if is_template_name_not_a_string:
            raise InvalidValueForField("template_name")

        template_name_after_strip = template_name.strip()
        is_template_name_empty = not template_name_after_strip
        if is_template_name_empty:
            raise InvalidValueForField("template_name")

    @staticmethod
    def _validate_template_id(template_id: str):
        is_template_id_string = type(template_id) == str
        is_template_id_not_a_string = not is_template_id_string
        from ib_tasks.exceptions.custom_exceptions import InvalidValueForField
        if is_template_id_not_a_string:
            raise InvalidValueForField("template_id")

        template_id_after_strip = template_id.strip()
        is_template_id_empty = not template_id_after_strip
        if is_template_id_empty:
            raise InvalidValueForField("template_id")

    @staticmethod
    def _validate_gof_id(gof_id: str):
        is_gof_id_string = type(gof_id) == str
        is_gof_id_not_a_string = not is_gof_id_string
        from ib_tasks.exceptions.custom_exceptions import InvalidValueForField
        if is_gof_id_not_a_string:
            raise InvalidValueForField("gof_id")

        gof_id_after_strip = gof_id.strip()
        is_gof_id_empty = not gof_id_after_strip
        if is_gof_id_empty:
            raise InvalidValueForField("gof_id")

    @staticmethod
    def _validate_order_of_gof(gof_dtos: List[GoFIDAndOrderDTO]):
        from ib_tasks.exceptions.custom_exceptions import InvalidValueForField
        for gof_dto in gof_dtos:
            is_order_not_int_type = not (type(gof_dto.order) == int)
            is_invalid_order = gof_dto.order < -1 or is_order_not_int_type
            if is_invalid_order:
                raise InvalidValueForField("order")

    @staticmethod
    def _get_gof_ids(gof_dtos: List[GoFIDAndOrderDTO]):
        gof_ids = [
            gof_dto.gof_id
            for gof_dto in gof_dtos
        ]
        return gof_ids

    @staticmethod
    def _validate_uniqueness_in_gof_ids(
            gof_ids: List[str]):
        from collections import Counter
        gof_ids_counter = Counter(gof_ids)

        duplicate_gof_ids = []
        for gof_id, count in gof_ids_counter.items():
            is_duplicate_gof_id = count > 1
            if is_duplicate_gof_id:
                duplicate_gof_ids.append(gof_id)

        from ib_tasks.exceptions.custom_exceptions \
            import DuplicateGoFIds
        if duplicate_gof_ids:
            raise DuplicateGoFIds(duplicate_gof_ids)
