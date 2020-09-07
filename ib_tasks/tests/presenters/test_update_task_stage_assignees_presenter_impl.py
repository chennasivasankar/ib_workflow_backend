import json

import pytest


class TestUpdateTaskStageAssigneesPresenterImplementation:
    @pytest.fixture
    def presenter(self):
        from ib_tasks.presenters.update_task_stage_assignees_presenter_impl import \
            UpdateTaskStageAssigneesPresenterImplementation
        return UpdateTaskStageAssigneesPresenterImplementation()

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

    def test_with_duplicate_stage_ids(self, presenter, snapshot):
        # Arrange
        duplicate_stage_ids = [2, 2]
        # Act
        json_response = presenter.raise_duplicate_stage_ids_not_valid(
            duplicate_stage_ids=duplicate_stage_ids)
        # Assert
        json_json_response = json.loads(json_response.content)
        snapshot.assert_match(
            json_json_response['http_status_code'], 'http_status_code')
        snapshot.assert_match(json_json_response['res_status'], 'res_status')
        snapshot.assert_match(json_json_response['response'],
                              'json_response')

    def test_given_invalid_stage_ids_raise_exception(self, presenter,
                                                     snapshot):
        # Arrange
        invalid_stage_ids = [1, 2]
        # Act
        json_response = presenter.raise_invalid_stage_ids_exception(
            invalid_stage_ids=invalid_stage_ids)
        # Assert
        json_json_response = json.loads(json_response.content)
        snapshot.assert_match(
            json_json_response['http_status_code'], 'http_status_code')
        snapshot.assert_match(json_json_response['res_status'], 'res_status')
        snapshot.assert_match(json_json_response['response'],
                              'json_response')

    def test_given_virtual_stageids_raise_exception(self, presenter,
                                                    snapshot):
        # Arrange
        virtual_stage_ids = [1, 2]
        # Act
        json_response = presenter.raise_virtual_stage_ids_exception(
            virtual_stage_ids=virtual_stage_ids)
        # Assert
        json_json_response = json.loads(json_response.content)
        snapshot.assert_match(
            json_json_response['http_status_code'], 'http_status_code')
        snapshot.assert_match(json_json_response['res_status'], 'res_status')
        snapshot.assert_match(json_json_response['response'],
                              'json_response')

    def test_raise_invalid_user_id_exception(self, presenter, snapshot):
        # Arrange
        user_id = "assignee_1"
        # Act
        json_response = presenter.raise_invalid_user_id_exception()
        # Assert
        json_json_response = json.loads(json_response.content)
        snapshot.assert_match(
            json_json_response['http_status_code'], 'http_status_code')
        snapshot.assert_match(json_json_response['res_status'], 'res_status')
        snapshot.assert_match(json_json_response['response'],
                              'json_response')

    def test_raise_stage_ids_with_invalid_permission_for_assignee_exception(
            self, presenter, snapshot):
        # Arrange
        invalid_stage_ids = [1, 2]
        # Act
        json_response = presenter. \
            raise_stage_ids_with_invalid_permission_for_assignee_exception(
            invalid_stage_ids=invalid_stage_ids)
        # Assert
        json_json_response = json.loads(json_response.content)
        snapshot.assert_match(
            json_json_response['http_status_code'], 'http_status_code')
        snapshot.assert_match(json_json_response['res_status'], 'res_status')
        snapshot.assert_match(json_json_response['response'],
                              'json_response')
