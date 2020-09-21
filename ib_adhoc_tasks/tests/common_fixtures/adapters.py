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
