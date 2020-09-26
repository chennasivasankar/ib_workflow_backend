import abc
from typing import List

from ib_adhoc_tasks.interactors.storage_interfaces.dtos import \
    GroupByResponseDTO


class GetGroupByPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def get_response_for_get_group_by(
            self, group_by_response_dtos: List[GroupByResponseDTO]
    ):
        pass


class AddOrEditGroupByPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def get_response_for_add_or_edit_group_by(
            self, group_by_response_dtos: List[GroupByResponseDTO]
    ):
        pass

    @abc.abstractmethod
    def get_response_for_user_not_allowed_to_create_more_than_one_group_by_in_list_view(
            self
    ):
        pass

    @abc.abstractmethod
    def get_response_for_user_not_allowed_to_create_more_than_two_group_by_in_kanban_view(
            self
    ):
        pass
