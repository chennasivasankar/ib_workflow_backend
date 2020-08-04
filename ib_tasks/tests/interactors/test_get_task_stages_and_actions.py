from unittest.mock import create_autospec

import pytest

from ib_tasks.interactors.get_task_stages_and_actions import \
    GetTaskStagesAndActions
from ib_tasks.interactors.storage_interfaces.fields_storage_interface import \
    FieldsStorageInterface
from ib_tasks.tests.common_fixtures.adapters.roles_service import \
    get_user_role_ids
from ib_tasks.tests.factories.storage_dtos import ActionDetailsDTOFactory, \
    StageDetailsDTOFactory


class TestGetTaskStagesAndActions:

    @pytest.fixture()
    def get_stage_actions(self):
        ActionDetailsDTOFactory.reset_sequence()
        actions = ActionDetailsDTOFactory.create_batch(size=3, stage_id="stage_id_1")
        actions.append(ActionDetailsDTOFactory(stage_id="stage_id_2"))
        actions.append(ActionDetailsDTOFactory(stage_id="stage_id_2"))
        actions.append(ActionDetailsDTOFactory(stage_id="stage_id_3"))
        actions.append(ActionDetailsDTOFactory(stage_id="stage_id_3"))
        return actions

    @pytest.fixture()
    def get_stage_details(self):
        StageDetailsDTOFactory.reset_sequence(1)
        return StageDetailsDTOFactory.create_batch(size=4)

    def test_when_user_has_permissions_get_stage_actions(
            self, snapshot,
            mocker,
            get_stage_actions,
            get_stage_details):
        # Arrange
        task_id = 1
        user_roles = ["FIN_PAYMENT_REQUESTER",
                      "FIN_PAYMENT_POC",
                      "FIN_PAYMENT_APPROVER",
                      "FIN_PAYMENTS_RP",
                      "FIN_FINANCE_RP"]
        user_roles_mock = get_user_role_ids(mocker)
        user_roles_mock.return_value = user_roles
        storage = create_autospec(FieldsStorageInterface)
        storage.get_task_stages.return_value = [
            "stage_id_1", "stage_id_2", "stage_id_3"]
        storage.get_actions_details.return_value = get_stage_actions
        storage.get_stage_complete_details.return_value = get_stage_details
        interactor = GetTaskStagesAndActions(storage=storage)

        # Act
        response = interactor.get_task_stages_and_actions(task_id=task_id,
                                                          user_id="user_id_1")

        # Assert
        snapshot.assert_match(response, "response")

    def test_when_user_has_no_permissions_returns_empty_actions(
            self, snapshot,
            mocker,
            get_stage_details):
        # Arrange
        task_id = 1
        user_roles = ["FIN_PAYMENT_REQUESTER",
                      "FIN_PAYMENT_POC",
                      "FIN_PAYMENT_APPROVER",
                      "FIN_PAYMENTS_RP",
                      "FIN_FINANCE_RP"]
        user_roles_mock = get_user_role_ids(mocker)
        user_roles_mock.return_value = user_roles
        storage = create_autospec(FieldsStorageInterface)
        storage.get_task_stages.return_value = [
            "stage_id_1", "stage_id_2", "stage_id_3"]
        storage.get_actions_details.return_value = []
        storage.get_stage_complete_details.return_value = get_stage_details
        interactor = GetTaskStagesAndActions(storage=storage)

        # Act
        response = interactor.get_task_stages_and_actions(task_id=task_id,
                                                          user_id="user_id_1")

        # Assert
        snapshot.assert_match(response, "response")
