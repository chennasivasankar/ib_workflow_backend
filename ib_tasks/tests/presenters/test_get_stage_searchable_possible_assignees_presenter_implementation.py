import pytest


class TestGetStageSearchablePossibleAssigneesPresenterImplementation:

    @pytest.fixture()
    def presenter(self):
        from ib_tasks.presenters.\
            get_stage_searchable_possible_assignees_presenter_implementation \
            import GetStageSearchablePossibleAssigneesPresenterImplementation

        presenter = \
            GetStageSearchablePossibleAssigneesPresenterImplementation()
        return presenter

    def test_raise_invalid_offset_exception(self, snapshot, presenter):
        # Act
        response_object = presenter.raise_invalid_offset_exception()

        # Assert
        import json
        response = json.loads(response_object.content)
        snapshot.assert_match(response['http_status_code'], 'http_status_code')
        snapshot.assert_match(response['res_status'], 'res_status')
        snapshot.assert_match(response['response'], 'response')

    def test_raise_invalid_limit_exception(self, snapshot, presenter):
        # Act
        response_object = presenter.raise_invalid_limit_exception()

        # Assert
        import json
        response = json.loads(response_object.content)
        snapshot.assert_match(response['http_status_code'], 'http_status_code')
        snapshot.assert_match(response['res_status'], 'res_status')
        snapshot.assert_match(response['response'], 'response')

    def test_raise_invalid_stage_id_exception(self, snapshot, presenter):
        # Arrange
        stage_id = 100
        from ib_tasks.exceptions.stage_custom_exceptions import InvalidStageId
        err = InvalidStageId(stage_id)

        # Act
        response_object = presenter.raise_invalid_stage_id_exception(err)

        # Assert
        import json
        response = json.loads(response_object.content)
        snapshot.assert_match(response['http_status_code'], 'http_status_code')
        snapshot.assert_match(response['res_status'], 'res_status')
        snapshot.assert_match(response['response'], 'response')

    def test_get_stage_assignee_details_response(self, snapshot, presenter):
        # Arrange
        from ib_tasks.tests.factories.interactor_dtos import \
            UserDetailsDTOFactory
        UserDetailsDTOFactory.reset_sequence()
        user_details_dtos = UserDetailsDTOFactory.create_batch(size=3)

        # Act
        response_object = presenter.get_stage_assignee_details_response(
            user_details_dtos=user_details_dtos
        )

        # Assert
        import json
        response = json.loads(response_object.content)
        snapshot.assert_match(response, 'user_details')

    def test_get_stage_assignee_details_response_when_no_assignees_returns_empty_list(
            self, snapshot, presenter):
        # Arrange
        user_details_dtos = []

        # Act
        response_object = presenter.get_stage_assignee_details_response(
            user_details_dtos=user_details_dtos
        )

        # Assert
        import json
        response = json.loads(response_object.content)
        snapshot.assert_match(response, 'user_details')
