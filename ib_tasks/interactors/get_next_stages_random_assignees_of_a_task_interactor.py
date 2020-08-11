from random import choice
from typing import List
from ib_tasks.adapters.dtos import UserDetailsDTO
from ib_tasks.constants.constants import EMPTY_STRING
from ib_tasks.exceptions.action_custom_exceptions import InvalidActionException
from ib_tasks.exceptions.custom_exceptions import InvalidModulePathFound, \
    InvalidMethodFound
from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskIdException

from ib_tasks.interactors.mixins.validation_mixin import ValidationMixin

from ib_tasks.interactors.stages_dtos import StageWithUserDetailsDTO
from ib_tasks.interactors.storage_interfaces.action_storage_interface import \
    ActionStorageInterface
from ib_tasks.interactors.storage_interfaces.stage_dtos import StageRoleDTO, \
    StageIdWithRoleIdsDTO, StageDetailsDTO, TaskStageHavingAssigneeIdDTO, \
    StageValueWithTaskIdsDTO
from ib_tasks.interactors.storage_interfaces.stages_storage_interface import \
    StageStorageInterface
from ib_tasks.exceptions.action_custom_exceptions \
    import InvalidKeyError
from ib_tasks.interactors.storage_interfaces.status_dtos import \
    StatusVariableDTO
from ib_tasks.interactors.storage_interfaces.storage_interface import \
    StorageInterface
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface
from ib_tasks.interactors.presenter_interfaces. \
    get_next_stages_random_assignees_of_a_task_presenter import \
    GetNextStagesRandomAssigneesOfATaskPresenterInterface


class GetNextStagesRandomAssigneesOfATaskInteractor(ValidationMixin):
    def __init__(self, storage: StorageInterface,
                 stage_storage: StageStorageInterface,
                 task_storage: TaskStorageInterface,
                 action_storage: ActionStorageInterface):
        self.stage_storage = stage_storage
        self.task_storage = task_storage
        self.action_storage = action_storage
        self.storage = storage

    def get_next_stages_random_assignees_of_a_task_wrapper(
            self, task_id: int, action_id: int,
            presenter: GetNextStagesRandomAssigneesOfATaskPresenterInterface):
        try:
            stage_with_user_details_dtos = \
                self.get_next_stages_random_assignees_of_a_task(
                    task_id=task_id, action_id=action_id)
            return presenter. \
                get_next_stages_random_assignees_of_a_task_response(
                stage_with_user_details_dtos)
        except InvalidTaskIdException as exception:
            return presenter.raise_invalid_task_id_exception(
                task_id=exception.task_id)
        except InvalidActionException as exception:
            return presenter.raise_exception_for_invalid_action(
                action_id=exception.action_id)
        except InvalidKeyError:
            return presenter.raise_invalid_key_error()
        except InvalidModulePathFound as exception:
            return presenter.raise_invalid_path_not_found_exception(
                path_name=exception.path_name)
        except InvalidMethodFound as exception:
            return presenter.raise_invalid_method_not_found_exception(
                method_name=exception.method_name)

    def get_next_stages_random_assignees_of_a_task(
            self, task_id: int,
            action_id: int) -> List[StageWithUserDetailsDTO]:
        self.validate_task_id(task_id=task_id)
        self.validate_action_id(action_id=action_id)
        status_variable_dtos = self. \
            get_status_variables_dtos_of_task_based_on_action(
            task_id=task_id, action_id=action_id)
        next_stage_ids_of_task = \
            self.get_next_stages_of_task(task_id=task_id, status_variable_dtos=
            status_variable_dtos)
        stage_detail_dtos = self.stage_storage. \
            get_stage_detail_dtos_given_stage_ids(next_stage_ids_of_task)
        db_stage_ids = self._get_db_stage_ids(stage_detail_dtos)
        stages_having_user_details_dtos = self. \
            _all_stages_assigned_with_random_user_details_dtos(
            db_stage_ids, stage_detail_dtos)
        return stages_having_user_details_dtos

    def _get_user_having_less_tasks_for_each_stage(self):
        task_id_with_max_stage_value_dtos = self.task_storage. \
            get_tasks_with_max_stage_value_dto()
        stage_values = [
            task_id_with_max_stage_value_dto.stage_value
            for task_id_with_max_stage_value_dto in
            task_id_with_max_stage_value_dtos
        ]
        task_ids_group_by_stage_value_dtos = \
            self._get_task_ids_group_by_stage_value_dtos(
                stage_values, task_id_with_max_stage_value_dtos
            )
        task_id_with_stage_details_dtos = self. \
            stage_storage. \
            get_task_id_with_stage_details_dtos_based_on_stage_value(
            stage_values=stage_values,
            task_ids_group_by_stage_value_dtos=
            task_ids_group_by_stage_value_dtos)

        stage_ids_of_tasks = [task_id_with_stage_details_dto.db_stage_id for
                              task_id_with_stage_details_dto in
                              task_id_with_stage_details_dtos]
        stage_ids_having_actions = self.action_storage.get_stage_ids_having_actions(
            db_stage_ids=stage_ids_of_tasks)

    @staticmethod
    def _get_task_ids_group_by_stage_value_dtos(
            stage_values: List[int], task_id_with_max_stage_value_dtos
    ) -> List[StageValueWithTaskIdsDTO]:
        task_ids_group_by_stage_value_dtos = []
        for each_value in stage_values:

            list_of_task_ids = []
            for each_task_id_with_max_stage_value_dto in \
                    task_id_with_max_stage_value_dtos:
                if each_task_id_with_max_stage_value_dto.stage_value == \
                        each_value:
                    list_of_task_ids.append(
                        each_task_id_with_max_stage_value_dto.task_id)
            each_stage_value_with_task_ids_dto = StageValueWithTaskIdsDTO(
                stage_value=each_value, task_ids=list_of_task_ids)
            task_ids_group_by_stage_value_dtos.append(
                each_stage_value_with_task_ids_dto)
        return task_ids_group_by_stage_value_dtos

    def _all_stages_assigned_with_random_user_details_dtos(
            self, db_stage_ids: List[int],
            stage_detail_dtos: List[StageDetailsDTO]) -> \
            List[StageWithUserDetailsDTO]:

        stage_with_random_user_details_dtos = self. \
            _get_stage_with_random_user_details_dtos(
            db_stage_ids=db_stage_ids,
            stage_detail_dtos=stage_detail_dtos)
        return stage_with_random_user_details_dtos

    def _get_stage_with_random_user_details_dtos(
            self, db_stage_ids: List[int],
            stage_detail_dtos: List[StageDetailsDTO]) -> List[
        StageWithUserDetailsDTO]:
        stage_role_dtos = \
            self.stage_storage.get_stage_role_dtos_given_db_stage_ids(
                db_stage_ids)
        role_ids_group_by_stage_id_dtos = \
            self._get_role_ids_group_by_stage_id_dtos(
                stage_ids=db_stage_ids,
                stage_role_dtos=stage_role_dtos)
        stage_with_random_user_details_dtos = self. \
            _get_random_permitted_user_details_dto_of_stage_id(
            role_ids_group_by_stage_id_dtos, stage_detail_dtos)
        return stage_with_random_user_details_dtos

    def get_status_variables_dtos_of_task_based_on_action(self, task_id: int,
                                                          action_id: int) -> \
            List[StatusVariableDTO]:
        from ib_tasks.interactors. \
            call_action_logic_function_and_get_status_variables_interactor \
            import CallActionLogicFunctionAndGetTaskStatusVariablesInteractor
        call_action_logic_function_interactor = \
            CallActionLogicFunctionAndGetTaskStatusVariablesInteractor(
                action_storage=self.action_storage,
                task_storage=self.task_storage,
                storage=self.storage)
        updated_status_variable_dtos = call_action_logic_function_interactor. \
            get_status_variables_dtos_of_task_based_on_action(
            task_id, action_id)
        return updated_status_variable_dtos

    def _get_random_permitted_user_details_dto_of_stage_id(
            self, role_ids_group_by_stage_id_dtos: List[StageIdWithRoleIdsDTO],
            stage_detail_dtos: List[StageDetailsDTO]
    ) -> List[StageWithUserDetailsDTO]:
        stage_with_user_details_dtos = []
        from ib_tasks.adapters.auth_service import AuthService
        auth_service_adapter = AuthService()
        for each_dto in role_ids_group_by_stage_id_dtos:
            permitted_user_details_dtos = auth_service_adapter. \
                get_permitted_user_details(role_ids=each_dto.role_ids)
            if not permitted_user_details_dtos:
                permitted_user_details_dtos = [UserDetailsDTO(
                    user_id=EMPTY_STRING,
                    user_name=EMPTY_STRING,
                    profile_pic_url=EMPTY_STRING)]

            random_permitted_user_detail_dto = choice(
                permitted_user_details_dtos)
            stage_with_user_details_dto = self._prepare_stage_with_user_details_dto(
                stage_detail_dtos=stage_detail_dtos,
                role_ids_group_by_stage_id_dto=each_dto,
                random_permitted_user_detail_dto=
                random_permitted_user_detail_dto)
            stage_with_user_details_dtos.append(stage_with_user_details_dto)
        return stage_with_user_details_dtos

    @staticmethod
    def _prepare_stage_with_user_details_dto(
            stage_detail_dtos: List[StageDetailsDTO],
            role_ids_group_by_stage_id_dto: StageIdWithRoleIdsDTO,
            random_permitted_user_detail_dto: UserDetailsDTO) -> \
            StageWithUserDetailsDTO:
        for each_stage_detail_dto in stage_detail_dtos:
            if each_stage_detail_dto.db_stage_id == \
                    role_ids_group_by_stage_id_dto.db_stage_id:
                name = each_stage_detail_dto.name

        stage_with_user_details_dto = StageWithUserDetailsDTO(
            db_stage_id=role_ids_group_by_stage_id_dto.db_stage_id,
            assignee_id=random_permitted_user_detail_dto.user_id,
            assignee_name=random_permitted_user_detail_dto.user_name,
            profile_pic_url=random_permitted_user_detail_dto.profile_pic_url,
            stage_display_name=name,
        )
        return stage_with_user_details_dto

    def _get_role_ids_group_by_stage_id_dtos(
            self, stage_ids: List[int], stage_role_dtos: List[StageRoleDTO]) \
            -> List[StageIdWithRoleIdsDTO]:
        role_ids_group_by_stage_id_dtos = []
        for each_stage_id in stage_ids:
            list_of_role_ids = []
            role_id = self._get_matched_role_id_from_stage_role_dtos(
                stage_role_dtos=stage_role_dtos, stage_id=each_stage_id)
            list_of_role_ids.append(role_id)
            each_stage_id_with_role_ids_dto = \
                StageIdWithRoleIdsDTO(db_stage_id=each_stage_id,
                                      role_ids=list_of_role_ids)
            role_ids_group_by_stage_id_dtos.append(
                each_stage_id_with_role_ids_dto)
        return role_ids_group_by_stage_id_dtos

    @staticmethod
    def _get_matched_role_id_from_stage_role_dtos(
            stage_role_dtos: List[StageRoleDTO], stage_id: int):
        for each_stage_role_dto in stage_role_dtos:
            if each_stage_role_dto.db_stage_id == stage_id:
                return each_stage_role_dto.role_id
        return None

    @staticmethod
    def _get_db_stage_ids(
            stage_detail_dtos: List[StageDetailsDTO]) -> List[int]:
        db_stage_ids = [
            each_stage_detail_dto.db_stage_id
            for each_stage_detail_dto in stage_detail_dtos
        ]
        return db_stage_ids

    def get_next_stages_of_task(self, task_id: int,
                                status_variable_dtos) -> List[str]:
        from ib_tasks.interactors. \
            get_task_stage_logic_satisfied_next_stages_given_status_vars import \
            GetTaskStageLogicSatisfiedNextStagesGivenStatusVarsInteractor
        get_task_stage_logic_satisfied_next_stages_interactor = \
            GetTaskStageLogicSatisfiedNextStagesGivenStatusVarsInteractor(
                storage=self.storage)
        next_stage_ids = get_task_stage_logic_satisfied_next_stages_interactor. \
            get_task_stage_logic_satisfied_next_stages(
            task_id=task_id, status_variable_dtos=status_variable_dtos)
        return next_stage_ids

    # If we dont want to override with random user when a stage is assigned
    # with user we can use this function instead of the
    # _all_stages_assigned_ with_random_user_details_dtos
    def _not_overriding_random_user_for_stages_having_assignees(
            self, db_stage_ids: List[int],
            stage_detail_dtos: List[StageDetailsDTO], task_id: int) -> \
            List[StageWithUserDetailsDTO]:
        task_stages_having_assignee_dtos = self.stage_storage. \
            get_stage_details_having_assignees_in_given_stage_ids(
            task_id, db_stage_ids)
        task_stage_ids_having_assignees = [
            each_task_stages_having_assignee_dto.db_stage_id
            for each_task_stages_having_assignee_dto in
            task_stages_having_assignee_dtos
        ]
        assignee_ids_assigned_to_stages = [
            each_task_stages_having_assignee_dto.assignee_id
            for each_task_stages_having_assignee_dto in
            task_stages_having_assignee_dtos
        ]
        task_stages_having_assignee_details_dtos = self. \
            _get_assignee_details_for_task_stages_having_assignees(
            assignee_ids_assigned_to_stages,
            task_stages_having_assignee_dtos)

        task_stage_ids_not_having_assignees = list(
            set(db_stage_ids) - set(task_stage_ids_having_assignees))
        stage_with_random_user_details_dtos = self. \
            _get_stage_with_random_user_details_dtos(
            db_stage_ids=
            task_stage_ids_not_having_assignees,
            stage_detail_dtos=stage_detail_dtos)

        all_stages_having_user_details_dtos = \
            task_stages_having_assignee_details_dtos + \
            stage_with_random_user_details_dtos
        return all_stages_having_user_details_dtos

    @staticmethod
    def _get_assignee_details_for_task_stages_having_assignees(
            assignee_ids_assigned_to_stages: List[str],
            task_stages_having_assignee_dtos:
            List[TaskStageHavingAssigneeIdDTO]) -> \
            List[StageWithUserDetailsDTO]:
        from ib_tasks.adapters.auth_service import AuthService
        auth_service_adapter = AuthService()
        user_details_dtos = auth_service_adapter.get_user_details(
            user_ids=assignee_ids_assigned_to_stages)
        task_stages_having_assignee_details_dtos = []
        for task_stage_with_assignee_dto in task_stages_having_assignee_dtos:
            for user_details_dto in user_details_dtos:
                if user_details_dto.user_id \
                        == task_stage_with_assignee_dto.assignee_id:
                    stage_with_user_details_dto = StageWithUserDetailsDTO(
                        db_stage_id=task_stage_with_assignee_dto.db_stage_id,
                        assignee_id=task_stage_with_assignee_dto.assignee_id,
                        assignee_name=user_details_dto.user_name,
                        profile_pic_url=user_details_dto.profile_pic_url,
                        stage_display_name=task_stage_with_assignee_dto.
                            stage_display_name)
                    task_stages_having_assignee_details_dtos.append(
                        stage_with_user_details_dto)
        return task_stages_having_assignee_details_dtos
