from typing import List

from ib_adhoc_tasks.adapters.dtos import TasksCompleteDetailsDTO
from ib_adhoc_tasks.adapters.iam_service import InvalidProjectId, \
    InvalidUserId, InvalidUserForProject
from ib_adhoc_tasks.exceptions.custom_exceptions import InvalidOffsetValue, \
    InvalidLimitValue
from ib_adhoc_tasks.interactors.dtos.dtos import GroupByInfoKanbanViewDTO, \
    OffsetLimitDTO, GroupByDTO, TaskOffsetAndLimitValuesDTO
from ib_adhoc_tasks.interactors.presenter_interfaces \
    .get_tasks_for_kanban_view_presenter_interface import \
    GetTasksForKanbanViewPresenterInterface, TaskDetailsWithGroupByInfoDTO
from ib_adhoc_tasks.interactors.storage_interfaces.dtos import \
    GroupByDetailsDTO, GroupDetailsDTO, ChildGroupCountDTO
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
        try:
            return self.get_tasks_for_kanban_view_response(
                group_by_info_kanban_view_dto, presenter
            )
        except InvalidProjectId:
            return presenter.raise_invalid_project_id()
        except InvalidOffsetValue:
            return presenter.raise_invalid_offset_value()
        except InvalidLimitValue:
            return presenter.raise_invalid_limit_value()
        except InvalidUserId:
            return presenter.raise_invalid_user_id()
        except InvalidUserForProject:
            return presenter.raise_invalid_user_for_project()

    def get_tasks_for_kanban_view_response(
            self, group_by_info_kanban_view_dto: GroupByInfoKanbanViewDTO,
            presenter: GetTasksForKanbanViewPresenterInterface
    ):
        task_details_with_group_by_info_dto = self.get_tasks_for_kanban_view(
            group_by_info_kanban_view_dto)

        response = presenter.get_task_details_group_by_info_response(
            task_details_with_group_by_info_dto)
        return response

    def get_tasks_for_kanban_view(
            self, group_by_info_kanban_view_dto: GroupByInfoKanbanViewDTO
    ) -> TaskDetailsWithGroupByInfoDTO:
        project_id = group_by_info_kanban_view_dto.project_id
        self._validate_project_id(project_id)
        self._validate_limit_offset_values(group_by_info_kanban_view_dto)
        group_details_dtos, total_groups_count, child_group_count_dtos = \
            self._get_group_details_dtos(
                group_by_info_kanban_view_dto)
        task_ids = self._get_task_ids(group_details_dtos)
        task_details_dtos = self._get_task_details_dtos(task_ids)
        task_details_with_group_by_info_dto = TaskDetailsWithGroupByInfoDTO(
            group_details_dtos=group_details_dtos,
            total_groups_count=total_groups_count,
            child_group_count_dtos=child_group_count_dtos,
            task_details_dtos=task_details_dtos
        )
        return task_details_with_group_by_info_dto

    @staticmethod
    def _validate_limit_offset_values(
            group_by_info_kanban_view_dto: GroupByInfoKanbanViewDTO
    ):
        task_offset_limit_dto = \
            group_by_info_kanban_view_dto.task_offset_limit_dto
        task_offset = task_offset_limit_dto.offset
        task_limit = task_offset_limit_dto.limit
        group1_offset_limit_dto = \
            group_by_info_kanban_view_dto.group1_offset_limit_dto
        group1_offset = group1_offset_limit_dto.offset
        group1_limit = group1_offset_limit_dto.limit
        group2_offset_limit_dto = \
            group_by_info_kanban_view_dto.group2_offset_limit_dto
        group2_offset = group2_offset_limit_dto.offset
        group2_limit = group2_offset_limit_dto.limit

        is_invalid_offset_values = task_offset < 0 or group1_offset < 0 or \
                                   group2_offset < 0
        is_invalid_limit_values = task_limit < 0 or group1_limit < 0 or \
                                  group2_limit < 0

        if is_invalid_offset_values:
            raise InvalidOffsetValue()
        if is_invalid_limit_values:
            raise InvalidLimitValue()

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
        task_details_dtos = task_service.get_task_complete_details_dto(
            task_ids)
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
    ) -> (List[GroupDetailsDTO], int, List[ChildGroupCountDTO]):
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
        group_details_dtos, total_groups_count, child_group_count_dtos = \
            interactor.get_task_ids_for_view(
                project_id=project_id, adhoc_template_id=adhoc_template_id,
                group_by_dtos=group_by_dtos,
                task_offset_and_limit_values_dto
                =task_offset_and_limit_values_dto
            )
        return group_details_dtos, total_groups_count, child_group_count_dtos

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
