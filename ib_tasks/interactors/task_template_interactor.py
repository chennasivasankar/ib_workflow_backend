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
        gof_ids = self._get_gof_ids(
            gof_dtos=create_task_template_dto.gof_dtos
        )
        self._validate_uniqueness_in_gof_ids(gof_ids=gof_ids)
        self._validate_template_name_with_existing_name_if_exists(
            template_id=create_task_template_dto.template_id,
            template_name=create_task_template_dto.template_name
        )
        self._check_existing_gof_of_template_are_in_given_gof(
            create_task_template_dto=create_task_template_dto
        )
        self._validate_fields_of_create_task_template_dto(
            create_task_template_dto=create_task_template_dto
        )
        gof_dtos_to_update, gof_dtos_to_create = \
            self._get_gof_dtos_to_update_and_create(
                create_task_template_dto=create_task_template_dto
            )
        if gof_dtos_to_update:
            create_task_template_dto.gof_dtos = gof_dtos_to_update
            self.task_storage.update_task_template(
                create_task_template_dto=create_task_template_dto
            )
            return

        self.task_storage.create_task_template(
            create_task_template_dto=create_task_template_dto
        )

    def _get_gof_dtos_to_update_and_create(
            self, create_task_template_dto: CreateTaskTemplateDTO):
        existing_gof_ids = \
            self.task_storage.get_existing_gof_of_template(
                template_id=create_task_template_dto.template_id,
            )
        gof_dtos = create_task_template_dto.gof_dtos
        gof_dtos_to_update = []
        gof_dtos_to_create = []
        for gof_dto in gof_dtos:
            gof_id = gof_dto.gof_id
            if gof_id in existing_gof_ids:
                gof_dtos_to_update.append(gof_dto)
            else:
                gof_dtos_to_create.append(gof_dto)
        return gof_dtos_to_update, gof_dtos_to_create

    def _validate_template_name_with_existing_name_if_exists(
            self, template_id: str, template_name: str):
        from ib_tasks.exceptions.custom_exceptions \
            import DifferentTemplateName, TemplateNotExists
        try:
            existing_template_name = \
                self.task_storage.get_task_template_name_if_exists(
                    template_id=template_id
                )
        except TemplateNotExists:
            return

        is_same_template_name = existing_template_name == template_name
        is_different_template_name = not is_same_template_name
        if is_different_template_name:
            raise DifferentTemplateName(template_name)

    def _check_existing_gof_of_template_are_in_given_gof(
            self, create_task_template_dto: CreateTaskTemplateDTO):
        existing_gof_ids = \
            self.task_storage.get_existing_gof_of_template(
                template_id=create_task_template_dto.template_id,
            )
        present_gof_ids = self._get_gof_ids(
            gof_dtos=create_task_template_dto.gof_dtos
        )
        gof_not_in_given_gof = [
            gof_id
            for gof_id in existing_gof_ids
            if gof_id not in present_gof_ids
        ]
        from ib_tasks.exceptions.custom_exceptions import \
            ExistingGOFNotInGivenGOF
        if gof_not_in_given_gof:
            raise ExistingGOFNotInGivenGOF(gof_not_in_given_gof)

    def _validate_fields_of_create_task_template_dto(
            self, create_task_template_dto: CreateTaskTemplateDTO):
        from ib_tasks.exceptions.custom_exceptions import InvalidValueForField
        template_name = create_task_template_dto.template_name
        template_id = create_task_template_dto.template_id
        gof_dtos = create_task_template_dto.gof_dtos

        self._validate_template_name(template_name=template_name)
        self._validate_template_id(template_id=template_id)

        gof_ids = self._get_gof_ids(gof_dtos=gof_dtos)
        self._validate_gof_ids(gof_ids=gof_ids)
        self._validate_order_of_gof(gof_dtos=gof_dtos)

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
    def _validate_order_of_gof(gof_dtos: GoFDTO):
        from ib_tasks.exceptions.custom_exceptions import InvalidValueForField
        for gof_dto in gof_dtos:
            is_invalid_order = \
                gof_dto.order <= -1 and (type(gof_dto.order) == int)
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
            import DuplicateGOFIds
        if duplicate_gof_ids:
            raise DuplicateGOFIds(duplicate_gof_ids)
