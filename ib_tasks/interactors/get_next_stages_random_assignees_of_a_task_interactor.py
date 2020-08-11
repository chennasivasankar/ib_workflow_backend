from random import choice
from typing import List, Dict, Any

from ib_tasks.adapters.auth_service import AuthService
from ib_tasks.exceptions.action_custom_exceptions import InvalidActionException
from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskIdException
from ib_tasks.interactors \
    .get_task_stage_logic_satisfied_next_stages_based_on_given_status_vars import \
    GetTaskStageLogicSatisfiedNextStagesGivenStatusVarsInteractor
from ib_tasks.interactors.stages_dtos import StageWithUserDetailsDTO
from ib_tasks.interactors.storage_interfaces.action_storage_interface import \
    ActionStorageInterface
from ib_tasks.interactors.storage_interfaces.stage_dtos import StageRoleDTO, \
    StageIdWithRoleIdsDTO, StageDetailsDTO
from ib_tasks.interactors.storage_interfaces.stages_storage_interface import \
    StageStorageInterface
from ib_tasks.exceptions.action_custom_exceptions \
    import InvalidKeyError, InvalidCustomLogicException
from ib_tasks.interactors.storage_interfaces.status_dtos import \
    StatusVariableDTO
from ib_tasks.interactors.storage_interfaces.storage_interface import \
    StorageInterface
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface
from ib_tasks.interactors.presenter_interfaces.get_next_stages_random_assignees_of_a_task_presenter import \
    GetNextStagesRandomAssigneesOfATaskPresenterInterface


class InvalidModulePathFound(Exception):
    def __init__(self, path_name: str):
        self.path_name = path_name


class InvalidMethodFound(Exception):
    def __init__(self, method_name: str):
        self.method_name = method_name


class GetNextStagesRandomAssigneesOfATaskInteractor:
    def __init__(self, storage: StorageInterface,
                 stage_storage: StageStorageInterface,
                 task_storage: TaskStorageInterface,
                 action_storage: ActionStorageInterface):
        self.stage_storage = stage_storage
        self.task_storage = task_storage
        self.action_storage = action_storage
        self.storage = storage

    def get_next_stages_random_assignees_of_a_task_wrapper(
            self, task_id: int, action_id: int, presenter:
            GetNextStagesRandomAssigneesOfATaskPresenterInterface):
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
        except InvalidCustomLogicException:
            return presenter.raise_invalid_custom_logic_function_exception()
        except InvalidModulePathFound as exception:
            return presenter.raise_invalid_path_not_found_exception(
                path_name=exception.path_name)
        except InvalidMethodFound as exception:
            return presenter.raise_invalid_method_not_found_exception(
                method_name=exception.method_name)

    def get_next_stages_random_assignees_of_a_task(self, task_id: int,
                                                   action_id: int)-> List[
        StageWithUserDetailsDTO]:
        self._validate_task_id(task_id=task_id)
        self._validate_action_id(action_id=action_id)
        updated_status_variable_dtos = self. \
            get_updated_status_variables_dtos_of_task(task_id, action_id)
        next_stages_of_task = \
            self.get_next_stages_of_task(task_id=task_id, status_variable_dtos=
            updated_status_variable_dtos)
        stage_detail_dtos = self.stage_storage. \
            get_stage_detail_dtos_given_stage_ids(next_stages_of_task)
        db_stage_ids = self._get_db_stage_ids(stage_detail_dtos)
        stage_role_dtos = \
            self.stage_storage.get_stage_role_dtos_given_db_stage_ids(
                db_stage_ids)
        role_ids_group_by_stage_id_dtos = \
            self._get_role_ids_group_by_stage_id_dtos(
                stage_ids=db_stage_ids, stage_role_dtos=stage_role_dtos)
        stage_with_user_details_dtos = self._get_random_permitted_user_details_dto_of_stage_id(
            role_ids_group_by_stage_id_dtos, stage_detail_dtos)
        return stage_with_user_details_dtos

    @staticmethod
    def _get_random_permitted_user_details_dto_of_stage_id(
            role_ids_group_by_stage_id_dtos: List[StageIdWithRoleIdsDTO],
            stage_detail_dtos: List[StageDetailsDTO]) -> List[
        StageWithUserDetailsDTO]:
        stage_with_user_details_dtos = []
        auth_service_adapter = AuthService()
        for each_dto in role_ids_group_by_stage_id_dtos:
            permitted_user_details_dtos = auth_service_adapter. \
                get_permitted_user_details(role_ids=each_dto.role_ids)
            random_permitted_user_detail_dto = choice(
                permitted_user_details_dtos)
            for each_stage_detail_dto in stage_detail_dtos:
                if each_stage_detail_dto.db_stage_id == each_dto.db_stage_id:
                    name = each_stage_detail_dto.name

            stage_with_user_details_dto = StageWithUserDetailsDTO(
                db_stage_id=each_dto.db_stage_id,
                assignee_id=random_permitted_user_detail_dto.user_id,
                assignee_name=random_permitted_user_detail_dto.user_name,
                profile_pic_url=random_permitted_user_detail_dto.
                    profile_pic_url,
                stage_display_name=name,
            )
            stage_with_user_details_dtos.append(
                stage_with_user_details_dto)
        return stage_with_user_details_dtos

    @staticmethod
    def _get_role_ids_group_by_stage_id_dtos(
            stage_ids: List[int], stage_role_dtos: List[StageRoleDTO]
    ) -> List[StageIdWithRoleIdsDTO]:
        role_ids_group_by_stage_id_dtos = []
        for each_stage_id in stage_ids:

            list_of_role_ids = []
            for each_stage_role_dto in stage_role_dtos:
                if each_stage_role_dto.db_stage_id == \
                        each_stage_id:
                    list_of_role_ids.append(each_stage_role_dto.role_id)
            each_stage_id_with_role_ids_dto = \
                StageIdWithRoleIdsDTO(db_stage_id=each_stage_id,
                                      role_ids=list_of_role_ids)
            role_ids_group_by_stage_id_dtos.append(
                each_stage_id_with_role_ids_dto)
        return role_ids_group_by_stage_id_dtos

    @staticmethod
    def _get_db_stage_ids(stage_detail_dtos):
        db_stage_ids = [
            each_stage_detail_dto.db_stage_id
            for each_stage_detail_dto in stage_detail_dtos
        ]
        return db_stage_ids

    def get_next_stages_of_task(self, task_id: int,
                                status_variable_dtos) -> List[str]:
        get_task_stage_logic_satisfied_next_stages_interactor = \
            GetTaskStageLogicSatisfiedNextStagesGivenStatusVarsInteractor(
                storage=self.storage)
        next_stages = get_task_stage_logic_satisfied_next_stages_interactor. \
            get_task_stage_logic_satisfied_next_stages(
            task_id=task_id, updated_status_variable_dtos=
            status_variable_dtos)
        return next_stages

    def get_updated_status_variables_dtos_of_task(self, task_id: int,
                                                  action_id: int) -> \
            List[StatusVariableDTO]:
        status_variables_dto = self._get_task_status_variables_dtos(
            task_id=task_id)
        task_dict = self._get_task_dict(status_variables_dto)
        task_dict = self._get_updated_task_dict(task_dict=task_dict,
                                                action_id=action_id,
                                                task_id=task_id)
        status_dict = task_dict.get("status_variables", {})
        updated_status_variable_dtos = self._get_updated_status_variable_dto(
            status_dict, status_variables_dto)
        return updated_status_variable_dtos

    @staticmethod
    def _get_updated_status_variable_dto(
            status_dict: Dict[str,
                              str],
            status_variables_dto: List[StatusVariableDTO]
    ) -> List[StatusVariableDTO]:
        lst = []
        for status_dto in status_variables_dto:
            status_dto.value = status_dict[status_dto.status_variable]
            lst.append(status_dto)
        return lst

    def _get_updated_task_dict(
            self, task_dict: Dict[str, Any], action_id: int, task_id: int) -> \
            Dict[str, Any]:
        method_object = \
            self._get_method_object_for_condition(action_id=action_id)
        global_constants = \
            self._get_global_constants_to_task(task_id=task_id)
        stage_value_dict = \
            self._get_stage_value_dict_to_task(task_id=task_id)
        from ib_tasks.exceptions.action_custom_exceptions \
            import InvalidKeyError, InvalidCustomLogicException
        try:
            task_dict = method_object(task_dict=task_dict,
                                      global_constants=global_constants,
                                      stage_value_dict=stage_value_dict)
        except KeyError:
            raise InvalidKeyError()
        except:
            raise InvalidCustomLogicException()

        return task_dict

    def _get_stage_value_dict_to_task(self, task_id: int) -> Dict[str, int]:

        task_stage_dtos = \
            self.storage.get_stage_dtos_to_task(task_id=task_id)

        stage_value_dict = {}
        for task_stage_dto in task_stage_dtos:
            stage_id = task_stage_dto.stage_id
            stage_value_dict[stage_id] = task_stage_dto.value
        return stage_value_dict

    def _get_global_constants_to_task(self, task_id: int) -> Dict[str, Any]:

        global_constants_dto = \
            self.storage.get_global_constants_to_task(task_id=task_id)

        global_constants = {}
        for global_constant_dto in global_constants_dto:
            constant_name = global_constant_dto.constant_name
            global_constants[constant_name] = global_constant_dto.value
        return global_constants

    def _get_method_object_for_condition(self, action_id: int):
        path_name = self.storage.get_path_name_to_action(action_id=action_id)
        path, method = path_name.rsplit(".", 1)
        from importlib import import_module
        try:
            module = import_module(path)
        except ModuleNotFoundError:
            raise InvalidModulePathFound(path_name=path_name)
        try:
            method_object = getattr(module, method)
        except AttributeError:
            raise InvalidMethodFound(method_name=method)
        return method_object

    @staticmethod
    def _get_task_dict(status_variables_dto: List[StatusVariableDTO]):
        task_dict = {}
        statuses_dict = {}
        for status_dto in status_variables_dto:
            statuses_dict[status_dto.status_variable] = status_dto.value
        task_dict["status_variables"] = statuses_dict
        return task_dict

    def _get_task_status_variables_dtos(
            self, task_id: int) -> List[StatusVariableDTO]:
        status_variable_dtos = \
            self.storage.get_status_variables_to_task(task_id=task_id)
        return status_variable_dtos

    def _validate_task_id(self, task_id: int):
        is_task_exists = self.task_storage. \
            check_is_task_exists(
            task_id=task_id)

        is_task_does_not_exists = not is_task_exists
        if is_task_does_not_exists:
            raise InvalidTaskIdException(task_id=task_id)

    def _validate_action_id(self, action_id: int):
        valid_action = self.action_storage.validate_action(action_id=action_id)
        is_invalid_action = not valid_action
        if is_invalid_action:
            raise InvalidActionException(action_id=action_id)
