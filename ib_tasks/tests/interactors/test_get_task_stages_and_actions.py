from unittest.mock import create_autospec

import pytest

from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskIdException
from ib_tasks.interactors.get_task_stages_and_actions import \
    GetTaskStagesAndActions
from ib_tasks.interactors.storage_interfaces.action_storage_interface import \
    ActionStorageInterface
from ib_tasks.interactors.storage_interfaces.fields_storage_interface import \
    FieldsStorageInterface
from ib_tasks.interactors.storage_interfaces.storage_interface import \
    StorageInterface
from ib_tasks.tests.common_fixtures.adapters.roles_service import \
    get_user_role_ids
from ib_tasks.tests.factories.storage_dtos import StageDetailsDTOFactory, \
    StageActionDetailsDTOFactory


class TestGetTaskStagesAndActions:

    @pytest.fixture()
    def get_stage_actions(self):
        StageActionDetailsDTOFactory.reset_sequence()
        actions = StageActionDetailsDTOFactory.create_batch(
            size=3, stage_id="stage_id_0")
        actions.append(StageActionDetailsDTOFactory(stage_id="stage_id_1"))
        actions.append(StageActionDetailsDTOFactory(stage_id="stage_id_1"))
        actions.append(StageActionDetailsDTOFactory(stage_id="stage_id_2"))
        actions.append(StageActionDetailsDTOFactory(stage_id="stage_id_2"))
        return actions

    @pytest.fixture()
    def get_stage_details(self):
        StageDetailsDTOFactory.reset_sequence()
        return StageDetailsDTOFactory.create_batch(size=3)

    @pytest.fixture()
    def get_stage_actions_for_one_stage(self):
        StageActionDetailsDTOFactory.reset_sequence(1)
        actions = StageActionDetailsDTOFactory.create_batch(size=2,
                                                            stage_id="stage_id_0")
        return actions

    @pytest.fixture()
    def get_stage_details_for_one_stage(self):
        StageDetailsDTOFactory.reset_sequence()
        return [StageDetailsDTOFactory()]

    @pytest.fixture()
    def get_user_roles(self):
        user_roles = ["FIN_PAYMENT_REQUESTER",
                      "FIN_PAYMENT_POC",
                      "FIN_PAYMENT_APPROVER",
                      "FIN_PAYMENTS_RP",
                      "FIN_FINANCE_RP"]
        return user_roles

    def test_when_user_has_permissions_get_stage_actions(
            self, snapshot,
            mocker,
            get_stage_actions,
            get_stage_details,
            get_user_roles):
        # Arrange
        task_id = 1
        user_roles = get_user_roles
        user_roles_mock = get_user_role_ids(mocker)
        user_roles_mock.return_value = user_roles
        storage = create_autospec(FieldsStorageInterface)
        action_storage = create_autospec(ActionStorageInterface)
        task_storage = create_autospec(StorageInterface)
        storage.get_task_stages.return_value = [
            "stage_id_0", "stage_id_1", "stage_id_2"]
        action_storage.get_actions_details.return_value = get_stage_actions
        storage.get_stage_complete_details.return_value = get_stage_details
        interactor = GetTaskStagesAndActions(storage=storage,
                                             task_storage=task_storage,
                                             action_storage=action_storage)

        # Act
        response = interactor.get_task_stages_and_actions(task_id=task_id,
                                                          user_id="user_id_1")

        # Assert
        snapshot.assert_match(response, "response")

    def test_when_user_has_no_permissions_returns_empty_actions(
            self, snapshot,
            mocker,
            get_user_roles,
            get_stage_details,
            get_stage_actions):
        # Arrange
        task_id = 1
        user_roles = get_user_roles
        user_roles_mock = get_user_role_ids(mocker)
        user_roles_mock.return_value = user_roles
        storage = create_autospec(FieldsStorageInterface)
        task_storage = create_autospec(StorageInterface)
        action_storage = create_autospec(ActionStorageInterface)
        task_storage.validate_task_id.return_value = True
        storage.get_task_stages.return_value = ["stage_id_0", "stage_id_1",
                                                "stage_id_2"]
        action_storage.get_actions_details.return_value = get_stage_actions
        storage.get_task_stages.return_value = [
            "stage_id_0", "stage_id_1", "stage_id_2"]
        action_storage.get_actions_details.return_value = []
        storage.get_stage_complete_details.return_value = get_stage_details
        interactor = GetTaskStagesAndActions(storage=storage,
                                             task_storage=task_storage,
                                             action_storage=action_storage)

        # Act
        response = interactor.get_task_stages_and_actions(
            task_id=task_id,
            user_id="123e4567-e89b-12d3-a456-426614174000")

        # Assert
        snapshot.assert_match(response, "response")

    def test_given_task_id_with_one_stage_returns_stage_and_their_actions(
            self, snapshot,
            mocker, get_user_roles,
            get_stage_actions_for_one_stage,
            get_stage_details_for_one_stage):
        # Arrange
        task_id = 1
        storage = create_autospec(FieldsStorageInterface)
        task_storage = create_autospec(StorageInterface)
        action_storage = create_autospec(ActionStorageInterface)
        task_storage.validate_task_id.return_value = True
        user_roles = get_user_roles
        user_roles_mock = get_user_role_ids(mocker)
        user_roles_mock.return_value = user_roles
        storage.get_task_stages.return_value = ["stage_id_0"]
        action_storage.get_actions_details.return_value = get_stage_actions_for_one_stage
        storage.get_stage_complete_details.return_value = get_stage_details_for_one_stage
        interactor = GetTaskStagesAndActions(storage=storage,
                                             task_storage=task_storage,
                                             action_storage=action_storage)

        # Act
        response = interactor.get_task_stages_and_actions(
            task_id=task_id,
            user_id="123e4567-e89b-12d3-a456-426614174000")

        # Assert
        snapshot.assert_match(response, "response")

    def test_given_task_id_but_task_has_no_actions_returns_actions_as_empty_list(
            self, mocker, get_user_roles, snapshot, get_stage_details):
        # Arrange
        task_id = 1
        storage = create_autospec(FieldsStorageInterface)
        task_storage = create_autospec(StorageInterface)
        action_storage = create_autospec(ActionStorageInterface)
        task_storage.validate_task_id.return_value = True
        user_roles = get_user_roles
        user_roles_mock = get_user_role_ids(mocker)
        user_roles_mock.return_value = user_roles
        storage.get_task_stages.return_value = ["stage_id_0", "stage_id_1",
                                                "stage_id_2"]
        action_storage.get_actions_details.return_value = []
        storage.get_stage_complete_details.return_value = get_stage_details
        interactor = GetTaskStagesAndActions(storage=storage,
                                             task_storage=task_storage,
                                             action_storage=action_storage)

        # Act
        response = interactor.get_task_stages_and_actions(
            task_id=task_id,
            user_id="123e4567-e89b-12d3-a456-426614174000")
        response = interactor.get_task_stages_and_actions(task_id=task_id,
                                                          user_id="user_id_1")

        # Assert
        snapshot.assert_match(response, "response")

    def test_given_task_id_with_one_stage_without_no_actions_returns_actions_as_empty_list(
            self, mocker, get_user_roles, snapshot, get_stage_details):
        # Arrange
        task_id = 1
        user_roles = get_user_roles
        user_roles_mock = get_user_role_ids(mocker)
        user_roles_mock.return_value = user_roles
        storage = create_autospec(FieldsStorageInterface)
        action_storage = create_autospec(ActionStorageInterface)
        task_storage = create_autospec(StorageInterface)
        task_storage.validate_task_id.return_value = True
        storage.get_task_stages.return_value = ["stage_id_0"]
        action_storage.get_actions_details.return_value = []
        storage.get_stage_complete_details.return_value = get_stage_details
        interactor = GetTaskStagesAndActions(storage=storage,
                                             task_storage=task_storage,
                                             action_storage=action_storage)

        # Act
        response = interactor.get_task_stages_and_actions(
            task_id=task_id,
            user_id="123e4567-e89b-12d3-a456-426614174000")

        # Assert
        snapshot.assert_match(response, "response")

    def test_validate_task_id_given_invalid_task_id_raises_exception(
            self, mocker, get_user_roles):
        # Arrange
        task_id = 1
        user_roles = get_user_roles
        user_roles_mock = get_user_role_ids(mocker)
        user_roles_mock.return_value = user_roles
        storage = create_autospec(FieldsStorageInterface)
        action_storage = create_autospec(ActionStorageInterface)
        task_storage = create_autospec(StorageInterface)
        task_storage.validate_task_id.return_value = False
        interactor = GetTaskStagesAndActions(storage=storage,
                                             task_storage=task_storage,
                                             action_storage=action_storage)

        # Act
        with pytest.raises(InvalidTaskIdException) as error:
            interactor.get_task_stages_and_actions(
                task_id=task_id,
                user_id="123e4567-e89b-12d3-a456-426614174000")

        # Assert
        task_storage.validate_task_id.assert_called_once_with(task_id)
