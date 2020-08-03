import json
from typing import Optional, List, Union

from ib_tasks.constants.enum import FieldTypes
from ib_tasks.exceptions.field_values_custom_exceptions import \
    InvalidPhoneNumberValue, InvalidEmailFieldValue, InvalidURLValue, \
    NotAStrongPassword, \
    InvalidNumberValue, InvalidFloatValue, \
    InvalidValueForDropdownField, IncorrectNameInGoFSelectorField, \
    IncorrectRadioGroupChoice, \
    IncorrectCheckBoxOptionsSelected, IncorrectMultiSelectOptionsSelected, \
    IncorrectMultiSelectLabelsSelected, InvalidDateFormat, InvalidTimeFormat, \
    InvalidUrlForImage, InvalidImageFormat, NotAnImageUrl, CouldNotReadImage, \
    InvalidUrlForFile, EmptyValueForRequiredField, InvalidFileFormat
from ib_tasks.exceptions.fields_custom_exceptions import \
    DuplicationOfFieldIdsExist, InvalidFieldIds
from ib_tasks.exceptions.gofs_custom_exceptions import InvalidGoFIds
from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskTemplateIds, \
    InvalidTaskException
from ib_tasks.interactors.presenter_interfaces. \
    create_or_update_task_presenter import CreateOrUpdateTaskPresenterInterface
from ib_tasks.interactors.presenter_interfaces.presenter_interface import \
    PresenterInterface
from ib_tasks.interactors.storage_interfaces. \
    create_or_update_task_storage_interface import \
    CreateOrUpdateTaskStorageInterface
from ib_tasks.interactors.storage_interfaces.fields_dtos import \
    FieldCompleteDetailsDTO
from ib_tasks.interactors.storage_interfaces.fields_storage_interface import \
    FieldsStorageInterface
from ib_tasks.interactors.storage_interfaces.get_task_dtos import \
    TaskGoFFieldDTO
from ib_tasks.interactors.storage_interfaces.stages_storage_interface import \
    StageStorageInterface
from ib_tasks.interactors.storage_interfaces.storage_interface import \
    StorageInterface
from ib_tasks.interactors.storage_interfaces.task_dtos import \
    TaskGoFWithTaskIdDTO, \
    TaskGoFDetailsDTO
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface
from ib_tasks.interactors.task_dtos import TaskDTO, FieldValuesDTO, \
    GoFFieldsDTO
from ib_tasks.interactors.user_action_on_task_interactor import \
    UserActionOnTaskInteractor


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
        act_on_task_interactor.user_action_on_task(act_on_task_presenter)

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
        return (
            task_gof_field_dtos_for_updation, task_gof_field_dtos_for_creation
        )

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
    def _get_field_type_for_given_field_id(
            field_id: str, field_details_dtos: List[FieldCompleteDetailsDTO]
    ) -> Union[None, FieldTypes]:
        for field_details_dto in field_details_dtos:
            field_id_matched = field_details_dto.field_id == field_id
            if field_id_matched:
                return field_details_dto.field_type
        return
