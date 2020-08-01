from typing import List, Any, Dict

from ib_tasks.interactors.storage_interfaces.stage_dtos import StageDisplayValueDTO
from ib_tasks.interactors.storage_interfaces.storage_interface \
    import StorageInterface
from ib_tasks.interactors.storage_interfaces.status_dtos \
    import StatusVariableDTO
from ib_tasks.interactors.task_dtos import StatusOperandStageDTO


class GetTaskStageLogicSatisfiedStages:

    def __init__(self, task_id: int,
                 storage: StorageInterface):
        self.task_id = task_id
        self.storage = storage

    def get_task_stage_logic_satisfied_stages(self):
        self._validate_task_id(task_id=self.task_id)
        stage_display_value_dtos = self.storage\
            .get_task_template_stage_logic_to_task(
                task_id=self.task_id
            )
        stage_display_logics = self._get_stage_display_logics(
            stage_display_value_dtos=stage_display_value_dtos
        )
        status_stage_dtos = self._get_status_operand_stage_dtos(
            stage_display_logics=stage_display_logics
        )
        status_variable_dict = self._get_task_status_variable_dict(
            task_id=self.task_id
        )
        stage_value_dict = self._get_stage_values_dict(stage_display_value_dtos)
        return self._get_stage_logic_satisfied_stages(
            status_stage_dtos, status_variable_dict, stage_value_dict
        )

    def _validate_task_id(self, task_id: int):

        valid_task = self.storage.validate_task_id(task_id=task_id)

        is_invalid_task = not valid_task
        if is_invalid_task:
            from ib_tasks.exceptions.task_custom_exceptions \
                import InvalidTaskException
            raise InvalidTaskException(task_id=task_id)

    @staticmethod
    def _get_stage_display_logics(
            stage_display_value_dtos: List[StageDisplayValueDTO]):

        return [
            stage_display_value_dto.display_logic
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

    def _get_stage_logic_satisfied_stages(self,
            status_stage_dtos: List[StatusOperandStageDTO],
            status_variable_dict: Dict[str, str],
            stage_value_dict: Dict[str, int]):

        logic_satisfied_stages = []
        for status_stage_dto in status_stage_dtos:
            self._calculate_display_logic(
                status_stage_dto, status_variable_dict,
                logic_satisfied_stages, stage_value_dict
            )

        return logic_satisfied_stages

    def _calculate_display_logic(
            self, status_stage_dto: StatusOperandStageDTO,
            status_variable_dict: Dict[str, Any],
            logic_satisfied_stages: List[str],
            stage_value_dict: Dict[str, int]
    ):

        if status_stage_dto.operator == "==":
            self._calculate_direct_logic(
                status_stage_dto, status_variable_dict, logic_satisfied_stages
            )
        else:
            self._calculate_indirect_logic(
                status_stage_dto, status_variable_dict,
                logic_satisfied_stages, stage_value_dict
            )

    def _calculate_direct_logic(self, status_stage_dto: StatusOperandStageDTO,
                                status_variable_dict: Dict[str, Any],
                                logic_satisfied_stages: List[str]):
        operator_dict = self._get_operator_dict()
        variable = status_stage_dto.variable
        stage = status_stage_dto.stage
        func = operator_dict[status_stage_dto.operator]
        if func(status_variable_dict[variable], stage):
            logic_satisfied_stages.append(stage)

    def _calculate_indirect_logic(
            self, status_stage_dto: StatusOperandStageDTO,
            status_variable_dict: Dict[str, Any],
            logic_satisfied_stages: List[str],
            stage_value_dict: Dict[str, int]
    ):
        operator_dict = self._get_operator_dict()
        val_of_stage = status_variable_dict[status_stage_dto.variable]

        right_stage = status_stage_dto.stage

        func = operator_dict[status_stage_dto.operator]
        left_stage_value = stage_value_dict[val_of_stage]
        right_stage_value = stage_value_dict[right_stage]
        if func(left_stage_value, right_stage_value):
            logic_satisfied_stages.append(right_stage)

    @staticmethod
    def _get_operator_dict():
        import operator
        return {
            "==": operator.eq,
            ">=": operator.ge,
            "<=": operator.le,
            ">": operator.le,
            "<": operator.ge,
            "!=": operator.ne
        }

    def _get_task_status_variable_dict(self, task_id: int):
        status_variable_dto = \
            self.storage.get_status_variables_to_task(task_id=task_id)
        status_variables_dict = \
            self._get_status_variables_dict(status_variable_dto)
        return status_variables_dict

    @staticmethod
    def _get_status_operand_stage_dtos(stage_display_logics: List[str]):
        from ib_tasks.interactors.get_stage_display_logic_interactor \
            import StageDisplayLogicInteractor
        interactor = StageDisplayLogicInteractor()
        status_operand_stage_dtos = interactor\
            .get_stage_display_logic_condition(stage_display_logics)
        return status_operand_stage_dtos

    @staticmethod
    def _get_status_variables_dict(status_variables_dto: List[StatusVariableDTO]):

        status_variables_dict = {}
        for status_variable_dto in status_variables_dto:
            variable = status_variable_dto.status_variable
            value = status_variable_dto.value
            status_variables_dict[variable] = value
        return status_variables_dict