from typing import List


class InvalidGoFIDsInGoFSelectorField(Exception):

    def __init__(self, gof_ids: List[str]):
        self.gof_ids = gof_ids


class EmptyValueForPlainTextField(Exception):

    def __init__(self, field_id: str):
        self.field_id = field_id


class InvalidPhoneNumberValue(Exception):

    def __init__(self, field_id: str, field_value: str):
        self.field_id = field_id
        self.field_value = field_value


class InvalidEmailFieldValue(Exception):

    def __init__(self, field_id: str, field_value: str):
        self.field_id = field_id
        self.field_value = field_value


class InvalidURLValue(Exception):

    def __init__(self, field_id: str, field_value: str):
        self.field_id = field_id
        self.field_value = field_value


class NotAStrongPassword(Exception):

    def __init__(self, field_id: str, field_value: str):
        self.field_id = field_id
        self.field_value = field_value


class InvalidNumberValue(Exception):

    def __init__(self, field_id: str, field_value: str):
        self.field_id = field_id
        self.field_value = field_value


class InvalidFloatValue(Exception):

    def __init__(self, field_id: str, field_value: str):
        self.field_id = field_id
        self.field_value = field_value


class InvalidValueForLongText(Exception):

    def __init__(self, field_id: str, field_value: str):
        self.field_id = field_id
        self.field_value = field_value


class InvalidValueForDropdownField(Exception):

    def __init__(self, field_id: str, field_value: str,
                 valid_values: List[str]):
        self.field_id = field_id
        self.field_value = field_value
        self.valid_values = valid_values


class IncorrectGoFIDInGoFSelectorField(Exception):

    def __init__(
            self, field_id: str, field_value: str,
            valid_gof_id_options: List[str]
    ):
        self.field_id = field_id
        self.field_value = field_value
        self.valid_gof_id_options = valid_gof_id_options


class IncorrectRadioGroupChoice(Exception):

    def __init__(
            self, field_id: str, field_value: str,
            valid_radio_group_options: List[str]
    ):
        self.field_id = field_id
        self.field_value = field_value
        self.valid_radio_group_options = valid_radio_group_options


class IncorrectCheckBoxOptionsSelected(Exception):

    def __init__(
            self, field_id: str,
            invalid_checkbox_options: List[str],
            valid_check_box_options: List[str]
    ):
        self.field_id = field_id
        self.invalid_checkbox_options = invalid_checkbox_options
        self.valid_check_box_options = valid_check_box_options


class IncorrectMultiSelectOptionsSelected(Exception):

    def __init__(
            self, field_id: str,
            invalid_multi_select_options: List[str],
            valid_multi_select_options: List[str]
    ):
        self.field_id = field_id
        self.invalid_multi_select_options = invalid_multi_select_options
        self.valid_multi_select_options = valid_multi_select_options


class IncorrectMultiSelectLabelsSelected(Exception):

    def __init__(
            self, field_id: str,
            invalid_multi_select_labels: List[str],
            valid_multi_select_labels: List[str]
    ):
        self.field_id = field_id
        self.invalid_multi_select_labels = invalid_multi_select_labels
        self.valid_multi_select_labels = valid_multi_select_labels


class InvalidDateFormat(Exception):

    def __init__(self, field_id: str, field_value: str, expected_format: str):
        self.field_id = field_id
        self.field_value = field_value
        self.expected_format = expected_format


class InvalidTimeFormat(Exception):

    def __init__(self, field_id: str, field_value: str, expected_format: str):
        self.field_id = field_id
        self.field_value = field_value
        self.expected_format = expected_format


class InvalidUrlForImage(Exception):

    def __init__(
            self, field_id: str, image_url: str
    ):
        self.field_id = field_id
        self.image_url = image_url


class InvalidUrlForFolder(Exception):

    def __init__(
            self, field_id: str, folder_url: str
    ):
        self.field_id = field_id
        self.folder_url = folder_url


class CouldNotReadImage(Exception):

    def __init__(self, field_id: str, given_url: str):
        self.field_id = field_id
        self.given_url = given_url


class InvalidImageFormat(Exception):

    def __init__(
            self, field_id: str, given_format: str, allowed_formats: List[str]
    ):
        self.field_id = field_id
        self.given_format = given_format
        self.allowed_formats = allowed_formats


class NotAnImageUrl(Exception):

    def __init__(self, field_id: str, given_url: str):
        self.field_id = field_id
        self.given_url = given_url
