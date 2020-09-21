def is_project_exists_mock(mocker):
    mock = mocker.patch(
        "ib_adhoc_tasks.adapters.iam_service.IAMService.is_project_exists"
    )
    return mock


def is_template_exists_mock(mocker):
    mock = mocker.patch(
        "ib_adhoc_tasks.adapters.task_service.TaskService.is_template_exists"
    )
    return mock


def get_user_role_ids_based_on_project_mock(mocker):
    mock = mocker.patch(
        "ib_adhoc_tasks.adapters.iam_service.IAMService.get_user_role_ids_based_on_project"
    )
    return mock


def get_stage_ids_based_on_user_roles_mock(mocker):
    mock = mocker.patch(
        "ib_adhoc_tasks.adapters.task_service.TaskService.get_stage_ids_based_on_user_roles"
    )
    return mock
