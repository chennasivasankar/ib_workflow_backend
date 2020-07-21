from ib_tasks.interactors.storage_interfaces.dtos \
    import FieldDTO


class FieldTypeSearchableValidationsInteractor:

    def field_type_searcahble_validations(self, field_dto: FieldDTO):
        self._validate_field_value(field_dto)
        self._check_for_empty_value(field_dto)

    @staticmethod
    def _validate_field_value(field_dto: FieldDTO):
        from ib_tasks.constants.enum import Searchable
        from ib_tasks.exceptions.custom_exceptions \
            import InvalidValueForSearchable
        from ib_tasks.constants.exception_messages \
            import INVALID_VALUE_FOR_SEARCHABLE
        from ib_tasks.constants.constants import SEARCHABLE_VALUES
        field_value = field_dto.field_values
        if field_value not in Searchable:
            raise InvalidValueForSearchable(
                INVALID_VALUE_FOR_SEARCHABLE.format(SEARCHABLE_VALUES)
            )
        return
