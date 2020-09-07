import abc

from django.http import response

from ib_tasks.exceptions.stage_custom_exceptions import InvalidStageId
from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskDisplayId
from ib_tasks.interactors.stages_dtos import UserDetailsWithTeamDetailsDTO


class GetStageSearchablePossibleAssigneesPresenterInterface(abc.ABC):
    @abc.abstractmethod
    def raise_invalid_stage_id_exception(
            self, err: InvalidStageId) -> response.HttpResponse:
        pass

    @abc.abstractmethod
    def raise_invalid_limit_exception(self) -> response.HttpResponse:
        pass

    @abc.abstractmethod
    def raise_invalid_offset_exception(self) -> response.HttpResponse:
        pass

    @abc.abstractmethod
    def raise_invalid_task_display_id_exception(
            self, err: InvalidTaskDisplayId) -> response.HttpResponse:
        pass

    @abc.abstractmethod
    def get_stage_assignee_details_response(
            self, user_details_with_team_details_dto:
            UserDetailsWithTeamDetailsDTO
    ) -> response.HttpResponse:
        pass
