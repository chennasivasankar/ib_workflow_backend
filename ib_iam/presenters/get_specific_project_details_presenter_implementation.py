from typing import List

from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_iam.constants.enums import StatusCode
from ib_iam.interactors.presenter_interfaces.get_specific_project_details_presenter_interface import \
    GetSpecificProjectDetailsPresenterInterface
from ib_iam.interactors.storage_interfaces.dtos import BasicUserDetailsDTO, \
    UserRoleDTO

INVALID_PROJECT_ID = (
    "Please send valid project id",
    "INVALID_PROJECT_ID"
)


class GetSpecificProjectDetailsPresenterImplementation(
    GetSpecificProjectDetailsPresenterInterface, HTTPResponseMixin
):

    def prepare_success_response_for_get_specific_project_details(
            self, basic_user_details_dtos: List[BasicUserDetailsDTO],
            user_role_dtos: List[UserRoleDTO]
    ):
        user_id_wise_user_roles_dict = \
            self._prepare_user_id_wise_user_roles_dict(
                user_role_dtos=user_role_dtos
            )
        user_details_with_roles_details_list = [
            {
                "user_id": str(basic_user_details_dto.user_id),
                "name": basic_user_details_dto.name,
                "roles": user_id_wise_user_roles_dict[
                    str(basic_user_details_dto.user_id)]
            }
            for basic_user_details_dto in basic_user_details_dtos
        ]
        response_dict = {"users": user_details_with_roles_details_list}
        return self.prepare_200_success_response(response_dict=response_dict)

    def _prepare_user_id_wise_user_roles_dict(
            self, user_role_dtos: List[UserRoleDTO]
    ):
        from collections import defaultdict
        user_roles_dict = defaultdict(list)
        for user_role_dto in user_role_dtos:
            user_id = user_role_dto.user_id
            role_dict = self._prepare_role_dict(user_role_dto)
            user_roles_dict[str(user_id)].append(role_dict)
        return user_roles_dict

    @staticmethod
    def _prepare_role_dict(user_role_dto: UserRoleDTO):
        role_dict = {
            "role_id": user_role_dto.role_id,
            "role_name": user_role_dto.name
        }
        return role_dict

    # TODO: write test case for this
    def response_for_invalid_project_id(self):
        response_dict = {
            "response": INVALID_PROJECT_ID[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_PROJECT_ID[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict)
