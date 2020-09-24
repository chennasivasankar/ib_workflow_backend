from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_adhoc_tasks.adapters.dtos import TasksCompleteDetailsDTO
from ib_adhoc_tasks.interactors.dtos.dtos import TaskIdsAndCountDTO
from ib_adhoc_tasks.interactors.presenter_interfaces.get_task_details_in_group_presenter_interface import \
    GetTaskDetailsInGroupPresenterInterface
from ib_adhoc_tasks.presenters.mixins.tasks_details_mixin import \
    TaskDetailsMixin


class GetTaskDetailsInGroupPresenterImplementation(
    GetTaskDetailsInGroupPresenterInterface,
    HTTPResponseMixin,
    TaskDetailsMixin
):

    def get_task_details_in_group_response(
            self, tasks_complete_details_dto: TasksCompleteDetailsDTO,
            task_ids_and_count_dto: TaskIdsAndCountDTO
    ):
        tasks = self.get_tasks_details(
            task_ids=task_ids_and_count_dto.task_ids,
            task_details_dto=tasks_complete_details_dto
        )
        response_dict = {
            "total_tasks": task_ids_and_count_dto.total_tasks_count,
            "tasks": tasks
        }
        return self.prepare_200_success_response(response_dict=response_dict)
