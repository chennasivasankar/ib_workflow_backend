"""
Created on: 14/07/20
Author: Pavankumar Pamuru

"""


def adapter_mock(mocker):

    mock = mocker.patch(
        'ib_boards.adapters.task_service.TaskService.validate_task_template_ids'
    )
    from ib_boards.exceptions.custom_exceptions import \
        InvalidTaskTemplateIdInStages
    mock.side_effect = InvalidTaskTemplateIdInStages(task_template_id='Invalid')
    return mock


def adapter_mock_for_task_template_stages(mocker):
    mock = mocker.patch(
        'ib_boards.adapters.task_service.TaskService.validate_task_template_stages_with_id'
    )

    from ib_boards.exceptions.custom_exceptions import \
        TaskTemplateStagesNotBelongsToTastTemplateId
    mock.side_effect = TaskTemplateStagesNotBelongsToTastTemplateId
    return mock