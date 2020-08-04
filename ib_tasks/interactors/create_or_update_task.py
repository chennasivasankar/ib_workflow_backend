import json
from typing import Optional, List, Union

from ib_tasks.constants.enum import FieldTypes
from ib_tasks.exceptions.field_values_custom_exceptions import \
    InvalidPhoneNumberValue, EmptyValueForPlainTextField, \
    InvalidEmailFieldValue, InvalidURLValue, NotAStrongPassword, \
    InvalidNumberValue, InvalidFloatValue, \
    InvalidValueForDropdownField, InvalidGoFIDsInGoFSelectorField, \
    IncorrectNameInGoFSelectorField, IncorrectRadioGroupChoice, \
    IncorrectCheckBoxOptionsSelected, IncorrectMultiSelectOptionsSelected, \
    IncorrectMultiSelectLabelsSelected, InvalidDateFormat, InvalidTimeFormat, \
    InvalidUrlForImage, InvalidImageFormat, NotAnImageUrl, CouldNotReadImage, \
    InvalidUrlForFile, EmptyValueForRequiredField, InvalidFileFormat
from ib_tasks.exceptions.fields_custom_exceptions import \
    DuplicationOfFieldIdsExist, InvalidFieldIds
from ib_tasks.exceptions.gofs_custom_exceptions import InvalidGoFIds
from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskTemplateIds, \
    InvalidTaskException
from ib_tasks.interactors.storage_interfaces. \
    create_or_update_task_storage_interface import \
    CreateOrUpdateTaskStorageInterface
from ib_tasks.interactors.storage_interfaces.fields_dtos import \
    FieldDetailsDTO, FieldCompleteDetailsDTO
from ib_tasks.interactors.storage_interfaces.fields_storage_interface import \
    FieldsStorageInterface
from ib_tasks.interactors.storage_interfaces.stages_storage_interface import \
    StageStorageInterface
from ib_tasks.interactors.storage_interfaces.task_dtos import \
    TaskGoFWithTaskIdDTO, \
    TaskGoFDetailsDTO
from ib_tasks.interactors.storage_interfaces.get_task_dtos import \
    TaskGoFFieldDTO
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface
from ib_tasks.interactors.presenter_interfaces. \
    create_or_update_task_presenter import CreateOrUpdateTaskPresenterInterface
from ib_tasks.interactors.task_dtos import TaskDTO, FieldValuesDTO, \
    GoFFieldsDTO
from ib_tasks.interactors.user_action_on_task_interactor import \
    UserActionOnTaskInteractor
from ib_tasks.interactors.storage_interfaces.storage_interface import \
    StorageInterface
from ib_tasks.interactors.presenter_interfaces.presenter_interface import \
    PresenterInterface


class CreateOrUpdateTaskInteractor:

    def __init__(
            self, task_storage: TaskStorageInterface,
            create_task_storage: CreateOrUpdateTaskStorageInterface,
            storage: StorageInterface, field_storage: FieldsStorageInterface,
            stage_storage: StageStorageInterface
    ):
        self.task_storage = task_storage
        self.create_task_storage = create_task_storage
        self.storage = storage
        self.field_storage = field_storage
        self.stage_storage = stage_storage

    def create_or_update_task_wrapper(
            self, presenter: CreateOrUpdateTaskPresenterInterface,
            task_dto: TaskDTO, act_on_task_presenter: PresenterInterface
    ):
        try:
            return self._prepare_response_for_create_or_update_task(
                presenter=presenter, task_dto=task_dto,
                act_on_task_presenter=act_on_task_presenter
            )
        except DuplicationOfFieldIdsExist as err:
            return presenter.raise_exception_for_duplicate_field_ids(err)
        except InvalidTaskTemplateIds as err:
            return presenter.raise_exception_for_invalid_task_template_id(err)
        except InvalidGoFIds as err:
            return presenter.raise_exception_for_invalid_gof_ids(err)
        except InvalidFieldIds as err:
            return presenter.raise_exception_for_invalid_field_ids(err)
        except IncorrectNameInGoFSelectorField as err:
            return presenter. \
                raise_exception_for_invalid_name_in_gof_selector_field_value(
                    err
                )
        except EmptyValueForRequiredField as err:
            return presenter. \
                raise_exception_for_empty_value_in_required_field(err)
        except InvalidPhoneNumberValue as err:
            return presenter.raise_exception_for_invalid_phone_number_value(
                err)
        except InvalidEmailFieldValue as err:
            return presenter.raise_exception_for_invalid_email_address(err)
        except InvalidURLValue as err:
            return presenter.raise_exception_for_invalid_url_address(err)
        except NotAStrongPassword as err:
            return presenter.raise_exception_for_weak_password(err)
        except InvalidNumberValue as err:
            return presenter.raise_exception_for_invalid_number_value(err)
        except InvalidFloatValue as err:
            return presenter.raise_exception_for_invalid_float_value(err)
        except InvalidValueForDropdownField as err:
            return presenter.raise_exception_for_invalid_dropdown_value(err)
        except IncorrectRadioGroupChoice as err:
            return presenter. \
                raise_exception_for_invalid_choice_in_radio_group_field(err)
        except IncorrectCheckBoxOptionsSelected as err:
            return presenter. \
                raise_exception_for_invalid_checkbox_group_options_selected(
                err
            )
        except IncorrectMultiSelectOptionsSelected as err:
            return presenter. \
                raise_exception_for_invalid_multi_select_options_selected(err)
        except IncorrectMultiSelectLabelsSelected as err:
            return presenter. \
                raise_exception_for_invalid_multi_select_labels_selected(err)
        except InvalidDateFormat as err:
            return presenter.raise_exception_for_invalid_date_format(err)
        except InvalidTimeFormat as err:
            return presenter.raise_exception_for_invalid_time_format(err)
        except InvalidUrlForImage as err:
            return presenter.raise_exception_for_invalid_image_url(err)
        except InvalidImageFormat as err:
            return presenter.raise_exception_for_not_acceptable_image_format(
                err)
        except InvalidUrlForFile as err:
            return presenter.raise_exception_for_invalid_file_url(err)
        except InvalidFileFormat as err:
            return presenter.raise_exception_for_not_acceptable_file_format(
                err
            )
        except InvalidTaskException as err:
            return presenter.raise_exception_for_invalid_task_id(err)

    def _prepare_response_for_create_or_update_task(
            self, presenter: CreateOrUpdateTaskPresenterInterface,
            task_dto: TaskDTO, act_on_task_presenter: PresenterInterface
    ):
        self.create_or_update_task(
            task_dto, act_on_task_presenter
        )
        response = presenter.get_response_for_create_or_update_task()
        return response

    def create_or_update_task(
            self, task_dto: TaskDTO, act_on_task_presenter: PresenterInterface
    ):
        gof_ids = [
            gof_fields_dto.gof_id
            for gof_fields_dto in task_dto.gof_fields_dtos
        ]
        field_values_dtos = self._get_field_values_dtos(
            task_dto.gof_fields_dtos
        )
        field_ids = [
            field_values_dto.field_id
            for field_values_dto in field_values_dtos
        ]
        self._validate_for_invalid_gof_ids(gof_ids)
        self._validate_for_invalid_field_ids(field_ids)
        self._validate_field_values(field_values_dtos)

        task_needs_to_be_updated = task_dto.task_id is not None
        if task_needs_to_be_updated:
            self._update_task(task_dto)
        else:
            created_task_id = self._create_task(task_dto)
            task_dto.task_id = created_task_id
        act_on_task_interactor = UserActionOnTaskInteractor(
            user_id=task_dto.created_by_id, board_id=None,
            task_id=task_dto.task_id,
            action_id=task_dto.action_id,
            storage=self.storage, gof_storage=self.create_task_storage,
            field_storage=self.field_storage, stage_storage=self.stage_storage
        )

        self.create_task_storage.set_status_variables_for_template_and_task(
            task_dto.task_template_id, task_dto.task_id
        )
        # TODO: fix the return value

        from ib_tasks.models import TaskStage
        from ib_tasks.models import TaskTemplateInitialStage
        TaskStage.objects.get_or_create(
            task_id=task_dto.task_id,
            stage=TaskTemplateInitialStage.objects.get(
                task_template_id=task_dto.task_template_id
            ).stage
        )
        act_on_task_interactor.user_action_on_task()

    def _update_task(self, task_dto: TaskDTO):
        task_id = task_dto.task_id
        invalid_task_id = \
            not self.create_task_storage.is_valid_task_id(task_id)
        if invalid_task_id:
            raise InvalidTaskException(task_id)
        existing_gof_ids = \
            self.create_task_storage.get_gof_ids_related_to_a_task(
                task_id
            )
        existing_field_ids = \
            self.create_task_storage.get_field_ids_related_to_given_task(
                task_id
            )
        task_gof_dtos = [
            TaskGoFWithTaskIdDTO(
                task_id=task_id,
                gof_id=gof_fields_dto.gof_id,
                same_gof_order=gof_fields_dto.same_gof_order
            )
            for gof_fields_dto in task_dto.gof_fields_dtos
        ]
        task_gof_dtos_for_updation, task_gof_dtos_for_creation = [], []
        for task_gof_dto in task_gof_dtos:
            gof_id_already_exists = task_gof_dto.gof_id in existing_gof_ids
            if gof_id_already_exists:
                task_gof_dtos_for_updation.append(task_gof_dto)
            else:
                task_gof_dtos_for_creation.append(task_gof_dto)
        if task_gof_dtos_for_updation:
            task_gof_details_dtos = \
                self.create_task_storage.update_task_gofs(
                    task_gof_dtos_for_updation
                )
            task_gof_field_dtos = \
                self._prepare_task_gof_fields_dtos(
                    task_dto, task_gof_details_dtos
                )
            task_gof_field_dtos_for_updation, task_gof_field_dtos_for_creation = \
                self._filter_task_gof_field_dtos(
                    task_gof_field_dtos, existing_field_ids
                )
            if task_gof_field_dtos_for_updation:
                self.create_task_storage.update_task_gof_fields(
                    task_gof_field_dtos_for_updation
                )

            if task_gof_field_dtos_for_creation:
                self.create_task_storage.create_task_gof_fields(
                    task_gof_field_dtos_for_creation
                )
        if task_gof_dtos_for_creation:
            task_gof_details_dtos = \
                self.create_task_storage.create_task_gofs(
                    task_gof_dtos_for_creation
                )
            task_gof_field_dtos = \
                self._prepare_task_gof_fields_dtos(
                    task_dto, task_gof_details_dtos
                )
            self.create_task_storage.create_task_gof_fields(
                task_gof_field_dtos
            )

    @staticmethod
    def _filter_task_gof_field_dtos(
            task_gof_field_dtos: List[TaskGoFFieldDTO],
            existing_field_ids: List[str]
    ) -> (List[TaskGoFFieldDTO], List[TaskGoFFieldDTO]):
        task_gof_field_dtos_for_updation, task_gof_field_dtos_for_creation = \
            [], []
        for task_gof_field_dto in task_gof_field_dtos:
            field_id_already_exists = \
                task_gof_field_dto.field_id in existing_field_ids
            if field_id_already_exists:
                task_gof_field_dtos_for_updation.append(task_gof_field_dto)
            else:
                task_gof_field_dtos_for_creation.append(task_gof_field_dto)
        return task_gof_field_dtos_for_updation, \
               task_gof_field_dtos_for_creation

    def _create_task(self, task_dto: TaskDTO):
        self._validate_task_template_id(task_dto.task_template_id)
        created_task_id = \
            self.create_task_storage.create_task_with_template_id(
                task_dto.task_template_id, task_dto.created_by_id
            )
        task_gof_dtos = [
            TaskGoFWithTaskIdDTO(
                task_id=created_task_id,
                gof_id=gof_fields_dto.gof_id,
                same_gof_order=gof_fields_dto.same_gof_order
            )
            for gof_fields_dto in task_dto.gof_fields_dtos
        ]
        task_gof_details_dtos = self.create_task_storage.create_task_gofs(
            task_gof_dtos=task_gof_dtos
        )
        task_gof_field_dtos = self._prepare_task_gof_fields_dtos(
            task_dto, task_gof_details_dtos
        )
        self.create_task_storage.create_task_gof_fields(task_gof_field_dtos)
        return created_task_id

    def _prepare_task_gof_fields_dtos(
            self, task_dto: TaskDTO,
            task_gof_details_dtos: List[TaskGoFDetailsDTO]
    ) -> List[TaskGoFFieldDTO]:
        task_gof_field_dtos = []
        for gof_fields_dto in task_dto.gof_fields_dtos:
            task_gof_id = self._get_gof_id_for_field_in_task_gof_details(
                gof_fields_dto.gof_id, gof_fields_dto.same_gof_order,
                task_gof_details_dtos
            )
            task_gof_field_dtos += [
                TaskGoFFieldDTO(
                    field_id=field_values_dto.field_id,
                    field_response=field_values_dto.field_response,
                    task_gof_id=task_gof_id
                )
                for field_values_dto in gof_fields_dto.field_values_dtos
            ]
        return task_gof_field_dtos

    @staticmethod
    def _get_gof_id_for_field_in_task_gof_details(
            gof_id: str, same_gof_order: int,
            task_gof_details_dtos: List[TaskGoFDetailsDTO]
    ) -> Optional[int]:
        for task_gof_details_dto in task_gof_details_dtos:
            gof_matched = (
                    task_gof_details_dto.gof_id == gof_id and
                    task_gof_details_dto.same_gof_order == same_gof_order
            )
            if gof_matched:
                return task_gof_details_dto.task_gof_id
        return

    def _validate_field_values(
            self, field_values_dtos: List[FieldValuesDTO]
    ):
        field_ids = [
            field_values_dto.field_id for field_values_dto in field_values_dtos
        ]
        field_details_dtos = self.task_storage. \
            get_field_details_for_given_field_ids(field_ids=field_ids)

        for field_details_dto in field_details_dtos:
            field_value = self._get_field_value_for_given_field_id(
                field_id=field_details_dto.field_id,
                field_values_dtos=field_values_dtos
            )
            field_value = field_value.strip()
            field_id = field_details_dto.field_id
            field_is_required_but_not_given = (
                    not field_value and field_details_dto.required
            )
            if field_is_required_but_not_given:
                raise EmptyValueForRequiredField(field_id)
            field_is_not_required_and_empty_string_given = \
                not field_value and not field_details_dto.required
            if field_is_not_required_and_empty_string_given:
                continue
            field_type = field_details_dto.field_type
            field_type_is_phone_number = (
                    field_type == FieldTypes.PHONE_NUMBER.value
            )
            if field_type_is_phone_number:
                self._validate_phone_number_value(field_value, field_id)
            field_type_is_email = field_type == FieldTypes.EMAIL.value
            if field_type_is_email:
                self._validate_for_email_field_value(field_value, field_id)
            field_type_is_url = field_type == FieldTypes.URL.value
            if field_type_is_url:
                self._validate_for_url_field_value(field_value, field_id)
            field_type_is_password = field_type == FieldTypes.PASSWORD.value
            if field_type_is_password:
                self._validate_for_strong_password(field_value, field_id)
            field_type_is_number = field_type == FieldTypes.NUMBER.value
            if field_type_is_number:
                self._validate_for_number_value(field_value, field_id)
            field_type_is_float = field_type == FieldTypes.FLOAT.value
            if field_type_is_float:
                self._validate_for_float_value(field_value, field_id)
            field_type_is_dropdown = field_type == FieldTypes.DROPDOWN.value
            if field_type_is_dropdown:
                valid_dropdown_values = json.loads(
                    field_details_dto.field_values)
                self._validate_for_dropdown_field_value(
                    field_value, field_id, valid_dropdown_values
                )
            field_type_is_gof_selector = (
                    field_type == FieldTypes.GOF_SELECTOR.value
            )
            if field_type_is_gof_selector:
                field_values_dicts = json.loads(
                    field_details_dto.field_values
                )
                valid_gof_selector_names = [
                    field_values_dict['name']
                    for field_values_dict in field_values_dicts
                ]

                self._validate_gof_selector_value(
                    field_value, field_id, valid_gof_selector_names
                )
            field_type_is_radio_group = (
                    field_type == FieldTypes.RADIO_GROUP.value
            )
            if field_type_is_radio_group:
                valid_radio_group_options = json.loads(
                    field_details_dto.field_values)
                self._validate_for_invalid_radio_group_value(
                    field_value, field_id, valid_radio_group_options
                )
            field_type_is_check_box_group = (
                    field_type == FieldTypes.CHECKBOX_GROUP.value
            )
            if field_type_is_check_box_group:
                valid_check_box_options = json.loads(
                    field_details_dto.field_values)
                self._validate_for_invalid_checkbox_values(
                    field_value, field_id, valid_check_box_options
                )
            field_type_is_multi_select_field = (
                    field_type == FieldTypes.MULTI_SELECT_FIELD.value
            )
            if field_type_is_multi_select_field:
                valid_multi_select_options = json.loads(
                    field_details_dto.field_values)
                self._validate_for_invalid_multi_select_options(
                    field_value, field_id, valid_multi_select_options
                )
            field_type_is_multi_select_labels = (
                    field_type == FieldTypes.MULTI_SELECT_LABELS.value
            )
            if field_type_is_multi_select_labels:
                valid_multi_select_labels = json.loads(
                    field_details_dto.field_values)
                self._validate_for_invalid_multi_select_labels(
                    field_value, field_id, valid_multi_select_labels
                )
            field_type_is_date = field_type == FieldTypes.DATE.value
            if field_type_is_date:
                self._validate_for_date_field_value(
                    field_value, field_id
                )
            field_type_is_time = field_type == FieldTypes.TIME.value
            if field_type_is_time:
                self._validate_for_time_field_value(
                    field_value, field_id
                )
            field_type_is_image_uploader = (
                    field_type == FieldTypes.IMAGE_UPLOADER.value
            )
            if field_type_is_image_uploader:
                allowed_formats = json.loads(field_details_dto.allowed_formats)
                self._validate_for_image_uploader_value(
                    field_value, field_id, allowed_formats
                )
            field_type_is_file_uploader = (
                    field_type == FieldTypes.FILE_UPLOADER.value
            )
            if field_type_is_file_uploader:
                allowed_formats = json.loads(field_details_dto.allowed_formats)
                self._validate_for_file_uploader_value(
                    field_value, field_id, allowed_formats
                )

    @staticmethod
    def _validate_for_file_uploader_value(
            field_value: str, field_id: str, allowed_formats: List[str]
    ) -> Union[None, InvalidUrlForFile, InvalidFileFormat]:
        from ib_tasks.constants.config import VALID_URL_REGEX_PATTERN
        invalid_url_path = not VALID_URL_REGEX_PATTERN.search(field_value)
        try:
            file = field_value[field_value.rindex("/") + 1:]
        except ValueError:
            raise InvalidUrlForFile(field_id, field_value)
        file_is_empty = not file
        if invalid_url_path or file_is_empty:
            raise InvalidUrlForFile(field_id, field_value)
        given_file_format = '.' + file.split('.')[-1]
        invalid_file_format = given_file_format not in allowed_formats
        if invalid_file_format:
            raise InvalidFileFormat(
                field_id, given_file_format, allowed_formats
            )
        return

    @staticmethod
    def _validate_for_image_uploader_value(
            field_value: str, field_id: str, allowed_formats: List[str]
    ) -> Union[
        None, InvalidUrlForImage, NotAnImageUrl, InvalidImageFormat,
        CouldNotReadImage
    ]:
        from ib_tasks.constants.config import VALID_URL_REGEX_PATTERN
        invalid_url_path = not VALID_URL_REGEX_PATTERN.search(field_value)
        try:
            image_file = field_value[field_value.rindex("/") + 1:]
        except ValueError:
            raise InvalidUrlForImage(field_id, field_value)
        image_file_is_empty = not image_file
        if invalid_url_path or image_file_is_empty:
            raise InvalidUrlForImage(field_id, field_value)
        given_image_format = '.' + image_file.split('.')[-1]
        given_image_format_not_in_allowed_formats = \
            given_image_format not in allowed_formats
        if given_image_format_not_in_allowed_formats:
            raise InvalidImageFormat(
                field_id, given_image_format, allowed_formats
            )
        return

    @staticmethod
    def _validate_for_time_field_value(
            field_value: str, field_id: str
    ) -> Optional[InvalidTimeFormat]:
        import datetime
        from ib_tasks.constants.config import TIME_FORMAT
        try:
            datetime.datetime.strptime(field_value, TIME_FORMAT).time()
        except ValueError:
            raise InvalidTimeFormat(
                field_id, field_value, TIME_FORMAT
            )
        return

    @staticmethod
    def _validate_for_date_field_value(
            field_value: str, field_id: str
    ) -> Optional[InvalidDateFormat]:
        import datetime
        from ib_tasks.constants.config import DATE_FORMAT
        try:
            datetime.datetime.strptime(field_value, DATE_FORMAT).date()
        except ValueError:
            raise InvalidDateFormat(
                field_id, field_value, DATE_FORMAT
            )
        return

    @staticmethod
    def _validate_for_invalid_multi_select_labels(
            field_value: str, field_id: str,
            valid_multi_select_labels: List[str]
    ) -> Optional[IncorrectMultiSelectLabelsSelected]:
        selected_multi_select_labels = json.loads(field_value)
        invalid_multi_select_labels = list(
            set(selected_multi_select_labels) - set(
                valid_multi_select_labels)
        )
        if invalid_multi_select_labels:
            raise IncorrectMultiSelectLabelsSelected(
                field_id, invalid_multi_select_labels,
                valid_multi_select_labels
            )
        return

    @staticmethod
    def _validate_for_invalid_multi_select_options(
            field_value: str, field_id: str,
            valid_multi_select_options: List[str]
    ) -> Optional[IncorrectMultiSelectOptionsSelected]:
        selected_multi_select_options = json.loads(field_value)
        invalid_multi_select_options = list(
            set(selected_multi_select_options) - set(
                valid_multi_select_options)
        )
        if invalid_multi_select_options:
            raise IncorrectMultiSelectOptionsSelected(
                field_id, invalid_multi_select_options,
                valid_multi_select_options
            )
        return

    @staticmethod
    def _validate_for_invalid_checkbox_values(
            field_value: str, field_id: str, valid_check_box_options: List[str]
    ) -> Optional[IncorrectCheckBoxOptionsSelected]:
        selected_check_box_options = json.loads(field_value)
        invalid_checkbox_options = list(
            set(selected_check_box_options) - set(valid_check_box_options)
        )
        if invalid_checkbox_options:
            raise IncorrectCheckBoxOptionsSelected(
                field_id, invalid_checkbox_options, valid_check_box_options
            )
        return

    @staticmethod
    def _validate_for_invalid_radio_group_value(
            field_value: str, field_id: str,
            valid_radio_group_options: List[str]
    ) -> Optional[IncorrectRadioGroupChoice]:
        invalid_radio_group_choice = \
            field_value not in valid_radio_group_options
        if invalid_radio_group_choice:
            raise IncorrectRadioGroupChoice(
                field_id, field_value, valid_radio_group_options
            )
        return

    @staticmethod
    def _validate_gof_selector_value(
            field_value: str, field_id: str,
            valid_gof_selector_names: List[str]
    ) -> Optional[IncorrectNameInGoFSelectorField]:
        invalid_gof_option = field_value not in valid_gof_selector_names
        if invalid_gof_option:
            raise IncorrectNameInGoFSelectorField(
                field_id, field_value, valid_gof_selector_names
            )
        return

    @staticmethod
    def _validate_for_dropdown_field_value(
            field_value: str, field_id: str, valid_dropdown_values: List[str]
    ) -> Optional[InvalidValueForDropdownField]:
        invalid_dropdown_value = field_value not in valid_dropdown_values
        if invalid_dropdown_value:
            raise InvalidValueForDropdownField(
                field_id, field_value, valid_dropdown_values
            )
        return

    @staticmethod
    def _validate_for_float_value(
            field_value: str, field_id: str
    ) -> Optional[InvalidFloatValue]:
        invalid_float_value = not field_value.replace('.', '', 1).isdigit()
        if invalid_float_value:
            raise InvalidFloatValue(field_id, field_value)
        return

    @staticmethod
    def _validate_for_number_value(
            field_value: str, field_id: str
    ) -> Optional[InvalidNumberValue]:
        invalid_number_value = not field_value.isdigit()
        if invalid_number_value:
            raise InvalidNumberValue(field_id, field_value)
        return

    @staticmethod
    def _validate_for_strong_password(
            field_value: str, field_id: str
    ) -> Optional[NotAStrongPassword]:
        import re
        from ib_tasks.constants.config import STRONG_PASSWORD_REGEX
        password_is_not_strong_enough = not re.search(
            STRONG_PASSWORD_REGEX, field_value
        )
        if password_is_not_strong_enough:
            raise NotAStrongPassword(field_id, field_value)
        return

    @staticmethod
    def _validate_for_url_field_value(
            field_value: str, field_id: str
    ) -> Optional[InvalidURLValue]:
        from ib_tasks.constants.config import VALID_URL_REGEX_PATTERN
        url_is_invalid = not VALID_URL_REGEX_PATTERN.search(field_value)
        if url_is_invalid:
            raise InvalidURLValue(field_id, field_value)
        return

    @staticmethod
    def _validate_for_email_field_value(
            field_value: str, field_id: str
    ) -> Optional[InvalidEmailFieldValue]:
        import re
        from ib_tasks.constants.config import VALID_EMAIL_REGEX
        email_address_is_invalid = not re.search(VALID_EMAIL_REGEX,
                                                 field_value)
        if email_address_is_invalid:
            raise InvalidEmailFieldValue(field_id, field_value)
        return

    @staticmethod
    def _validate_phone_number_value(
            field_value: str, field_id: str
    ) -> Optional[InvalidPhoneNumberValue]:
        phone_number_has_non_digit_chars = not field_value.isdigit()
        if phone_number_has_non_digit_chars:
            raise InvalidPhoneNumberValue(field_id, field_value)
        phone_number_does_not_contain_10_digits = len(field_value) != 10
        if phone_number_does_not_contain_10_digits:
            raise InvalidPhoneNumberValue(field_id, field_value)
        return

    def _validate_task_template_id(
            self, task_template_id: str
    ) -> Optional[InvalidTaskTemplateIds]:
        task_template_existence = \
            self.task_storage.check_is_template_exists(
                template_id=task_template_id)
        if not task_template_existence:
            raise InvalidTaskTemplateIds(
                invalid_task_template_ids=[task_template_id]
            )
        return

    def _validate_for_invalid_gof_ids(
            self, gof_ids: List[str]
    ) -> Optional[InvalidGoFIds]:
        valid_gof_ids = self.task_storage.get_existing_gof_ids(gof_ids)
        invalid_gof_ids = list(set(gof_ids) - set(valid_gof_ids))
        if invalid_gof_ids:
            raise InvalidGoFIds(gof_ids)
        return

    def _validate_for_invalid_field_ids(
            self, field_ids: List[str]
    ) -> Optional[InvalidFieldIds]:
        valid_field_ids = self.task_storage.get_existing_field_ids(field_ids)
        invalid_field_ids = list(set(field_ids) - set(valid_field_ids))
        if invalid_field_ids:
            raise InvalidFieldIds(invalid_field_ids)
        return

    @staticmethod
    def _get_field_values_dtos(
            gof_fields_dtos: List[GoFFieldsDTO]
    ) -> List[FieldValuesDTO]:
        field_values_dtos = []
        for gof_fields_dto in gof_fields_dtos:
            field_values_dtos += [
                field_value_dto
                for field_value_dto in gof_fields_dto.field_values_dtos
            ]
        return field_values_dtos

    @staticmethod
    def _get_duplicates_in_given_list(values: List):
        duplicate_values = list(
            set(
                [
                    value
                    for value in values if values.count(value) > 1
                ]
            )
        )
        return duplicate_values

    @staticmethod
    def _get_field_value_for_given_field_id(
            field_id: str, field_values_dtos: List[FieldValuesDTO]
    ) -> Union[None, str, List[str]]:
        for field_values_dto in field_values_dtos:
            field_id_matched = field_values_dto.field_id == field_id
            if field_id_matched:
                return field_values_dto.field_response
        return

    @staticmethod
    def _get_field_type_for_given_field_id(
            field_id: str, field_details_dtos: List[FieldCompleteDetailsDTO]
    ) -> Union[None, FieldTypes]:
        for field_details_dto in field_details_dtos:
            field_id_matched = field_details_dto.field_id == field_id
            if field_id_matched:
                return field_details_dto.field_type
        return
