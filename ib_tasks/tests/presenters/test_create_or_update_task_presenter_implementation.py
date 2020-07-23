import pytest


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
        from ib_tasks.exceptions.custom_exceptions import \
            InvalidTaskTemplateIds
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
        from ib_tasks.exceptions.custom_exceptions import \
            InvalidGoFIds
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
        from ib_tasks.exceptions.custom_exceptions import \
            InvalidFieldIds
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
        from ib_tasks.exceptions.custom_exceptions import \
            EmptyValueForPlainTextField
        err = EmptyValueForPlainTextField(
            field_id="FIELD_ID-1"
        )

        # Act
        response_object = presenter.raise_exception_for_empty_value_in_plain_text_field(err)

        # Assert
        snapshot.assert_match(
            name="response_object", value=response_object.content
        )
