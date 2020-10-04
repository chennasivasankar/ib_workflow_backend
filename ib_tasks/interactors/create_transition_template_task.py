from typing import Optional, List

from ib_tasks.constants.enum import ActionTypes
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
    DuplicateFieldIdsToGoF, UserDidNotFillRequiredFields, \
    FieldsFilledAlreadyBySomeone
from ib_tasks.exceptions.gofs_custom_exceptions import \
    DuplicateSameGoFOrderForAGoF, InvalidGoFIds, UserDidNotFillRequiredGoFs
from ib_tasks.exceptions.permission_custom_exceptions import \
    UserNeedsGoFWritablePermission, UserNeedsFieldWritablePermission
from ib_tasks.exceptions.stage_custom_exceptions import InvalidStageId, \
    TransitionTemplateIsNotRelatedToGivenStageAction
from ib_tasks.exceptions.task_custom_exceptions import \
    InvalidTaskIdException, \
    InvalidTransitionChecklistTemplateId, InvalidGoFsOfTaskTemplate, \
    InvalidFieldsOfGoF, InvalidTaskDisplayId
from ib_tasks.interactors.create_or_update_task \
    .gofs_details_validations_interactor import \
    GoFsDetailsValidationsInteractor
from ib_tasks.interactors.create_or_update_task.task_crud_operations_interactor import \
    TaskCrudOperationsInteractor
from ib_tasks.interactors.mixins.get_task_id_for_task_display_id_mixin import \
    GetTaskIdForTaskDisplayIdMixin
from ib_tasks.interactors.mixins.task_operations_utilities_mixin import \
    TaskOperationsUtilitiesMixin
from ib_tasks.interactors.presenter_interfaces \
    .create_transition_checklist_presenter_interface import \
    CreateOrUpdateTransitionChecklistPresenterInterface
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
    TaskGoFDetailsDTO, TaskGoFWithTaskIdDTO
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface
from ib_tasks.interactors.storage_interfaces.task_template_storage_interface \
    import TaskTemplateStorageInterface
from ib_tasks.interactors.task_dtos import GoFFieldsDTO
from ib_tasks.interactors.task_template_dtos import \
    CreateTransitionChecklistTemplateDTO, \
    CreateTransitionChecklistTemplateWithTaskDisplayIdDTO, \
    TransitionTaskCreationDTO


class CreateTransitionTemplateTaskInteractor(
    GetTaskIdForTaskDisplayIdMixin, TaskOperationsUtilitiesMixin
):

    def __init__(self,
                 create_or_update_task_storage:
                 CreateOrUpdateTaskStorageInterface,
                 template_storage: TaskTemplateStorageInterface,
                 stage_action_storage: ActionStorageInterface,
                 task_storage: TaskStorageInterface,
                 gof_storage: GoFStorageInterface, storage: StorageInterface,
                 field_storage: FieldsStorageInterface,
                 task_template_storage: TaskTemplateStorageInterface
                 ):
        self.field_storage = field_storage
        self.storage = storage
        self.gof_storage = gof_storage
        self.task_storage = task_storage
        self.stage_action_storage = stage_action_storage
        self.template_storage = template_storage
        self.create_task_storage = create_or_update_task_storage
        self.task_template_storage = task_template_storage

    def create_transition_template_task_wrapper(
            self,
            transition_template_dto:
            CreateTransitionChecklistTemplateWithTaskDisplayIdDTO,
            presenter: CreateOrUpdateTransitionChecklistPresenterInterface):
        try:
            return self._prepare_create_transition_template_task_response(
                transition_template_dto, presenter)
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
            return presenter.raise_transition_template_is_not_linked_to_action(
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
        except UserDidNotFillRequiredGoFs as err:
            return presenter.raise_user_did_not_fill_required_gofs(err)
        except UserDidNotFillRequiredFields as err:
            return presenter.raise_user_did_not_fill_required_fields(err)
        except FieldsFilledAlreadyBySomeone as err:
            return presenter.raise_fields_already_filled_by_someone(err)
        except EmptyValueForRequiredField as err:
            return presenter.raise_empty_value_in_required_field(err)
        except InvalidPhoneNumberValue as err:
            return presenter.raise_invalid_phone_number_value(err)
        except InvalidEmailFieldValue as err:
            return presenter.raise_invalid_email_address(err)
        except InvalidURLValue as err:
            return presenter.raise_invalid_url_address(err)
        except NotAStrongPassword as err:
            return presenter.raise_weak_password(err)
        except InvalidNumberValue as err:
            return presenter.raise_invalid_number_value(err)
        except InvalidFloatValue as err:
            return presenter.raise_invalid_float_value(err)
        except InvalidValueForDropdownField as err:
            return presenter.raise_invalid_dropdown_value(err)
        except IncorrectNameInGoFSelectorField as err:
            return presenter.raise_invalid_name_in_gof_selector(err)
        except IncorrectRadioGroupChoice as err:
            return presenter.raise_invalid_choice_in_radio_group_field(err)
        except IncorrectCheckBoxOptionsSelected as err:
            return presenter.raise_invalid_checkbox_group_options_selected(err)
        except IncorrectMultiSelectOptionsSelected as err:
            return presenter.raise_invalid_multi_select_options_selected(err)
        except IncorrectMultiSelectLabelsSelected as err:
            return presenter.raise_invalid_multi_select_labels_selected(err)
        except InvalidDateFormat as err:
            return presenter.raise_invalid_date_format(err)
        except InvalidTimeFormat as err:
            return presenter.raise_invalid_time_format(err)
        except InvalidUrlForImage as err:
            return presenter.raise_invalid_image_url(err)
        except InvalidImageFormat as err:
            return presenter.raise_not_acceptable_image_format(err)
        except InvalidUrlForFile as err:
            return presenter.raise_invalid_file_url(err)
        except InvalidFileFormat as err:
            return presenter.raise_not_acceptable_file_format(err)

    def _prepare_create_transition_template_task_response(
            self,
            transition_template_dto:
            CreateTransitionChecklistTemplateWithTaskDisplayIdDTO,
            presenter: CreateOrUpdateTransitionChecklistPresenterInterface):
        task_id = self.get_task_id_for_task_display_id(
            transition_template_dto.task_display_id)
        template_id = transition_template_dto.transition_checklist_template_id
        checklist_gofs = transition_template_dto.transition_checklist_gofs
        transition_template_dto = CreateTransitionChecklistTemplateDTO(
            task_id=task_id,
            created_by_id=transition_template_dto.created_by_id,
            transition_checklist_template_id=template_id,
            action_id=transition_template_dto.action_id,
            stage_id=transition_template_dto.stage_id,
            transition_checklist_gofs=checklist_gofs)
        self.create_transition_template_task(transition_template_dto)
        response = presenter.get_create_transition_checklist_response()
        return response

    def create_transition_template_task(
            self,
            transition_template_dto: CreateTransitionChecklistTemplateDTO):
        self._validate_transition_template_task_details(
            transition_template_dto)
        self._create_gofs_and_fields_of_transition_template(
            transition_template_dto)

    def _validate_transition_template_task_details(
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
        self._validate_for_duplicate_same_gof_order(
            transition_template_dto.transition_checklist_gofs)
        action_type = \
            self.stage_action_storage.get_action_type_for_given_action_id(
                action_id=transition_template_dto.action_id)
        stage_id = self.stage_action_storage.get_stage_id_for_action_id(
            transition_template_dto.action_id)
        project_id = self.task_storage.get_project_id_for_the_task_id(
            transition_template_dto.task_id)
        self._perform_gof_details_validation(
            transition_template_dto, action_type, project_id)
        action_type_is_not_no_validations = \
            action_type != ActionTypes.NO_VALIDATIONS.value
        if action_type_is_not_no_validations:
            self._validate_all_user_stage_permitted_fields_are_filled_or_not(
                transition_template_dto.created_by_id,
                transition_template_dto.task_id, project_id, stage_id,
                transition_template_dto.transition_checklist_template_id)

    def _create_gofs_and_fields_of_transition_template(
            self,
            transition_template_dto: CreateTransitionChecklistTemplateDTO):
        task_crud_interactor = TaskCrudOperationsInteractor(
            self.create_task_storage)
        task_id = transition_template_dto.task_id
        action_id = transition_template_dto.action_id
        template_id = transition_template_dto.transition_checklist_template_id
        created_by = transition_template_dto.created_by_id
        transition_task_creation_dto = TransitionTaskCreationDTO(
            template_id=template_id, created_by=created_by)
        created_transition_task_id = \
            self.task_storage.create_transition_task(
                transition_task_creation_dto)
        self.task_storage.create_transition_template_task_entry(
            task_id, action_id, created_transition_task_id)
        checklist_gofs = transition_template_dto.transition_checklist_gofs
        task_gofs = self._prepare_task_gof_dtos(
            checklist_gofs, created_transition_task_id)
        task_gof_details = task_crud_interactor.create_task_gofs(task_gofs)
        task_gof_fields = self._prepare_task_gof_fields(
            task_gof_details, checklist_gofs)
        task_crud_interactor.create_task_gof_fields(task_gof_fields)

    @staticmethod
    def _prepare_task_gof_dtos(
            checklist_gofs: List[GoFFieldsDTO],
            created_transition_task_id: int
    ) -> List[TaskGoFWithTaskIdDTO]:
        task_gofs = [
            TaskGoFWithTaskIdDTO(
                task_id=created_transition_task_id,
                gof_id=checklist_gof.gof_id,
                same_gof_order=checklist_gof.same_gof_order)
            for checklist_gof in checklist_gofs
        ]
        return task_gofs

    def _prepare_task_gof_fields(
            self, task_gof_details: List[TaskGoFDetailsDTO],
            checklist_gofs: List[GoFFieldsDTO]
    ) -> List[TaskGoFFieldDTO]:
        task_gof_fields = []
        for checklist_gof in checklist_gofs:
            task_gof_id = self._get_task_gof_id_for_gof(
                task_gof_details, checklist_gof.gof_id,
                checklist_gof.same_gof_order)
            task_gof_fields += [
                TaskGoFFieldDTO(
                    task_gof_id=task_gof_id,
                    field_id=checklist_gof_field.field_id,
                    field_response=checklist_gof_field.field_response)
                for checklist_gof_field in checklist_gof.field_values_dtos
            ]
        return task_gof_fields

    @staticmethod
    def _get_task_gof_id_for_gof(
            task_gof_details: List[TaskGoFDetailsDTO],
            gof_id: str, same_gof_order: int) -> Optional[int]:
        for task_gof in task_gof_details:
            gof_matched = (
                    task_gof.gof_id == gof_id and
                    task_gof.same_gof_order == same_gof_order)
            if gof_matched:
                return task_gof.task_gof_id
        return

    def _perform_gof_details_validation(
            self,
            transition_template_dto: CreateTransitionChecklistTemplateDTO,
            action_type: ActionTypes, project_id: str
    ):
        gof_details_validation_interactor = \
            GoFsDetailsValidationsInteractor(
                task_storage=self.task_storage, gof_storage=self.gof_storage,
                create_task_storage=self.create_task_storage,
                storage=self.storage, field_storage=self.field_storage,
                task_template_storage=self.task_template_storage
            )
        stage_id = self.stage_action_storage.get_stage_id_for_action_id(
            transition_template_dto.action_id)
        gof_details_validation_interactor.perform_gofs_details_validations(
            transition_template_dto.transition_checklist_gofs,
            transition_template_dto.created_by_id,
            transition_template_dto.transition_checklist_template_id,
            project_id, action_type, stage_id)

    def _validate_task_id(self, task_id) -> Optional[InvalidTaskIdException]:
        is_valid_task_id = self.create_task_storage.is_valid_task_id(
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
        self.stage_action_storage.validate_transition_template_relation_with_action(
            transition_checklist_template_id, action_id, stage_id)
        return

    def _validate_for_duplicate_same_gof_order(
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

    def _validate_all_user_stage_permitted_fields_are_filled_or_not(
            self, user_id: str, task_id: int, project_id: str, stage_id: int,
            transition_template_id: str
    ):
        from ib_tasks.adapters.roles_service_adapter import \
            get_roles_service_adapter
        roles_service_adapter = get_roles_service_adapter()
        user_roles = roles_service_adapter.roles_service \
            .get_user_role_ids_based_on_project(user_id, project_id)
        template_gof_ids = \
            self.task_template_storage.get_template_stage_permitted_gof_ids(
                task_template_id=transition_template_id, stage_id=stage_id)
        gof_id_with_display_name_dtos = \
            self.gof_storage.get_user_write_permitted_gof_ids_in_given_gof_ids(
                user_roles, template_gof_ids)
        user_permitted_gof_ids = [
            dto.gof_id for dto in gof_id_with_display_name_dtos]
        field_id_with_display_name_dtos = \
            self.field_storage.get_user_writable_fields_for_given_gof_ids(
                user_roles, user_permitted_gof_ids)
        filled_gofs_with_task_gof_ids = \
            self.gof_storage.get_filled_task_gofs_with_gof_id(task_id)
        task_gof_ids = [
            dto.task_gof_id for dto in filled_gofs_with_task_gof_ids]
        filled_field_ids = \
            self.gof_storage.get_filled_field_ids_of_given_task_gof_ids(
                task_gof_ids)
        self._validate_all_user_permitted_field_ids_are_filled_or_not(
            field_id_with_display_name_dtos, filled_field_ids)

    @staticmethod
    def _validate_all_user_permitted_field_ids_are_filled_or_not(
            permitted_fields, filled_field_ids
    ) -> Optional[UserDidNotFillRequiredFields]:
        permitted_field_ids = [
            permitted_field.field_id for permitted_field in permitted_fields]
        unfilled_field_ids = list(sorted(
            set(permitted_field_ids) - set(filled_field_ids)))
        if unfilled_field_ids:
            unfilled_field_dtos = [
                permitted_field
                for permitted_field in permitted_fields
                if permitted_field.field_id in unfilled_field_ids
            ]
            raise UserDidNotFillRequiredFields(unfilled_field_dtos)
        return