def get_valid_project_ids_mock(mocker):
    mock = mocker.patch(
        "ib_tasks.adapters.project_service.ProjectService."
        "get_valid_project_ids"
    )
    return mock
