
def mock_storage(mocker, task_template_ids):
    mock = mocker.patch(
        'ib_tasks.storages.task_template_storage_implementation.TaskTemplateStorageImplementation.get_valid_template_ids_in_given_template_ids'
    )
    mock.return_value = task_template_ids


def mock_filter_tasks(mocker):
    mock = mocker.patch(
        'ib_tasks.storages.elasticsearch_storage_implementation.ElasticSearchStorageImplementation.filter_tasks'
    )
    mock.return_value = ([1, 2, 3], 3)
