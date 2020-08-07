from typing import Optional, List

from ib_tasks.exceptions.gofs_custom_exceptions import \
    DuplicateSameGoFOrderForAGoF
from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskIdException
from ib_tasks.interactors.create_or_update_task \
    .template_gofs_fields_base_validations import \
    TemplateGoFsFieldsBaseValidationsInteractor
from ib_tasks.interactors.storage_interfaces.action_storage_interface import \
    ActionStorageInterface
from ib_tasks.interactors.storage_interfaces \
    .create_or_update_task_storage_interface import \
    CreateOrUpdateTaskStorageInterface
from ib_tasks.interactors.storage_interfaces.task_template_storage_interface \
    import \
    TaskTemplateStorageInterface
from ib_tasks.interactors.task_dtos import GoFFieldsDTO
from ib_tasks.interactors.task_template_dtos import \
    CreateTransitionChecklistTemplateDTO


class CreateTransitionChecklistTemplateInteractor:

    def __init__(self,
                 create_or_update_task_storage:
                 CreateOrUpdateTaskStorageInterface,
                 template_storage: TaskTemplateStorageInterface,
                 stage_action_storage: ActionStorageInterface,
                 task
        ):
        self.stage_action_storage = stage_action_storage
        self.template_storage = template_storage
        self.create_or_update_task_storage = create_or_update_task_storage

    def create_transition_checklist_wrapper(self):
        pass

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
        template_gofs_fields_validation_interactor.perform_base_validations_for_template_gofs_and_fields(
            task_dto.gof_fields_dtos, task_dto.created_by_id,
            task_dto.task_template_id, action_type
        )

    def _validate_task_id(self, task_id) -> Optional[InvalidTaskIdException]:
        is_valid_task_id = self.create_or_update_task_storage.is_valid_task_id(
            task_id)
        invalid_task_id = not is_valid_task_id
        if invalid_task_id:
            raise InvalidTaskIdException(task_id)
        return

    def _validate_transition_template_id(self,
                                         transition_checklist_template_id):
        self.template_storage.validate_transition_template_id(
            transition_checklist_template_id)

    def _validate_action_id(self, action_id):
        self.stage_action_storage.validate_action_id(action_id)

    def _validate_stage_id(self, stage_id):
        self.stage_action_storage.validate_stage_id(stage_id)

    def _validate_transition_template_id_related_to_given_stage_action(
            self, transition_checklist_template_id, action_id, stage_id
    ):
        self.stage_action_storage \
            .validate_transition_template_id_is_related_to_given_stage_action(
            transition_checklist_template_id, action_id, stage_id
        )

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
