from typing import List

from ib_tasks.exceptions.action_custom_exceptions import InvalidActionException
from ib_tasks.exceptions.permission_custom_exceptions import UserActionPermissionDenied
from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskException
from ib_tasks.interactors\
    .call_action_logic_function_and_update_task_status_variables_interactor \
    import CallActionLogicFunctionAndUpdateTaskStatusVariablesInteractor
from ib_tasks.adapters.dtos import ColumnFieldDTO, ColumnStageDTO
from ib_tasks.interactors.get_field_details import GetFieldsDetails
from ib_tasks.interactors.get_gofs_and_status_variables_to_task import \
    GetGroupOfFieldsAndStatusVariablesToTaskInteractor
from ib_tasks.interactors.get_user_permitted_stage_actions import GetUserPermittedStageActions
from ib_tasks.interactors.gofs_dtos import TaskGofAndStatusesDTO
from ib_tasks.interactors.presenter_interfaces.dtos import TaskCompleteDetailsDTO
from ib_tasks.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from ib_tasks.interactors.storage_interfaces.storage_interface import StorageInterface


class InvalidBoardIdException(Exception):

    def __init__(self, board_id: str):
        self.board_id = board_id


class UserActionOnTaskInteractor:

    def __init__(self, user_id: str, board_id: str,
                 task_id: int, action_id: int, storage: StorageInterface):
        self.user_id = user_id
        self.board_id = board_id
        self.task_id = task_id
        self.action_id = action_id
        self.storage = storage

    def user_action_on_task(self, presenter: PresenterInterface):

        try:
            task_complete_details_dto = self._user_action_on_task()
        except InvalidTaskException as err:
            presenter.raise_exception_for_invalid_task(error_obj=err)
            return
        except InvalidBoardIdException as err:
            presenter.raise_exception_for_invalid_board(error_obj=err)
            return
        except InvalidActionException as err:
            presenter.raise_exception_for_invalid_action(error_obj=err)
            return
        except UserActionPermissionDenied as err:
            presenter.raise_exception_for_user_action_permission_denied(
                error_obj=err
            )
            return
        return presenter.get_response_for_user_action_on_task(
            task_complete_details_dto=task_complete_details_dto
        )

    def _user_action_on_task(self):

        self._validations_for_task_action()
        task_dto = self._get_task_dto()
        stage_ids = self._call_logic_and_update_status_variables_and_get_stage_ids(
            task_dto=task_dto
        )
        task_boards_details = self._get_task_boards_details(stage_ids)
        column_fields_dtos = task_boards_details.columns_fields_dtos
        column_stage_dtos = task_boards_details.column_stage_dtos
        stage_ids = self._get_stage_ids(column_stage_dtos)
        actions_dto = self._get_user_permitted_actions(stage_ids=stage_ids)
        field_ids = self._get_field_ids(column_fields_dtos=column_fields_dtos)
        field_dtos = self._get_fields_dtos(field_ids=field_ids)
        return TaskCompleteDetailsDTO(
            task_id=self.task_id,
            task_boards_details=task_boards_details,
            actions_dto=actions_dto,
            field_dtos=field_dtos
        )

    def _get_fields_dtos(self, field_ids: List[str]):
        get_fields_obj = GetFieldsDetails(user_id=self.user_id,
                                          field_ids=field_ids,
                                          storage=self.storage)
        fields_dto = get_fields_obj.get_fields_details()
        return fields_dto

    def _get_user_permitted_actions(self, stage_ids: List[str]):

        stage_action_obj = GetUserPermittedStageActions(
            storage=self.storage, user_id=self.user_id, stage_ids=stage_ids
        )
        actions_dto = stage_action_obj.get_user_permitted_stage_actions()
        return actions_dto

    def _get_task_boards_details(self, stage_ids: List[str]):

        from ib_tasks.adapters.service_adapter import ServiceAdapter
        adapter = ServiceAdapter()
        task_boards_details = adapter.boards_service \
            .get_display_boards_and_column_details(
                user_id=self.user_id, board_id=self.board_id,
                stage_ids=stage_ids
            )
        return task_boards_details

    def _call_logic_and_update_status_variables_and_get_stage_ids(
            self, task_dto: TaskGofAndStatusesDTO):
        update_status_variable_obj = \
            CallActionLogicFunctionAndUpdateTaskStatusVariablesInteractor(
                action_id=self.action_id, storage=self.storage
            )
        stage_ids = update_status_variable_obj \
            .call_action_logic_function_and_update_task_status_variables(
                task_dto=task_dto
            )
        return stage_ids

    def _get_task_dto(self):

        gof_and_status_obj = \
            GetGroupOfFieldsAndStatusVariablesToTaskInteractor(
                storage=self.storage
            )
        task_dto = gof_and_status_obj \
            .get_gofs_and_status_variables_to_task(task_id=self.task_id)
        return task_dto

    @staticmethod
    def _get_field_ids(column_fields_dtos: List[ColumnFieldDTO]):

        field_ids = []
        for column_field_dto in column_fields_dtos:
            for field_id in column_field_dto.field_ids:
                field_ids.append(field_id)
        return field_ids

    @staticmethod
    def _get_stage_ids(column_stage_dtos: List[ColumnStageDTO]):

        return [
            column_stage_dto.stage_id
            for column_stage_dto in column_stage_dtos
        ]

    def _validations_for_task_action(self):

        from ib_tasks.adapters.service_adapter import ServiceAdapter
        adapter = ServiceAdapter()
        self._validate_task_id()
        self._validate_board_id()
        valid_action = self.storage.validate_action(action_id=self.action_id)
        is_invalid_action = not valid_action
        if is_invalid_action:
            raise InvalidActionException(action_id=self.action_id)
        action_roles = self.storage.get_action_roles(action_id=self.action_id)
        self._validate_user_permission_to_user(
            self.user_id, action_roles, self.action_id
        )

    def _validate_task_id(self):

        task_id = self.task_id
        valid_task = self.storage.validate_task_id(task_id=task_id)
        is_invalid_task = not valid_task
        if is_invalid_task:
            raise InvalidTaskException(task_id=task_id)

    def _validate_board_id(self):

        from ib_tasks.adapters.service_adapter import ServiceAdapter
        adapter = ServiceAdapter()
        board_id = self.board_id
        valid_board = \
            adapter.boards_service.validate_board_id(board_id=board_id)
        is_invalid_board = not valid_board
        if is_invalid_board:
            raise InvalidBoardIdException(board_id=board_id)

    @staticmethod
    def _validate_user_permission_to_user(user_id: str,
                                          action_roles: List[str],
                                          action_id: int):

        from ib_tasks.interactors.user_role_validation_interactor \
            import UserRoleValidationInteractor
        interactor = UserRoleValidationInteractor()
        permit = interactor.does_user_has_required_permission(
            user_id=user_id, role_ids=action_roles
        )
        is_permission_denied = not permit
        if is_permission_denied:
            raise UserActionPermissionDenied(action_id=action_id)
