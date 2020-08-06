from typing import List

from ib_tasks.interactors.global_constants_dtos import GlobalConstantsDTO, \
    GlobalConstantsWithTemplateIdDTO
from ib_tasks.interactors.storage_interfaces.task_template_storage_interface \
    import \
    TaskTemplateStorageInterface


class GlobalConstantsInteractor:
    def __init__(
            self, task_template_storage: TaskTemplateStorageInterface,
    ):
        self.task_template_storage = task_template_storage

    def create_global_constants_to_template_wrapper(
            self,
            global_constants_with_template_id_dto:
            GlobalConstantsWithTemplateIdDTO):
        self.create_global_constants_to_template(
            global_constants_with_template_id_dto
            =global_constants_with_template_id_dto
        )

    def create_global_constants_to_template(
            self,
            global_constants_with_template_id_dto:
            GlobalConstantsWithTemplateIdDTO):
        template_id = global_constants_with_template_id_dto.template_id
        global_constants_dtos = \
            global_constants_with_template_id_dto.global_constants_dtos
        self._make_validations(
            template_id=template_id,
            global_constants_dtos=global_constants_dtos
        )
        existing_global_constant_names = self.task_template_storage. \
            get_constant_names_of_existing_global_constants_of_template(
            template_id=template_id
        )
        existing_global_constant_names_not_in_given_data = \
            self._get_existing_global_constant_names_that_are_not_in_given_data(
                existing_global_constant_names=existing_global_constant_names,
                global_constants_dtos=global_constants_dtos
            )
        self._create_global_constants_in_db(
            template_id=template_id,
            existing_global_constant_names=existing_global_constant_names,
            global_constants_dtos=global_constants_dtos
        )

        from ib_tasks.exceptions.constants_custom_exceptions import \
            ExistingGlobalConstantNamesNotInGivenData
        from ib_tasks.constants.exception_messages import \
            EXISTING_GLOBAL_CONSTANT_NAMES_NOT_IN_GIVEN_DATA
        if existing_global_constant_names_not_in_given_data:
            message = EXISTING_GLOBAL_CONSTANT_NAMES_NOT_IN_GIVEN_DATA.format(
                existing_global_constant_names_not_in_given_data
            )
            raise ExistingGlobalConstantNamesNotInGivenData(message)

    def _create_global_constants_in_db(
            self, template_id: str,
            global_constants_dtos: List[GlobalConstantsDTO],
            existing_global_constant_names: List[str]):

        global_constants_dtos_to_create, global_constants_dtos_to_update = \
            self._filter_global_constants_dtos_to_create_and_update(
                global_constants_dtos=global_constants_dtos,
                existing_global_constant_names=existing_global_constant_names
            )

        self.task_template_storage.create_global_constants_to_template(
            template_id=template_id,
            global_constants_dtos=global_constants_dtos_to_create
        )
        self.task_template_storage.update_global_constants_to_template(
            template_id=template_id,
            global_constants_dtos=global_constants_dtos_to_update
        )

    def _make_validations(
            self, template_id: str,
            global_constants_dtos: List[GlobalConstantsDTO]):
        self._validate_field_values_of_given_data(
            template_id=template_id,
            global_constants_dtos=global_constants_dtos
        )
        constant_names = self._get_constant_names(
            global_constants_dtos=global_constants_dtos
        )
        self._validate_uniqueness_in_constant_names(
            constant_names=constant_names
        )
        self._validate_template_id_in_db(template_id=template_id)

    def _validate_field_values_of_given_data(
            self, template_id: str,
            global_constants_dtos: List[GlobalConstantsDTO]):
        self._validate_value_for_template_id_field(template_id=template_id)
        self._validate_values_for_constant_name_fields_in_global_constants(
            global_constants_dtos=global_constants_dtos
        )
        self._validate_values_for_value_fields_in_global_constants(
            global_constants_dtos=global_constants_dtos
        )

    def _validate_template_id_in_db(self, template_id: str):
        is_valid_template_id = \
            self.task_template_storage.check_is_template_exists(
            template_id=template_id
        )
        is_invalid_template_id = not is_valid_template_id
        from ib_tasks.exceptions.task_custom_exceptions import \
            TemplateDoesNotExists
        from ib_tasks.constants.exception_messages import \
            TEMPLATE_DOES_NOT_EXISTS
        if is_invalid_template_id:
            message = TEMPLATE_DOES_NOT_EXISTS.format(template_id)
            raise TemplateDoesNotExists(message)

    def _validate_values_for_constant_name_fields_in_global_constants(
            self, global_constants_dtos: List[GlobalConstantsDTO]):
        for global_constants_dto in global_constants_dtos:
            self._validate_value_for_constant_name_field_in_global_constants(
                constant_name=global_constants_dto.constant_name
            )

    def _validate_values_for_value_fields_in_global_constants(
            self, global_constants_dtos: List[GlobalConstantsDTO]):
        for global_constants_dto in global_constants_dtos:
            self._validate_value_for_value_field_in_global_constants(
                value=global_constants_dto.value
            )

    def _get_existing_global_constant_names_that_are_not_in_given_data(
            self, existing_global_constant_names: List[str],
            global_constants_dtos: List[GlobalConstantsDTO]):
        given_global_constant_names = \
            self._get_constant_names(
                global_constants_dtos=global_constants_dtos
            )

        existing_global_constant_names_not_in_given_data = [
            global_constant_name
            for global_constant_name in existing_global_constant_names
            if global_constant_name not in given_global_constant_names
        ]
        return existing_global_constant_names_not_in_given_data

    @staticmethod
    def _validate_value_for_template_id_field(template_id: str):
        template_id_after_strip = template_id.strip()
        is_template_id_empty = not template_id_after_strip
        from ib_tasks.exceptions.fields_custom_exceptions import \
            InvalidValueForField
        from ib_tasks.constants.exception_messages import \
            INVALID_VALUE_FOR_TEMPLATE_ID
        if is_template_id_empty:
            message = INVALID_VALUE_FOR_TEMPLATE_ID
            raise InvalidValueForField(message)

    @staticmethod
    def _validate_value_for_constant_name_field_in_global_constants(
            constant_name: str):
        constant_name_after_strip = constant_name.strip()
        is_constant_name_empty = not constant_name_after_strip
        from ib_tasks.exceptions.fields_custom_exceptions import \
            InvalidValueForField
        from ib_tasks.constants.exception_messages import \
            INVALID_VALUE_FOR_CONSTANT_NAME
        if is_constant_name_empty:
            message = INVALID_VALUE_FOR_CONSTANT_NAME
            raise InvalidValueForField(message)

    @staticmethod
    def _validate_value_for_value_field_in_global_constants(value: int):
        is_invalid_value = value < 0
        from ib_tasks.exceptions.fields_custom_exceptions import \
            InvalidValueForField
        from ib_tasks.constants.exception_messages import \
            INVALID_VALUE_FOR_VALUE
        if is_invalid_value:
            message = INVALID_VALUE_FOR_VALUE.format(value)
            raise InvalidValueForField(message)

    @staticmethod
    def _validate_uniqueness_in_constant_names(constant_names: List[str]):
        from collections import Counter
        constant_names_counter = Counter(constant_names)

        duplicate_constant_names = []
        for constant_name, count in constant_names_counter.items():
            is_duplicate_constant_name = count > 1
            if is_duplicate_constant_name:
                duplicate_constant_names.append(constant_name)

        from ib_tasks.exceptions.constants_custom_exceptions import \
            DuplicateConstantNames
        from ib_tasks.constants.exception_messages import \
            DUPLICATE_CONSTANT_NAMES
        if duplicate_constant_names:
            message = \
                DUPLICATE_CONSTANT_NAMES.format(duplicate_constant_names)
            raise DuplicateConstantNames(message)

    @staticmethod
    def _get_constant_names(global_constants_dtos: List[GlobalConstantsDTO]):
        constant_names = [
            global_constants_dto.constant_name
            for global_constants_dto in global_constants_dtos
        ]
        return constant_names

    @staticmethod
    def _filter_global_constants_dtos_to_create_and_update(
            existing_global_constant_names: List[str],
            global_constants_dtos: List[GlobalConstantsDTO]):
        global_constant_dtos_to_create = []
        global_constant_dtos_to_update = []

        for global_constant_dto in global_constants_dtos:
            is_global_constant_already_exists = \
                global_constant_dto.constant_name in \
                existing_global_constant_names
            if is_global_constant_already_exists:
                global_constant_dtos_to_update.append(global_constant_dto)
            else:
                global_constant_dtos_to_create.append(global_constant_dto)
        return global_constant_dtos_to_create, global_constant_dtos_to_update
