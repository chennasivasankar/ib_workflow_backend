from unittest.mock import create_autospec
import pytest
from ib_tasks.exceptions.custom_exceptions import (
    InvalidStageValues, InvalidStagesTaskTemplateId, DuplicateStageIds,
    InvalidTaskTemplateIds, InvalidStageDisplayLogic, InvalidStagesDisplayName)
from ib_tasks.interactors.storage_interfaces.storage_interface import \
    StageStorageInterface
from ib_tasks.interactors.create_or_update_stages import \
    CreateOrUpdateStagesInterface
from ib_tasks.tests.factories.storage_dtos import (
    StageDTOFactory, TaskStagesDTOFactory)


class TestCreateOrUpdateStageInformation:

    @pytest.fixture
    def create_stage_dtos(self):
        StageDTOFactory.reset_sequence()
        return StageDTOFactory.create_batch(
            size=2
        )

    @pytest.fixture
    def create_task_stages_dtos(self):
        TaskStagesDTOFactory.reset_sequence()
        return TaskStagesDTOFactory.create_batch(size=2)

    def test_create_stage_given_valid_information_creates_stage_with_given_information(
            self, create_stage_dtos):
        # Arrange

        stage_ids = ["stage_id_0", "stage_id_1"]
        storage = create_autospec(StageStorageInterface)
        stage_interactor = CreateOrUpdateStagesInterface(
            stage_storage=storage
        )
        storage.get_valid_task_template_ids.return_value = ["task_template_id_0", "task_template_id_1"]
        storage.get_existing_stage_ids.return_value = []

        # Act
        stage_interactor.create_or_update_stages(
            stages_details=create_stage_dtos
        )

        # Assert
        storage.get_existing_stage_ids.assert_called_once_with(
            stage_ids=stage_ids
        )
        storage.create_stages.assert_called_once_with(
            create_stage_dtos
        )

    def test_update_stage_when_stage_id_already_exists_for_given_task_template_updates_stage_details(
            self, create_stage_dtos, create_task_stages_dtos):
        # Arrange
        stages_details = create_stage_dtos

        storage = create_autospec(StageStorageInterface)
        storage.get_existing_stage_ids.return_value = ["stage_id_0", "stage_id_1"]
        storage.validate_stages_related_task_template_ids.return_value = []
        task_stages_dto = create_task_stages_dtos
        storage.get_valid_task_template_ids.return_value = ["task_template_id_0", "task_template_id_1"]

        stage_interactor = CreateOrUpdateStagesInterface(
            stage_storage=storage
        )

        # Act
        stage_interactor.create_or_update_stages(
            stages_details=stages_details
        )

        # Assert
        storage.validate_stages_related_task_template_ids. \
            assert_called_once_with(
            task_stages_dto
        )
        storage.update_stages.assert_called_once_with(
            stages_details
        )

    def test_validate_values_when_given_invalid_values_raises_exception(self):
        # Arrange
        StageDTOFactory.reset_sequence()
        stages_information = StageDTOFactory.create_batch(
            value=-2, size=2
        )
        storage = create_autospec(StageStorageInterface)
        storage.get_valid_task_template_ids.return_value = ["task_template_id_0", "task_template_id_1"]
        storage.get_existing_stage_ids.return_value = []
        storage.validate_stages_related_task_template_ids.return_value = []

        stage_interactor = CreateOrUpdateStagesInterface(
            stage_storage=storage
        )

        # Act
        with pytest.raises(InvalidStageValues) as error:
            stage_interactor.create_or_update_stages(
                stages_details=stages_information
            )

        # Assert

    def test_invalid_task_template_id_with_valid_stage_id_raises_exception(
            self, create_stage_dtos, create_task_stages_dtos):
        # Arrange
        stages_details = create_stage_dtos
        task_stages_dto = create_task_stages_dtos
        storage = create_autospec(StageStorageInterface)
        storage.get_existing_stage_ids.return_value = ["PR_PENDING RP APPROVAL"]
        storage.validate_stages_related_task_template_ids. \
            return_value = ["PR_PENDING RP APPROVAL"]
        task_template_ids = ["task_template_id_0", "task_template_id_1"]

        stage_interactor = CreateOrUpdateStagesInterface(
            stage_storage=storage
        )
        storage.get_valid_task_template_ids.return_value = task_template_ids

        # Act
        with pytest.raises(InvalidStagesTaskTemplateId) as err:
            stage_interactor.create_or_update_stages(
                stages_details=stages_details
            )

        # Assert
        storage.get_valid_task_template_ids.assert_called_once_with(task_template_ids)
        storage.validate_stages_related_task_template_ids. \
            assert_called_once_with(
            task_stages_dto
        )

    def test_check_for_duplicate_stage_ids_raises_exception(self):
        # Arrange
        StageDTOFactory.reset_sequence()
        stages_details = StageDTOFactory.create_batch(
            stage_id="stage_id_1", size=2
        )
        storage = create_autospec(StageStorageInterface)
        storage.get_existing_stage_ids.return_value = []
        storage.get_valid_task_template_ids.return_value = ["FIN_PR"]
        storage.validate_stages_related_task_template_ids.return_value = []

        stage_interactor = CreateOrUpdateStagesInterface(
            stage_storage=storage
        )

        # Act
        with pytest.raises(DuplicateStageIds) as error:
            stage_interactor.create_or_update_stages(
                stages_details=stages_details
            )

        # Assert

    def test_validate_task_template_ids_if_doesnot_exists_raises_exception(
            self, create_stage_dtos):
        # Arrange
        stages_information = create_stage_dtos
        storage = create_autospec(StageStorageInterface)
        task_template_ids = ["task_template_id_0", "task_template_id_1"]
        storage.get_valid_task_template_ids.return_value = [""]

        stage_interactor = CreateOrUpdateStagesInterface(
            stage_storage=storage
        )

        # Act
        with pytest.raises(InvalidTaskTemplateIds) as error:
            stage_interactor.create_or_update_stages(
                stages_details=stages_information
            )

        # Assert
        storage.get_valid_task_template_ids.assert_called_once_with(task_template_ids)

    def test_validate_stage_display_logic_invalid_stage_display_logic_raises_exception(
            self):
        # Arrange

        StageDTOFactory.reset_sequence()
        stages_information = StageDTOFactory.create_batch(
            stage_display_logic="", size=2
        )
        storage = create_autospec(StageStorageInterface)
        storage.get_valid_task_template_ids.return_value = ["task_template_id_0", "task_template_id_1"]

        stage_interactor = CreateOrUpdateStagesInterface(
            stage_storage=storage
        )

        # Act
        with pytest.raises(InvalidStageDisplayLogic) as error:
            stage_interactor.create_or_update_stages(
                stages_details=stages_information
            )

        # Assert

    def test_validate_stage_display_name_invalid_stage_display_name_raises_exception(
            self):
        # Arrange

        StageDTOFactory.reset_sequence()
        stages_information = StageDTOFactory.create_batch(
            stage_display_name="", size=2
        )
        storage = create_autospec(StageStorageInterface)

        stage_interactor = CreateOrUpdateStagesInterface(
            stage_storage=storage
        )

        # Act
        with pytest.raises(InvalidStagesDisplayName) as error:
            stage_interactor.create_or_update_stages(
                stages_details=stages_information
            )

        # Assert
