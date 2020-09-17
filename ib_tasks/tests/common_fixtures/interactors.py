from typing import List

from ib_tasks.adapters.dtos import TaskBoardsDetailsDTO
from ib_tasks.tests.factories.storage_dtos import (
    StageActionDetailsDTOFactory)


def prepare_mock_for_next_stage_random_assignees(mocker):
    path = "ib_tasks.interactors" \
           ".GetNextStageRandomAssigneesOfTaskAndUpdateInDbInteractor" \
           ".get_random_assignees_of_next_stages_and_update_in_db"
    mock_obj = mocker.patch(path)
    return mock_obj


def prepare_get_field_ids_having_write_permission_for_user(mocker, field_ids):
    path = "ib_tasks.interactors.user_role_validation_interactor." \
           "UserRoleValidationInteractor" \
           ".get_field_ids_having_write_permission_for_user"
    mock_obj = mocker.patch(path)
    mock_obj.return_value = field_ids
    return mock_obj


def prepare_get_field_ids__user(mocker, user_roles):
    path = "ib_tasks.adapters.roles_service.RolesService.get_user_role_ids_based_on_project"
    mock_obj = mocker.patch(path)
    mock_obj.return_value = user_roles
    return mock_obj


def prepare_get_field_ids_having_permission_for_user_projects(mocker,
                                                              field_ids):
    path = "ib_tasks.interactors.user_role_validation_interactor." \
           "UserRoleValidationInteractor" \
           ".get_field_ids_having_permission_for_user"
    mock_obj = mocker.patch(path)
    mock_obj.return_value = field_ids
    return mock_obj


def prepare_get_stage_ids_for_user(mocker, stage_ids):
    path = "ib_tasks.interactors.user_role_validation_interactor." \
           "UserRoleValidationInteractor.get_permitted_stage_ids_given_user_id"
    mock_obj = mocker.patch(path)
    mock_obj.return_value = stage_ids
    return mock_obj


def prepare_get_permitted_action_ids(mocker, action_ids):
    path = "ib_tasks.interactors.user_role_validation_interactor." \
           "UserRoleValidationInteractor" \
           ".get_permitted_action_ids_for_given_user_id"
    mock_obj = mocker.patch(path)
    mock_obj.return_value = action_ids
    return mock_obj


def prepare_get_permitted_action_ids_for_project(mocker, action_ids):
    path = "ib_tasks.interactors.user_role_validation_interactor." \
           "UserRoleValidationInteractor" \
           ".get_permitted_action_ids_for_given_user_in_projects"
    mock_obj = mocker.patch(path)
    mock_obj.return_value = action_ids
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
    column1 = ColumnStageDTOFactory(column_id='column_1',
                                    stage_id='stage_id_1')
    column2 = ColumnStageDTOFactory(column_id='column_2',
                                    stage_id='stage_id_2')
    return TaskBoardsDetailsDTO(
            board_dto=boards_dto,
            column_stage_dtos=[column1, column2],
            columns_dtos=column_dtos,
    )


def prepare_fields_and_actions_dto(mocker):
    path = 'ib_tasks.interactors.get_task_fields_and_actions' \
           '.GetTaskFieldsAndActionsInteractor' \
           '.get_task_fields_and_action'
    mock_obj = mocker.patch(path)
    from ib_tasks.interactors.storage_interfaces.stage_dtos \
        import GetTaskStageCompleteDetailsDTO
    from ib_tasks.tests.factories.interactor_dtos import FieldDetailsDTOFactory
    FieldDetailsDTOFactory.reset_sequence()
    StageActionDetailsDTOFactory.reset_sequence()
    from ib_tasks.tests.factories.interactor_dtos import \
        ActionDetailsDTOFactory
    ActionDetailsDTOFactory.reset_sequence()
    lst = [
            GetTaskStageCompleteDetailsDTO(
                    task_id=1, stage_id="stage_1",
                    stage_color="blue",
                    db_stage_id=1,
                    display_name='display_name',
                    field_dtos=[FieldDetailsDTOFactory()],
                    action_dtos=[StageActionDetailsDTOFactory()]
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
            "ib_tasks.interactors.user_action_on_task_interactor"
            ".UserActionOnTaskInteractor.act_on_task"
    )
    mock_method.return_value = mock_object
    return mock_method


def prepare_task_ids_with_stage_ids(
        mocker, stage_ids_dto, fields_and_actions, stage_ids):
    mock = mocker.patch(
            'ib_tasks.interactors'
            '.get_valid_task_ids_for_user_based_on_stage_ids'
            '.GetTaskIdsOfUserBasedOnStagesInteractor'
            '.get_task_ids_of_user_based_on_stage_ids')
    mock.return_value = stage_ids_dto
    mock = mocker.patch(
            'ib_tasks.interactors.get_task_fields_and_actions'
            '.GetTaskFieldsAndActionsInteractor.get_task_fields_and_action')
    mock.return_value = fields_and_actions

    mock = mocker.patch(
            'ib_tasks.interactors.get_allowed_stage_ids_of_user_interactor'
            '.GetAllowedStageIdsOfUserInteractor'
            '.get_allowed_stage_ids_of_user')
    mock = stage_ids


def prepare_mock_for_filters_interactor(mocker):
    mock = mocker.patch(
            'ib_tasks.interactors'
            '.get_task_ids_by_applying_filters_with_stage_ids'
            '.GetTaskIdsBasedOnUserFiltersInColumns'
            '.get_task_ids_by_applying_filters')
    return mock


def prepare_assignees_interactor_mock(mocker):
    mock = mocker.patch(
            'ib_tasks.interactors.get_stages_assignees_details_interactor'
            '.GetStagesAssigneesDetailsInteractor'
            '.get_stages_assignee_details_by_given_task_ids'
    )
    return mock


def prepare_fields_for_get_task_fields_and_actions(mocker, fields_dtos,
                                                   task_stage_dtos):
    mock = mocker.patch('ib_tasks.interactors.get_task_fields'
                        '.GetTaskFieldsInteractor.get_task_fields')
    mock.return_value = fields_dtos, task_stage_dtos


def prepare_actions_for_get_task_fields_and_actions(mocker, action_dtos):
    mock = mocker.patch(
        'ib_tasks.interactors.get_task_actions.GetTaskActionsInteractor'
        '.get_task_actions')
    mock.return_value = action_dtos


def get_gof_ids_having_read_permission_for_user_mock(mocker):
    mock_method = mocker.patch(
        "ib_tasks.interactors.user_role_validation_interactor."
        "UserRoleValidationInteractor."
        "get_gof_ids_having_read_permission_for_user")
    gof_ids = ["gof_1", "gof_2"]
    mock_method.return_value = gof_ids
    return mock_method


def get_field_ids_having_read_permission_for_user_mock(mocker):
    mock_method = mocker.patch(
        "ib_tasks.interactors.user_role_validation_interactor."
        "UserRoleValidationInteractor."
        "get_field_ids_having_read_permission_for_user")
    field_ids = ['field0', 'field1', 'field2', 'field3']
    mock_method.return_value = field_ids
    return mock_method


def get_user_permitted_stage_ids_in_given_stage_ids_mock(
        mocker, stage_ids: List[int]):
    path = "ib_tasks.interactors.user_role_validation_interactor." \
           "UserRoleValidationInteractor." \
           "get_user_permitted_stage_ids_in_given_stage_ids"
    mock_obj = mocker.patch(path)
    mock_obj.return_value = stage_ids
    return mock_obj
