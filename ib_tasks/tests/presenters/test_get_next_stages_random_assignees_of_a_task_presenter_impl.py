import json

import factory
import pytest


class TestGetNextStagesRandomAssigneesOfATaskPresenterImpl:
    @pytest.fixture
    def presenter(self):
        from ib_tasks.presenters.get_next_stages_random_assignees_of_a_task_presenter_impl import \
            GetNextStagesRandomAssigneesOfATaskPresenterImpl
        return GetNextStagesRandomAssigneesOfATaskPresenterImpl()

    def test_with_invalid_task_display_id(self, presenter, snapshot):
        # Arrange
        from ib_tasks.exceptions.task_custom_exceptions import \
            InvalidTaskDisplayId
        task_display_id = "task_display_id"
        err = InvalidTaskDisplayId(task_display_id)

        # Act
        json_response = presenter.raise_invalid_task_display_id(err)

        # Assert
        json_json_response = json.loads(json_response.content)
        snapshot.assert_match(
            json_json_response['http_status_code'], 'http_status_code')
        snapshot.assert_match(json_json_response['res_status'], 'res_status')
        snapshot.assert_match(json_json_response['response'],
                              'json_response')

    def test_raise_invalid_action_id(self, presenter, snapshot):
        # Arrange
        action_id = 1
        from ib_tasks.exceptions.action_custom_exceptions import \
            InvalidActionException
        err = InvalidActionException(action_id)

        # Act
        json_response = presenter.raise_exception_for_invalid_action(action_id)

        # Assert
        json_json_response = json.loads(json_response.content)
        snapshot.assert_match(
            json_json_response['http_status_code'], 'http_status_code')
        snapshot.assert_match(json_json_response['res_status'], 'res_status')
        snapshot.assert_match(json_json_response['response'],
                              'json_response')

    def test_raise_users_not_exists_for_given_projects(self, presenter,
                                                       snapshot):
        # Arrange
        user_ids = ["user_1", "user_2"]

        # Act
        json_response = presenter.raise_users_not_exists_for_given_projects(
            user_ids=user_ids)

        # Assert
        json_json_response = json.loads(json_response.content)
        snapshot.assert_match(
            json_json_response['http_status_code'], 'http_status_code')
        snapshot.assert_match(json_json_response['res_status'], 'res_status')
        snapshot.assert_match(json_json_response['response'],
                              'json_response')

    def test_raise_invalid_key_error(self, presenter, snapshot):
        # Act
        json_response = presenter.raise_invalid_key_error()

        # Assert
        json_json_response = json.loads(json_response.content)
        snapshot.assert_match(
            json_json_response['http_status_code'], 'http_status_code')
        snapshot.assert_match(json_json_response['res_status'], 'res_status')
        snapshot.assert_match(json_json_response['response'],
                              'json_response')

    def test_raise_invalid_custom_logic_function_exception(
            self, presenter, snapshot):
        # Act
        json_response = presenter.raise_invalid_custom_logic_function_exception()

        # Assert
        json_json_response = json.loads(json_response.content)
        snapshot.assert_match(
            json_json_response['http_status_code'], 'http_status_code')
        snapshot.assert_match(json_json_response['res_status'], 'res_status')
        snapshot.assert_match(json_json_response['response'],
                              'json_response')

    def test_raise_invalid_path_not_found_exception(self, presenter, snapshot):
        path_name = "ib_tasks.populate.stage_ac.stage_1_action_name_1"
        # Act
        json_response = presenter.raise_invalid_path_not_found_exception(
            path_name=path_name)

        # Assert
        json_json_response = json.loads(json_response.content)
        snapshot.assert_match(
            json_json_response['http_status_code'], 'http_status_code')
        snapshot.assert_match(json_json_response['res_status'], 'res_status')
        snapshot.assert_match(json_json_response['response'],
                              'json_response')

    def test_raise_invalid_method_not_found_exception(
            self, presenter, snapshot):
        method_name = "stage_1_action_name_1"
        # Act
        json_response = presenter.raise_invalid_method_not_found_exception(
            method_name=method_name)

        # Assert
        json_json_response = json.loads(json_response.content)
        snapshot.assert_match(
            json_json_response['http_status_code'], 'http_status_code')
        snapshot.assert_match(json_json_response['res_status'], 'res_status')
        snapshot.assert_match(json_json_response['response'],
                              'json_response')

    def test_given_valid_details_get_expected_result(self, presenter,
                                                     snapshot):
        given_stage_ids = [2, 3]
        from ib_tasks.interactors.stages_dtos import \
            StageWithUserDetailsAndTeamDetailsDTO
        from ib_tasks.tests.factories.adapter_dtos import \
            UserIdWIthTeamDetailsDTOFactory, TeamDetailsDTOFactory
        from ib_tasks.tests.factories.interactor_dtos import \
            StageWithUserDetailsDTOFactory
        stage_with_user_details_and_team_details_dto = \
            StageWithUserDetailsAndTeamDetailsDTO(
                stages_with_user_details_dtos=
                StageWithUserDetailsDTOFactory.create_batch(
                    2, db_stage_id=factory.Iterator(given_stage_ids)),
                user_with_team_details_dtos=[
                    UserIdWIthTeamDetailsDTOFactory(
                        user_id="123e4567-e89b-12d3-a456-426614174000",
                        team_details=TeamDetailsDTOFactory(team_id='team_1')),
                    UserIdWIthTeamDetailsDTOFactory(
                        user_id="123e4567-e89b-12d3-a456-426614174001",
                        team_details=TeamDetailsDTOFactory(team_id='team_2'))])
        # Act
        json_response = presenter.get_next_stages_random_assignees_of_a_task_response(
            stage_with_user_details_and_team_details_dto=stage_with_user_details_and_team_details_dto)

        # Assert
        json_json_response = json.loads(json_response.content)
        snapshot.assert_match(json_json_response,
                              'json_response')
