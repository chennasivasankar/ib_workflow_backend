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
from ib_tasks.exceptions.gofs_custom_exceptions import \
    DuplicateSameGoFOrderForAGoF, InvalidGoFIds
from ib_tasks.exceptions.permission_custom_exceptions import \
    UserNeedsGoFWritablePermission, UserNeedsFieldWritablePermission
from ib_tasks.exceptions.stage_custom_exceptions import InvalidStageId, \
    TransitionTemplateIsNotRelatedToGivenStageAction
from ib_tasks.exceptions.task_custom_exceptions import \
    InvalidTaskIdException, \
    InvalidTransitionChecklistTemplateId, InvalidGoFsOfTaskTemplate, \
    InvalidFieldsOfGoF, InvalidTaskDisplayId
from ib_tasks.interactors.create_or_update_task \
    .template_gofs_fields_base_validations import \
    TemplateGoFsFieldsBaseValidationsInteractor
from ib_tasks.interactors.mixins.get_task_id_for_task_display_id_mixin import \
    GetTaskIdForTaskDisplayIdMixin
from ib_tasks.interactors.presenter_interfaces \
    .create_transition_checklist_presenter_interface import \
    CreateTransitionChecklistTemplatePresenterInterface
from ib_tasks.interactors.storage_interfaces.action_storage_interface import \
    ActionStorageInterface
from ib_tasks.interactors.storage_interfaces \
    .create_or_update_task_storage_interface import \
    CreateOrUpdateTaskStorageInterface
from ib_tasks.interactors.storage_interfaces.fields_storage_interface import \
    FieldsStorageInterface
from ib_tasks.interactors.storage_interfaces.get_task_dtos import \
    TaskGoFFieldDTO
from ib_tasks.interactors.storage_interfaces.gof_storage_interface import \
    GoFStorageInterface
from ib_tasks.interactors.storage_interfaces.storage_interface import \
    StorageInterface
from ib_tasks.interactors.storage_interfaces.task_dtos import \
    TaskGoFWithTaskIdDTO, TaskGoFDetailsDTO
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface
from ib_tasks.interactors.storage_interfaces.task_template_storage_interface \
    import \
    TaskTemplateStorageInterface
from ib_tasks.interactors.task_dtos import GoFFieldsDTO
from ib_tasks.interactors.task_template_dtos import \
    CreateTransitionChecklistTemplateDTO, \
    CreateTransitionChecklistTemplateWithTaskDisplayIdDTO


class CreateTransitionChecklistTemplateInteractor(
    GetTaskIdForTaskDisplayIdMixin
):

    def __init__(self,
                 create_or_update_task_storage:
                 CreateOrUpdateTaskStorageInterface,
                 template_storage: TaskTemplateStorageInterface,
                 stage_action_storage: ActionStorageInterface,
                 task_storage: TaskStorageInterface,
                 gof_storage: GoFStorageInterface, storage: StorageInterface,
                 field_storage: FieldsStorageInterface
                 ):
        self.field_storage = field_storage
        self.storage = storage
        self.gof_storage = gof_storage
        self.task_storage = task_storage
        self.stage_action_storage = stage_action_storage
        self.template_storage = template_storage
        self.create_or_update_task_storage = create_or_update_task_storage

    def create_transition_checklist_wrapper(
            self,
            transition_template_dto:
            CreateTransitionChecklistTemplateWithTaskDisplayIdDTO,
            presenter: CreateTransitionChecklistTemplatePresenterInterface
    ):
        try:
            return self._prepare_create_transition_checklist_response(
                transition_template_dto, presenter
            )
        except InvalidTaskDisplayId as err:
            return presenter.raise_invalid_task_display_id(err)
        except InvalidTaskIdException as err:
            return presenter.raise_invalid_task_id(err)
        except InvalidTransitionChecklistTemplateId as err:
            return presenter.raise_invalid_transition_checklist_template_id(
                err)
        except InvalidActionException as err:
            return presenter.raise_invalid_action(err)
        except InvalidStageId as err:
            return presenter.raise_invalid_stage_id(err)
        except TransitionTemplateIsNotRelatedToGivenStageAction as err:
            return \
                presenter.raise_transition_template_is_not_related_to_given_stage_action(
                    err)
        except DuplicateSameGoFOrderForAGoF as err:
            return presenter.raise_same_gof_order_for_a_gof(err)
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

    def _prepare_create_transition_checklist_response(
            self,
            transition_template_dto:
            CreateTransitionChecklistTemplateWithTaskDisplayIdDTO,
            presenter: CreateTransitionChecklistTemplatePresenterInterface
    ):
        task_id = self.get_task_id_for_task_display_id(
            transition_template_dto.task_display_id)
        transition_template_dto = CreateTransitionChecklistTemplateDTO(
            task_id=task_id,
            created_by_id=transition_template_dto.created_by_id,
            transition_checklist_template_id=transition_template_dto
                .transition_checklist_template_id,
            action_id=transition_template_dto.action_id,
            stage_id=transition_template_dto.stage_id,
            transition_checklist_gofs=transition_template_dto
                .transition_checklist_gofs
        )
        self.create_transition_checklist(transition_template_dto)
        response = presenter.get_create_transition_checklist_response()
        return response

    def create_transition_checklist(
            self,
            transition_template_dto: CreateTransitionChecklistTemplateDTO):
        self._validate_task_id(transition_template_dto.task_id)
        self._validate_transition_template_id(
            transition_template_dto.transition_checklist_template_id)
        self._validate_action_id(transition_template_dto.action_id)
        self._validate_stage_id(transition_template_dto.stage_id)
        self._validate_transition_template_id_related_to_given_stage_action(
            transition_template_dto.transition_checklist_template_id,
            transition_template_dto.action_id, transition_template_dto.stage_id
        )
        self._validate_same_gof_order(
            transition_template_dto.transition_checklist_gofs)
        template_gofs_fields_validation_interactor = \
            TemplateGoFsFieldsBaseValidationsInteractor(
                task_storage=self.task_storage, gof_storage=self.gof_storage,
                create_task_storage=self.create_or_update_task_storage,
                storage=self.storage, field_storage=self.field_storage
            )
        action_type = \
            self.stage_action_storage.get_action_type_for_given_action_id(
                action_id=transition_template_dto.action_id
            )
        template_gofs_fields_validation_interactor \
            .perform_base_validations_for_template_gofs_and_fields(
            transition_template_dto.transition_checklist_gofs,
            transition_template_dto.created_by_id,
            transition_template_dto.transition_checklist_template_id,
            action_type
        )
        task_gof_dtos = [
            TaskGoFWithTaskIdDTO(
                task_id=transition_template_dto.task_id,
                gof_id=gof_fields_dto.gof_id,
                same_gof_order=gof_fields_dto.same_gof_order
            )
            for gof_fields_dto in
            transition_template_dto.transition_checklist_gofs
        ]
        task_gof_details_dtos = \
            self.create_or_update_task_storage.create_task_gofs(
                task_gof_dtos=task_gof_dtos
            )
        task_gof_field_dtos = self._prepare_task_gof_fields_dtos(
            transition_template_dto.transition_checklist_gofs,
            task_gof_details_dtos
        )
        self.create_or_update_task_storage.create_task_gof_fields(
            task_gof_field_dtos)

    def _validate_task_id(self, task_id) -> Optional[InvalidTaskIdException]:
        is_valid_task_id = self.create_or_update_task_storage.is_valid_task_id(
            task_id)
        invalid_task_id = not is_valid_task_id
        if invalid_task_id:
            raise InvalidTaskIdException(task_id)
        return

    def _validate_transition_template_id(
            self, transition_checklist_template_id: str
    ) -> Optional[InvalidTransitionChecklistTemplateId]:
        self.template_storage.validate_transition_template_id(
            transition_checklist_template_id)
        return

    def _validate_action_id(
            self, action_id) -> Optional[InvalidActionException]:
        self.stage_action_storage.validate_action_id(action_id)
        return

    def _validate_stage_id(self, stage_id: int) -> Optional[InvalidStageId]:
        self.stage_action_storage.validate_stage_id(stage_id)
        return

    def _validate_transition_template_id_related_to_given_stage_action(
            self, transition_checklist_template_id, action_id, stage_id
    ) -> Optional[TransitionTemplateIsNotRelatedToGivenStageAction]:
        self.stage_action_storage \
            .validate_transition_template_id_is_related_to_given_stage_action(
            transition_checklist_template_id, action_id, stage_id
        )
        return

    def _validate_same_gof_order(
            self, transition_checklist_gof_dtos: List[GoFFieldsDTO]
    ) -> Optional[DuplicateSameGoFOrderForAGoF]:
        from collections import defaultdict
        gof_with_order_dict = defaultdict(list)
        for transition_checklist_gof_dto in transition_checklist_gof_dtos:
            gof_with_order_dict[
                transition_checklist_gof_dto.gof_id].append(
                transition_checklist_gof_dto.same_gof_order)
        for gof_id, same_gof_orders in gof_with_order_dict.items():
            duplicate_same_gof_orders = self._get_duplicates_in_given_list(
                same_gof_orders)
            if duplicate_same_gof_orders:
                raise DuplicateSameGoFOrderForAGoF(gof_id,
                                                   duplicate_same_gof_orders)
        return

    @staticmethod
    def _get_duplicates_in_given_list(values: List) -> List:
        duplicate_values = list(
            set(
                [
                    value
                    for value in values if values.count(value) > 1
                ]
            )
        )
        return duplicate_values

    def _prepare_task_gof_fields_dtos(
            self, transition_checklist_gofs, task_gof_details_dtos
    ) -> List[TaskGoFFieldDTO]:
        task_gof_field_dtos = []
        for checklist_gof_dto in transition_checklist_gofs:
            task_gof_id = self._get_gof_id_for_field_in_task_gof_details(
                checklist_gof_dto.gof_id, checklist_gof_dto.same_gof_order,
                task_gof_details_dtos
            )
            task_gof_field_dtos += [
                TaskGoFFieldDTO(
                    field_id=field_values_dto.field_id,
                    field_response=field_values_dto.field_response,
                    task_gof_id=task_gof_id
                )
                for field_values_dto in checklist_gof_dto.field_values_dtos
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
