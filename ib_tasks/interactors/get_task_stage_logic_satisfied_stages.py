from typing import List, Any, Dict

from ib_tasks.interactors.storage_interfaces.stage_dtos import \
    StageDisplayValueDTO, StageDisplayDTO
from ib_tasks.interactors.storage_interfaces.stages_storage_interface import \
    StageStorageInterface
from ib_tasks.interactors.storage_interfaces.storage_interface \
    import StorageInterface
from ib_tasks.interactors.storage_interfaces.status_dtos \
    import StatusVariableDTO
from ib_tasks.interactors.task_dtos import StageDisplayLogicDTO


class GetTaskStageLogicSatisfiedStagesInteractor:

    def __init__(self, task_id: int,
                 storage: StorageInterface,
                 stage_storage: StageStorageInterface):
        self.task_id = task_id
        self.storage = storage
        self.stage_storage = stage_storage

    def get_task_stage_logic_satisfied_next_stages_given_status_variable_dtos(
            self, status_variable_dtos: List[StatusVariableDTO]) -> List[str]:
        stage_display_logic_dtos, stage_display_value_dtos \
            = self._validate_task_and_get_stage_display_logic_dtos()
        status_variable_dict = self. \
            _get_task_status_variable_dict_given_status_variable_dtos(
            status_variable_dtos=status_variable_dtos)
        stage_value_dict = self._get_stage_values_dict(
            stage_display_value_dtos)
        logic_satisfied_stages = self._get_stage_logic_satisfied_stages(
            stage_display_logic_dtos, status_variable_dict, stage_value_dict)
        logic_satisfied_next_stages_removing_current_task_stages = self. \
            _get_logic_satisfied_next_stages_removing_current_task_stages(
            stage_ids=logic_satisfied_stages, task_id=self.task_id)
        return logic_satisfied_next_stages_removing_current_task_stages

    def get_task_stage_logic_satisfied_stages(self):
        stage_display_logic_dtos, stage_display_value_dtos \
            = self._validate_task_and_get_stage_display_logic_dtos()
        status_variable_dict = self._get_task_status_variable_dict_given_task_id(
            task_id=self.task_id
        )
        stage_value_dict = self._get_stage_values_dict(
            stage_display_value_dtos)
        return self._get_stage_logic_satisfied_stages(
            stage_display_logic_dtos, status_variable_dict, stage_value_dict
        )

    def _validate_task_and_get_stage_display_logic_dtos(self):
        self._validate_task_id(task_id=self.task_id)
        stage_display_value_dtos = self.storage \
            .get_task_template_stage_logic_to_task(
            task_id=self.task_id)
        stage_display_dtos = self._get_stage_display_dtos(
            stage_display_value_dtos=stage_display_value_dtos)
        stage_display_logic_dtos = self._get_status_operand_stage_dtos(
            stage_display_dtos=stage_display_dtos
        )
        return stage_display_logic_dtos, stage_display_value_dtos

    def _validate_task_id(self, task_id: int):

        valid_task = self.storage.validate_task_id(task_id=task_id)

        is_invalid_task = not valid_task
        if is_invalid_task:
            from ib_tasks.exceptions.task_custom_exceptions \
                import InvalidTaskException
            raise InvalidTaskException(task_id=task_id)

    @staticmethod
    def _get_stage_display_dtos(
            stage_display_value_dtos: List[StageDisplayValueDTO]
    ) -> List[StageDisplayDTO]:

        return [
            StageDisplayDTO(
                stage_id=stage_display_value_dto.stage_id,
                display_value=stage_display_value_dto.display_logic
            )
            for stage_display_value_dto in stage_display_value_dtos
        ]

    @staticmethod
    def _get_stage_values_dict(
            stage_display_value_dtos: List[StageDisplayValueDTO]):

        stage_value_dict = {}
        for stage_display_value_dto in stage_display_value_dtos:
            stage_id = stage_display_value_dto.stage_id
            value = stage_display_value_dto.value
            stage_value_dict[stage_id] = value
        return stage_value_dict

    def _get_stage_logic_satisfied_stages(
            self, stage_display_logic_dtos: List[StageDisplayLogicDTO],
            status_variable_dict: Dict[str, str],
            stage_value_dict: Dict[str, int]):

        logic_satisfied_stages = []
        for status_stage_dto in stage_display_logic_dtos:
            self._calculate_display_logic(
                status_stage_dto, status_variable_dict,
                logic_satisfied_stages, stage_value_dict
            )

        return logic_satisfied_stages

    def _calculate_display_logic(
            self, stage_display_logic_dto: StageDisplayLogicDTO,
            status_variable_dict: Dict[str, Any],
            logic_satisfied_stages: List[str],
            stage_value_dict: Dict[str, int]
    ):
        stage_display_dto = stage_display_logic_dto.display_logic_dto
        if stage_display_dto.operator == "==":
            self._calculate_direct_logic(
                stage_display_logic_dto, status_variable_dict,
                logic_satisfied_stages
            )
        else:
            self._calculate_indirect_logic(
                stage_display_logic_dto, status_variable_dict,
                logic_satisfied_stages, stage_value_dict
            )

    def _calculate_direct_logic(self,
                                stage_display_logic_dto: StageDisplayLogicDTO,
                                status_variable_dict: Dict[str, Any],
                                logic_satisfied_stages: List[str]):
        operator_dict = self._get_operator_dict()
        stage_display_dto = stage_display_logic_dto.display_logic_dto
        current_stage = stage_display_logic_dto.current_stage
        variable = stage_display_dto.variable
        stage = stage_display_dto.stage
        func = operator_dict[stage_display_dto.operator]
        if func(status_variable_dict[variable], stage):
            logic_satisfied_stages.append(current_stage)

    def _calculate_indirect_logic(
            self, stage_display_logic_dto: StageDisplayLogicDTO,
            status_variable_dict: Dict[str, Any],
            logic_satisfied_stages: List[str],
            stage_value_dict: Dict[str, int]
    ):
        operator_dict = self._get_operator_dict()
        stage_display_dto = stage_display_logic_dto.display_logic_dto
        left_stage = status_variable_dict[stage_display_dto.variable]

        right_stage = stage_display_dto.stage
        current_stage = stage_display_logic_dto.current_stage
        func = operator_dict[stage_display_dto.operator]
        left_stage_value = stage_value_dict[left_stage]
        right_stage_value = stage_value_dict[right_stage]
        if func(left_stage_value, right_stage_value):
            logic_satisfied_stages.append(current_stage)

    @staticmethod
    def _get_operator_dict():
        import operator
        return {
            "==": operator.eq,
            ">=": operator.ge,
            "<=": operator.le,
            ">": operator.gt,
            "<": operator.lt,
            "!=": operator.ne
        }

    def _get_task_status_variable_dict_given_task_id(self, task_id: int):
        status_variable_dto = \
            self.storage.get_status_variables_to_task(task_id=task_id)
        status_variables_dict = \
            self._get_status_variables_dict(status_variable_dto)
        return status_variables_dict

    @staticmethod
    def _get_status_operand_stage_dtos(
            stage_display_dtos: List[StageDisplayDTO]
    ) -> List[StageDisplayLogicDTO]:
        from ib_tasks.interactors.get_stage_display_logic_interactor \
            import StageDisplayLogicInteractor
        interactor = StageDisplayLogicInteractor()
        stage_display_logic_dtos = interactor \
            .get_stage_display_logic_condition(stage_display_dtos)
        return stage_display_logic_dtos

    @staticmethod
    def _get_status_variables_dict(
            status_variables_dto: List[StatusVariableDTO]):

        status_variables_dict = {}
        for status_variable_dto in status_variables_dto:
            variable = status_variable_dto.status_variable
            value = status_variable_dto.value
            status_variables_dict[variable] = value
        return status_variables_dict


    def _get_task_status_variable_dict_given_status_variable_dtos(
            self, status_variable_dtos: List[StatusVariableDTO]):
        status_variables_dict = \
            self._get_status_variables_dict(status_variable_dtos)
        return status_variables_dict

    def _get_logic_satisfied_next_stages_removing_current_task_stages(
            self, task_id, stage_ids: List[str]) -> List[str]:
        current_stages_of_task = self.stage_storage. \
            get_current_stages_of_task_in_given_stages(
            task_id=task_id, stage_ids=stage_ids)
        logic_satisfied_next_stages = [stage_id for stage_id in stage_ids if
                                       stage_id not in current_stages_of_task]
        return logic_satisfied_next_stages
