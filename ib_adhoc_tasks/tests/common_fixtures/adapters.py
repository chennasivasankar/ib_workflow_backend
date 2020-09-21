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
