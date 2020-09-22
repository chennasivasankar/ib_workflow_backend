
def validate_project_ids_for_kanban_view_mock(mocker):
    mock = mocker.patch(
        "ib_adhoc_tasks.adapters.iam_service.IamService"
        ".get_valid_project_ids"
    )
    from ib_adhoc_tasks.tests.factories.interactor import \
        GroupByInfoKanbanViewDTOFactory
    GroupByInfoKanbanViewDTOFactory.reset_sequence()
    group_by_info_kanban_view_dto = GroupByInfoKanbanViewDTOFactory()
    valid_project_ids = [group_by_info_kanban_view_dto.project_id]
    mock.return_value = valid_project_ids
    return mock

