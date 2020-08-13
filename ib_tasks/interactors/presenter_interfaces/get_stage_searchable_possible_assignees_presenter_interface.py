import abc
from typing import List

from django.http import response

from ib_tasks.adapters.dtos import UserDetailsDTO
from ib_tasks.exceptions.fields_custom_exceptions import \
    LimitShouldBeGreaterThanZeroException, \
    OffsetShouldBeGreaterThanZeroException
from ib_tasks.exceptions.stage_custom_exceptions import InvalidStageId


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
    def get_stage_assignee_details_response(
            self, user_details_dtos: List[UserDetailsDTO]
    ) -> response.HttpResponse:
        pass
