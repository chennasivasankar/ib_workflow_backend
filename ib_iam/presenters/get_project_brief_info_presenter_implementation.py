from typing import List

from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_iam.constants.enums import StatusCode
from ib_iam.interactors.presenter_interfaces.get_project_brief_info_presenter_interface import \
    GetProjectBriefInfoPresenterInterface
from ib_iam.interactors.storage_interfaces.dtos import ProjectWithDisplayIdDTO

USER_DOES_NOT_EXIST = (
    "Please access with valid user, to get access for project",
    "USER_DOES_NOT_EXIST"
)


class GetProjectBriefInfoPresenterImplementation(
    GetProjectBriefInfoPresenterInterface, HTTPResponseMixin
):

    def response_for_user_does_not_exist(self):
        response_dict = {
            "response": USER_DOES_NOT_EXIST[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": USER_DOES_NOT_EXIST[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict
        )

    def success_response_for_get_project_brief_info(
            self, project_dtos: List[ProjectWithDisplayIdDTO]
    ):
        project_list = [
            {
                "project_id": project_dto.project_id,
                "project_display_id": project_dto.display_id,
                "name": project_dto.name,
                "logo_url": project_dto.logo_url
            }
            for project_dto in project_dtos
        ]
        response_dict = {"projects": project_list}
        return self.prepare_200_success_response(response_dict=response_dict)
