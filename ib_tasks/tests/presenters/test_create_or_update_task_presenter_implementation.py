import pytest

from ib_tasks.exceptions.fields_custom_exceptions import InvalidFieldIds

from ib_tasks.exceptions.field_values_custom_exceptions import \
    EmptyValueForPlainTextField
from ib_tasks.exceptions.gofs_custom_exceptions import InvalidGoFIds
from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskTemplateIds


class TestCreateOrUpdateTaskPresenterImplementation:

    @pytest.fixture
    def presenter(self):
        from ib_tasks.presenters.create_or_update_task_presenter_implementation \
            import CreateOrUpdateTaskPresenterImplementation
        return CreateOrUpdateTaskPresenterImplementation()

    def test_raise_exception_for_duplicate_field_ids(
            self, presenter, snapshot
    ):
        # Arrange
        from ib_tasks.exceptions.fields_custom_exceptions import \
            DuplicationOfFieldIdsExist
        err = DuplicationOfFieldIdsExist(
            field_ids=["FIELD_ID-1", "FIELD_ID-2"]
        )

        # Act
        response_object = \
            presenter.raise_exception_for_duplicate_field_ids(err)

        # Assert
        snapshot.assert_match(
            name="response_object", value=response_object.content
        )

    def test_raise_exception_for_invalid_task_template_id(
            self, presenter, snapshot
    ):
        # Arrange

        err = InvalidTaskTemplateIds(
            invalid_task_template_ids=["TASK_TEMPLATE_ID-0"]
        )

        # Act
        response_object = presenter.raise_exception_for_invalid_task_template_id(err)

        # Assert
        snapshot.assert_match(
            name="response_object", value=response_object.content
        )

    def test_raise_exception_for_invalid_gof_ids(self, presenter, snapshot):
        # Arrange

        err = InvalidGoFIds(
            invalid_gof_ids=["GOF_ID-0", "GOF_ID-1"]
        )

        # Act
        response_object = presenter.raise_exception_for_invalid_gof_ids(err)

        # Assert
        snapshot.assert_match(
            name="response_object", value=response_object.content
        )

    def test_raise_exception_for_invalid_field_ids(self, presenter, snapshot):
        # Arrange

        err = InvalidFieldIds(
            invalid_field_ids=["FIELD_ID-1", "FIELD_ID-2"]
        )

        # Act
        response_object = presenter.raise_exception_for_invalid_field_ids(err)

        # Assert
        snapshot.assert_match(
            name="response_object", value=response_object.content
        )

    def test_raise_exception_for_empty_value_in_plain_text_field(
            self, presenter, snapshot
    ):
        # Arrange

        err = EmptyValueForPlainTextField(
            field_id="FIELD_ID-1"
        )

        # Act
        response_object = presenter.raise_exception_for_empty_value_in_plain_text_field(err)

        # Assert
        snapshot.assert_match(
            name="response_object", value=response_object.content
        )

    def test_raise_exception_for_invalid_phone_number_value(selfself, presenter, snapshot):
        # Arrange
        from ib_tasks.exceptions.field_values_custom_exceptions import InvalidPhoneNumberValue
        err = InvalidPhoneNumberValue(field_id="FIELD_ID-1", field_value="73247832")

        # Act
        response_object = presenter.raise_exception_for_invalid_phone_number_value(err)

        # Assert
        snapshot.assert_match(
            name="response_object", value=response_object.content
        )

    def test_raise_exception_for_invalid_email_address(self, presenter, snapshot):
        # Arrange
        from ib_tasks.exceptions.field_values_custom_exceptions import InvalidEmailFieldValue
        err = InvalidEmailFieldValue(
            field_id="FIELD_ID-1", field_value="ibhubs@gmail.com"
        )

        # Act
        response_object = presenter.raise_exception_for_invalid_email_address(err)

        # Assert
        snapshot.assert_match(
            name="response_object", value=response_object.content
        )

    def test_raise_exception_for_invalid_url_address(self, presenter, snapshot):
        # Arrange
        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidURLValue
        err = InvalidURLValue(
            field_id="FIELD_ID-1", field_value="https://eiiuwe.com"
        )

        # Act
        response_object = presenter.raise_exception_for_invalid_url_address(err)

        # Assert
        snapshot.assert_match(
            name="response_object", value=response_object.content
        )
