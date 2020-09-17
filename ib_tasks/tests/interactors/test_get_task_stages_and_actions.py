from unittest.mock import create_autospec

import pytest

from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskIdException
from ib_tasks.interactors.get_task_stages_and_actions import \
    GetTaskStagesAndActions
from ib_tasks.interactors.storage_interfaces.action_storage_interface import \
    ActionStorageInterface
from ib_tasks.interactors.storage_interfaces.fields_storage_interface import \
    FieldsStorageInterface
from ib_tasks.interactors.storage_interfaces.stages_storage_interface import \
    StageStorageInterface
from ib_tasks.interactors.storage_interfaces.storage_interface import \
    StorageInterface
from ib_tasks.tests.common_fixtures.adapters.roles_service import \
    (get_user_role_ids, get_user_role_ids_based_on_project_mock)
from ib_tasks.tests.common_fixtures.interactors import \
    prepare_get_permitted_action_ids
from ib_tasks.tests.factories.storage_dtos import (StageDetailsDTOFactory,
                                                   StageActionDetailsDTOFactory)
from ib_tasks.tests.interactors.storage_method_mocks import StorageMethodsMock
from unittest.mock import create_autospec

import pytest

from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskIdException
from ib_tasks.interactors.get_task_stages_and_actions import \
    GetTaskStagesAndActions
from ib_tasks.interactors.storage_interfaces.action_storage_interface import \
    ActionStorageInterface
from ib_tasks.interactors.storage_interfaces.fields_storage_interface import \
    FieldsStorageInterface
from ib_tasks.interactors.storage_interfaces.stages_storage_interface import \
    StageStorageInterface
from ib_tasks.interactors.storage_interfaces.storage_interface import \
    StorageInterface
from ib_tasks.tests.common_fixtures.adapters.roles_service import \
    (get_user_role_ids, get_user_role_ids_based_on_project_mock)
from ib_tasks.tests.common_fixtures.interactors import \
    prepare_get_permitted_action_ids
from ib_tasks.tests.factories.storage_dtos import (StageDetailsDTOFactory,
                                                   StageActionDetailsDTOFactory)
from ib_tasks.tests.interactors.storage_method_mocks import StorageMethodsMock


class TestGetTaskStagesAndActions(StorageMethodsMock):

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

    @pytest.fixture
    def stage_storage(self):
        return create_autospec(StageStorageInterface)

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

    @pytest.fixture
    def interactor(self, action_storage, storage_mock,
                   field_storage, stage_storage):
        interactor = GetTaskStagesAndActions(storage=field_storage,
                                             stage_storage=stage_storage,
                                             task_storage=storage_mock,
                                             action_storage=action_storage)
        return interactor

    def test_validate_task_id_given_invalid_task_id_raises_exception(
            self, mocker, get_user_roles, stage_storage, field_storage,
            storage_mock, action_storage, interactor):
        # Arrange
        task_id = 1
        user_roles = get_user_roles
        user_roles_mock = get_user_role_ids(mocker)
        user_roles_mock.return_value = user_roles
        storage_mock.validate_task_id.return_value = False

        # Act
        with pytest.raises(InvalidTaskIdException) as error:
            interactor.get_task_stages_and_actions(
                task_id=task_id,
                user_id="123e4567-e89b-12d3-a456-426614174000")

        # Assert
        storage_mock.validate_task_id.assert_called_once_with(task_id)

    def test_when_user_has_permissions_get_stage_actions(
            self, snapshot, interactor,
            mocker, field_storage, action_storage, storage_mock,
            stage_storage,
            get_stage_actions,
            get_stage_details,
            get_user_roles):
        # Arrange
        task_id = 1
        action_ids = [1, 2, 3, 4]
        stage_ids = ["stage_id_0", "stage_id_1", "stage_id_2"]
        user_roles = get_user_roles

        get_user_role_ids_based_on_project_mock(mocker)
        user_roles_mock = get_user_role_ids(mocker)
        user_roles_mock.return_value = user_roles

        field_storage.get_task_stages.return_value = [
            "stage_id_0", "stage_id_1", "stage_id_2"]
        stage_storage.get_permitted_stage_ids_given_stage_ids. \
            return_value = stage_ids
        prepare_get_permitted_action_ids(mocker, action_ids=action_ids)
        action_storage.get_actions_details.return_value = \
            get_stage_actions
        field_storage.get_stage_complete_details.return_value = \
            get_stage_details

        # Act
        response = interactor.get_task_stages_and_actions(task_id=task_id,
                                                          user_id="user_id_1")

        # Assert
        field_storage.get_task_stages.assert_called_once_with(task_id)
        action_storage.get_actions_details.assert_called_once_with(
            action_ids)
        field_storage.get_stage_complete_details.assert_called_once_with(
            stage_ids)
        snapshot.assert_match(response, "response")

    def test_when_user_has_no_permissions_returns_empty_actions(
            self, snapshot,
            mocker, field_storage, storage_mock, action_storage,
            stage_storage, interactor,
            get_user_roles,
            get_stage_details,
            get_stage_actions):
        # Arrange
        task_id = 1
        user_roles = get_user_roles
        stage_ids = [
            "stage_id_0", "stage_id_1", "stage_id_2"]

        user_roles_mock = get_user_role_ids(mocker)
        user_roles_mock.return_value = user_roles
        get_user_role_ids_based_on_project_mock(mocker)

        storage_mock.validate_task_id.return_value = True
        field_storage.get_task_stages.return_value = \
            ["stage_id_0", "stage_id_1", "stage_id_2"]
        action_storage.get_actions_details.return_value = \
            get_stage_actions
        field_storage.get_task_stages.return_value = stage_ids
        stage_storage.get_permitted_stage_ids_given_stage_ids \
            .return_value = [
            "stage_id_0", "stage_id_1", "stage_id_2"]
        prepare_get_permitted_action_ids(mocker, action_ids=[])
        action_storage.get_actions_details.return_value = []
        field_storage.get_stage_complete_details.return_value = \
            get_stage_details

        # Act
        response = interactor.get_task_stages_and_actions(
            task_id=task_id,
            user_id="123e4567-e89b-12d3-a456-426614174000")

        # Assert
        field_storage.get_task_stages.assert_called_once_with(task_id)
        action_storage.get_actions_details.assert_called_once_with([])
        field_storage.get_stage_complete_details.assert_called_once_with(
            stage_ids)
        snapshot.assert_match(response, "response")

    def test_given_task_id_with_one_stage_returns_stage_and_their_actions(
            self, snapshot,
            mocker, field_storage, action_storage, storage_mock,
            stage_storage, interactor,
            get_user_roles,
            get_stage_actions_for_one_stage,
            get_stage_details_for_one_stage):
        # Arrange
        project_id = "project_id_1"
        task_id = 1
        action_ids = [1, 2]
        stage_ids = ["stage_id_0"]
        user_id = "123e4567-e89b-12d3-a456-426614174000"

        user_roles = get_user_roles
        user_roles_mock = get_user_role_ids(mocker)
        user_roles_mock.return_value = user_roles
        get_user_role_ids_based_on_project_mock(mocker)

        storage_mock.validate_task_id.return_value = True
        storage_mock.get_task_project_id.return_value = project_id
        prepare_get_permitted_action_ids(mocker, action_ids=action_ids)
        field_storage.get_task_stages.return_value = ["stage_id_0"]
        action_storage.get_actions_details.return_value = \
            get_stage_actions_for_one_stage
        stage_storage.get_permitted_stage_ids_given_stage_ids \
            .return_value = stage_ids
        field_storage.get_stage_complete_details.return_value = \
            get_stage_details_for_one_stage

        # Act
        response = interactor.get_task_stages_and_actions(
            task_id=task_id,
            user_id=user_id)

        # Assert

        field_storage.get_task_stages.assert_called_once_with(task_id)
        action_storage.get_actions_details.assert_called_once_with(
            action_ids)
        field_storage.get_stage_complete_details.assert_called_once_with(
            stage_ids)
        snapshot.assert_match(response, "response")

    def test_given_task_id_but_task_has_no_actions_returns_actions_as_empty_list(
            self, mocker, get_user_roles, snapshot, get_stage_details,
            stage_storage, field_storage, storage_mock,
            action_storage, interactor):
        # Arrange
        task_id = 1
        user_id = "123e4567-e89b-12d3-a456-426614174000"
        stage_ids = ["stage_id_0", "stage_id_1", "stage_id_2"]
        project_id = "project_id_1"

        storage_mock.validate_task_id.return_value = True
        user_roles = get_user_roles
        user_roles_mock = get_user_role_ids(mocker)
        user_roles_mock.return_value = user_roles
        get_user_role_ids_based_on_project_mock(mocker)
        storage_mock.get_task_project_id.return_value = project_id
        field_storage.get_task_stages.return_value = stage_ids
        prepare_get_permitted_action_ids(mocker, action_ids=[])
        action_storage.get_actions_details.return_value = []
        stage_storage.get_permitted_stage_ids_given_stage_ids \
            .return_value = stage_ids
        field_storage.get_stage_complete_details.return_value = \
            get_stage_details

        # Act
        response = interactor.get_task_stages_and_actions(
            task_id=task_id,
            user_id=user_id)

        # Assert
        storage_mock.validate_task_id.assert_called_once_with(task_id)
        storage_mock.get_task_project_id.assert_called_once_with(task_id)
        field_storage.get_task_stages.assert_called_once_with(task_id)

        field_storage.get_stage_complete_details.assert_called_once_with(
            stage_ids)
        snapshot.assert_match(response, "response")

    def test_given_task_id_with_one_stage_without_no_actions_returns_actions_as_empty_list(
            self, mocker, get_user_roles, snapshot, get_stage_details,
            stage_storage, action_storage, storage_mock,
            field_storage, interactor):
        # Arrange
        task_id = 1
        project_id = "project_id_1"
        user_roles = get_user_roles
        user_id = "123e4567-e89b-12d3-a456-426614174000"
        user_roles_mock = get_user_role_ids(mocker)
        get_user_role_ids_based_on_project_mock(mocker)
        user_roles_mock.return_value = user_roles
        storage = field_storage
        action_storage = action_storage
        task_storage = storage_mock
        task_storage.validate_task_id.return_value = True
        task_storage.get_task_project_id.return_value = project_id
        storage.get_task_stages.return_value = ["stage_id_0"]
        prepare_get_permitted_action_ids(mocker, action_ids=[])
        action_storage.get_actions_details.return_value = []
        storage.get_stage_complete_details.return_value = get_stage_details
        stage_storage.get_permitted_stage_ids_given_stage_ids \
            .return_value = ["stage_id_0"]

        # Act
        response = interactor.get_task_stages_and_actions(
            task_id=task_id,
            user_id=user_id)

        # Assert
        task_storage.validate_task_id.assert_called_once_with(task_id)
        storage.get_task_stages.assert_called_once_with(task_id)
        snapshot.assert_match(response, "response")

    def test_when_user_has_no_permissions_returns_empty_stage_actions(
            self, snapshot, interactor, field_storage, storage_mock,
            mocker, action_storage,
            stage_storage,
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
        get_user_role_ids_based_on_project_mock(mocker)
        action_storage.get_actions_details.return_value = get_stage_actions
        stage_storage.get_permitted_stage_ids_given_stage_ids \
            .return_value = []
        prepare_get_permitted_action_ids(mocker, action_ids=[])
        action_storage.get_actions_details.return_value = []
        storage.get_stage_complete_details.return_value = get_stage_details

        # Act
        response = interactor.get_task_stages_and_actions(
            task_id=task_id,
            user_id="123e4567-e89b-12d3-a456-426614174000")

        # Assert
        snapshot.assert_match(response, "response")

    def test_when_user_has_permissions_for_only_some_stages_with_no_permitted_actions_returns_stage_actions(
            self, snapshot, interactor, storage_mock, field_storage,
            mocker, action_storage,
            stage_storage,
            get_user_roles,
            get_stage_details,
            get_stage_actions):
        # Arrange
        task_id = 1
        user_roles = get_user_roles
        user_roles_mock = get_user_role_ids(mocker)
        user_roles_mock.return_value = user_roles
        storage_mock.validate_task_id.return_value = True
        field_storage.get_task_stages.return_value = ["stage_id_0",
                                                      "stage_id_1",
                                                      "stage_id_2"]
        get_user_role_ids_based_on_project_mock(mocker)
        action_storage.get_actions_details.return_value = \
            get_stage_actions
        stage_storage.get_permitted_stage_ids_given_stage_ids \
            .return_value = ["stage_id_0", "stage_id_1"]
        prepare_get_permitted_action_ids(mocker, action_ids=[])
        action_storage.get_actions_details.return_value = []
        field_storage.get_stage_complete_details.return_value = \
            get_stage_details

        # Act
        response = interactor.get_task_stages_and_actions(
            task_id=task_id,
            user_id="123e4567-e89b-12d3-a456-426614174000")

        # Assert
        snapshot.assert_match(response, "response")

    def test_when_user_has_permissions_for_only_some_stages_get_stage_actions(
            self, snapshot, interactor, field_storage, storage_mock,
            mocker, action_storage,
            stage_storage,
            get_stage_actions,
            get_stage_details,
            get_user_roles):
        # Arrange
        task_id = 1
        user_roles = get_user_roles
        user_roles_mock = get_user_role_ids(mocker)
        user_roles_mock.return_value = user_roles
        field_storage.get_task_stages.return_value = [
            "stage_id_0", "stage_id_1", "stage_id_2"]
        action_ids = [1, 2, 3, 4]
        get_user_role_ids_based_on_project_mock(mocker)
        stage_storage.get_permitted_stage_ids_given_stage_ids \
            .return_value = [
            "stage_id_0", "stage_id_1"]
        prepare_get_permitted_action_ids(mocker, action_ids=action_ids)
        action_storage.get_actions_details.return_value = \
            get_stage_actions
        field_storage.get_stage_complete_details.return_value = \
            get_stage_details

        # Act
        response = interactor.get_task_stages_and_actions(task_id=task_id,
                                                          user_id="user_id_1")

        # Assert
        snapshot.assert_match(response, "response")
