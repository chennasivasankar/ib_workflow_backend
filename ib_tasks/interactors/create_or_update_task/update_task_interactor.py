from typing import Optional, List

from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskException
from ib_tasks.interactors.create_or_update_task.create_or_update_task_base_validations import \
    CreateOrUpdateTaskBaseValidationsInteractor
from ib_tasks.interactors.presenter_interfaces.field_response_validations_presenter import \
    FieldResponseValidationsPresenter
from ib_tasks.interactors.presenter_interfaces.presenter_interface import \
    PresenterInterface
from ib_tasks.interactors.presenter_interfaces.update_task_presenter import \
    UpdateTaskPresenterInterface
from ib_tasks.interactors.storage_interfaces.create_or_update_task_storage_interface import \
    CreateOrUpdateTaskStorageInterface
from ib_tasks.interactors.storage_interfaces.fields_storage_interface import \
    FieldsStorageInterface
from ib_tasks.interactors.storage_interfaces.get_task_dtos import \
    TaskGoFFieldDTO
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
            create_task_storage: CreateOrUpdateTaskStorageInterface,
            storage: StorageInterface, field_storage: FieldsStorageInterface,
            stage_storage: StageStorageInterface
    ):
        self.task_storage = task_storage
        self.create_task_storage = create_task_storage
        self.storage = storage
        self.field_storage = field_storage
        self.stage_storage = stage_storage

    def update_task_wrapper(
            self, presenter: UpdateTaskPresenterInterface,
            task_dto: UpdateTaskDTO, act_on_task_presenter: PresenterInterface,
            field_validations_presenter: FieldResponseValidationsPresenter
    ):
        try:
            return self._prepare_update_task_response(
                task_dto, presenter, act_on_task_presenter,
                field_validations_presenter
            )
        except:
            pass

    def _prepare_update_task_response(
            self, task_dto: UpdateTaskDTO,
            presenter: UpdateTaskPresenterInterface,
            act_on_task_presenter: PresenterInterface,
            field_validations_presenter: FieldResponseValidationsPresenter
    ):
        self.update_task(
            task_dto, field_validations_presenter, act_on_task_presenter
        )
        return presenter.get_update_task_response()

    def update_task(
            self, task_dto: UpdateTaskDTO,
            field_validations_presenter: FieldResponseValidationsPresenter,
            act_on_task_presenter: PresenterInterface
    ):
        task_id = task_dto.task_id
        self._validate_task_id(task_id)
        task_template_id = \
            self.create_task_storage.get_template_id_for_given_task(task_id)
        base_validations_interactor = \
            CreateOrUpdateTaskBaseValidationsInteractor(
                self.task_storage, self.create_task_storage, self.storage,
                self.field_storage
            )
        base_validations_interactor. \
            perform_base_validations_for_create_or_update_task(
            task_dto, task_template_id, field_validations_presenter)
        existing_gof_ids = \
            self.create_task_storage.get_gof_ids_related_to_a_task(
                task_id)
        existing_field_ids = \
            self.create_task_storage.get_field_ids_related_to_given_task(
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
            gof_id_already_exists = task_gof_dto.gof_id in existing_gof_ids
            if gof_id_already_exists:
                task_gof_dtos_for_updation.append(task_gof_dto)
            else:
                task_gof_dtos_for_creation.append(task_gof_dto)
        if task_gof_dtos_for_updation:
            self._update_task_gofs(
                task_gof_dtos_for_updation, task_dto, existing_field_ids)
        if task_gof_dtos_for_creation:
            self._create_task_gofs(task_gof_dtos_for_creation, task_dto)

        act_on_task_interactor = UserActionOnTaskInteractor(
            user_id=task_dto.created_by_id, board_id=None,
            task_id=task_id,
            action_id=task_dto.action_id,
            storage=self.storage, gof_storage=self.create_task_storage,
            field_storage=self.field_storage, stage_storage=self.stage_storage
        )
        act_on_task_interactor.user_action_on_task(act_on_task_presenter)

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

    def _update_task_gofs(
            self, task_gof_dtos_for_updation: List[TaskGoFWithTaskIdDTO],
            task_dto: UpdateTaskDTO, existing_field_ids: List[str]
    ):
        task_gof_details_dtos = \
            self.create_task_storage.update_task_gofs(
                task_gof_dtos_for_updation
            )
        task_gof_field_dtos = self._prepare_task_gof_fields_dtos(
            task_dto, task_gof_details_dtos)
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
