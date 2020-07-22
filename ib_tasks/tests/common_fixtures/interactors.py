from ib_tasks.adapters.dtos import TaskBoardsDetailsDTO




def prepare_gof_and_status_variables_dto():
    from ib_tasks.interactors.dtos import TaskGofAndStatusesDTO

    from ib_tasks.tests.factories.storage_dtos import (
        FieldValueDTOFactory, StatusVariableDTOFactory,
        GroupOfFieldsDTOFactory
    )
    GroupOfFieldsDTOFactory.reset_sequence()
    FieldValueDTOFactory.reset_sequence()
    StatusVariableDTOFactory.reset_sequence()
    group_of_fields = [GroupOfFieldsDTOFactory()]
    fields = [FieldValueDTOFactory()]
    statuses = [StatusVariableDTOFactory()]
    task_dto = TaskGofAndStatusesDTO(
        task_id="task_1",
        group_of_fields_dto=group_of_fields,
        fields_dto=fields,
        statuses_dto=statuses
    )
    return task_dto


def prepare_stage_ids_call_action_logic_update_stages(mocker):

    path = "ib_tasks.interactors.call_action_logic_function_and_update_task_status_variables_interactor" \
           ".CallActionLogicFunctionAndUpdateTaskStatusVariablesInteractor" \
           ".call_action_logic_function_and_update_task_status_variables"
    print(path)
    mock_obj = mocker.patch(path)
    mock_obj.return_value = ['stage_1', "stage_2"]
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
    column_fields = ColumnFieldDTOFactory.create_batch(size=2)
    return TaskBoardsDetailsDTO(
        board_dto=boards_dto,
        column_stage_dtos=columns_stage_dtos,
        columns_dtos=column_dtos,
        columns_fields_dtos=column_fields
    )


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
