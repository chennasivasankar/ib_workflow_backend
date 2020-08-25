from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskDisplayId
from ib_tasks.interactors.presenter_interfaces.get_task_rps_presenter_interface \
    import GetTaskRpsPresenterInterface


class GetTaskRpsPresenterImplementation(GetTaskRpsPresenterInterface):
    def response_for_invalid_task_id(self, err: InvalidTaskDisplayId):
        pass

    def response_for_user_is_not_assignee_for_task(self):
        pass

    def response_for_invalid_stage_id(self):
        pass

