def get_adhoc_template_fields_interactor_mock(mocker, response):
    mock = mocker.patch(
        'ib_adhoc_tasks.interactors.get_adhoc_task_template_fields_interactor.AdhocTaskTemplateFieldsInteractor.get_adhoc_task_template_fields'
    )
    mock.return_value = response


def get_group_by_interactor_mock(mocker, response):
    mock = mocker.patch(
        'ib_adhoc_tasks.interactors.group_by_interactor.GroupByInteractor.get_group_by'
    )
    mock.return_value = response


def get_add_group_by_interactor_mock(mocker, response):
    mock = mocker.patch(
        'ib_adhoc_tasks.interactors.group_by_interactor.GroupByInteractor.add_or_edit_group_by'
    )
    mock.return_value = response
