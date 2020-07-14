from typing import List
from ib_tasks.interactors.storage_interfaces.task_storage_interface \
    import TaskStorageInterface
from ib_tasks.interactors.dtos import CreateTaskTemplateDTO, GroupOfFieldsDTO


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
        group_of_fields_ids = self._get_group_of_field_ids(
            group_of_fields_dtos=create_task_template_dto.group_of_fields_dtos
        )
        self._validate_uniqueness_in_group_of_fields_ids(
            group_of_fields_ids=group_of_fields_ids
        )
        self._validate_template_name(
            template_id=create_task_template_dto.template_id,
            template_name=create_task_template_dto.template_name)
        self. \
            _check_existing_group_of_fields_of_template_are_in_given_group_of_fields(
            create_task_template_dto=create_task_template_dto
        )
        self._validate_fields_of_create_task_template_dto(
            create_task_template_dto=create_task_template_dto
        )
        group_of_fields_dtos_to_update, group_of_fields_dtos_to_create = \
            self._get_group_of_fields_to_update_and_create(
                create_task_template_dto=create_task_template_dto
            )
        if group_of_fields_dtos_to_update:
            create_task_template_dto.group_of_fields_dtos = \
                group_of_fields_dtos_to_update
            self.task_storage.update_task_template(
                create_task_template_dto=create_task_template_dto
            )
            return
        self.task_storage.create_task_template(
            create_task_template_dto=create_task_template_dto
        )

    def _get_group_of_fields_to_update_and_create(
            self, create_task_template_dto=CreateTaskTemplateDTO):
        existing_group_of_fields_ids = \
            self.task_storage.get_existing_group_of_fields_of_template(
                template_id=create_task_template_dto.template_id,
            )
        group_of_fields_dtos = create_task_template_dto.group_of_fields_dtos
        group_of_fields_dtos_to_update = []
        group_of_fields_dtos_to_create = []
        for group_of_fields_dto in group_of_fields_dtos:
            group_of_fields_id = group_of_fields_dto.group_of_fields_id
            if group_of_fields_id in existing_group_of_fields_ids:
                group_of_fields_dtos_to_update.append(group_of_fields_dto)
            else:
                group_of_fields_dtos_to_create.append(group_of_fields_dto)
        return group_of_fields_dtos_to_update, group_of_fields_dtos_to_create

    def _validate_template_name(self, template_id: str, template_name: str):
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

    def _check_existing_group_of_fields_of_template_are_in_given_group_of_fields(
            self, create_task_template_dto: CreateTaskTemplateDTO):
        existing_group_of_fields_ids = \
            self.task_storage.get_existing_group_of_fields_of_template(
                template_id=create_task_template_dto.template_id,
            )
        present_group_of_fields_ids = self._get_group_of_field_ids(
            group_of_fields_dtos=create_task_template_dto.group_of_fields_dtos
        )
        group_of_fields_not_in_given_group_of_fields = \
            [
                group_of_fields_id
                for group_of_fields_id in existing_group_of_fields_ids
                if group_of_fields_id not in present_group_of_fields_ids
            ]
        from ib_tasks.exceptions.custom_exceptions import \
            ExistingGroupOfFieldsNotInGivenGroupOfFields
        if group_of_fields_not_in_given_group_of_fields:
            raise ExistingGroupOfFieldsNotInGivenGroupOfFields(
                group_of_fields_not_in_given_group_of_fields
            )

    @staticmethod
    def _validate_order_of_group_of_fileds(
            group_of_fields_dtos: GroupOfFieldsDTO):
        from ib_tasks.exceptions.custom_exceptions import InvalidOrder
        for group_of_fields_dto in group_of_fields_dtos:
            is_invalid_order = group_of_fields_dto.order <= -1 and \
                               (type(group_of_fields_dto.order) == int)
            if is_invalid_order:
                raise InvalidOrder(
                    group_of_fields_dto.group_of_fields_id,
                    group_of_fields_dto.order
                )

    @staticmethod
    def _get_group_of_field_ids(group_of_fields_dtos: List[GroupOfFieldsDTO]):
        group_of_fields_ids = [
            group_of_fields_dto.group_of_fields_id
            for group_of_fields_dto in group_of_fields_dtos
        ]
        return group_of_fields_ids

    @staticmethod
    def _validate_uniqueness_in_group_of_fields_ids(
            group_of_fields_ids: List[str]):
        from collections import Counter
        group_of_fields_ids_counter = Counter(group_of_fields_ids)

        duplicate_group_of_fields_ids = []
        for group_of_fields_id, count in group_of_fields_ids_counter.items():
            is_duplicate_group_of_fields_id = count > 1
            if is_duplicate_group_of_fields_id:
                duplicate_group_of_fields_ids.append(group_of_fields_id)

        from ib_tasks.exceptions.custom_exceptions \
            import DuplicateGroupOfFields
        if duplicate_group_of_fields_ids:
            raise DuplicateGroupOfFields(duplicate_group_of_fields_ids)

    def _validate_fields_of_create_task_template_dto(
            self, create_task_template_dto: CreateTaskTemplateDTO):
        from ib_tasks.exceptions.custom_exceptions import InvalidValueForField
        template_name = create_task_template_dto.template_name
        template_id = create_task_template_dto.template_id
        group_of_fields_dtos = create_task_template_dto.group_of_fields_dtos
        is_template_name_valid = \
            template_name and (type(template_name) == str)
        is_template_name_invalid = not is_template_name_valid
        if is_template_name_invalid:
            raise InvalidValueForField("template_name")
        is_template_id_valid = template_id and (type(template_id) == str)
        is_template_id_invalid = not is_template_id_valid
        if is_template_id_invalid:
            raise InvalidValueForField("template_id")
        group_of_fields_ids = self._get_group_of_field_ids(
            group_of_fields_dtos=group_of_fields_dtos
        )
        for group_of_fields_id in group_of_fields_ids:
            is_group_of_fields_id_valid = \
                group_of_fields_id and (type(group_of_fields_id) == str)
            is_group_of_fields_id_invalid = not is_group_of_fields_id_valid
            if is_group_of_fields_id_invalid:
                raise InvalidValueForField("group_of_fields_id")
        self._validate_order_of_group_of_fileds(
            group_of_fields_dtos=group_of_fields_dtos
        )
