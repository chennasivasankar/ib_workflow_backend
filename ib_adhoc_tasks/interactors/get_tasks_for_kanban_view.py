from typing import List

from ib_adhoc_tasks.adapters.dtos import TasksCompleteDetailsDTO
from ib_adhoc_tasks.exceptions.custom_exceptions import InvalidProjectId
from ib_adhoc_tasks.interactors.dtos import GroupByInfoKanbanViewDTO, \
    OffsetLimitDTO, GroupByDTO, TaskOffsetAndLimitValuesDTO
from ib_adhoc_tasks.interactors.presenter_interfaces \
    .get_tasks_for_kanban_view_presenter_interface import \
    GetTasksForKanbanViewPresenterInterface
from ib_adhoc_tasks.interactors.storage_interfaces.dtos import \
    GroupByDetailsDTO, GroupDetailsDTO
from ib_adhoc_tasks.interactors.storage_interfaces.elastic_storage_interface \
    import \
    ElasticStorageInterface
from ib_adhoc_tasks.interactors.storage_interfaces.storage_interface import \
    StorageInterface


class GetTasksForKanbanViewInteractor:

    def __init__(
            self, storage: StorageInterface,
            elastic_storage: ElasticStorageInterface
    ):
        self.storage = storage
        self.elastic_storage = elastic_storage

    def get_tasks_for_kanban_view_wrapper(
            self,
            group_by_info_kanban_view_dto: GroupByInfoKanbanViewDTO,
            presenter: GetTasksForKanbanViewPresenterInterface
    ):
        from ib_adhoc_tasks.exceptions.custom_exceptions import \
            InvalidProjectId
        try:
            return self.get_tasks_for_kanban_view_response(
                group_by_info_kanban_view_dto, presenter
            )
        except InvalidProjectId:
            return presenter.raise_invalid_project_id()

    def get_tasks_for_kanban_view_response(
            self, group_by_info_kanban_view_dto: GroupByInfoKanbanViewDTO,
            presenter: GetTasksForKanbanViewPresenterInterface
    ):
        group_details_dtos, task_details_dtos = self.get_tasks_for_kanban_view(
            group_by_info_kanban_view_dto)

        response = presenter.get_task_details_group_by_info_response(
            group_details_dtos, task_details_dtos)
        return response

    def get_tasks_for_kanban_view(
            self, group_by_info_kanban_view_dto: GroupByInfoKanbanViewDTO
    ):
        project_id = group_by_info_kanban_view_dto.project_id
        self._validate_project_id(project_id)
        group_details_dtos = self._get_group_details_dtos(
            group_by_info_kanban_view_dto)
        task_ids = self._get_task_ids(group_details_dtos)
        task_details_dtos = self._get_task_details_dtos(task_ids)
        return group_details_dtos, task_details_dtos

    @staticmethod
    def _get_task_ids(group_details_dtos: List[GroupDetailsDTO]):
        all_task_ids = []
        for dto in group_details_dtos:
            task_ids = dto.task_ids
            all_task_ids += task_ids
        return all_task_ids

    @staticmethod
    def _get_task_details_dtos(
            task_ids: List[str]
    ) -> List[TasksCompleteDetailsDTO]:
        from ib_adhoc_tasks.adapters.service_adapter import get_service_adapter
        task_service_adapter = get_service_adapter()
        task_service = task_service_adapter.task_service
        task_details_dtos = task_service.get_task_complete_details_dtos(task_ids)
        return task_details_dtos

    @staticmethod
    def _validate_project_id(project_id: str):
        from ib_adhoc_tasks.adapters.service_adapter import get_service_adapter
        iam_service_adapter = get_service_adapter()
        iam_service = iam_service_adapter.iam_service
        valid_project_ids = iam_service.get_valid_project_ids([project_id])
        flag = 0
        for valid_project_id in valid_project_ids:
            if valid_project_id == project_id:
                flag = 1
                break
        if flag == 0:
            raise InvalidProjectId()

    def _get_group_details_dtos(
            self,
            group_by_info_kanban_view_dto: GroupByInfoKanbanViewDTO
    ) -> List[GroupDetailsDTO]:
        user_id = group_by_info_kanban_view_dto.user_id
        project_id = group_by_info_kanban_view_dto.project_id
        group_by_details_dtos = self.storage.get_group_by_details_dtos(user_id)
        group_by_dtos = self._get_group_by_dtos(
            group_by_details_dtos,
            group_by_info_kanban_view_dto
        )
        task_offset_limit_dto = \
            group_by_info_kanban_view_dto.task_offset_limit_dto
        task_offset_and_limit_values_dto = TaskOffsetAndLimitValuesDTO(
            offset=task_offset_limit_dto.offset,
            limit=task_offset_limit_dto.limit
        )
        from ib_adhoc_tasks.constants.constants import ADHOC_TEMPLATE_ID
        adhoc_template_id = ADHOC_TEMPLATE_ID
        from ib_adhoc_tasks.interactors.get_task_ids_for_view_interactor \
            import \
            GetTaskIdsForViewInteractor
        interactor = GetTaskIdsForViewInteractor(
            elastic_storage=self.elastic_storage)
        group_details_dtos = interactor.get_task_ids_for_view(
            project_id=project_id, adhoc_template_id=adhoc_template_id,
            group_by_dtos=group_by_dtos,
            task_offset_and_limit_values_dto=task_offset_and_limit_values_dto
        )
        return group_details_dtos

    def _get_group_by_dtos(
            self, group_by_details_dtos: List[GroupByDetailsDTO],
            group_by_info_kanban_view_dto: GroupByInfoKanbanViewDTO
    ):
        group1_offset_limit = \
            group_by_info_kanban_view_dto.group1_offset_limit_dto
        group2_offset_limit = \
            group_by_info_kanban_view_dto.group2_offset_limit_dto
        length = len(group_by_details_dtos)
        if length == 2:
            group_by_dtos = \
                self._get_group_by_dtos_when_selected_two_group_by_options(
                    group_by_details_dtos, group1_offset_limit,
                    group2_offset_limit
                )
        else:
            group_by_dtos = \
                self._group_by_dtos_when_selected_single_group_by_option(
                    group_by_details_dtos, group1_offset_limit
                )
        return group_by_dtos

    @staticmethod
    def _get_group_by_dtos_when_selected_two_group_by_options(
            group_by_details_dtos: List[GroupByDetailsDTO],
            group1_offset_limit: OffsetLimitDTO,
            group2_offset_limit: OffsetLimitDTO
    ):
        group_by_dtos = [
            GroupByDTO(
                group_by_value=group_by_details_dtos[0].group_by,
                order=group_by_details_dtos[0].order,
                offset=group1_offset_limit.offset,
                limit=group1_offset_limit.limit
            ),
            GroupByDTO(
                group_by_value=group_by_details_dtos[1].group_by,
                order=group_by_details_dtos[1].order,
                offset=group2_offset_limit.offset,
                limit=group2_offset_limit.limit
            )
        ]
        return group_by_dtos

    @staticmethod
    def _group_by_dtos_when_selected_single_group_by_option(
            group_by_details_dtos: List[GroupByDetailsDTO],
            group1_offset_limit: OffsetLimitDTO
    ):
        group_by_dtos = [
            GroupByDTO(
                group_by_value=group_by_details_dtos[0].group_by,
                order=group_by_details_dtos[0].order,
                offset=group1_offset_limit.offset,
                limit=group1_offset_limit.limit
            )
        ]
        return group_by_dtos
