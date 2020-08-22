from typing import List

from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_tasks.adapters.dtos import UserIdWIthTeamDetailsDTOs, TeamDetailsDTO
from ib_tasks.interactors.presenter_interfaces \
    .get_next_stages_random_assignees_of_a_task_presenter import \
    GetNextStagesRandomAssigneesOfATaskPresenterInterface
from ib_tasks.interactors.stages_dtos import StageWithUserDetailsDTO, \
    StageWithUserDetailsAndTeamDetailsDTO


class GetNextStagesRandomAssigneesOfATaskPresenterImpl(
    GetNextStagesRandomAssigneesOfATaskPresenterInterface, HTTPResponseMixin
):
    def raise_invalid_task_display_id(self, err):
        from ib_tasks.constants.exception_messages import \
            INVALID_TASK_DISPLAY_ID
        message = INVALID_TASK_DISPLAY_ID[0].format(err.task_display_id)
        data = {
            "response": message,
            "http_status_code": 400,
            "res_status": INVALID_TASK_DISPLAY_ID[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_invalid_task_id_exception(self, task_id: int):
        from ib_tasks.constants.exception_messages import INVALID_TASK_ID
        data = {
            "response": INVALID_TASK_ID[0].format(task_id),
            "http_status_code": 404,
            "res_status": INVALID_TASK_ID[1]
        }
        return self.prepare_404_not_found_response(data)

    def raise_exception_for_invalid_action(self, action_id: int):
        from ib_tasks.constants.exception_messages import INVALID_ACTION_ID
        response_message = INVALID_ACTION_ID[0].format(action_id)
        data = {
            "response": response_message,
            "http_status_code": 404,
            "res_status": INVALID_ACTION_ID[1]
        }
        return self.prepare_404_not_found_response(data)

    def raise_invalid_key_error(self):
        from ib_tasks.constants.exception_messages import \
            INVALID_KEY_ERROR
        data = {
            "response": INVALID_KEY_ERROR[0],
            "http_status_code": 400,
            "res_status": INVALID_KEY_ERROR[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_invalid_custom_logic_function_exception(self):
        from ib_tasks.constants.exception_messages import \
            INVALID_CUSTOM_LOGIC
        data = {
            "response": INVALID_CUSTOM_LOGIC[0],
            "http_status_code": 400,
            "res_status": INVALID_CUSTOM_LOGIC[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_invalid_path_not_found_exception(self, path_name):
        from ib_tasks.constants.exception_messages import \
            PATH_NOT_FOUND
        data = {
            "response": PATH_NOT_FOUND[0],
            "http_status_code": 400,
            "res_status": PATH_NOT_FOUND[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_invalid_method_not_found_exception(self, method_name):
        from ib_tasks.constants.exception_messages import \
            METHOD_NOT_FOUND
        data = {
            "response": METHOD_NOT_FOUND[0],
            "http_status_code": 400,
            "res_status": METHOD_NOT_FOUND[1]
        }
        return self.prepare_400_bad_request_response(data)

    def get_next_stages_random_assignees_of_a_task_response(
            self,
            stage_with_user_details_and_team_details_dto:
            StageWithUserDetailsAndTeamDetailsDTO):
        user_with_team_details_dtos = \
            stage_with_user_details_and_team_details_dto.\
                user_with_team_details_dtos
        all_stage_assignees_details = []
        for each_stage_with_user_details_dto in \
                stage_with_user_details_and_team_details_dto.\
                        stages_with_user_details_dtos:
            assignee_details_dto = each_stage_with_user_details_dto.\
                assignee_details_dto
            assignee_details_dto_dict = None
            if assignee_details_dto:
                assignee_id = assignee_details_dto.assignee_id
                team_details_dtos = self._get_team_info_of_user_id(
                    assignee_id, user_with_team_details_dtos)
                team_info = [{"team_id": team_details_dto.team_id,
                              "team_name": team_details_dto.name} for
                             team_details_dto in team_details_dtos]
                assignee_details_dto_dict = {
                    "assignee_id": assignee_id,
                    "name": assignee_details_dto.name,
                    "profile_pic_url": assignee_details_dto.
                        profile_pic_url,
                    "team_info": team_info}

            stage_assignees_details = {
                "stage_id": each_stage_with_user_details_dto.db_stage_id,
                "stage_display_name": each_stage_with_user_details_dto.
                    stage_display_name,
                "assignee": assignee_details_dto_dict}
            all_stage_assignees_details.append(stage_assignees_details)

        response_dict = {"stage_assignees": all_stage_assignees_details}
        response_object = self.prepare_200_success_response(
            response_dict=response_dict
        )
        return response_object

    @staticmethod
    def _get_team_info_of_user_id(assignee_id: str,
                                  user_with_team_details_dtos:
                                  List[UserIdWIthTeamDetailsDTOs]) -> List[
        TeamDetailsDTO]:

        for user_with_team_details_dto in user_with_team_details_dtos:
            if assignee_id == user_with_team_details_dto.user_id:
                return user_with_team_details_dto.team_details
