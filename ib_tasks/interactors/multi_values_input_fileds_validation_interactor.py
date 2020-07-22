import collections
from typing import Optional
import json
from ib_tasks.interactors.storage_interfaces.dtos \
    import FieldDTO

from ib_tasks.exceptions.fields_custom_exceptions import (
    EmptyValuesForFieldValues,
    DuplicationOfFieldValuesForFieldTypeMultiValues
)


class MultiValuesInputFieldsValidationInteractor:

    def multi_values_input_fields_validations(self, field_dto: FieldDTO):
        self._check_field_values_is_empty(field_dto)
        self._check_for_empty_values_in_field_values(field_dto)
        self._check_for_duplication_of_field_values(field_dto)
        field_value = field_dto.field_values
        field_dto.field_values = json.dumps(field_value)

    @staticmethod
    def _check_field_values_is_empty(
            field_dto: FieldDTO
    ) -> Optional[EmptyValuesForFieldValues]:
        from ib_tasks.constants.exception_messages \
            import EMPTY_VALUE_FOR_FIELD_VALUE
        field_values = field_dto.field_values
        is_field_values_empty = not field_values
        if is_field_values_empty:
            raise EmptyValuesForFieldValues(
                EMPTY_VALUE_FOR_FIELD_VALUE.format(field_dto.field_id)
            )
        return

    @staticmethod
    def _check_for_empty_values_in_field_values(
            field_dto: FieldDTO
    ) -> Optional[EmptyValuesForFieldValues]:

        from ib_tasks.constants.exception_messages \
            import EMPTY_VALUE_FOR_FIELD_VALUE
        field_values = field_dto.field_values
        for field_value in field_values:
            is_field_value_empty = not field_value.strip()
            if is_field_value_empty:
                field_id = field_dto.field_id
                raise EmptyValuesForFieldValues(
                    EMPTY_VALUE_FOR_FIELD_VALUE.format(field_id)
                )
        return

    @staticmethod
    def _check_for_duplication_of_field_values(
            field_dto: FieldDTO
    ) -> Optional[DuplicationOfFieldValuesForFieldTypeMultiValues]:

        from ib_tasks.constants.exception_messages \
            import DUPLICATION_OF_FIELD_VALUES
        field_values = field_dto.field_values
        duplication_of_field_values = [
            value
            for value, count in collections.Counter(field_values).items()
            if count > 1
        ]
        if duplication_of_field_values:
            field_dict = {
                "field_id": field_dto.field_id,
                "field_type": field_dto.field_type,
                "duplication_of_values": duplication_of_field_values
            }
            raise DuplicationOfFieldValuesForFieldTypeMultiValues(
                DUPLICATION_OF_FIELD_VALUES.format(field_dict)
            )
        return
