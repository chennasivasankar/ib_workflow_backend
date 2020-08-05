import pytest
from ib_tasks.tests.factories.storage_dtos import \
    FieldDTOFactory
from ib_tasks.interactors.multi_values_input_fileds_validation_interactor \
    import MultiValuesInputFieldsValidationInteractor
from ib_tasks.constants.enum import FieldTypes


class TestMultiValuesInputFieldsValidationInteractor:

    @pytest.mark.parametrize(
        "field_type",
        [
            FieldTypes.DROPDOWN.value,
            FieldTypes.RADIO_GROUP.value,
            FieldTypes.CHECKBOX_GROUP.value,
            FieldTypes.MULTI_SELECT_LABELS.value,
            FieldTypes.MULTI_SELECT_FIELD.value
        ]
    )
    def test_given_field_values_is_empty_raise_exceptions(self, field_type):
        # Arrange
        from ib_tasks.exceptions.fields_custom_exceptions \
            import EmptyValuesForFieldValues
        from ib_tasks.constants.exception_messages \
            import EMPTY_VALUE_FOR_FIELD_VALUE

        field_dto = FieldDTOFactory(
            field_id="field1", field_type=field_type, field_values=[]
        )
        field_id = "field1"
        exception_message = EMPTY_VALUE_FOR_FIELD_VALUE.format(field_id)
        interactor = MultiValuesInputFieldsValidationInteractor()

        # Act
        with pytest.raises(EmptyValuesForFieldValues) as err:
            interactor.multi_values_input_fields_validations(field_dto)

        # Assert
        assert str(err.value) == exception_message

    @pytest.mark.parametrize(
        "field_type",
        [
            FieldTypes.DROPDOWN.value,
            FieldTypes.RADIO_GROUP.value,
            FieldTypes.CHECKBOX_GROUP.value,
            FieldTypes.MULTI_SELECT_LABELS.value,
            FieldTypes.MULTI_SELECT_FIELD.value
        ]
    )
    def test_given_empty_values_in_field_values_raise_exceptions(
            self, field_type
    ):
        # Arrange
        from ib_tasks.exceptions.fields_custom_exceptions \
            import EmptyValuesForFieldValues
        from ib_tasks.constants.exception_messages \
            import EMPTY_VALUE_FOR_FIELD_VALUE

        field_dto = FieldDTOFactory(
            field_id="field1", field_type=field_type,
            field_values=["Mr", "  ", "Mrs"]
        )
        field_id = "field1"
        exception_message = EMPTY_VALUE_FOR_FIELD_VALUE.format(field_id)
        interactor = MultiValuesInputFieldsValidationInteractor()

        # Act
        with pytest.raises(EmptyValuesForFieldValues) as err:
            interactor.multi_values_input_fields_validations(field_dto)

        # Assert
        assert str(err.value) == exception_message

    @pytest.mark.parametrize(
        "field_type",
        [
            FieldTypes.DROPDOWN.value,
            FieldTypes.RADIO_GROUP.value,
            FieldTypes.CHECKBOX_GROUP.value,
            FieldTypes.MULTI_SELECT_LABELS.value,
            FieldTypes.MULTI_SELECT_FIELD.value
        ]
    )
    def test_given_duplication_of_field_values_raise_exception(
            self, field_type
    ):
        # Arrange
        from ib_tasks.exceptions.fields_custom_exceptions \
            import DuplicationOfFieldValuesForFieldTypeMultiValues
        from ib_tasks.constants.exception_messages \
            import DUPLICATION_OF_FIELD_VALUES

        field_dto = FieldDTOFactory(
            field_id="field1", field_type=field_type,
            field_values=["Mr", "Mrs", "Mrs"]
        )
        duplication_of_field_values = ["Mrs"]
        field_dict = {
            "field_id": "field1",
            "field_type": field_dto.field_type,
            "duplication_of_values": duplication_of_field_values
        }
        exception_message = DUPLICATION_OF_FIELD_VALUES.format(field_dict)
        interactor = MultiValuesInputFieldsValidationInteractor()

        # Act
        with pytest.raises(
                DuplicationOfFieldValuesForFieldTypeMultiValues
        ) as err:
            interactor.multi_values_input_fields_validations(field_dto)

        # Assert
        assert str(err.value) == exception_message
