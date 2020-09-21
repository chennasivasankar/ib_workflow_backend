from ib_tasks.interactors.presenter_interfaces.dtos import \
    AllTasksOverviewDetailsDTO
from ib_tasks.presenters.get_all_tasks_overview_for_user_presenter_impl import \
    GetAllTasksOverviewForUserPresenterImpl
from ib_tasks.tests.factories.presenter_dtos import \
    TaskIdWithStageDetailsDTOFactory, GetTaskStageCompleteDetailsDTOFactory, \
    TaskWithCompleteStageDetailsDTOFactory
from ib_tasks.tests.factories.storage_dtos import FieldDetailsDTOFactory, \
    StageActionDetailsDTOFactory


class TestGetAllTasksOverviewForUserPresenterImpl:
    def test_raise_exception_for_limit_less_than_zero(self):
        # Arrange
        from ib_tasks.constants.exception_messages import \
            LIMIT_SHOULD_BE_GREATER_THAN_ZERO
        expected_response = LIMIT_SHOULD_BE_GREATER_THAN_ZERO[0]
        response_status_code = LIMIT_SHOULD_BE_GREATER_THAN_ZERO[1]

        presenter = GetAllTasksOverviewForUserPresenterImpl()
        # Act
        response_object = presenter. \
            raise_limit_should_be_greater_than_zero_exception()
        # Assert
        import json
        response = json.loads(response_object.content)
        assert response['http_status_code'] == 400
        assert response['res_status'] == response_status_code
        assert response['response'] == expected_response

    def test_raise_exception_for_offset_less_than_zero(self):
        # Arrange
        from ib_tasks.constants.exception_messages import \
            OFFSET_SHOULD_BE_GREATER_THAN_ZERO
        expected_response = \
            OFFSET_SHOULD_BE_GREATER_THAN_ZERO[0]
        response_status_code = \
            OFFSET_SHOULD_BE_GREATER_THAN_ZERO[1]

        presenter = GetAllTasksOverviewForUserPresenterImpl()
        # Act
        response_object = presenter. \
            raise_offset_should_be_greater_than_zero_exception()
        # Assert
        import json
        response = json.loads(response_object.content)
        assert response['http_status_code'] == 400
        assert response['res_status'] == response_status_code
        assert response['response'] == expected_response

    def test_raise_exception_when_given_empty_stage_ids_list(self):
        # Arrange
        from ib_tasks.constants.exception_messages import \
            EMPTY_STAGE_IDS_ARE_INVALID
        expected_response = \
            EMPTY_STAGE_IDS_ARE_INVALID[0]
        response_status_code = \
            EMPTY_STAGE_IDS_ARE_INVALID[1]

        presenter = GetAllTasksOverviewForUserPresenterImpl()
        # Act
        response_object = presenter. \
            raise_stage_ids_empty_exception()
        # Assert
        import json
        response = json.loads(response_object.content)
        assert response['http_status_code'] == 400
        assert response['res_status'] == response_status_code
        assert response['response'] == expected_response

    def test_given_valid_details_get_all_tasks_overview_details_response(
            self, snapshot):
        # Arrange
        TaskIdWithStageDetailsDTOFactory.reset_sequence()
        GetTaskStageCompleteDetailsDTOFactory.reset_sequence()
        FieldDetailsDTOFactory.reset_sequence()
        StageActionDetailsDTOFactory.reset_sequence()
        TaskWithCompleteStageDetailsDTOFactory.reset_sequence()
        task_with_complete_stage_details_dtos = \
            TaskWithCompleteStageDetailsDTOFactory.create_batch(2)
        import factory
        task_fields_and_action_details_dtos = \
            GetTaskStageCompleteDetailsDTOFactory.create_batch(
                2, field_dtos=[FieldDetailsDTOFactory()], task_id=factory.Iterator([1, 2]),
                action_dtos=StageActionDetailsDTOFactory.create_batch(2))

        all_tasks_overview_details_dto = AllTasksOverviewDetailsDTO(
            task_with_complete_stage_details_dtos=
            task_with_complete_stage_details_dtos,
            task_fields_and_action_details_dtos=
            task_fields_and_action_details_dtos)

        presenter = GetAllTasksOverviewForUserPresenterImpl()
        # Act
        response_object = presenter.all_tasks_overview_details_response(
            all_tasks_overview_details_dto)

        # Assert
        import json
        response = json.loads(response_object.content)
        snapshot.assert_match(response, 'response')
