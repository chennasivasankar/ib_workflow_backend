
def mock_storage(mocker, task_template_ids):
    mock = mocker.patch(
        'ib_tasks.storages.tasks_storage_implementation.TasksStorageImplementation.get_valid_template_ids_in_given_template_ids'
    )
    mock.return_value = task_template_ids