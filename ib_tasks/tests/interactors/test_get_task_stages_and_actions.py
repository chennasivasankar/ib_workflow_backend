from unittest.mock import create_autospec

import pytest

from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskIdException
from ib_tasks.interactors.get_task_stages_and_actions import \
    GetTaskStagesAndActions
from ib_tasks.interactors.storage_interfaces.fields_storage_interface import \
    FieldsStorageInterface
from ib_tasks.tests.factories.storage_dtos import ActionDetailsDTOFactory, \
    StageDetailsDTOFactory


class TestGetTaskStagesAndActions:

    @pytest.fixture()
    def get_stage_actions(self):
        ActionDetailsDTOFactory.reset_sequence()
        actions = ActionDetailsDTOFactory.create_batch(size=2, stage_id="stage_id_0")
        actions.append(ActionDetailsDTOFactory(stage_id="stage_id_1"))
        actions.append(ActionDetailsDTOFactory(stage_id="stage_id_2"))
        return actions

    @pytest.fixture()
    def get_stage_details(self):
        StageDetailsDTOFactory.reset_sequence()
        return StageDetailsDTOFactory.create_batch(size=3)

    @pytest.fixture()
    def get_stage_actions_for_one_stage(self):
        ActionDetailsDTOFactory.reset_sequence()
        actions = ActionDetailsDTOFactory.create_batch(size=2, stage_id="stage_id_0")
        return actions

    @pytest.fixture()
    def get_stage_details_for_one_stage(self):
        StageDetailsDTOFactory.reset_sequence()
        return [StageDetailsDTOFactory()]

    def test_given_task_id_returns_task_related_stages_and_their_actions(
            self, snapshot,
            get_stage_actions,
            get_stage_details):
        # Arrange
        task_id = 1
        storage = create_autospec(FieldsStorageInterface)
        storage.validate_task_id.return_value = True
        storage.get_task_stages.return_value = ["stage_id_0", "stage_id_1", "stage_id_2"]
        storage.get_actions_details.return_value = get_stage_actions
        storage.get_stage_complete_details.return_value = get_stage_details
        interactor = GetTaskStagesAndActions(storage=storage)

        # Act
        response = interactor.get_task_stages_and_actions(
            task_id=task_id,
            user_id="123e4567-e89b-12d3-a456-426614174000")

        # Assert
        snapshot.assert_match(response, "response")

    def test_given_task_id_with_one_stage_returns_stage_and_their_actions(
            self, snapshot,
            get_stage_actions_for_one_stage,
            get_stage_details_for_one_stage):
        # Arrange
        task_id = 1
        storage = create_autospec(FieldsStorageInterface)
        storage.validate_task_id.return_value = True
        storage.get_task_stages.return_value = ["stage_id_0"]
        storage.get_actions_details.return_value = get_stage_actions_for_one_stage
        storage.get_stage_complete_details.return_value = get_stage_details_for_one_stage
        interactor = GetTaskStagesAndActions(storage=storage)

        # Act
        response = interactor.get_task_stages_and_actions(
            task_id=task_id,
            user_id="123e4567-e89b-12d3-a456-426614174000")

        # Assert
        snapshot.assert_match(response, "response")

    def test_given_task_id_but_task_has_no_actions_returns_actions_as_empty_list(
            self, snapshot, get_stage_details):
        # Arrange
        task_id = 1
        storage = create_autospec(FieldsStorageInterface)
        storage.validate_task_id.return_value = True
        storage.get_task_stages.return_value = ["stage_id_0", "stage_id_1", "stage_id_2"]
        storage.get_actions_details.return_value = []
        storage.get_stage_complete_details.return_value = get_stage_details
        interactor = GetTaskStagesAndActions(storage=storage)

        # Act
        response = interactor.get_task_stages_and_actions(
            task_id=task_id,
            user_id="123e4567-e89b-12d3-a456-426614174000")

        # Assert
        snapshot.assert_match(response, "response")

    def test_given_task_id_with_one_stage_without_no_actions_returns_actions_as_empty_list(
            self, snapshot, get_stage_details):
        # Arrange
        task_id = 1
        storage = create_autospec(FieldsStorageInterface)
        storage.validate_task_id.return_value = True
        storage.get_task_stages.return_value = ["stage_id_0"]
        storage.get_actions_details.return_value = []
        storage.get_stage_complete_details.return_value = get_stage_details
        interactor = GetTaskStagesAndActions(storage=storage)

        # Act
        response = interactor.get_task_stages_and_actions(
            task_id=task_id,
            user_id="123e4567-e89b-12d3-a456-426614174000")

        # Assert
        snapshot.assert_match(response, "response")

    def test_validate_task_id_given_invalid_task_id_raises_exception(self):
        # Arrange
        task_id = 1
        storage = create_autospec(FieldsStorageInterface)
        storage.validate_task_id.return_value = False
        interactor = GetTaskStagesAndActions(storage=storage)

        # Act
        with pytest.raises(InvalidTaskIdException) as error:
            interactor.get_task_stages_and_actions(
                task_id=task_id, user_id="123e4567-e89b-12d3-a456-426614174000")

        # Assert
        storage.validate_task_id.assert_called_once_with(task_id)
