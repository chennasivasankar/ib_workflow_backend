from typing import List

from ib_adhoc_tasks.adapters.dtos import TasksDetailsInputDTO, \
    TasksCompleteDetailsDTO
from ib_adhoc_tasks.constants.enum import ViewType
from ib_adhoc_tasks.interactors.dtos.dtos import GetChildGroupsInGroupInputDTO
from ib_adhoc_tasks.interactors.presenter_interfaces.get_child_groups_in_group_presenter_interface import \
    GetChildGroupsInGroupPresenterInterface
from ib_adhoc_tasks.interactors.storage_interfaces.dtos import GroupDetailsDTO
from ib_adhoc_tasks.interactors.storage_interfaces.elastic_storage_interface import \
    ElasticStorageInterface
from ib_adhoc_tasks.interactors.storage_interfaces.storage_interface import \
    StorageInterface


class GetChildGroupsInGroupInteractor:

    def __init__(
            self, storage: StorageInterface,
            elastic_storage: ElasticStorageInterface):
        self.storage = storage
        self.elastic_storage = elastic_storage

    def get_child_groups_in_group_wrapper(
            self, presenter: GetChildGroupsInGroupPresenterInterface,
            get_child_groups_in_group_input_dto: GetChildGroupsInGroupInputDTO
    ):
        group_details_dtos, task_details_dto, total_child_groups_count = \
            self.get_child_groups_in_group(
                get_child_groups_in_group_input_dto=get_child_groups_in_group_input_dto
            )
        response = presenter.prepare_response_for_get_child_groups_in_group(
            group_details_dtos=group_details_dtos,
            total_child_groups_count=total_child_groups_count,
            task_details_dto=task_details_dto
        )
        return response

    def get_child_groups_in_group(
            self,
            get_child_groups_in_group_input_dto: GetChildGroupsInGroupInputDTO
    ):
        group_by_response_dtos = self.storage.get_group_by_dtos(
            user_id=get_child_groups_in_group_input_dto.user_id,
            view_type=ViewType.KANBAN.value
        )

        stage_ids = self._get_user_valid_stage_ids(
            get_child_groups_in_group_input_dto)

        group_details_dtos, total_child_groups_count = \
            self.elastic_storage.get_child_group_details_of_group(
                get_child_groups_in_group_input_dto=get_child_groups_in_group_input_dto,
                group_by_response_dtos=group_by_response_dtos,
                stage_ids=stage_ids
            )

        type_of_child_group_by = ""
        for group_by_response_dto in group_by_response_dtos:
            if group_by_response_dto.order == 2:
                type_of_child_group_by = group_by_response_dto.group_by_key

        from ib_adhoc_tasks.interactors.get_task_ids_for_view_interactor import \
            GetTaskIdsForViewInteractor
        get_task_ids_for_view_interactor = GetTaskIdsForViewInteractor(
            elastic_storage=self.elastic_storage
        )
        group_details_dtos = \
            get_task_ids_for_view_interactor.add_child_group_by_display_name_to_dtos(
                group_details_dtos=group_details_dtos,
                type_of_child_group_by=type_of_child_group_by
            )

        task_ids = self._get_task_ids(group_details_dtos)
        task_details_input_dto = TasksDetailsInputDTO(
            task_ids=task_ids,
            project_id=get_child_groups_in_group_input_dto.project_id,
            user_id=get_child_groups_in_group_input_dto.user_id,
            view_type=ViewType.LIST.value
        )
        task_details_dto = self._get_task_details_dto(task_details_input_dto)

        return group_details_dtos, task_details_dto, total_child_groups_count

    @staticmethod
    def _get_task_details_dto(
            task_details_input_dto: TasksDetailsInputDTO
    ) -> TasksCompleteDetailsDTO:
        from ib_adhoc_tasks.adapters.service_adapter import get_service_adapter
        task_service_adapter = get_service_adapter()
        task_service = task_service_adapter.task_service
        task_details_dto = task_service.get_task_complete_details_dto(
            task_details_input_dto)
        return task_details_dto

    @staticmethod
    def _get_task_ids(group_details_dtos: List[GroupDetailsDTO]):
        all_task_ids = []
        for dto in group_details_dtos:
            task_ids = dto.task_ids
            all_task_ids += task_ids
        return all_task_ids

    @staticmethod
    def _get_user_valid_stage_ids(
            get_child_groups_in_group_input_dto: GetChildGroupsInGroupInputDTO
    ):
        from ib_adhoc_tasks.adapters.service_adapter import get_service_adapter
        service_adapter = get_service_adapter()
        user_role_ids = \
            service_adapter.iam_service.get_user_role_ids_based_on_project(
                user_id=get_child_groups_in_group_input_dto.user_id,
                project_id=get_child_groups_in_group_input_dto.project_id
            )
        stage_ids = service_adapter.task_service.get_user_permitted_stage_ids(
            user_role_ids=user_role_ids
        )
        return stage_ids
