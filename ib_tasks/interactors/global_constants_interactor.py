from typing import List
from ib_tasks.interactors.storage_interfaces.task_storage_interface \
    import TaskStorageInterface
from ib_tasks.interactors.dtos import GlobalConstantsWithTemplateIdDTO, \
    GlobalConstantsDTO


class GlobalConstantsInteractor:
    def __init__(self, task_storage: TaskStorageInterface):
        self.task_storage = task_storage

    def create_global_constants_wrapper(
            self,
            global_constants_with_template_id_dto: GlobalConstantsWithTemplateIdDTO
    ):
        self.create_global_constants(
            global_constants_with_template_id_dto=global_constants_with_template_id_dto
        )

    def create_global_constants(
            self,
            global_constants_with_template_id_dto: GlobalConstantsWithTemplateIdDTO
    ):
        template_id = global_constants_with_template_id_dto.template_id
        global_constants_dtos = \
            global_constants_with_template_id_dto.global_constants_dtos

        self._validate_field_values_of_given_data(
            template_id=template_id,
            global_constants_dtos=global_constants_dtos
        )
        self._validate_template_id_in_db(template_id=template_id)
        existing_global_constant_names = self.task_storage.\
            get_constant_names_of_existing_global_constants_of_template(
                template_id=template_id
            )
        existing_global_constant_names_not_in_given_data = \
            self._get_existing_global_constant_names_that_are_not_in_given_data(
                existing_global_constant_names=existing_global_constant_names,
                global_constants_dtos=global_constants_dtos
            )
        global_constants_dtos_to_create = \
            self._get_global_constant_dtos_to_create(
                global_constants_dtos=global_constants_dtos,
                existing_global_constant_names=existing_global_constant_names
            )
        self.task_storage.create_global_constants_to_template(
            template_id=template_id,
            global_constants_dtos=global_constants_dtos_to_create
        )
        from ib_tasks.exceptions.custom_exceptions import \
            ExistingGlobalConstantNamesNotInGivenData
        if existing_global_constant_names_not_in_given_data:
            raise ExistingGlobalConstantNamesNotInGivenData(
                existing_global_constant_names_not_in_given_data
            )

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
        is_valid_template_id = self.task_storage.check_is_template_exists(
            template_id=template_id
        )
        is_invalid_template_id = not is_valid_template_id
        from ib_tasks.exceptions.custom_exceptions import \
            TemplateDoesNotExists
        if is_invalid_template_id:
            raise TemplateDoesNotExists(template_id)

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

    @staticmethod
    def _validate_value_for_template_id_field(template_id: str):
        is_template_id_is_string = (type(template_id) == str)
        is_template_id_not_a_string = not is_template_id_is_string
        from ib_tasks.exceptions.custom_exceptions import InvalidValueForField
        if is_template_id_not_a_string:
            raise InvalidValueForField("template_id")

        template_id_after_strip = template_id.strip()
        is_template_id_empty = not template_id_after_strip
        if is_template_id_empty:
            raise InvalidValueForField("template_id")

    @staticmethod
    def _validate_value_for_constant_name_field_in_global_constants(
            constant_name: str):
        is_constant_name_is_string = (type(constant_name) == str)
        is_constant_name_not_a_string = not is_constant_name_is_string
        from ib_tasks.exceptions.custom_exceptions import InvalidValueForField
        if is_constant_name_not_a_string:
            raise InvalidValueForField("constant_name")

        constant_name_after_strip = constant_name.strip()
        is_constant_name_empty = not constant_name_after_strip
        if is_constant_name_empty:
            raise InvalidValueForField("constant_name")

    @staticmethod
    def _validate_value_for_value_field_in_global_constants(value: str):
        is_value_is_string = (type(value) == str)
        is_value_not_a_string = not is_value_is_string
        from ib_tasks.exceptions.custom_exceptions import InvalidValueForField
        if is_value_not_a_string:
            raise InvalidValueForField("value")
        value_after_strip = value.strip()
        is_value_empty = not value_after_strip
        if is_value_empty:
            raise InvalidValueForField("value")

    @staticmethod
    def _get_existing_global_constant_names_that_are_not_in_given_data(
            existing_global_constant_names: List[str],
            global_constants_dtos=List[GlobalConstantsDTO]):
        given_global_constant_names = [
            global_constants_dto.constant_name
            for global_constants_dto in global_constants_dtos
        ]
        existing_global_constant_names_not_in_given_data = [
            global_constant_name
            for global_constant_name in existing_global_constant_names
            if global_constant_name not in given_global_constant_names
        ]
        return existing_global_constant_names_not_in_given_data

    @staticmethod
    def _get_global_constant_dtos_to_create(
            existing_global_constant_names: List[str],
            global_constants_dtos=List[GlobalConstantsDTO]):
        global_constants_dtos_to_add_to_template = [
            global_constants_dto
            for global_constants_dto in global_constants_dtos
            if global_constants_dto.constant_name not in existing_global_constant_names
        ]
        return global_constants_dtos_to_add_to_template
