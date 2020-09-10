import datetime

from ib_tasks.adapters.service_adapter import get_service_adapter
from ib_tasks.exceptions.stage_custom_exceptions import InvalidStageIdException
from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskDisplayId, \
    UserIsNotAssigneeToTask
from ib_tasks.interactors.mixins.get_task_id_for_task_display_id_mixin import \
    GetTaskIdForTaskDisplayIdMixin
from ib_tasks.interactors.presenter_interfaces.get_task_rps_presenter_interface import \
    GetTaskRpsPresenterInterface
from ib_tasks.interactors.storage_interfaces.storage_interface import \
    StorageInterface
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface
from ib_tasks.interactors.task_dtos import GetTaskRPsParametersDTO


class DueDateIsNotAddedException(Exception):
    pass


class GetTaskRPsInteractor(GetTaskIdForTaskDisplayIdMixin):
    def __init__(self, storage: StorageInterface,
                 task_storage: TaskStorageInterface):
        self.storage = storage
        self.task_storage = task_storage

    def get_task_rps_wrapper(self, presenter: GetTaskRpsPresenterInterface,
                             parameters: GetTaskRPsParametersDTO):
        try:
            rps_dtos = self.get_task_rps(parameters)
        except InvalidTaskDisplayId as err:
            return presenter.response_for_invalid_task_id(err)
        except UserIsNotAssigneeToTask:
            return presenter.response_for_user_is_not_assignee_for_task()
        except InvalidStageIdException:
            return presenter.response_for_invalid_stage_id()
        except DueDateIsNotAddedException:
            return presenter.response_for_due_date_does_not_exist_to_task()
        return presenter.response_for_get_rps_details(rps_dtos)

    def get_task_rps(self, paramters: GetTaskRPsParametersDTO):
        task_display_id = paramters.task_id
        user_id = paramters.user_id
        stage_id = paramters.stage_id
        task_id = self.get_task_id_for_task_display_id(task_display_id)

        self._validate_stage_id(stage_id)
        self._validate_if_task_is_assigned_to_user(
            task_id=task_id, user_id=user_id, stage_id=stage_id)
        rps_details_dtos = self._get_rps_details(paramters, task_id)
        return rps_details_dtos

    def _get_rps_details(self, parameters: GetTaskRPsParametersDTO,
                         task_id: int):
        user_id = parameters.user_id

        stage_id = parameters.stage_id
        due_date = self.task_storage.get_task_due_datetime(
            task_id)

        if due_date is None:
            raise DueDateIsNotAddedException

        service_adapter = get_service_adapter()

        if due_date > datetime.datetime.now():
            rp_ids = self.storage.get_rp_ids(task_id, stage_id)

            if rp_ids:
                return service_adapter.auth_service.get_user_details(rp_ids)
            return []

        return self._get_rp_details_if_due_date_is_missed(
            stage_id, due_date, task_id, user_id)

    def _get_rp_details_if_due_date_is_missed(self, stage_id: int, due_date,
                                              task_id: int, user_id: str):
        service_adapter = get_service_adapter()

        user_team_id = self.task_storage.get_team_id(stage_id, task_id)
        rp_added_datetime = self.storage.get_latest_rp_added_datetime(task_id, stage_id)
        if rp_added_datetime and rp_added_datetime < due_date:
            self.add_rp_when_due_date_is_missed(stage_id, task_id, user_id, user_team_id)
        elif rp_added_datetime is None:
            self.add_rp_when_due_date_is_missed(stage_id, task_id, user_id, user_team_id)

        rp_ids = self.storage.get_rp_ids(task_id, stage_id)
        if not rp_ids:
            return []

        rp_details_dtos = service_adapter.auth_service.get_user_details(rp_ids)
        rp_dict = {}
        for rp_dto in rp_details_dtos:
            rp_dict[rp_dto.user_id] = rp_dto
        rp_dtos = [
                rp_dict[rp_id]
                for rp_id in rp_ids
        ]

        return rp_dtos

    def add_rp_when_due_date_is_missed(self, stage_id, task_id, user_id, user_team_id):

        service_adapter = get_service_adapter()

        assignee_id = user_id
        rp_id = self.storage.get_latest_rp_id_if_exists(task_id, stage_id)
        if rp_id:
            assignee_id = rp_id
        superior_id = service_adapter.auth_service.get_immediate_superior_user_id(
            user_id=assignee_id, team_id=user_team_id)
        if superior_id:
            self.storage.add_superior_to_db(
                superior_id=superior_id,
                task_id=task_id, stage_id=stage_id)

    def _validate_stage_id(self, stage_id: int):
        is_valid = self.storage.validate_stage_id(stage_id)
        if not is_valid:
            raise InvalidStageIdException

    def _validate_if_task_is_assigned_to_user(self, task_id: int, user_id: str,
                                              stage_id: int):
        # is_assigned = self.storage.validate_if_task_is_assigned_to_user_in_given_stage(
        #     task_id, user_id, stage_id
        # )
        # is_not_assigned = not is_assigned
        # if is_not_assigned:
        #     raise UserIsNotAssigneeToTask
        pass
