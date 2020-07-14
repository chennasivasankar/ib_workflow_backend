from unittest.mock import create_autospec
import pytest
from ib_tasks.interactors.storage_interfaces.dtos import (
    StageInformationDTO, TaskStagesDTO)
from ib_tasks.exceptions.custom_exceptions import (
    InvalidStageValues, InvalidStagesTaskTemplateId, DuplicateStageIds,
    InvalidTaskTemplateIds, InvalidStageDisplayLogic)
from ib_tasks.interactors.storage_interfaces.storage_interface import \
    StageStorageInterface
from ib_tasks.interactors.create_or_update_stages import \
    CreateOrUpdateStagesInterface
from ib_tasks.tests.factories.storage_dtos import (
    StageInformationDTOFactory, TaskStagesDTOFactory)


class TestCreateOrUpdateStageInformation:

    @pytest.fixture
    def create_stage_dtos(self):
        StageInformationDTOFactory.reset_sequence()
        return StageInformationDTOFactory.create_batch(
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
        storage.get_task_template_ids.return_value = ["task_template_id_0", "task_template_id_1"]
        storage.validate_stage_ids.return_value = []

        # Act
        stage_interactor.create_or_update_stages_information(
            stages_information=create_stage_dtos
        )

        # Assert
        storage.validate_stage_ids.assert_called_once_with(
            stage_ids=stage_ids
        )
        storage.create_stages_with_given_information.assert_called_once_with(
            create_stage_dtos
        )

    def test_update_stage_when_stage_id_already_exists_for_given_task_template_updates_stage_details(
            self, create_stage_dtos, create_task_stages_dtos):
        # Arrange
        stages_information = create_stage_dtos

        storage = create_autospec(StageStorageInterface)
        storage.validate_stage_ids.return_value = ["stage_id_0", "stage_id_1"]
        storage.validate_stages_related_task_template_ids.return_value = []
        task_stages_dto = create_task_stages_dtos
        storage.get_task_template_ids.return_value = ["task_template_id_0", "task_template_id_1"]

        stage_interactor = CreateOrUpdateStagesInterface(
            stage_storage=storage
        )

        # Act
        stage_interactor.create_or_update_stages_information(
            stages_information=stages_information
        )

        # Assert
        storage.validate_stages_related_task_template_ids.\
            assert_called_once_with(
                task_stages_dto
            )
        storage.update_stages_with_given_information.assert_called_once_with(
            stages_information
        )

    def test_validate_values_when_given_invalid_values_raises_exception(self):
        # Arrange
        StageInformationDTOFactory.reset_sequence()
        stages_information = StageInformationDTOFactory.create_batch(
            value=-1, size=2
        )
        storage = create_autospec(StageStorageInterface)
        storage.get_task_template_ids.return_value = ["task_template_id_0", "task_template_id_1"]
        storage.validate_stage_ids.return_value = []
        storage.validate_stages_related_task_template_ids.return_value = []

        stage_interactor = CreateOrUpdateStagesInterface(
            stage_storage=storage
        )

        # Act
        with pytest.raises(InvalidStageValues) as error:
            stage_interactor.create_or_update_stages_information(
                stages_information=stages_information
            )

        # Assert

    def test_invalid_task_template_id_with_valid_stage_id_raises_exception(
            self, create_stage_dtos, create_task_stages_dtos):
        # Arrange
        stages_information = create_stage_dtos
        task_stages_dto = create_task_stages_dtos
        storage = create_autospec(StageStorageInterface)
        storage.validate_stage_ids.return_value = ["PR_PENDING RP APPROVAL"]
        storage.validate_stages_related_task_template_ids.\
            return_value = ["PR_PENDING RP APPROVAL"]


        stage_interactor = CreateOrUpdateStagesInterface(
            stage_storage=storage
        )
        storage.get_task_template_ids.return_value = ["task_template_id_0", "task_template_id_1"]

        # Act
        with pytest.raises(InvalidStagesTaskTemplateId) as err:
            stage_interactor.create_or_update_stages_information(
                stages_information=stages_information
            )

        # Assert
        storage.get_task_template_ids.assert_called_once()
        storage.validate_stages_related_task_template_ids.\
            assert_called_once_with(
                task_stages_dto
            )


    def test_check_for_duplicate_stage_ids_raises_exception(self):
        # Arrange
        StageInformationDTOFactory.reset_sequence()
        stages_information = StageInformationDTOFactory.create_batch(
            stage_id="stage_id_1", size=2
        )
        storage = create_autospec(StageStorageInterface)
        storage.validate_stage_ids.return_value = []
        storage.get_task_template_ids.return_value = ["FIN_PR"]
        storage.validate_stages_related_task_template_ids.return_value = []

        stage_interactor = CreateOrUpdateStagesInterface(
            stage_storage=storage
        )

        # Act
        with pytest.raises(DuplicateStageIds) as error:
            stage_interactor.create_or_update_stages_information(
                stages_information=stages_information
            )

        # Assert

    def test_validate_task_template_ids_if_doesnot_exists_raises_exception(
            self, create_stage_dtos):
        # Arrange
        stages_information = create_stage_dtos
        storage = create_autospec(StageStorageInterface)
        storage.get_task_template_ids.return_value = ["BACKEND"]

        stage_interactor = CreateOrUpdateStagesInterface(
            stage_storage=storage
        )

        # Act
        with pytest.raises(InvalidTaskTemplateIds) as error:
            stage_interactor.create_or_update_stages_information(
                stages_information=stages_information
            )

        # Assert
        storage.get_task_template_ids.assert_called_once()

    def test_validate_stage_display_logic_invalid_stage_display_logic_raises_exception(
            self):
        # Arrange

        StageInformationDTOFactory.reset_sequence()
        stages_information = StageInformationDTOFactory.create_batch(
            stage_display_logic="", size=2
        )
        storage = create_autospec(StageStorageInterface)
        storage.get_task_template_ids.return_value = ["task_template_id_0", "task_template_id_1"]

        stage_interactor = CreateOrUpdateStagesInterface(
            stage_storage=storage
        )

        # Act
        with pytest.raises(InvalidStageDisplayLogic) as error:
            stage_interactor.create_or_update_stages_information(
                stages_information=stages_information
            )

        # Assert