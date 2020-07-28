from typing import List

from ib_tasks.interactors.gofs_dtos import TaskGofAndStatusesDTO
from ib_tasks.interactors.storage_interfaces.fields_dtos import FieldValueDTO
from ib_tasks.interactors.storage_interfaces.storage_interface \
    import StorageInterface, GroupOfFieldsDTO, StatusVariableDTO


class InvalidModulePathFound(Exception):
    def __init__(self, path_name: str):
        self.path_name = path_name


class InvalidMethodFound(Exception):
    def __init__(self, method_name: str):
        self.method_name = method_name


class CallActionLogicFunctionAndUpdateTaskStatusVariablesInteractor:

    def __init__(self, storage: StorageInterface,
                 action_id: int):
        self.storage = storage
        self.action_id = action_id

    def call_action_logic_function_and_update_task_status_variables(
            self, task_dto: TaskGofAndStatusesDTO):
        group_of_fields_dto = task_dto.group_of_fields_dto
        gof_multiple_enable_dict = self._get_gof_multiple_enable_dict(
            task_id=task_dto.task_id,
            group_of_fields_dto=group_of_fields_dto)
        fields_dto = task_dto.fields_dto
        gof_fields_dto_dict = self._get_gof_field_dtos_dict(fields_dto)
        status_variables_dto = task_dto.statuses_dto
        task_dict = self._get_task_dict(group_of_fields_dto,
                                        gof_multiple_enable_dict,
                                        gof_fields_dto_dict,
                                        status_variables_dto)
        method_object = self._get_method_object_for_condition(
            action_id=self.action_id)
        global_constants = self._get_global_constants_to_task_template(
            task_id=task_dto.task_id)
        stage_value_dict = self._get_stage_value_dict_to_task_template(
            task_id=task_dto.task_id)
        task_dict = method_object(
            task_dict=task_dict, global_constants=global_constants,
            stage_value_dict=stage_value_dict
        )
        status_dict = task_dict["statuses"]
        updated_status_variables_dto = self._get_updated_status_variable_dto(
            status_dict, status_variables_dto)
        self.storage.update_status_variables_to_task(
            task_id=task_dto.task_id,
            status_variables_dto=updated_status_variables_dto)

    def _get_global_constants_to_task_template(self, task_id: int):

        global_constants_dto = \
            self.storage.get_global_constants_to_task(task_id=task_id)

        global_constants = {}
        for global_constant_dto in global_constants_dto:
            constant_name = global_constant_dto.constant_name
            global_constants[constant_name] = global_constant_dto.value
        return global_constants

    def _get_stage_value_dict_to_task_template(self, task_id: int):

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
            print(module)
        except ModuleNotFoundError:
            raise InvalidModulePathFound(path_name=path_name)
        try:
            method_object = getattr(module, method)
        except AttributeError:
            raise InvalidMethodFound(method_name=method)
        return method_object

    @staticmethod
    def _get_updated_status_variable_dto(status_dict, status_variables_dto):
        for status_dto in status_variables_dto:
            status_dto.value = status_dict[status_dto.status_variable]
        return status_variables_dto

    def _get_task_dict(self, group_of_fields_dto, gof_multiple_enable_dict,
                       gof_fields_dto_dict, status_variables_dto):
        task_dict = {}
        from collections import defaultdict
        multiple_gof_dict = defaultdict(list)
        single_gof_dict = {}
        for group_of_field_dto in group_of_fields_dto:
            self._update_multiple_and_single_dict(
                gof_fields_dto_dict, gof_multiple_enable_dict,
                multiple_gof_dict, single_gof_dict, group_of_field_dto)
        task_dict.update(multiple_gof_dict)
        task_dict.update(single_gof_dict)
        statuses_dict = {}
        for status_dto in status_variables_dto:
            statuses_dict[status_dto.status_variable] = status_dto.value

        task_dict["statuses"] = statuses_dict
        return task_dict

    def _update_multiple_and_single_dict(
            self, gof_fields_dto_dict, gof_multiple_enable_dict,
            multiple_gof_dict, single_gof_dict, group_of_field_dto
    ):
        group_of_field_id = group_of_field_dto.group_of_field_id
        if gof_multiple_enable_dict[group_of_field_id]:
            multiple_gof_dict[group_of_field_id].append(
                self._get_fields_dto_dict(
                    gof_fields_dto_dict[group_of_field_dto.database_id])
            )
        else:
            single_gof_dict[group_of_field_id] = \
                self._get_fields_dto_dict(
                    gof_fields_dto_dict[group_of_field_dto.database_id])

    @staticmethod
    def _get_common_gof_ids(group_of_fields_dto: List[GroupOfFieldsDTO]):

        return list({
            group_of_field_dto.group_of_field_id
            for group_of_field_dto in group_of_fields_dto
        })

    @staticmethod
    def _get_fields_dto_dict(fields_dto: List[FieldValueDTO]):

        field_dict = {}
        for field_dto in fields_dto:
            field_dict[field_dto.field_id] = field_dto.value
        return field_dict

    def _get_gof_multiple_enable_dict(
            self, task_id: int, group_of_fields_dto: List[GroupOfFieldsDTO]):

        common_gof_ids = self._get_common_gof_ids(
            group_of_fields_dto=group_of_fields_dto
        )
        gof_multiple_enable_dtos = self.storage \
            .get_enable_multiple_gofs_field_to_gof_ids(
            task_id=task_id,
            gof_ids=common_gof_ids
        )
        gof_multiple_enable_dict = {}
        for gof_multiple_enable_dto in gof_multiple_enable_dtos:
            gof_multiple_enable_dict[
                gof_multiple_enable_dto.group_of_field_id] = \
                    gof_multiple_enable_dto.multiple_status
        return gof_multiple_enable_dict

    @staticmethod
    def _get_gof_field_dtos_dict(fields_dto: List[FieldValueDTO]):
        from collections import defaultdict
        gof_field_dtos_dict = defaultdict(list)
        for field_dto in fields_dto:
            gof_field_dtos_dict[field_dto.gof_database_id].append(field_dto)
        return gof_field_dtos_dict
