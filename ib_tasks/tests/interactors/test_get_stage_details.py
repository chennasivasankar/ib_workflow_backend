import pytest

from ib_tasks.interactors.get_stage_details import GetStageDetails
from ib_tasks.tests.factories.storage_dtos import \
    StageDisplayNameValueDTOFactory


class TestGetStageDetails:

    @pytest.fixture
    def storage_stage_details_dtos(self):
        StageDisplayNameValueDTOFactory.reset_sequence()
        return StageDisplayNameValueDTOFactory.create_batch(2)

    @pytest.fixture
    def storage_mock(self):
        from unittest.mock import create_autospec
        from ib_tasks.interactors.storage_interfaces \
            .stages_storage_interface import \
            StageStorageInterface
        return create_autospec(StageStorageInterface)

    @pytest.fixture
    def interactor_mock(self, storage_mock):
        interactor = GetStageDetails(storage_mock)
        return interactor

    def test_get_stage_details_given_stage_ids(
            self, storage_mock, interactor_mock,
            storage_stage_details_dtos):
        # Arrange
        stage_ids = ["stage_id_0", "stage_id_1"]
        expected_output = storage_stage_details_dtos
        storage_mock.get_valid_stage_ids_in_given_stage_ids.return_value = \
            stage_ids
        storage_mock.get_stage_display_name_value_dtos_for_stage_ids \
            .return_value = storage_stage_details_dtos

        # Act
        response = interactor_mock.get_stage_details(stage_ids)

        # Assert
        storage_mock.get_valid_stage_ids_in_given_stage_ids \
            .assert_called_once_with(stage_ids)
        storage_mock.get_stage_display_name_value_dtos_for_stage_ids \
            .assert_called_once_with(stage_ids)
        assert response == expected_output

    def test_with_invalid_details_raises_exception(
            self, storage_mock, interactor_mock):
        # Arrange
        stage_ids = ["stage_id_0", "stage_id_1"]

        storage_mock.get_valid_stage_ids_in_given_stage_ids.return_value = []

        # Act
        from ib_tasks.exceptions.stage_custom_exceptions import \
            InvalidStageIdsException
        with pytest.raises(InvalidStageIdsException) as error:
            interactor_mock.get_stage_details(stage_ids)

        # Assert
        storage_mock.get_valid_stage_ids_in_given_stage_ids \
            .assert_called_once_with(stage_ids)
