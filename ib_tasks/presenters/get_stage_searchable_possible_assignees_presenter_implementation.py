from typing import List

from django.http import response
from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_tasks.adapters.dtos import UserDetailsDTO
from ib_tasks.exceptions.stage_custom_exceptions import InvalidStageId
from ib_tasks.interactors.presenter_interfaces. \
    get_stage_searchable_possible_assignees_presenter_interface import \
    GetStageSearchablePossibleAssigneesPresenterInterface


class GetStageSearchablePossibleAssigneesPresenterImplementation(
        GetStageSearchablePossibleAssigneesPresenterInterface,
        HTTPResponseMixin):
    def raise_invalid_limit_exception(self) -> response.HttpResponse:
        from ib_tasks.constants.exception_messages import \
            LIMIT_SHOULD_BE_GREATER_THAN_ZERO
        response_dict = {
            "response": LIMIT_SHOULD_BE_GREATER_THAN_ZERO[0],
            "http_status_code": 400,
            "res_status": LIMIT_SHOULD_BE_GREATER_THAN_ZERO[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict
        )

    def raise_invalid_offset_exception(self) -> response.HttpResponse:
        from ib_tasks.constants.exception_messages import \
            OFFSET_SHOULD_BE_GREATER_THAN_OR_EQUAL_TO_ZERO
        response_dict = {
            "response": OFFSET_SHOULD_BE_GREATER_THAN_OR_EQUAL_TO_ZERO[0],
            "http_status_code": 400,
            "res_status":
                OFFSET_SHOULD_BE_GREATER_THAN_OR_EQUAL_TO_ZERO[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict
        )

    def get_stage_assignee_details_response(
            self, user_details_dtos: List[UserDetailsDTO]
    ) -> response.HttpResponse:

        user_details_dicts = []
        for user_details_dto in user_details_dtos:
            user_details_dict = {
                'id': user_details_dto.user_id,
                'name': user_details_dto.user_name,
                'profile_pic_url': user_details_dto.profile_pic_url
            }
            user_details_dicts.append(user_details_dict)

        return self.prepare_200_success_response(
            response_dict=user_details_dicts)

    def raise_invalid_stage_id_exception(
            self, err: InvalidStageId) -> response.HttpResponse:
        from ib_tasks.constants.exception_messages import \
            INVALID_STAGE_ID
        response_dict = {
            "response": INVALID_STAGE_ID[0],
            "http_status_code": 404,
            "res_status": INVALID_STAGE_ID[1]
        }

        return self.prepare_404_not_found_response(
            response_dict=response_dict
        )
