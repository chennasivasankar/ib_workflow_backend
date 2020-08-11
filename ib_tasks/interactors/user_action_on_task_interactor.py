from typing import List, Optional
from ib_tasks.exceptions.action_custom_exceptions import \
    InvalidKeyError, InvalidCustomLogicException
from ib_tasks.exceptions.action_custom_exceptions import InvalidActionException
from ib_tasks.exceptions.permission_custom_exceptions import UserActionPermissionDenied, UserBoardPermissionDenied

from ib_tasks.exceptions.stage_custom_exceptions import DuplicateStageIds, \
    InvalidDbStageIdsListException, StageIdsWithInvalidPermissionForAssignee
from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskException
from ib_tasks.interactors\
    .call_action_logic_function_and_update_task_status_variables_interactor \
    import CallActionLogicFunctionAndUpdateTaskStatusVariablesInteractor
from ib_tasks.adapters.dtos import ColumnFieldDTO, ColumnStageDTO
from ib_tasks.interactors.get_field_details import GetFieldsDetails
from ib_tasks.interactors \
    .get_next_stages_random_assignees_of_a_task_interactor import \
    InvalidModulePathFound, InvalidMethodFound
from ib_tasks.interactors\
    .get_random_assignees_of_next_stages_and_update_in_db_interactor import \
    GetNextStageRandomAssigneesOfTaskAndUpdateInDbInteractor
from ib_tasks.interactors.get_user_permitted_stage_actions \
    import GetUserPermittedStageActions
from ib_tasks.interactors.gofs_dtos import FieldDisplayDTO
from ib_tasks.interactors.presenter_interfaces.dtos import TaskCompleteDetailsDTO
from ib_tasks.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from ib_tasks.interactors.storage_interfaces.action_storage_interface import \
    ActionStorageInterface
from ib_tasks.interactors.storage_interfaces.actions_dtos import ActionDetailsDTO, ActionDTO
from ib_tasks.interactors.storage_interfaces.create_or_update_task_storage_interface import \
    CreateOrUpdateTaskStorageInterface
from ib_tasks.interactors.storage_interfaces.fields_dtos import FieldDetailsDTO
from ib_tasks.interactors.storage_interfaces.fields_storage_interface import FieldsStorageInterface
from ib_tasks.interactors.storage_interfaces.get_task_dtos import TaskDetailsDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import GetTaskStageCompleteDetailsDTO
from ib_tasks.interactors.storage_interfaces.stages_storage_interface import StageStorageInterface
from ib_tasks.interactors.storage_interfaces.storage_interface import StorageInterface
from ib_tasks.exceptions.action_custom_exceptions \
    import InvalidPresentStageAction
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface


class InvalidBoardIdException(Exception):

    def __init__(self, board_id: str):
        self.board_id = board_id


class UserActionOnTaskInteractor:

    def __init__(self, user_id: str, task_id: int,
                 action_id: int, storage: StorageInterface,
                 gof_storage: CreateOrUpdateTaskStorageInterface,
                 board_id: Optional[str],
                 field_storage: FieldsStorageInterface,
                 stage_storage: StageStorageInterface,
                 task_storage: TaskStorageInterface,
                 action_storage: ActionStorageInterface
                 ):
        self.user_id = user_id
        self.board_id = board_id
        self.task_id = task_id
        self.action_id = action_id
        self.storage = storage
        self.gof_storage = gof_storage
        self.field_storage = field_storage
        self.stage_storage = stage_storage
        self.task_storage = task_storage
        self.action_storage = action_storage

    def user_action_on_task_wrapper(self, presenter: PresenterInterface):

        try:
            task_complete_details_dto = self.user_action_on_task()
        except InvalidTaskException as err:
            return presenter.raise_exception_for_invalid_task(error_obj=err)
        except InvalidBoardIdException as err:
            return presenter.raise_exception_for_invalid_board(error_obj=err)
        except InvalidActionException as err:
            return presenter.raise_exception_for_invalid_action(error_obj=err)
        except UserActionPermissionDenied as err:
            return presenter.raise_exception_for_user_action_permission_denied(
                error_obj=err
            )
        except InvalidPresentStageAction as err:
            return presenter.raise_exception_for_invalid_present_actions(
                error_obj=err
            )
        except UserBoardPermissionDenied as err:
            return presenter.raise_exception_for_user_board_permission_denied(
                error_obj=err
            )
        except InvalidKeyError:
            return presenter.raise_invalid_key_error()
        except InvalidCustomLogicException:
            return presenter.raise_invalid_custom_logic_function_exception()
        except InvalidModulePathFound as exception:
            return presenter.raise_invalid_path_not_found_exception(
                path_name=exception.path_name)
        except InvalidMethodFound as exception:
            return presenter.raise_invalid_method_not_found_exception(
                method_name=exception.method_name)
        except DuplicateStageIds as exception:
            return presenter.raise_duplicate_stage_ids_not_valid(
                duplicate_stage_ids=exception.duplicate_stage_ids)
        except InvalidDbStageIdsListException as exception:
            return presenter.raise_invalid_stage_ids_exception(
                invalid_stage_ids=exception.invalid_stage_ids)
        except StageIdsWithInvalidPermissionForAssignee as exception:
            return presenter. \
                raise_stage_ids_with_invalid_permission_for_assignee_exception(
                    invalid_stage_ids=exception.invalid_stage_ids)
        return presenter.get_response_for_user_action_on_task(
            task_complete_details_dto=task_complete_details_dto
        )

    def user_action_on_task(self):
        # self._validations_for_task_action()
        task_dto = self._get_task_dto()
        self._call_logic_and_update_status_variables_and_get_stage_ids(
            task_dto=task_dto
        )

        stage_ids = self._get_task_stage_display_satifsied_stage_ids()
        self._update_task_stages(stage_ids=stage_ids)
        if self.board_id:
            task_boards_details = self._get_task_boards_details(stage_ids)
        else:
            task_boards_details = None
        actions_dto, fields_dto = \
            self._get_task_fields_and_actions_dto(stage_ids)
        set_stage_assignees_interactor = \
            GetNextStageRandomAssigneesOfTaskAndUpdateInDbInteractor(
                storage=self.storage, stage_storage=self.stage_storage,
                task_storage=self.task_storage,
                action_storage=self.action_storage
            )
        set_stage_assignees_interactor \
            .get_random_assignees_of_next_stages_and_update_in_db(
                task_id=self.task_id, action_id=self.action_id
            )
        return TaskCompleteDetailsDTO(
            task_id=self.task_id,
            task_boards_details=task_boards_details,
            actions_dto=actions_dto,
            field_dtos=fields_dto
        )

    def _get_task_fields_and_actions_dto(self, stage_ids: List[str]):

        from ib_tasks.interactors.task_dtos import GetTaskDetailsDTO
        task_stage_dtos = [
            GetTaskDetailsDTO(
                task_id=self.task_id,
                stage_id=stage_id
            )
            for stage_id in stage_ids
        ]
        from ib_tasks.interactors.get_task_fields_and_actions \
            import GetTaskFieldsAndActionsInteractor
        interactor = GetTaskFieldsAndActionsInteractor(
            field_storage=self.field_storage,
            task_storage=self.task_storage,
            action_storage=self.action_storage,
            stage_storage=self.stage_storage
        )
        from ib_boards.constants.enum import ViewType
        task_stage_details_dtos = interactor.get_task_fields_and_action(
            task_dtos=task_stage_dtos, user_id=self.user_id,
            view_type=ViewType.KANBAN.value
        )
        actions_dto, fields_dto = self._get_field_dtos_and_actions_dtos(
            task_stage_details_dtos=task_stage_details_dtos)
        return actions_dto, fields_dto

    def _get_field_dtos_and_actions_dtos(
            self, task_stage_details_dtos: List[GetTaskStageCompleteDetailsDTO]):

        actions_dto = []
        for task_stage_details_dto in task_stage_details_dtos:
            for action_dto in task_stage_details_dto.action_dtos:
                actions_dto.append(action_dto)
        actions_dto = self._get_actions_dto(actions_dto)

        fields_dto = []
        for task_stage_details_dto in task_stage_details_dtos:
            stage_id = task_stage_details_dto.stage_id
            for field_dto in task_stage_details_dto.field_dtos:
                fields_dto.append(self._get_field_dto(field_dto, stage_id))
        return actions_dto, fields_dto

    @staticmethod
    def _get_field_dto(field_dto: FieldDetailsDTO, stage_id: str):

        return FieldDisplayDTO(
            field_id=str(field_dto.field_id),
            field_type=field_dto.field_type,
            stage_id=stage_id,
            key=field_dto.key,
            value=field_dto.value
        )

    @staticmethod
    def _get_actions_dto(actions_dto: List[ActionDetailsDTO]):

        return [
            ActionDTO(
                action_id=action_dto.action_id,
                name=action_dto.name,
                stage_id=action_dto.stage_id,
                button_text=action_dto.button_text,
                button_color=action_dto.button_color
            )
            for action_dto in actions_dto
        ]

    def _update_task_stages(self, stage_ids: List[str]):

        self.storage.update_task_stages(
            task_id=self.task_id, stage_ids=stage_ids
        )

    def _get_task_stage_display_satifsied_stage_ids(self):
        from ib_tasks.interactors.get_task_stage_logic_satisfied_stages \
            import GetTaskStageLogicSatisfiedStages
        interactor = GetTaskStageLogicSatisfiedStages(
            task_id=self.task_id, storage=self.storage
        )
        stage_ids = interactor.get_task_stage_logic_satisfied_stages()
        return stage_ids

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
        return adapter.boards_service \
            .get_display_boards_and_column_details(
                user_id=self.user_id, board_id=self.board_id,
                stage_ids=stage_ids
            )

    def _call_logic_and_update_status_variables_and_get_stage_ids(
            self, task_dto: TaskDetailsDTO):
        update_status_variable_obj = \
            CallActionLogicFunctionAndUpdateTaskStatusVariablesInteractor(
                action_id=self.action_id, storage=self.storage, task_id=self.task_id
            )
        stage_ids = update_status_variable_obj \
            .call_action_logic_function_and_update_task_status_variables(
                task_dto=task_dto
            )
        return stage_ids

    def _get_task_dto(self):

        from ib_tasks.interactors.get_task_base_interactor \
            import GetTaskBaseInteractor
        gof_and_status_obj = \
            GetTaskBaseInteractor(
                storage=self.gof_storage
            )
        task_dto = gof_and_status_obj \
            .get_task(task_id=self.task_id)
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

        self._validate_task_id()
        if self.board_id:
            self._validate_board_id()
        valid_action = self.storage.validate_action(action_id=self.action_id)
        is_invalid_action = not valid_action
        if is_invalid_action:
            raise InvalidActionException(action_id=self.action_id)
        action_roles = self.storage.get_action_roles(action_id=self.action_id)
        self._validate_present_task_stage_actions()
        self._validate_user_permission_to_user(
            self.user_id, action_roles, self.action_id
        )

    def _validate_present_task_stage_actions(self):

        action_id = self.action_id
        action_ids = self.storage.get_task_present_stage_actions(
            task_id=self.task_id
        )
        is_not_present_stage_actions = int(action_id) not in action_ids
        if is_not_present_stage_actions:
            raise InvalidPresentStageAction(action_id=action_id)

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
