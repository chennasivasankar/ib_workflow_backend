from typing import List, Dict, Any

from ib_tasks.interactors.mixins.validation_mixin import ValidationMixin
from ib_tasks.interactors.storage_interfaces.action_storage_interface import \
    ActionStorageInterface
from ib_tasks.interactors.storage_interfaces.status_dtos import \
    StatusVariableDTO
from ib_tasks.interactors.storage_interfaces.storage_interface import \
    StorageInterface
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface


class CallActionLogicFunctionAndGetTaskStatusVariablesInteractor(
    ValidationMixin):

    def __init__(self, storage: StorageInterface,
                 task_storage: TaskStorageInterface,
                 action_storage: ActionStorageInterface):
        self.storage = storage
        self.task_storage = task_storage
        self.action_storage = action_storage

    def get_status_variables_dtos_of_task_based_on_action(self, task_id: int,
                                                          action_id: int) -> \
            List[StatusVariableDTO]:
        self.validate_task_id(task_id=task_id)
        self.validate_action_id(action_id=action_id)
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

    def _get_task_status_variables_dtos(
            self, task_id: int) -> List[StatusVariableDTO]:
        status_variable_dtos = \
            self.storage.get_status_variables_to_task(task_id=task_id)
        return status_variable_dtos

    @staticmethod
    def _get_task_dict(status_variables_dto: List[StatusVariableDTO]):
        task_dict = {}
        statuses_dict = {}
        for status_dto in status_variables_dto:
            statuses_dict[status_dto.status_variable] = status_dto.value
        task_dict["status_variables"] = statuses_dict
        return task_dict

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

    def _get_method_object_for_condition(self, action_id: int):
        path_name = self.storage.get_path_name_to_action(action_id=action_id)
        path, method = path_name.rsplit(".", 1)
        from importlib import import_module
        from ib_tasks.exceptions.custom_exceptions import \
            InvalidModulePathFound, InvalidMethodFound
        try:
            module = import_module(path)

        except ModuleNotFoundError:
            raise InvalidModulePathFound(path_name=path_name)
        try:
            method_object = getattr(module, method)
        except AttributeError:
            raise InvalidMethodFound(method_name=method)
        return method_object

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
