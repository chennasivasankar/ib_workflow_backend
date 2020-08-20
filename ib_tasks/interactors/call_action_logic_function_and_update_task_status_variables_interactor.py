from typing import List, Any, Dict

from ib_tasks.interactors.storage_interfaces.fields_dtos \
    import FieldValueDTO
from ib_tasks.interactors.storage_interfaces.get_task_dtos \
    import TaskDetailsDTO, TaskGoFDTO, TaskGoFFieldDTO
from ib_tasks.interactors.storage_interfaces.status_dtos import \
    StatusVariableDTO
from ib_tasks.interactors.storage_interfaces.storage_interface \
    import StorageInterface


class InvalidModulePathFound(Exception):
    def __init__(self, path_name: str):
        self.path_name = path_name


class InvalidMethodFound(Exception):
    def __init__(self, method_name: str):
        self.method_name = method_name


class CallActionLogicFunctionAndUpdateTaskStatusVariablesInteractor:

    def __init__(self, storage: StorageInterface,
                 action_id: int, task_id: int):
        self.storage = storage
        self.action_id = action_id
        self.task_id = task_id

    def call_action_logic_function_and_update_task_status_variables(
            self, task_dto: TaskDetailsDTO) -> TaskDetailsDTO:
        task_gof_dtos = task_dto.task_gof_dtos
        gof_multiple_enable_dict = self._get_gof_multiple_enable_dict(
            template_id=task_dto.task_base_details_dto.template_id)
        task_gof_fields_dto = task_dto.task_gof_field_dtos
        task_gof_dtos, task_gof_fields_dto = \
            self._get_updated_task_gof_and_filed_dtos(
                gof_multiple_enable_dict, task_gof_dtos, task_gof_fields_dto
            )
        task_gof_fields_dto_dict = \
            self._get_task_gof_fields_dict(task_gof_fields_dto)
        status_variables_dto = self._get_task_status_dtos(self.task_id)
        task_dict = self._get_task_dict(
            task_gof_dtos, gof_multiple_enable_dict,
            task_gof_fields_dto_dict, status_variables_dto)
        task_dict = self._get_updated_task_dict(task_dict)
        # TODO update fields
        status_dict = task_dict.get("status_variables", {})
        self._update_task_status_variables(status_dict, status_variables_dto)
        return task_dto

    def _get_updated_task_gof_and_filed_dtos(
            self, gof_multiple_enable_dict: Dict[str, bool],
            task_gof_dtos: List[TaskGoFDTO],
            task_gof_fields_dto: List[TaskGoFFieldDTO]
    ):
        updated_task_gofs = []
        for task_gof_dto in task_gof_dtos:
            gof_id = task_gof_dto.gof_id
            if gof_id in gof_multiple_enable_dict:
                updated_task_gofs.append(task_gof_dto)

        updated_task_fields = []

        task_gof_ids = [
            task_gof_dto.task_gof_id
            for task_gof_dto in updated_task_gofs
        ]

        for task_gof_field_dto in task_gof_fields_dto:
            task_gof_id = task_gof_field_dto.task_gof_id
            if task_gof_id in task_gof_ids:
                updated_task_fields.append(task_gof_field_dto)
        return updated_task_gofs, updated_task_fields

    def _get_updated_task_dict(
            self, task_dict: Dict[str, Any]) -> Dict[str, Any]:
        method_object = \
            self._get_method_object_for_condition(action_id=self.action_id)
        global_constants = \
            self._get_global_constants_to_task(task_id=self.task_id)
        stage_value_dict = \
            self._get_stage_value_dict_to_task(task_id=self.task_id)
        from ib_tasks.exceptions.action_custom_exceptions \
            import InvalidKeyError, InvalidCustomLogicException
        try:
            task_dict = method_object(
                task_dict=task_dict, global_constants=global_constants,
                stage_value_dict=stage_value_dict
            )
        except KeyError:
            raise InvalidKeyError()
        except:
            raise InvalidCustomLogicException()

        return task_dict

    def _update_task_status_variables(
            self, status_dict: Dict[str, str],
            status_variables_dto: List[StatusVariableDTO]):
        updated_status_variables_dto = self._get_updated_status_variable_dto(
            status_dict, status_variables_dto)
        self.storage.update_status_variables_to_task(
            task_id=self.task_id,
            status_variables_dto=updated_status_variables_dto)

    def _get_task_status_dtos(self, task_id: int) -> List[StatusVariableDTO]:

        status_variable_dtos = \
            self.storage.get_status_variables_to_task(task_id=task_id)
        return status_variable_dtos

    def _get_global_constants_to_task(self, task_id: int) -> Dict[str, Any]:

        global_constants_dto = \
            self.storage.get_global_constants_to_task(task_id=task_id)

        global_constants = {}
        for global_constant_dto in global_constants_dto:
            constant_name = global_constant_dto.constant_name
            global_constants[constant_name] = global_constant_dto.value
        return global_constants

    def _get_stage_value_dict_to_task(self, task_id: int) -> Dict[str, int]:

        task_stage_dtos = \
            self.storage.get_stage_dtos_to_task(task_id=task_id)

        stage_value_dict = {}
        for task_stage_dto in task_stage_dtos:
            stage_id = task_stage_dto.stage_id
            stage_value_dict[stage_id] = task_stage_dto.value
        return stage_value_dict

    def _get_method_object_for_condition(self, action_id: int):
        path_name = self.storage.get_path_name_to_action(
            action_id=action_id
        )
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
    def _get_updated_status_variable_dto(
            status_dict: Dict[str, str], status_variables_dto: List[StatusVariableDTO]):
        lst = []
        for status_dto in status_variables_dto:
            status_dto.value = status_dict[status_dto.status_variable]
            lst.append(status_dto)
        return lst

    def _get_task_dict(
            self, task_gof_dtos: List[TaskGoFDTO],
            gof_multiple_enable_dict: Dict[str, bool],
            task_gof_fields_dto_dict: Dict[int, Dict[str, Any]],
            status_variables_dto: List[StatusVariableDTO]):
        task_dict = {}
        from collections import defaultdict
        multiple_gof_dict = defaultdict(list)
        single_gof_dict = {}
        task_gof_dtos.sort(key=lambda x: [x.gof_id, x.same_gof_order])
        for task_gof_dto in task_gof_dtos:
            self._update_multiple_and_single_dict(
                task_gof_fields_dto_dict, gof_multiple_enable_dict,
                multiple_gof_dict, single_gof_dict, task_gof_dto)
        task_dict.update(multiple_gof_dict)
        task_dict.update(single_gof_dict)
        statuses_dict = {}
        for status_dto in status_variables_dto:
            statuses_dict[status_dto.status_variable] = status_dto.value

        task_dict["status_variables"] = statuses_dict
        return task_dict

    @staticmethod
    def _update_multiple_and_single_dict(
            task_gof_fields_dict, gof_multiple_enable_dict,
            multiple_gof_dict, single_gof_dict, task_gof_dto
    ):
        gof_id = task_gof_dto.gof_id
        task_gof_id = task_gof_dto.task_gof_id
        fields_dict = task_gof_fields_dict[task_gof_id]

        if gof_multiple_enable_dict.get(gof_id):
            multiple_gof_dict[gof_id].append(fields_dict)
        else:
            single_gof_dict[gof_id] = fields_dict

    @staticmethod
    def _get_fields_dto_dict(
            fields_dto: List[FieldValueDTO]) -> Dict[str, Any]:

        field_dict = {}
        for field_dto in fields_dto:
            field_dict[field_dto.field_id] = field_dto.value
        return field_dict

    def _get_gof_multiple_enable_dict(
            self, template_id: str) -> Dict[str, bool]:

        gof_multiple_enable_dtos = self.storage \
            .get_enable_multiple_gofs_field_to_gof_ids(
                template_id=template_id
            )
        gof_multiple_enable_dict = {}
        for gof_multiple_enable_dto in gof_multiple_enable_dtos:
            gof_multiple_enable_dict[
                gof_multiple_enable_dto.group_of_field_id] = \
                gof_multiple_enable_dto.multiple_status
        return gof_multiple_enable_dict

    @staticmethod
    def _get_task_gof_fields_dict(
            fields_dto: List[TaskGoFFieldDTO]) -> Dict[int, Dict[str, Any]]:
        from collections import defaultdict
        task_gof_fields_dict = defaultdict(dict)
        for field_dto in fields_dto:
            field_id = field_dto.field_id
            response = field_dto.field_response
            task_gof_id = field_dto.task_gof_id
            task_gof_fields_dict[task_gof_id][field_id] = response
        return task_gof_fields_dict
