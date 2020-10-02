from typing import List, Any, Dict

from ib_tasks.constants.enum import FieldTypes
from ib_tasks.interactors.storage_interfaces.action_storage_interface import \
    ActionStorageInterface
from ib_tasks.interactors.storage_interfaces.fields_dtos \
    import FieldValueDTO, FieldTypeDTO
from ib_tasks.interactors.storage_interfaces.fields_storage_interface import \
    FieldsStorageInterface
from ib_tasks.interactors.storage_interfaces.get_task_dtos \
    import TaskDetailsDTO, TaskGoFDTO, TaskGoFFieldDTO
from ib_tasks.interactors.storage_interfaces.gof_storage_interface import \
    GoFStorageInterface
from ib_tasks.interactors.storage_interfaces.stages_storage_interface import \
    StageStorageInterface
from ib_tasks.interactors.storage_interfaces.status_dtos import \
    StatusVariableDTO
from ib_tasks.interactors.storage_interfaces.storage_interface \
    import StorageInterface
from ib_tasks.interactors.storage_interfaces.task_dtos import \
    TaskGoFWithTaskIdDTO
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface


class InvalidModulePathFound(Exception):
    def __init__(self, path_name: str):
        self.path_name = path_name


class InvalidMethodFound(Exception):
    def __init__(self, method_name: str):
        self.method_name = method_name


class CallActionLogicFunctionAndGetOrUpdateTaskStatusVariablesInteractor:
    from ib_tasks.interactors.storage_interfaces. \
        create_or_update_task_storage_interface import \
        CreateOrUpdateTaskStorageInterface

    def __init__(self, storage: StorageInterface,
                 task_storage: TaskStorageInterface,
                 create_task_storage: CreateOrUpdateTaskStorageInterface,
                 field_storage: FieldsStorageInterface,
                 action_id: int, task_id: int,
                 gof_storage: GoFStorageInterface,
                 action_storage: ActionStorageInterface,
                 stage_storage: StageStorageInterface
                 ):
        self.stage_storage = stage_storage
        self.action_storage = action_storage
        self.storage = storage
        self.action_id = action_id
        self.task_id = task_id
        self.task_storage = task_storage
        self.create_task_storage = create_task_storage
        self.field_storage = field_storage
        self.gof_storage = gof_storage

    def call_action_logic_function_and_get_status_variables_dtos_of_task(self) \
            -> List[StatusVariableDTO]:
        task_dto = self._get_task_dto(self.task_id)
        status_dict, status_variables_dto = \
            self._call_action_logic_function(task_dto=task_dto)
        updated_status_variable_dtos = self._get_updated_status_variable_dto(
            status_dict, status_variables_dto)
        return updated_status_variable_dtos

    def call_action_logic_function_and_update_task_status_variables(
            self) -> TaskDetailsDTO:
        task_dto = self._get_task_dto(self.task_id)
        status_dict, status_variables_dto = \
            self._call_action_logic_function(task_dto=task_dto)
        self._update_task_status_variables(status_dict, status_variables_dto)
        return task_dto

    def _call_action_logic_function(
            self, task_dto: TaskDetailsDTO):
        task_gof_dtos = task_dto.task_gof_dtos
        gof_multiple_enable_dict = self._get_gof_multiple_enable_dict(
            template_id=task_dto.task_base_details_dto.template_id)
        task_gof_fields_dto = task_dto.task_gof_field_dtos
        task_gof_fields_dto_dict = self._get_task_gof_fields_dict(
            task_gof_fields_dto)
        status_variable_dtos = self.task_storage \
            .get_status_variables_to_task(task_id=self.task_id)
        task_dict = self._get_task_dict(
            task_gof_dtos, gof_multiple_enable_dict,
            task_gof_fields_dto_dict, status_variable_dtos)
        task_dict = self._get_updated_task_dict(task_dict)
        from ib_tasks.interactors.create_or_update_task \
            .task_crud_operations_interactor \
            import TaskCrudOperationsInteractor
        interactor = TaskCrudOperationsInteractor(
            create_task_storage=self.create_task_storage)
        task_gof_with_task_id_dtos = self._convert_and_update_task_gof_dtos(
            task_gof_dtos, self.task_id)
        task_gof_fields_dto = self._prepare_task_gof_fields_dtos(
            task_dict, task_dto.task_gof_dtos, task_dto.task_gof_field_dtos
        )
        interactor.update_task_gofs(task_gof_with_task_id_dtos)
        interactor.update_task_gof_fields(task_gof_fields_dto)
        status_dict = task_dict.get("status_variables", {})
        return (
            status_dict, status_variable_dtos
        )

    @staticmethod
    def _convert_and_update_task_gof_dtos(
            task_gof_dtos: List[TaskGoFDTO], task_id: int
    ) -> List[TaskGoFWithTaskIdDTO]:
        task_gof_with_task_id_dtos = [
            TaskGoFWithTaskIdDTO(
                task_id=task_id,
                gof_id=task_gof_dto.gof_id,
                same_gof_order=task_gof_dto.same_gof_order,
                task_gof_id=task_gof_dto.task_gof_id
            ) for task_gof_dto in task_gof_dtos
        ]
        return task_gof_with_task_id_dtos

    def _prepare_task_gof_fields_dtos(
            self, task_dict: Dict, task_gofs: List[TaskGoFDTO],
            task_gof_fields: List[TaskGoFFieldDTO]
    ) -> List[TaskGoFFieldDTO]:
        task_gof_fields_for_updation = []
        for task_gof in task_gofs:
            task_gof_id = task_gof.task_gof_id
            field_id = self._get_task_gof_field_id(
                task_gof_id, task_gof_fields)
            task_gof_field_dto = self._get_task_gof_field_dto(
                task_dict, task_gof.gof_id, task_gof.same_gof_order,
                task_gof.task_gof_id, field_id)
            task_gof_fields_for_updation.append(task_gof_field_dto)
        return task_gof_fields

    @staticmethod
    def _get_task_gof_field_id(
            task_gof_id: int, task_gof_fields: List[TaskGoFFieldDTO]) -> str:
        for task_gof_field in task_gof_fields:
            if task_gof_field.task_gof_id == task_gof_id:
                return task_gof_field.field_id

    @staticmethod
    def _get_task_gof_field_dto(
            task_dict: Dict, gof_id: str, same_gof_order: int,
            task_gof_id: int, field_id: str,
    ) -> List[TaskGoFFieldDTO]:
        gof_field_dicts = task_dict.get(gof_id)
        if same_gof_order:
            field_dict = gof_field_dicts[same_gof_order]
        else:
            field_dict = task_dict.get(gof_id)
        field_response = field_dict.get(field_id)
        task_gof_field_dto = TaskGoFFieldDTO(
            task_gof_id=task_gof_id, field_id=field_id,
            field_response=field_response)
        return task_gof_field_dto

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
        self.task_storage.update_status_variables_to_task(
            task_id=self.task_id,
            status_variables_dto=updated_status_variables_dto)

    def _get_global_constants_to_task(self, task_id: int) -> Dict[str, Any]:

        global_constants_dto = \
            self.task_storage.get_global_constants_to_task(task_id=task_id)

        global_constants = {}
        for global_constant_dto in global_constants_dto:
            constant_name = global_constant_dto.constant_name
            global_constants[constant_name] = global_constant_dto.value
        return global_constants

    def _get_stage_value_dict_to_task(self, task_id: int) -> Dict[str, int]:

        task_stage_dtos = \
            self.stage_storage.get_stage_dtos_to_task(task_id=task_id)

        stage_value_dict = {}
        for task_stage_dto in task_stage_dtos:
            stage_id = task_stage_dto.stage_id
            stage_value_dict[stage_id] = task_stage_dto.value
        return stage_value_dict

    def _get_method_object_for_condition(self, action_id: int):
        path_name = self.action_storage.get_path_name_to_action(
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

    def _get_gof_multiple_enable_dict(
            self, template_id: str) -> Dict[str, bool]:

        gof_multiple_enable_dtos = self.gof_storage \
            .get_enable_multiple_gofs_field_to_gof_ids(
            template_id=template_id)
        gof_multiple_enable_dict = {}
        for gof_multiple_enable_dto in gof_multiple_enable_dtos:
            gof_multiple_enable_dict[
                gof_multiple_enable_dto.group_of_field_id] = \
                gof_multiple_enable_dto.multiple_status
        return gof_multiple_enable_dict

    def _get_task_gof_fields_dict(
            self, fields_dto: List[TaskGoFFieldDTO]
    ) -> Dict[int, Dict[str, Any]]:
        field_ids = self._get_field_ids(fields_dto)
        field_type_dtos = self.field_storage.get_field_type_dtos(field_ids)
        from collections import defaultdict
        task_gof_fields_dict = defaultdict(dict)
        field_type_dict = self._get_field_type_dict(field_type_dtos)
        for field_dto in fields_dto:
            self._append_field_to_task_gof_field_dict(
                field_dto, task_gof_fields_dict, field_type_dict
            )
        return task_gof_fields_dict

    def _append_field_to_task_gof_field_dict(
            self, field_dto: TaskGoFFieldDTO,
            task_gof_fields_dict: Dict[int, Dict[str, Any]],
            field_type_dict: Dict[str, FieldTypes]
    ):
        field_id = field_dto.field_id
        response = field_dto.field_response
        task_gof_id = field_dto.task_gof_id
        if self._check_field_type_number_or_float(
                field_type_dict[field_id]):
            response = float(field_dto.field_response)
        task_gof_fields_dict[task_gof_id][field_id] = response

    def _get_task_dto(self, task_id: int):

        from ib_tasks.interactors.get_task_base_interactor \
            import GetTaskBaseInteractor
        gof_and_status_obj = \
            GetTaskBaseInteractor(
                storage=self.create_task_storage,
                gof_storage=self.gof_storage
            )
        task_dto = gof_and_status_obj \
            .get_task(task_id=task_id)
        return task_dto

    @staticmethod
    def _get_field_ids(
            task_gof_fields_dto: List[TaskGoFFieldDTO]
    ) -> List[str]:
        field_ids = [
            dto.field_id
            for dto in task_gof_fields_dto
        ]
        return field_ids

    @staticmethod
    def _check_field_type_number_or_float(
            field_type: FieldTypes
    ) -> bool:
        is_number_or_float = (
                field_type == FieldTypes.NUMBER.value
                or field_type == FieldTypes.FLOAT.value
        )
        if is_number_or_float:
            return True
        return False

    @staticmethod
    def _get_field_type_dict(
            field_type_dtos: List[FieldTypeDTO]
    ) -> Dict[str, FieldTypes]:

        return {
            field_type_dto.field_id: field_type_dto.field_type
            for field_type_dto in field_type_dtos
        }

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

    @staticmethod
    def _get_updated_status_variable_dto(
            status_dict: Dict[str, str],
            status_variable_dtos: List[StatusVariableDTO]) -> \
            List[StatusVariableDTO]:
        return [
            StatusVariableDTO(
                status_id=status_dto.status_id,
                status_variable=status_dto.status_variable,
                value=status_dict[status_dto.status_variable]
            )
            for status_dto in status_variable_dtos
        ]
