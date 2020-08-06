from typing import Optional, List

from ib_tasks.exceptions.action_custom_exceptions import InvalidActionException
from ib_tasks.exceptions.field_values_custom_exceptions import \
    EmptyValueForRequiredField, InvalidPhoneNumberValue, \
    InvalidEmailFieldValue, InvalidURLValue, NotAStrongPassword, \
    InvalidNumberValue, InvalidFloatValue, InvalidValueForDropdownField, \
    IncorrectNameInGoFSelectorField, IncorrectRadioGroupChoice, \
    IncorrectCheckBoxOptionsSelected, IncorrectMultiSelectOptionsSelected, \
    IncorrectMultiSelectLabelsSelected, InvalidDateFormat, InvalidTimeFormat, \
    InvalidUrlForImage, InvalidImageFormat, InvalidUrlForFile, \
    InvalidFileFormat
from ib_tasks.exceptions.fields_custom_exceptions import InvalidFieldIds, \
    DuplicateFieldIdsToGoF
from ib_tasks.exceptions.gofs_custom_exceptions import InvalidGoFIds
from ib_tasks.exceptions.permission_custom_exceptions import \
    UserNeedsGoFWritablePermission, UserNeedsFieldWritablePermission, \
    UserActionPermissionDenied, UserBoardPermissionDenied
from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskException, \
    InvalidGoFsOfTaskTemplate, InvalidFieldsOfGoF
from ib_tasks.interactors.create_or_update_task. \
    create_or_update_task_base_validations import \
    CreateOrUpdateTaskBaseValidationsInteractor
from ib_tasks.interactors.field_dtos import FieldIdWithTaskGoFIdDTO
from ib_tasks.interactors.gofs_dtos import GoFIdWithSameGoFOrder
from ib_tasks.interactors.presenter_interfaces.update_task_presenter import \
    UpdateTaskPresenterInterface
from ib_tasks.interactors.storage_interfaces. \
    create_or_update_task_storage_interface import \
    CreateOrUpdateTaskStorageInterface
from ib_tasks.interactors.storage_interfaces.fields_storage_interface import \
    FieldsStorageInterface
from ib_tasks.interactors.storage_interfaces.get_task_dtos import \
    TaskGoFFieldDTO
from ib_tasks.interactors.storage_interfaces.gof_storage_interface import \
    GoFStorageInterface
from ib_tasks.interactors.storage_interfaces.stages_storage_interface import \
    StageStorageInterface
from ib_tasks.interactors.storage_interfaces.storage_interface import \
    StorageInterface
from ib_tasks.interactors.storage_interfaces.task_dtos import \
    TaskGoFWithTaskIdDTO, TaskGoFDetailsDTO
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface
from ib_tasks.interactors.task_dtos import UpdateTaskDTO
from ib_tasks.interactors.user_action_on_task_interactor import \
    UserActionOnTaskInteractor


class UpdateTaskInteractor:

    def __init__(
            self, task_storage: TaskStorageInterface,
            gof_storage: GoFStorageInterface,
            create_task_storage: CreateOrUpdateTaskStorageInterface,
            storage: StorageInterface, field_storage: FieldsStorageInterface,
            stage_storage: StageStorageInterface
    ):
        self.gof_storage = gof_storage
        self.task_storage = task_storage
        self.create_task_storage = create_task_storage
        self.storage = storage
        self.field_storage = field_storage
        self.stage_storage = stage_storage

    def update_task_wrapper(
            self, presenter: UpdateTaskPresenterInterface,
            task_dto: UpdateTaskDTO
    ):
        try:
            return self._prepare_update_task_response(
                task_dto, presenter)
        except InvalidTaskException as err:
            return presenter.raise_invalid_task_id(err)
        except InvalidActionException as err:
            return presenter.raise_invalid_action_id(err)
        except InvalidGoFIds as err:
            return presenter.raise_invalid_gof_ids(err)
        except InvalidFieldIds as err:
            return presenter.raise_invalid_field_ids(err)
        except InvalidGoFsOfTaskTemplate as err:
            return presenter.raise_invalid_gofs_given_to_a_task_template(err)
        except DuplicateFieldIdsToGoF as err:
            return presenter.raise_duplicate_field_ids_to_a_gof(err)
        except InvalidFieldsOfGoF as err:
            return presenter.raise_invalid_fields_given_to_a_gof(err)
        except UserNeedsGoFWritablePermission as err:
            return presenter.raise_user_needs_gof_writable_permission(err)
        except UserNeedsFieldWritablePermission as err:
            return presenter.raise_user_needs_field_writable_permission(err)
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
        except IncorrectNameInGoFSelectorField as err:
            return presenter. \
                raise_exception_for_invalid_name_in_gof_selector_field_value(
                err)
        except IncorrectRadioGroupChoice as err:
            return presenter. \
                raise_exception_for_invalid_choice_in_radio_group_field(err)
        except IncorrectCheckBoxOptionsSelected as err:
            return presenter. \
                raise_exception_for_invalid_checkbox_group_options_selected(
                err)
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
                err)
        except UserActionPermissionDenied as err:
            return presenter.raise_exception_for_user_action_permission_denied(
                error_obj=err
            )
        except UserBoardPermissionDenied as err:
            return presenter.raise_exception_for_user_board_permission_denied(
                error_obj=err
            )

    def _prepare_update_task_response(
            self, task_dto: UpdateTaskDTO,
            presenter: UpdateTaskPresenterInterface
    ):
        self.update_task(task_dto)
        return presenter.get_update_task_response()

    def update_task(self, task_dto: UpdateTaskDTO):
        task_id = task_dto.task_id
        self._validate_task_id(task_id)
        task_template_id = \
            self.create_task_storage.get_template_id_for_given_task(task_id)
        base_validations_interactor = \
            CreateOrUpdateTaskBaseValidationsInteractor(
                self.task_storage, self.gof_storage,
                self.create_task_storage, self.storage,
                self.field_storage
            )
        base_validations_interactor. \
            perform_base_validations_for_create_or_update_task(
                task_dto, task_template_id)
        existing_gofs = \
            self.create_task_storage \
                .get_gof_ids_with_same_gof_order_related_to_a_task(task_id)
        existing_fields = \
            self.create_task_storage \
                .get_field_ids_with_task_gof_id_related_to_given_task(
                    task_id)
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
            gof_already_exists = \
                self._is_gof_already_exists(
                    task_gof_dto.gof_id, task_gof_dto.same_gof_order,
                    existing_gofs
                )
            if gof_already_exists:
                task_gof_dtos_for_updation.append(task_gof_dto)
            else:
                task_gof_dtos_for_creation.append(task_gof_dto)
        if task_gof_dtos_for_updation:
            self._update_task_gofs(
                task_gof_dtos_for_updation, task_dto, existing_fields)
        if task_gof_dtos_for_creation:
            self._create_task_gofs(task_gof_dtos_for_creation, task_dto)

        act_on_task_interactor = UserActionOnTaskInteractor(
            user_id=task_dto.created_by_id, board_id=None,
            task_id=task_id,
            action_id=task_dto.action_id,
            storage=self.storage, gof_storage=self.create_task_storage,
            field_storage=self.field_storage, stage_storage=self.stage_storage
        )
        act_on_task_interactor.user_action_on_task()

    def _validate_task_id(
            self, task_id: int) -> Optional[InvalidTaskException]:
        invalid_task_id = \
            not self.create_task_storage.is_valid_task_id(task_id)
        if invalid_task_id:
            raise InvalidTaskException(task_id)
        return

    def _prepare_task_gof_fields_dtos(
            self, task_dto: UpdateTaskDTO,
            task_gof_details_dtos: List[TaskGoFDetailsDTO]
    ) -> List[TaskGoFFieldDTO]:
        task_gof_field_dtos = []
        for gof_fields_dto in task_dto.gof_fields_dtos:
            task_gof_id = self._get_task_gof_id_for_field_in_task_gof_details(
                gof_fields_dto.gof_id, gof_fields_dto.same_gof_order,
                task_gof_details_dtos)
            if task_gof_id is not None:
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
    def _get_task_gof_id_for_field_in_task_gof_details(
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

    def _filter_task_gof_field_dtos(
            self, task_gof_field_dtos: List[TaskGoFFieldDTO],
            existing_fields: List[FieldIdWithTaskGoFIdDTO]
    ) -> (List[TaskGoFFieldDTO], List[TaskGoFFieldDTO]):
        task_gof_field_dtos_for_updation, task_gof_field_dtos_for_creation = \
            [], []
        for task_gof_field_dto in task_gof_field_dtos:
            field_id_already_exists = self._is_field_already_exists(
                task_gof_field_dto.field_id, task_gof_field_dto.task_gof_id,
                existing_fields
            )
            if field_id_already_exists:
                task_gof_field_dtos_for_updation.append(task_gof_field_dto)
            else:
                task_gof_field_dtos_for_creation.append(task_gof_field_dto)
        return (
            task_gof_field_dtos_for_updation, task_gof_field_dtos_for_creation
        )

    def _update_task_gofs(
            self, task_gof_dtos_for_updation: List[TaskGoFWithTaskIdDTO],
            task_dto: UpdateTaskDTO,
            existing_fields: List[FieldIdWithTaskGoFIdDTO]
    ):
        task_gof_details_dtos = \
            self.create_task_storage.update_task_gofs(
                task_gof_dtos_for_updation
            )
        task_gof_field_dtos = self._prepare_task_gof_fields_dtos(
            task_dto, task_gof_details_dtos)
        task_gof_field_dtos_for_updation, task_gof_field_dtos_for_creation = \
            self._filter_task_gof_field_dtos(
                task_gof_field_dtos, existing_fields)
        if task_gof_field_dtos_for_updation:
            self.create_task_storage.update_task_gof_fields(
                task_gof_field_dtos_for_updation
            )

        if task_gof_field_dtos_for_creation:
            self.create_task_storage.create_task_gof_fields(
                task_gof_field_dtos_for_creation
            )

    def _create_task_gofs(
            self, task_gof_dtos_for_creation: List[TaskGoFWithTaskIdDTO],
            task_dto: UpdateTaskDTO
    ):
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
    def _is_field_already_exists(
            field_id: str, task_gof_id: int,
            existing_fields: List[FieldIdWithTaskGoFIdDTO]
    ) -> bool:
        for existing_field in existing_fields:
            field_already_exists = (
                    field_id == existing_field.field_id and
                    task_gof_id == existing_field.task_gof_id)
            if field_already_exists:
                return True
        return False

    @staticmethod
    def _is_gof_already_exists(
            gof_id: str, same_gof_order: int,
            existing_gofs_with_same_gof_order: List[GoFIdWithSameGoFOrder]
    ) -> bool:
        for existing_gof in existing_gofs_with_same_gof_order:
            gof_already_exists = (
                    gof_id == existing_gof.gof_id and
                    same_gof_order == existing_gof.same_gof_order)
            if gof_already_exists:
                return True
        return False
