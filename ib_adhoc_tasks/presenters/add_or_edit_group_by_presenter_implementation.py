from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_adhoc_tasks.constants.enum import StatusCode
from ib_adhoc_tasks.interactors.presenter_interfaces \
    .group_by_presenter_interface import AddOrEditGroupByPresenterInterface
from ib_adhoc_tasks.interactors.storage_interfaces.dtos import \
    GroupByResponseDTO


class AddOrEditGroupByPresenterImplementation(
    AddOrEditGroupByPresenterInterface, HTTPResponseMixin
):

    def get_response_for_add_or_edit_group_by(
            self, group_by_response_dto: GroupByResponseDTO
    ):
        group_by_response_dictionary = self._convert_to_group_by_response_dict(
            group_by_response_dto=group_by_response_dto
        )
        return self.prepare_200_success_response(
            response_dict=group_by_response_dictionary
        )

    @staticmethod
    def _convert_to_group_by_response_dict(
            group_by_response_dto: GroupByResponseDTO
    ):
        return {
            "group_by_key": group_by_response_dto.group_by_key,
            "display_name": group_by_response_dto.display_name,
            "order": group_by_response_dto.order
        }

    def get_response_for_user_not_allowed_to_create_more_than_one_group_by_in_list_view(
            self
    ):
        from ib_adhoc_tasks.constants.exception_messages import \
            USER_NOT_ALLOWED_TO_CREATE_MORE_THAN_ONE_GROUP_BY_IN_LIST_VIEW
        response_dict = {
            "response":
                USER_NOT_ALLOWED_TO_CREATE_MORE_THAN_ONE_GROUP_BY_IN_LIST_VIEW[
                    0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status":
                USER_NOT_ALLOWED_TO_CREATE_MORE_THAN_ONE_GROUP_BY_IN_LIST_VIEW[
                    1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict
        )

    def get_response_for_user_not_allowed_to_create_more_than_two_group_by_in_kanban_view(
            self
    ):
        from ib_adhoc_tasks.constants.exception_messages import \
            USER_NOT_ALLOWED_TO_CREATE_MORE_THAN_TWO_GROUP_BY_IN_KANBAN_VIEW
        response_dict = {
            "response":
                USER_NOT_ALLOWED_TO_CREATE_MORE_THAN_TWO_GROUP_BY_IN_KANBAN_VIEW[
                    0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status":
                USER_NOT_ALLOWED_TO_CREATE_MORE_THAN_TWO_GROUP_BY_IN_KANBAN_VIEW[
                    1],
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict
        )
