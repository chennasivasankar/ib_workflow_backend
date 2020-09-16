import pytest
from ib_tasks.tests.factories.storage_dtos \
    import FieldDTOFactory
from ib_tasks.constants.enum import FieldTypes
from ib_tasks.interactors.create_or_update_fields\
    .field_type_searchable_validations_interactor \
    import FieldTypeSearchableValidationsInteractor


class TestFieldTypeSearchableValidationsInteractor:

    def test_given_empty_values_for_field_values_for_field_type_searchable_raise_exception(self):
        # Arrange
        from ib_tasks.constants.constants import SEARCHABLE_VALUES
        from ib_tasks.exceptions.fields_custom_exceptions import InvalidValueForSearchable
        from ib_tasks.constants.exception_messages \
            import INVALID_VALUE_FOR_SEARCHABLE
        field_dto = FieldDTOFactory(
            field_id="field1",
            field_type=FieldTypes.SEARCHABLE.value,
            field_values=" "
        )
        field_id = "field1"
        exception_message = INVALID_VALUE_FOR_SEARCHABLE.format(
            SEARCHABLE_VALUES, field_id
        )
        interactor = FieldTypeSearchableValidationsInteractor()

        # Act
        with pytest.raises(InvalidValueForSearchable) as err:
            interactor.field_type_searcahble_validations(field_dto)

        # Assert
        assert str(err.value) == exception_message

    def test_given_invalid_field_values_for_field_type_searchable_raise_exception(self):
        # Arrange
        from ib_tasks.constants.constants import SEARCHABLE_VALUES
        from ib_tasks.exceptions.fields_custom_exceptions import InvalidValueForSearchable
        from ib_tasks.constants.exception_messages \
            import INVALID_VALUE_FOR_SEARCHABLE
        field_dto = FieldDTOFactory(
            field_id="field1",
            field_type=FieldTypes.SEARCHABLE.value,
            field_values="Hello"
        )
        field_id = "field1"
        exception_message = INVALID_VALUE_FOR_SEARCHABLE.format(
            SEARCHABLE_VALUES, field_id
        )
        interactor = FieldTypeSearchableValidationsInteractor()

        # Act
        with pytest.raises(InvalidValueForSearchable) as err:
            interactor.field_type_searcahble_validations(field_dto)

        # Assert
        assert str(err.value) == exception_message