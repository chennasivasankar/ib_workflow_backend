from ib_tasks.adapters.dtos import TaskBoardsDetailsDTO
from ib_tasks.tests.factories.storage_dtos import TaskDetailsDTOFactory


def prepare_task_gof_and_fields_dto():

    from ib_tasks.tests.factories.storage_dtos import TaskGoFDTOFactory
    TaskGoFDTOFactory.reset_sequence()
    task_gof_dtos = [
        TaskGoFDTOFactory(task_gof_id=1, gof_id="gof1", same_gof_order=1),
        TaskGoFDTOFactory(task_gof_id=2, gof_id="gof2", same_gof_order=1),
        TaskGoFDTOFactory(task_gof_id=3, gof_id="gof2", same_gof_order=2),
    ]
    from ib_tasks.tests.factories.storage_dtos import TaskGoFFieldDTOFactory
    TaskGoFFieldDTOFactory.reset_sequence(1)
    gof_field_dtos = TaskGoFFieldDTOFactory.create_batch(size=3)
    task_dto = TaskDetailsDTOFactory(
        task_gof_dtos=task_gof_dtos,
        task_gof_field_dtos=gof_field_dtos
    )
    return task_dto


def prepare_call_action_logic_update_stages_mock(mocker):

    path = "ib_tasks.interactors.call_action_logic_function_and_update_task_status_variables_interactor" \
           ".CallActionLogicFunctionAndUpdateTaskStatusVariablesInteractor" \
           ".call_action_logic_function_and_update_task_status_variables"
    mock_obj = mocker.patch(path)
    return mock_obj


def prepare_stage_display_satisfied_stage_ids(mocker):

    path = 'ib_tasks.interactors.get_task_stage_logic_satisfied_stages.GetTaskStageLogicSatisfiedStages' \
           '.get_task_stage_logic_satisfied_stages'
    mock_obj = mocker.patch(path)
    return mock_obj


def prepare_task_boards_details():

    from ib_tasks.tests.factories.adapter_dtos import (
        BoardDTOFactory, ColumnDTOFactory, ColumnStageDTOFactory,
        ColumnFieldDTOFactory
    )
    BoardDTOFactory.reset_sequence()
    ColumnDTOFactory.reset_sequence()
    ColumnStageDTOFactory.reset_sequence()
    ColumnFieldDTOFactory.reset_sequence()
    boards_dto = BoardDTOFactory()
    column_dtos = ColumnDTOFactory.create_batch(size=2, board_id="board_1")
    columns_stage_dtos = ColumnStageDTOFactory.create_batch(size=2)
    return TaskBoardsDetailsDTO(
        board_dto=boards_dto,
        column_stage_dtos=columns_stage_dtos,
        columns_dtos=column_dtos,
    )


def prepare_integration_task_boards_details():

    from ib_tasks.tests.factories.adapter_dtos import (
        BoardDTOFactory, ColumnDTOFactory, ColumnStageDTOFactory,
        ColumnFieldDTOFactory
    )
    BoardDTOFactory.reset_sequence()
    ColumnDTOFactory.reset_sequence()
    ColumnStageDTOFactory.reset_sequence()
    ColumnFieldDTOFactory.reset_sequence()
    boards_dto = BoardDTOFactory()
    column_dtos = ColumnDTOFactory.create_batch(size=2, board_id="board_1")
    column1 = ColumnStageDTOFactory(column_id='column_1', stage_id='stage_id_1')
    column2 = ColumnStageDTOFactory(column_id='column_2', stage_id='stage_id_2')
    return TaskBoardsDetailsDTO(
        board_dto=boards_dto,
        column_stage_dtos=[column1, column2],
        columns_dtos=column_dtos,
    )


def prepare_fields_and_actions_dto(mocker):

    path = 'ib_tasks.interactors.get_task_fields_and_actions.GetTaskFieldsAndActionsInteractor' \
           '.get_task_fields_and_action'
    mock_obj = mocker.patch(path)
    from ib_tasks.interactors.storage_interfaces.stage_dtos \
        import GetTaskStageCompleteDetailsDTO
    from ib_tasks.tests.factories.interactor_dtos import FieldDetailsDTOFactory
    FieldDetailsDTOFactory.reset_sequence()
    from ib_tasks.tests.factories.interactor_dtos import ActionDetailsDTOFactory
    ActionDetailsDTOFactory.reset_sequence()
    lst = [
        GetTaskStageCompleteDetailsDTO(
            task_id=1, stage_id="stage_1",
            field_dtos=[FieldDetailsDTOFactory()],
            action_dtos=[ActionDetailsDTOFactory()]
        )
    ]
    mock_obj.return_value = lst
    return mock_obj


def prepare_user_permitted_actions():
    from ib_tasks.tests.factories.storage_dtos import ActionDTOFactory
    ActionDTOFactory.reset_sequence()
    action_dtos = ActionDTOFactory.create_batch(size=2)
    return action_dtos


def prepare_fields_dto():
    from ib_tasks.tests.factories.interactor_dtos import FieldDisplayDTOFactory
    FieldDisplayDTOFactory.reset_sequence()
    field_dtos = FieldDisplayDTOFactory.create_batch(size=2)
    return field_dtos


def mock_user_action_on_task_method(mocker, mock_object):
    mock_method = mocker.patch(
        "ib_tasks.interactors.user_action_on_task_interactor.UserActionOnTaskInteractor.user_action_on_task"
    )
    mock_method.return_value = mock_object
    return mock_method
