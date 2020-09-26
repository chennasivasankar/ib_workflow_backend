from typing import List

from ib_adhoc_tasks.adapters.dtos import TaskIdWithSubTasksCountDTO, \
    TaskIdWithCompletedSubTasksCountDTO
from ib_adhoc_tasks.interactors.dtos.dtos import \
    GetTaskDetailsInGroupInputDTO, \
    GroupByValueDTO, TaskIdsForGroupsParameterDTO
from ib_adhoc_tasks.interactors.presenter_interfaces \
    .get_task_details_in_group_presenter_interface import \
    GetTaskDetailsInGroupPresenterInterface
from ib_adhoc_tasks.interactors.storage_interfaces.elastic_storage_interface \
    import \
    ElasticStorageInterface
from ib_adhoc_tasks.interactors.storage_interfaces.storage_interface import \
    StorageInterface


class GetTaskDetailsInGroupInteractor:

    def __init__(
            self, storage: StorageInterface,
            elastic_storage: ElasticStorageInterface):
        self.storage = storage
        self.elastic_storage = elastic_storage

    def get_task_details_in_group_wrapper(
            self,
            get_task_details_in_group_input_dto: GetTaskDetailsInGroupInputDTO,
            presenter: GetTaskDetailsInGroupPresenterInterface
    ):
        tasks_complete_details_dto, task_ids_and_count_dto = \
            self.get_task_details_in_group(
                get_task_details_in_group_input_dto
                =get_task_details_in_group_input_dto
            )
        task_ids = task_ids_and_count_dto.task_ids
        task_with_sub_tasks_count_dtos = \
            self._get_task_id_with_sub_tasks_count_dtos(task_ids)
        task_completed_sub_tasks_count_dtos = \
            self._get_task_with_completed_sub_tasks_count_dtos(task_ids)
        response = presenter.get_task_details_in_group_response(
            tasks_complete_details_dto=tasks_complete_details_dto,
            task_ids_and_count_dto=task_ids_and_count_dto,
            task_with_sub_tasks_count_dtos=task_with_sub_tasks_count_dtos,
            task_completed_sub_tasks_count_dtos
            =task_completed_sub_tasks_count_dtos
        )
        return response

    @staticmethod
    def _get_task_id_with_sub_tasks_count_dtos(
            task_ids: List[int]
    ) -> List[TaskIdWithSubTasksCountDTO]:
        from ib_adhoc_tasks.adapters.service_adapter import get_service_adapter
        service_adapter = get_service_adapter()
        task_id_with_sub_tasks_count_dtos = \
            service_adapter.task_service.get_sub_tasks_count_task_ids(
                task_ids=task_ids
            )
        return task_id_with_sub_tasks_count_dtos

    @staticmethod
    def _get_task_with_completed_sub_tasks_count_dtos(
            task_ids: List[int]
    ) -> List[TaskIdWithCompletedSubTasksCountDTO]:
        from ib_adhoc_tasks.adapters.service_adapter import get_service_adapter
        service_adapter = get_service_adapter()
        _get_task_with_completed_sub_tasks_count_dtos = \
            service_adapter.task_service \
                .get_completed_sub_tasks_count_for_task_ids(task_ids=task_ids)
        return _get_task_with_completed_sub_tasks_count_dtos

    def get_task_details_in_group(
            self,
            get_task_details_in_group_input_dto: GetTaskDetailsInGroupInputDTO
    ):
        # TODO: need to be optimise
        group_by_response_dtos = self.storage.get_group_by_dtos(
            user_id=get_task_details_in_group_input_dto.user_id,
            view_type=get_task_details_in_group_input_dto.view_type
        )
        group_by_response_dtos = sorted(group_by_response_dtos,
                                        key=lambda x: x.order)
        group_by_values = get_task_details_in_group_input_dto.group_by_values
        group_by_value_dtos = [
            GroupByValueDTO(
                group_by_value=group_by_value,
                group_by_display_name=group_by_response_dto.group_by_key
            )
            for group_by_value, group_by_response_dto in
            list(zip(group_by_values, group_by_response_dtos))
        ]

        from ib_adhoc_tasks.constants.constants import ADHOC_TEMPLATE_ID
        task_ids_for_groups_parameter_dto = TaskIdsForGroupsParameterDTO(
            project_id=get_task_details_in_group_input_dto.project_id,
            template_id=ADHOC_TEMPLATE_ID,
            user_id=get_task_details_in_group_input_dto.user_id,
            groupby_value_dtos=group_by_value_dtos,
            limit=get_task_details_in_group_input_dto.limit,
            offset=get_task_details_in_group_input_dto.offset
        )

        from ib_adhoc_tasks.interactors.get_task_ids_for_group_interactor \
            import \
            GetTaskIdsForGroupInteractor
        get_task_ids_for_group_interactor = GetTaskIdsForGroupInteractor(
            elastic_storage=self.elastic_storage
        )
        task_ids_and_count_dto = \
            get_task_ids_for_group_interactor.get_task_ids_for_groups(
                task_ids_for_groups_parameter_dto
                =task_ids_for_groups_parameter_dto
            )
        from ib_adhoc_tasks.adapters.dtos import TasksDetailsInputDTO
        task_details_input_dto = TasksDetailsInputDTO(
            task_ids=task_ids_and_count_dto.task_ids,
            project_id=get_task_details_in_group_input_dto.project_id,
            user_id=get_task_details_in_group_input_dto.user_id,
            view_type=get_task_details_in_group_input_dto.view_type
        )
        from ib_adhoc_tasks.adapters.service_adapter import get_service_adapter
        service_adapter = get_service_adapter()
        tasks_complete_details_dto = \
            service_adapter.task_service.get_task_complete_details_dto(
                task_details_input_dto=task_details_input_dto
            )
        return tasks_complete_details_dto, task_ids_and_count_dto
