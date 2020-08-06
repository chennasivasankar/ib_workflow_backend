from typing import List

from ib_tasks.exceptions.task_custom_exceptions \
    import InvalidTaskIdException
from ib_tasks.interactors.get_task_base_interactor \
    import GetTaskBaseInteractor
from ib_tasks.interactors.presenter_interfaces.get_task_presenter_interface \
    import GetTaskPresenterInterface
from ib_tasks.interactors.presenter_interfaces.get_task_presenter_interface \
    import TaskCompleteDetailsDTO
from ib_tasks.interactors.storage_interfaces.create_or_update_task_storage_interface \
    import CreateOrUpdateTaskStorageInterface
from ib_tasks.interactors.storage_interfaces.fields_storage_interface \
    import FieldsStorageInterface
from ib_tasks.interactors.storage_interfaces.get_task_dtos import (
    TaskGoFDTO,
    TaskGoFFieldDTO,
    TaskDetailsDTO
)


class GetTaskInteractor:

    def __init__(
            self, storage: CreateOrUpdateTaskStorageInterface,
            stages_storage: FieldsStorageInterface
    ):
        self.storage = storage
        self.stages_storage = stages_storage

    def get_task_details_wrapper(
            self, user_id: str, task_id: int,
            presenter: GetTaskPresenterInterface
    ):
        try:
            return self.get_task_details_response(user_id, task_id, presenter)
        except InvalidTaskIdException as err:
            response = presenter.raise_exception_for_invalid_task_id(err)
            return response

    def get_task_details_response(
            self, user_id: str, task_id: int,
            presenter: GetTaskPresenterInterface
    ):
        task_complete_details_dto = self.get_task_details(user_id, task_id)
        response = presenter.get_task_response(task_complete_details_dto)
        return response

    def get_task_details(self, user_id: str, task_id: int):
        get_task_base_interactor = GetTaskBaseInteractor(storage=self.storage)
        task_details_dto = get_task_base_interactor.get_task(task_id)
        user_roles = self._get_user_roles(user_id)
        task_details_dto = self._get_task_details_dto(
            task_details_dto, user_roles
        )
        stages_and_actions_details_dtos = \
            self._get_stages_and_actions_details_dtos(task_id, user_id)
        task_complete_details_dto = TaskCompleteDetailsDTO(
            task_id=task_id,
            task_details_dto=task_details_dto,
            stages_and_actions_details_dtos=stages_and_actions_details_dtos

        )
        return task_complete_details_dto

    def _get_task_details_dto(
            self, task_details_dto: TaskDetailsDTO, user_roles: List[str]
    ):
        template_id = task_details_dto.template_id
        task_gof_dtos = task_details_dto.task_gof_dtos
        all_task_gof_field_dtos = task_details_dto.task_gof_field_dtos
        permission_task_gof_dtos = self._get_permission_task_gof_dtos(
            task_gof_dtos, user_roles
        )
        task_gof_field_dtos = self._get_task_gof_field_dtos(
            permission_task_gof_dtos, all_task_gof_field_dtos
        )
        permission_task_gof_field_dtos = self._get_permission_task_gof_field_dtos(
            task_gof_field_dtos, user_roles
        )
        task_details_dto = TaskDetailsDTO(
            template_id=template_id,
            task_gof_dtos=permission_task_gof_dtos,
            task_gof_field_dtos=permission_task_gof_field_dtos
        )
        return task_details_dto

    def _get_stages_and_actions_details_dtos(
            self, task_id: int, user_id: str
    ):
        from ib_tasks.interactors.get_task_stages_and_actions \
            import GetTaskStagesAndActions
        from ib_tasks.interactors.storage_interfaces.storage_interface import \
            StorageInterface
        interactor = GetTaskStagesAndActions(
            storage=self.stages_storage,
            task_storage=StorageInterface()
        )
        stages_and_actions_details_dtos = \
            interactor.get_task_stages_and_actions(task_id, user_id)
        return stages_and_actions_details_dtos

    @staticmethod
    def _get_task_gof_field_dtos(
            permission_task_gof_dtos: List[TaskGoFDTO],
            all_task_gof_field_dtos: List[TaskGoFFieldDTO]
    ) -> List[TaskGoFFieldDTO]:

        task_gof_ids = [
            permission_task_gof_dto.task_gof_id
            for permission_task_gof_dto in permission_task_gof_dtos
        ]
        task_gof_field_dtos = [
            task_gof_field_dto
            for task_gof_field_dto in all_task_gof_field_dtos
            if task_gof_field_dto.task_gof_id in task_gof_ids
        ]
        return task_gof_field_dtos

    def _get_permission_task_gof_field_dtos(
            self, task_gof_field_dtos: List[TaskGoFFieldDTO],
            user_roles: List[str]
    ) -> List[TaskGoFFieldDTO]:

        field_ids = [
            task_gof_field_dto.field_id
            for task_gof_field_dto in task_gof_field_dtos
        ]
        permission_field_ids = self.storage.get_field_ids_having_permission(
            field_ids, user_roles
        )
        permission_task_gof_field_dtos = [
            task_gof_field_dto
            for task_gof_field_dto in task_gof_field_dtos
            if task_gof_field_dto.field_id in permission_field_ids
        ]
        return permission_task_gof_field_dtos

    def _get_permission_task_gof_dtos(
            self, task_gof_dtos: List[TaskGoFDTO], user_roles: List[str]
    ) -> List[TaskGoFDTO]:

        gof_ids = [
            task_gof_dto.gof_id
            for task_gof_dto in task_gof_dtos
        ]
        permission_gof_ids = self.storage.get_gof_ids_having_permission(
            gof_ids, user_roles
        )
        permission_task_gof_dtos = [
            task_gof_dto
            for task_gof_dto in task_gof_dtos
            if task_gof_dto.gof_id in permission_gof_ids
        ]
        return permission_task_gof_dtos

    def _get_user_roles(self, user_id: str) -> List[str]:

        from ib_tasks.adapters.roles_service_adapter \
            import get_roles_service_adapter
        roles_service_adapter = get_roles_service_adapter()
        roles_service = roles_service_adapter.roles_service
        user_roles = roles_service.get_user_role_ids(user_id)
        return user_roles
