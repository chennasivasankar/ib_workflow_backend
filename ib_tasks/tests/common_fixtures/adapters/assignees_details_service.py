def assignee_details_dtos_mock(mocker):
    path = "ib_tasks.adapters.assignees_details_service" \
           ".AssigneeDetailsService.get_assignees_details_dtos"
    mock = mocker.patch(path)
    from ib_tasks.tests.factories.adapter_dtos import AssigneeDetailsDTOFactory
    AssigneeDetailsDTOFactory.reset_sequence()
    assignee_details_dtos = [
        AssigneeDetailsDTOFactory(),
        AssigneeDetailsDTOFactory(),
        AssigneeDetailsDTOFactory()
    ]
    mock.return_value = assignee_details_dtos
    return mock


def get_assignee_details_dtos_mock(mocker, api_user):
    path = "ib_tasks.adapters.assignees_details_service" \
           ".AssigneeDetailsService.get_assignees_details_dtos"
    mock = mocker.patch(path)
    from ib_tasks.tests.factories.adapter_dtos import AssigneeDetailsDTOFactory
    AssigneeDetailsDTOFactory.reset_sequence()
    assignee_details_dtos = [
        AssigneeDetailsDTOFactory(
            assignee_id=api_user
        ),
        AssigneeDetailsDTOFactory(
            assignee_id="123e4567-e89b-12d3-a456-426614174001"
        ),
        AssigneeDetailsDTOFactory(
            assignee_id="123e4567-e89b-12d3-a456-426614174002"
        ),
        AssigneeDetailsDTOFactory(
            assignee_id="123e4567-e89b-12d3-a456-426614174003"
        )
    ]
    mock.return_value = assignee_details_dtos
    return mock
