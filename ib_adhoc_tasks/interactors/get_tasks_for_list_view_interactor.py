from typing import List

from ib_adhoc_tasks.adapters.dtos import TasksCompleteDetailsDTO, \
    TasksDetailsInputDTO
from ib_adhoc_tasks.constants.enum import ViewType
from ib_adhoc_tasks.exceptions.custom_exceptions import \
    InvalidOffsetOrLimitValue
from ib_adhoc_tasks.exceptions.custom_exceptions import InvalidProjectId
from ib_adhoc_tasks.interactors.dtos.dtos import GroupByInfoListViewDTO, \
    TaskOffsetAndLimitValuesDTO, GroupByDTO
from ib_adhoc_tasks.interactors.presenter_interfaces \
    .get_tasks_for_list_view_presenter_interface import \
    GetTasksForListViewPresenterInterface
from ib_adhoc_tasks.interactors.storage_interfaces.dtos import \
    GroupDetailsDTO, \
    GroupByDetailsDTO
from ib_adhoc_tasks.interactors.storage_interfaces.elastic_storage_interface \
    import \
    ElasticStorageInterface
from ib_adhoc_tasks.interactors.storage_interfaces.storage_interface import \
    StorageInterface


class GetTasksForListViewInteractor:

    def __init__(
            self, storage: StorageInterface,
            elastic_storage: ElasticStorageInterface
    ):
        self.storage = storage
        self.elastic_storage = elastic_storage

    def get_tasks_for_list_view_wrapper(
            self,
            group_by_info_list_view_dto: GroupByInfoListViewDTO,
            presenter: GetTasksForListViewPresenterInterface
    ):
        from ib_adhoc_tasks.exceptions.custom_exceptions import \
            InvalidProjectId
        try:
            return self.get_tasks_for_list_view_response(
                group_by_info_list_view_dto, presenter
            )
        except InvalidProjectId:
            return presenter.raise_invalid_project_id()
        except InvalidOffsetOrLimitValue:
            return presenter.raise_invalid_offset_or_limit_value()

    def get_tasks_for_list_view_response(
            self, group_by_info_list_view_dto: GroupByInfoListViewDTO,
            presenter: GetTasksForListViewPresenterInterface
    ):
        group_details_dtos, task_details_dto = self.get_tasks_for_list_view(
            group_by_info_list_view_dto)

        response = presenter.get_task_details_group_by_info_response(
            group_details_dtos, task_details_dto)
        return response

    def get_tasks_for_list_view(
            self, group_by_info_list_view_dto: GroupByInfoListViewDTO
    ):
        project_id = group_by_info_list_view_dto.project_id
        self._validate_limit_offset_values(group_by_info_list_view_dto)
        self._validate_project_id(project_id)
        group_details_dtos = self._get_group_details_dtos(
            group_by_info_list_view_dto)
        task_ids = self._get_task_ids(group_details_dtos)
        user_id = group_by_info_list_view_dto.user_id
        task_details_input_dto = TasksDetailsInputDTO(
            task_ids=task_ids,
            project_id=project_id,
            user_id=user_id,
            view_type=ViewType.LIST.value
        )
        task_details_dto = self._get_task_details_dto(task_details_input_dto)
        return group_details_dtos, task_details_dto

    @staticmethod
    def _validate_limit_offset_values(
            group_by_info_list_view_dto: GroupByInfoListViewDTO
    ):
        task_offset_limit_dto = \
            group_by_info_list_view_dto.task_offset_limit_dto
        task_offset = task_offset_limit_dto.offset
        task_limit = task_offset_limit_dto.limit
        group_offset_limit_dto = \
            group_by_info_list_view_dto.group_offset_limit_dto
        group_offset = group_offset_limit_dto.offset
        group_limit = group_offset_limit_dto.limit

        is_invalid_offset_or_limit_values = (
                task_limit < 0 or task_offset < 0 or group_offset < 0 or
                group_limit < 0)

        if is_invalid_offset_or_limit_values:
            raise InvalidOffsetOrLimitValue()

    @staticmethod
    def _get_task_ids(group_details_dtos: List[GroupDetailsDTO]):
        all_task_ids = []
        for dto in group_details_dtos:
            task_ids = dto.task_ids
            all_task_ids += task_ids
        return all_task_ids

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

    def _get_group_details_dtos(
            self,
            group_by_info_list_view_dto: GroupByInfoListViewDTO
    ) -> List[GroupDetailsDTO]:
        user_id = group_by_info_list_view_dto.user_id
        project_id = group_by_info_list_view_dto.project_id
        group_by_details_dtos = self.storage.get_group_by_details_dtos(user_id)
        group_by_dtos = self._get_group_by_dtos(
            group_by_details_dtos,
            group_by_info_list_view_dto
        )
        task_offset_limit_dto = \
            group_by_info_list_view_dto.task_offset_limit_dto
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
        group_details_dtos, group_count_dtos, child_group_count_dtos = \
            interactor.get_task_ids_for_view(
                project_id=project_id, adhoc_template_id=adhoc_template_id,
                group_by_dtos=group_by_dtos, user_id=user_id,
                task_offset_and_limit_values_dto=task_offset_and_limit_values_dto
            )
        return group_details_dtos

    @staticmethod
    def _get_group_by_dtos(
            group_by_details_dtos: List[GroupByDetailsDTO],
            group_by_info_list_view_dto: GroupByInfoListViewDTO
    ):
        group_offset_limit = \
            group_by_info_list_view_dto.group_offset_limit_dto
        group_by_dtos = [
            GroupByDTO(
                group_by_value=group_by_details_dtos[0].group_by,
                order=group_by_details_dtos[0].order,
                offset=group_offset_limit.offset,
                limit=group_offset_limit.limit
            )
        ]
        return group_by_dtos

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
