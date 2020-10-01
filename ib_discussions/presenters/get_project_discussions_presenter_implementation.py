from typing import List

from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_discussions.constants.enum import StatusCode
from ib_discussions.interactors.presenter_interfaces.dtos import \
    DiscussionsWithUsersAndDiscussionCountDTO, DiscussionIdWithEditableStatusDTO
from ib_discussions.interactors.presenter_interfaces.presenter_interface import \
    GetProjectDiscussionsPresenterInterface
from ib_discussions.interactors.storage_interfaces.dtos import \
    DiscussionIdWithCommentsCountDTO

INVALID_OFFSET = (
    "Please send the valid offset value",
    "INVALID_OFFSET"
)

INVALID_LIMIT = (
    "Please send the valid limit value",
    "INVALID_LIMIT"
)

INVALID_USER_ID = (
    "Please send the valid user id",
    "INVALID_USER_ID"
)

DISCUSSION_SET_NOT_FOUND = (
    "There is no discussion for given entity id and entity type",
    "DISCUSSION_SET_NOT_FOUND"
)

INVALID_PROJECT_ID = (
    "Please send valid project id",
    "INVALID_PROJECT_ID"
)

INVALID_USER_FOR_PROJECT = (
    "Please send valid user for project",
    "INVALID_USER_FOR_PROJECT"
)


class GetProjectDiscussionsPresenterImplementation(
    GetProjectDiscussionsPresenterInterface, HTTPResponseMixin
):

    def response_for_invalid_offset(self):
        response_dict = {
            "response": INVALID_OFFSET[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_OFFSET[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict
        )

    def response_for_invalid_limit(self):
        response_dict = {
            "response": INVALID_LIMIT[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_LIMIT[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict
        )

    def response_for_invalid_user_id(self):
        response_dict = {
            "response": INVALID_USER_ID[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_USER_ID[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict
        )

    def response_for_invalid_project_id(self):
        response_dict = {
            "response": INVALID_PROJECT_ID[0],
            "http_status_code": StatusCode.NOT_FOUND.value,
            "res_status": INVALID_PROJECT_ID[1]
        }
        return self.prepare_404_not_found_response(response_dict=response_dict)

    def response_for_invalid_user_for_project(self):
        response_dict = {
            "response": INVALID_USER_FOR_PROJECT[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_USER_FOR_PROJECT[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict
        )

    def prepare_response_for_project_discussions_details_dto(
            self,
            discussions_with_users_and_discussion_count_dto: DiscussionsWithUsersAndDiscussionCountDTO,
            discussion_id_with_editable_status_dtos: List[
                DiscussionIdWithEditableStatusDTO],
            discussion_id_with_comments_count_dtos: List[
                DiscussionIdWithCommentsCountDTO]
    ):
        from ib_discussions.presenters.get_discussion_presenter_implementation import \
            GetDiscussionPresenterImplementation
        presenter = GetDiscussionPresenterImplementation()
        response = presenter.prepare_response_for_discussions_details_dto(
            discussion_id_with_comments_count_dtos=discussion_id_with_comments_count_dtos,
            discussion_id_with_editable_status_dtos=discussion_id_with_editable_status_dtos,
            discussions_with_users_and_discussion_count_dto=discussions_with_users_and_discussion_count_dto
        )
        return response
