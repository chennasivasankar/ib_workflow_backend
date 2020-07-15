from typing import List
from ib_tasks.interactors.storage_interfaces.task_storage_interface \
    import TaskStorageInterface
from ib_tasks.interactors.dtos import CreateTaskTemplateDTO, GoFDTO


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
        self._validate_field_values_of_create_task_template_dto(
            create_task_template_dto=create_task_template_dto
        )
        gof_ids = self._get_gof_ids(
            gof_dtos=create_task_template_dto.gof_dtos
        )
        self._validate_uniqueness_in_gof_ids(gof_ids=gof_ids)
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
                gof_dtos_to_add_to_template=create_task_template_dto.gof_dtos
            )
            return

        self._check_existing_gofs_of_template_are_in_given_gofs(
            create_task_template_dto=create_task_template_dto
        )
        gof_dtos_to_add_to_template = self._get_gof_dtos_to_add_to_template(
            create_task_template_dto=create_task_template_dto
        )
        if gof_dtos_to_add_to_template:
            self.task_storage.add_gofs_to_task_template(
                template_id=create_task_template_dto.template_id,
                gof_dtos_to_add_to_template=gof_dtos_to_add_to_template
            )

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
        is_template_name_valid = \
            template_name and (type(template_name) == str)
        is_template_name_invalid = not is_template_name_valid

        from ib_tasks.exceptions.custom_exceptions import InvalidValueForField
        if is_template_name_invalid:
            raise InvalidValueForField("template_name")

    @staticmethod
    def _validate_template_id(template_id: str):
        is_template_id_valid = template_id and (type(template_id) == str)
        is_template_id_invalid = not is_template_id_valid

        from ib_tasks.exceptions.custom_exceptions import InvalidValueForField
        if is_template_id_invalid:
            raise InvalidValueForField("template_id")

    @staticmethod
    def _validate_gof_ids(gof_ids: List[str]):
        from ib_tasks.exceptions.custom_exceptions import InvalidValueForField
        for gof_id in gof_ids:
            is_gof_id_valid = gof_id and (type(gof_id) == str)
            is_gof_id_invalid = not is_gof_id_valid
            if is_gof_id_invalid:
                raise InvalidValueForField("gof_id")

    @staticmethod
    def _validate_order_of_gof(gof_dtos: List[GoFDTO]):
        from ib_tasks.exceptions.custom_exceptions import InvalidValueForField
        for gof_dto in gof_dtos:
            is_order_not_int_type = not (type(gof_dto.order) == int)
            is_invalid_order = gof_dto.order < -1 or is_order_not_int_type
            if is_invalid_order:
                raise InvalidValueForField("order")

    @staticmethod
    def _get_gof_ids(gof_dtos: List[GoFDTO]):
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
