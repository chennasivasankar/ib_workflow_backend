def get_valid_project_ids_mock(mocker):
    mock = mocker.patch(
        "ib_adhoc_tasks.adapters.iam_service.IamService.get_valid_project_ids"
    )
    return mock


def validate_task_template_id_mock(mocker):
    mock = mocker.patch(
        "ib_adhoc_tasks.adapters.task_service.TaskService.validate_task_template_id"
    )
    return mock


def get_user_role_ids_based_on_project_mock(mocker):
    mock = mocker.patch(
        "ib_adhoc_tasks.adapters.iam_service.IamService.get_user_role_ids_based_on_project"
    )
    return mock


def get_user_permitted_stage_ids_mock(mocker):
    mock = mocker.patch(
        "ib_adhoc_tasks.adapters.task_service.TaskService.get_user_permitted_stage_ids"
    )
    return mock


def get_user_role_ids_mock(mocker):
    mock = mocker.patch(
        "ib_adhoc_tasks.adapters.iam_service.IamService.get_user_role_ids_based_on_project"
    )
    return mock


def is_valid_user_id_for_given_project_mock(mocker):
    mock = mocker.patch(
        "ib_adhoc_tasks.adapters.iam_service.IamService.is_valid_user_id_for_given_project"
    )
    return mock


def validate_project_ids_for_kanban_view_mock(mocker):
    mock = mocker.patch(
        "ib_adhoc_tasks.adapters.iam_service.IamService"
        ".get_valid_project_ids"
    )
    from ib_adhoc_tasks.tests.factories.interactor_dtos import \
        GroupByInfoKanbanViewDTOFactory
    GroupByInfoKanbanViewDTOFactory.reset_sequence()
    group_by_info_kanban_view_dto = GroupByInfoKanbanViewDTOFactory()
    valid_project_ids = [group_by_info_kanban_view_dto.project_id]
    mock.return_value = valid_project_ids
    return mock


def get_stage_details_mock(mocker):
    mock = mocker.patch(
        "ib_adhoc_tasks.adapters.task_service.TaskService.get_stage_details"
    )
    return mock
