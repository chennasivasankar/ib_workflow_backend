def get_valid_project_ids_mock(mocker):
    mock = mocker.patch(
        "ib_adhoc_tasks.adapters.iam_service.IamService.get_valid_project_ids"
    )
    return mock


def validate_task_template_id_mock(mocker):
    mock = mocker.patch(
        "ib_adhoc_tasks.adapters.task_interface.TaskService.validate_task_template_id"
    )
    return mock


def get_user_permitted_stage_ids_mock(mocker):
    mock = mocker.patch(
        "ib_adhoc_tasks.adapters.task_interface.TaskService.get_user_permitted_stage_ids"
    )
    return mock


def get_user_role_ids_mock(mocker):
    mock = mocker.patch(
        "ib_adhoc_tasks.adapters.iam_service.IamService.get_user_role_ids"
    )
    return mock
