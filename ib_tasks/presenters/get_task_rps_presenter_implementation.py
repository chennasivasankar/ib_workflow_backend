from typing import List

from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_tasks.adapters.dtos import UserDetailsDTO
from ib_tasks.constants.exception_messages import USER_IS_NOT_ASSIGNED_TO_TASK
from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskDisplayId
from ib_tasks.interactors.presenter_interfaces.get_task_rps_presenter_interface \
    import GetTaskRpsPresenterInterface

INVALID_STAGE_ID = ("please give a valid stage id",
                    "INVALID_STAGE_ID")


class GetTaskRpsPresenterImplementation(GetTaskRpsPresenterInterface,
                                        HTTPResponseMixin):
    def response_for_invalid_task_id(self, err: InvalidTaskDisplayId):
        from ib_tasks.constants.exception_messages import \
            INVALID_TASK_DISPLAY_ID
        message = INVALID_TASK_DISPLAY_ID[0].format(err.task_display_id)
        data = {
            "response": message,
            "http_status_code": 404,
            "res_status": INVALID_TASK_DISPLAY_ID[1]
        }
        return self.prepare_404_not_found_response(data)

    def response_for_user_is_not_assignee_for_task(self):
        response_message = USER_IS_NOT_ASSIGNED_TO_TASK[0]
        data = {
            "response": response_message,
            "http_status_code": 403,
            "res_status": USER_IS_NOT_ASSIGNED_TO_TASK[1]
        }
        response_object = self.prepare_403_forbidden_response(
            response_dict=data
        )
        return response_object

    def response_for_invalid_stage_id(self):
        response_message = INVALID_STAGE_ID[0]
        data = {
            "response": response_message,
            "http_status_code": 404,
            "res_status": INVALID_STAGE_ID[1]
        }
        response_object = self.prepare_404_not_found_response(
            response_dict=data
        )
        return response_object

    def response_for_get_rps_details(self, rps_dtos: List[UserDetailsDTO]):
        list_of_rp_details = [self._convert_rp_details_dto_to_dict(rp_dto)
                              for rp_dto in rps_dtos]

        response_object = self.prepare_200_success_response(
            response_dict=list_of_rp_details
        )
        return response_object

    @staticmethod
    def _convert_rp_details_dto_to_dict(rp_dto: UserDetailsDTO):
        return {
            "user_id": rp_dto.user_id,
            "name": rp_dto.user_name,
            "profile_pic_url": rp_dto.profile_pic_url
        }
