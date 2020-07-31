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
        response_object = presenter.raise_exception_for_invalid_task_template_id(
            err)

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
        response_object = presenter.raise_exception_for_empty_value_in_plain_text_field(
            err)

        # Assert
        snapshot.assert_match(
            name="response_object", value=response_object.content
        )

    def test_raise_exception_for_invalid_phone_number_value(selfself,
                                                            presenter,
                                                            snapshot):
        # Arrange
        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidPhoneNumberValue
        err = InvalidPhoneNumberValue(field_id="FIELD_ID-1",
                                      field_value="73247832")

        # Act
        response_object = presenter.raise_exception_for_invalid_phone_number_value(
            err)

        # Assert
        snapshot.assert_match(
            name="response_object", value=response_object.content
        )

    def test_raise_exception_for_invalid_email_address(self, presenter,
                                                       snapshot):
        # Arrange
        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidEmailFieldValue
        err = InvalidEmailFieldValue(
            field_id="FIELD_ID-1", field_value="ibhubs@gmail.com"
        )

        # Act
        response_object = presenter.raise_exception_for_invalid_email_address(
            err)

        # Assert
        snapshot.assert_match(
            name="response_object", value=response_object.content
        )

    def test_raise_exception_for_invalid_url_address(self, presenter,
                                                     snapshot):
        # Arrange
        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidURLValue
        err = InvalidURLValue(
            field_id="FIELD_ID-1", field_value="https://eiiuwe.com"
        )

        # Act
        response_object = presenter.raise_exception_for_invalid_url_address(
            err)

        # Assert
        snapshot.assert_match(
            name="response_object", value=response_object.content
        )

    def test_raise_exception_for_weak_password(self, presenter, snapshot):
        # Arrange
        from ib_tasks.exceptions.field_values_custom_exceptions import \
            NotAStrongPassword
        err = NotAStrongPassword(
            field_id="FIELD_ID-1", field_value="admin123"
        )

        # Act
        response_object = presenter.raise_exception_for_weak_password(err)

        # Assert
        snapshot.assert_match(
            name="response_object", value=response_object.content
        )

    def test_raise_exception_for_invalid_number_value(self, presenter,
                                                      snapshot):
        # Arrange
        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidNumberValue
        err = InvalidNumberValue(
            field_id="FIELD_ID-1", field_value="123a"
        )

        # Act
        response_object = presenter.raise_exception_for_invalid_number_value(
            err)

        # Assert
        snapshot.assert_match(
            name="response_object", value=response_object.content
        )

    def test_raise_exception_for_invalid_float_value(self, presenter,
                                                     snapshot):
        # Arrange
        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidFloatValue
        err = InvalidFloatValue(
            field_id="FIELD_ID-1", field_value="123a.0"
        )

        # Act
        response_object = presenter.raise_exception_for_invalid_float_value(
            err)

        # Assert
        snapshot.assert_match(
            name="response_object", value=response_object.content
        )

    def test_raise_exception_for_invalid_dropdown_value(self, presenter,
                                                        snapshot):
        # Arrange
        expected_valid_dropdown_values = ["DROPDOWN_1", "DROPDOWN_2"]
        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidValueForDropdownField
        err = InvalidValueForDropdownField(
            field_id="FIELD_ID-1", field_value="32684902319",
            valid_values=expected_valid_dropdown_values
        )

        # Act
        response_object = presenter.raise_exception_for_invalid_dropdown_value(
            err)

        # Assert
        snapshot.assert_match(
            name="response_object", value=response_object.content
        )

    def test_raise_exceptions_for_invalid_gof_id_selected_in_gof_selector(self,
                                                                          presenter,
                                                                          snapshot):
        # Arrange
        expected_valid_gof_id_options = ["industry", "individual"]
        from ib_tasks.exceptions.field_values_custom_exceptions import \
            IncorrectNameInGoFSelectorField
        err = IncorrectNameInGoFSelectorField(
            field_id="FIELD_ID-1", field_value="32684902319",
            valid_gof_selector_names=expected_valid_gof_id_options
        )

        # Act
        response_object = presenter.raise_exceptions_for_invalid_gof_id_selected_in_gof_selector(
            err)

        # Assert
        snapshot.assert_match(
            name="response_object", value=response_object.content
        )

    def test_raise_exception_for_invalid_choice_in_radio_group_field(self,
                                                                     presenter,
                                                                     snapshot):
        # Arrange
        expected_valid_radio_group_choice = ["RADIO_1", "RADIO_2"]
        from ib_tasks.exceptions.field_values_custom_exceptions import \
            IncorrectRadioGroupChoice
        err = IncorrectRadioGroupChoice(
            field_id="FIELD_ID-1", field_value="32684902319",
            valid_radio_group_options=expected_valid_radio_group_choice
        )

        # Act
        response_object = presenter.raise_exception_for_invalid_choice_in_radio_group_field(
            err)

        # Assert
        snapshot.assert_match(
            name="response_object", value=response_object.content
        )

    def test_raise_exception_for_invalid_checkbox_group_options_selected(self,
                                                                         presenter,
                                                                         snapshot):
        # Arrange
        expected_valid_checkbox_options = ["CHECK_BOX_1", "CHECK_BOX_2"]
        expected_invalid_checkbox_options = ["CHECK_BOX_3", "CHECK_BOX_4"]
        from ib_tasks.exceptions.field_values_custom_exceptions import \
            IncorrectCheckBoxOptionsSelected
        err = IncorrectCheckBoxOptionsSelected(
            field_id="FIELD_ID-1",
            valid_check_box_options=expected_valid_checkbox_options,
            invalid_checkbox_options=expected_invalid_checkbox_options
        )

        # Act
        response_object = presenter.raise_exception_for_invalid_checkbox_group_options_selected(
            err)

        # Assert
        snapshot.assert_match(
            name="response_object", value=response_object.content
        )

    def test_raise_exception_for_invalid_multi_select_options_selected(self,
                                                                       presenter,
                                                                       snapshot):
        # Arrange
        expected_valid_multi_select_options = ["MULTI_SELECT_1",
                                               "MULTI_SELECT_2"]
        expected_invalid_multi_select_options = ["MULTI_SELECT_3",
                                                 "MULTI_SELECT_4"]
        from ib_tasks.exceptions.field_values_custom_exceptions import \
            IncorrectMultiSelectOptionsSelected
        err = IncorrectMultiSelectOptionsSelected(
            field_id="FIELD_ID-1",
            invalid_multi_select_options=expected_invalid_multi_select_options,
            valid_multi_select_options=expected_valid_multi_select_options
        )

        # Act
        response_object = presenter.raise_exception_for_invalid_multi_select_options_selected(
            err)

        # Assert
        snapshot.assert_match(
            name="response_object", value=response_object.content
        )

    def test_raise_exception_for_invalid_multi_select_labels_selected(self,
                                                                      presenter,
                                                                      snapshot):
        # Arrange
        expected_valid_multi_select_labels = ["MULTI_SELECT_LABEL_1",
                                              "MULTI_SELECT_LABEL_2"]
        expected_invalid_multi_select_labels = ["MULTI_SELECT_LABEL_3",
                                                "MULTI_SELECT_LABEL_4"]
        from ib_tasks.exceptions.field_values_custom_exceptions import \
            IncorrectMultiSelectLabelsSelected
        err = IncorrectMultiSelectLabelsSelected(
            field_id="FIELD_ID-1",
            valid_multi_select_labels=expected_valid_multi_select_labels,
            invalid_multi_select_labels=expected_invalid_multi_select_labels
        )

        # Act
        response_object = presenter.raise_exception_for_invalid_multi_select_labels_selected(
            err)

        # Assert
        snapshot.assert_match(
            name="response_object", value=response_object.content
        )

    def test_raise_exception_for_invalid_date_format(self,
                                                     presenter,
                                                     snapshot):
        # Arrange
        expected_invalid_date = "02-04-2002"
        expected_format = "YYYY/MM/DD"
        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidDateFormat
        err = InvalidDateFormat(
            field_id="FIELD_ID-1",
            field_value=expected_invalid_date,
            expected_format=expected_format
        )

        # Act
        response_object = presenter.raise_exception_for_invalid_date_format(
            err)

        # Assert
        snapshot.assert_match(
            name="response_object", value=response_object.content
        )

    def test_raise_exception_for_invalid_time_format(self,
                                                     presenter,
                                                     snapshot):
        # Arrange
        expected_invalid_time = "04/50"
        expected_format = "HH:SS"
        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidTimeFormat
        err = InvalidTimeFormat(
            field_id="FIELD_ID-1",
            field_value=expected_invalid_time,
            expected_format=expected_format
        )

        # Act
        response_object = presenter.raise_exception_for_invalid_time_format(
            err)

        # Assert
        snapshot.assert_match(
            name="response_object", value=response_object.content
        )

    def test_raise_exception_for_not_acceptable_image_format(self,
                                                             presenter,
                                                             snapshot):
        # Arrange
        invalid_url = "ib_hubs.pdf"
        expected_valid_formats = ['jpeg', 'jpg', 'png']
        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidImageFormat
        err = InvalidImageFormat(
            field_id="FIELD_ID-1",
            given_format=invalid_url,
            allowed_formats=expected_valid_formats
        )

        # Act
        response_object = presenter.raise_exception_for_not_acceptable_image_format(
            err)

        # Assert
        snapshot.assert_match(
            name="response_object", value=response_object.content
        )

    def test_raise_exception_for_invalid_image_url(self, presenter, snapshot):
        # Arrange
        invalid_url = "https://google.com/ib.pdf"
        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidUrlForImage
        err = InvalidUrlForImage(
            field_id="FIELD_ID-1",
            image_url=invalid_url
        )

        # Act
        response_object = presenter.raise_exception_for_invalid_image_url(err)

        # Assert
        snapshot.assert_match(
            name="response_object", value=response_object.content
        )

    def test_raise_exception_for_invalid_file_url(self, presenter, snapshot):
        # Arrange
        invalid_url = "https://google.com/ib.pdf"
        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidUrlForFile
        err = InvalidUrlForFile(
            field_id="FIELD_ID-1",
            file_url=invalid_url
        )

        # Act
        response_object = presenter.raise_exception_for_invalid_file_url(err)

        # Assert
        snapshot.assert_match(
            name="response_object", value=response_object.content
        )

    def test_raise_exception_for_gof_ids_in_gof_selector_field_value(self,
                                                                     presenter,
                                                                     snapshot):
        # Arrange
        invalid_gof_ids = ['gof_1', 'gof_2']
        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidGoFIDsInGoFSelectorField
        err = InvalidGoFIDsInGoFSelectorField(
            gof_ids=invalid_gof_ids
        )

        # Act
        response_object = presenter.raise_exception_for_invalid_name_in_gof_selector_field_value(
            err)

        # Assert
        snapshot.assert_match(
            name="response_object", value=response_object.content
        )

    def test_raise_exception_for_not_acceptable_file_format(self, presenter,
                                                            snapshot):
        # Arrange
        invalid_file_format = ".mp4"
        expected_allowed_formats = ['pdf']
        field_id = "FIELD_1"
        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidFileFormat
        err = InvalidFileFormat(
            field_id=field_id, given_format=invalid_file_format,
            allowed_formats=expected_allowed_formats
        )

        # Act
        response_object = presenter.raise_exception_for_not_acceptable_file_format(
            err)

        # Assert
        snapshot.assert_match(
            name="response_object", value=response_object.content
        )

    def test_raise_exception_for_empty_value_in_required_field(self, presenter,
                                                               snapshot):
        # Arrange
        field_id = "FIELD_1"
        from ib_tasks.exceptions.field_values_custom_exceptions import \
            EmptyValueForRequiredField
        err = EmptyValueForRequiredField(field_id=field_id)

        # Act
        response_object = presenter.raise_exception_for_empty_value_in_required_field(
            err)

        # Assert
        snapshot.assert_match(
            name="response_object", value=response_object.content
        )
