from unittest.mock import create_autospec
import pytest

from ib_tasks.interactors.dtos import StageDTO
from ib_tasks.interactors.storage_interfaces.dtos import TaskStagesDTO
from ib_tasks.exceptions.custom_exceptions import (
    InvalidStageValues, InvalidStagesTaskTemplateId, DuplicateStageIds,
    InvalidTaskTemplateIds, InvalidStageDisplayLogic)
from ib_tasks.interactors.storage_interfaces.stages_storage_interface import StageStorageInterface
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface
from ib_tasks.interactors.create_or_update_stages import \
    CreateOrUpdateStagesInterface
from ib_tasks.tests.factories.storage_dtos import ValidStageDTOFactory


class TestCreateOrUpdateStageInformation:

    @pytest.fixture()
    def valid_stages_dto(self):
        return ValidStageDTOFactory.create_batch(size=1, stage_id="PR_PENDING RP APPROVAL")

    @pytest.fixture()
    def stage_storage(self):
        return create_autospec(StageStorageInterface)

    @pytest.fixture()
    def task_storage(self):
        return create_autospec(TaskStorageInterface)

    def test_create_stage_given_valid_information_creates_stage_with_given_information(
            self, valid_stages_dto, task_storage, stage_storage):
        # Arrange
        task_template_id = "FIN_PR"
        stage_id = "PR_PENDING RP APPROVAL"
        stage_display_name = "Pending RP Approval"
        stage_display_logic = "Value[Status1]==Value[PR_PENDING_RP_APPROVAL]"
        value = 2
        stage_ids = ["PR_PENDING RP APPROVAL"]
        stages_information = [StageDTO(
            task_template_id=task_template_id,
            stage_id=stage_id,
            id=None,
            stage_display_name=stage_display_name,
            stage_display_logic=stage_display_logic,
            value=value
        )]

        stage_interactor = CreateOrUpdateStagesInterface(
            stage_storage=stage_storage, task_storage=task_storage
        )
        task_storage.get_valid_template_ids_in_given_template_ids.return_value = ["FIN_PR"]
        stage_storage.get_valid_stage_ids.return_value = []

        # Act
        stage_interactor.create_or_update_stages_information(
            stages_information=stages_information
        )

        # Assert
        stage_storage.get_valid_stage_ids.assert_called_once_with(
            stage_ids=stage_ids
        )
        stage_storage.create_stages.assert_called_once_with(
            stages_information
        )

    def test_update_stage_when_stage_id_already_exists_for_given_task_template_updates_stage_details(
            self, valid_stages_dto, task_storage, stage_storage):
        # Arrange
        task_template_id = "FIN_PR"
        stage_id = "PR_PENDING RP APPROVAL"
        stage_display_name = "Pending RP Approval"
        stage_display_logic = "Value[Status1]==Value[PR_PENDING_RP_APPROVAL]"
        value = 2
        stages_information = [StageDTO(
            task_template_id=task_template_id,
            stage_id=stage_id,
            id=1,
            stage_display_name=stage_display_name,
            stage_display_logic=stage_display_logic,
            value=value
        )]
        stage_ids = ["PR_PENDING RP APPROVAL"]
        stage_storage.get_valid_stage_ids.return_value = valid_stages_dto
        stage_storage.validate_stages_related_task_template_ids.return_value = []
        task_stages_dto = [TaskStagesDTO(
            task_template_id=task_template_id,
            stage_id=stage_id
        )]
        task_storage.get_valid_template_ids_in_given_template_ids.return_value = ["FIN_PR"]
        stage_interactor = CreateOrUpdateStagesInterface(
            stage_storage=stage_storage, task_storage=task_storage
        )

        # Act
        stage_interactor.create_or_update_stages_information(
            stages_information=stages_information
        )

        # Assert
        stage_storage.validate_stages_related_task_template_ids.\
            assert_called_once_with(
                task_stages_dto
            )
        stage_storage.update_stages.assert_called_once_with(
            stages_information
        )

    def test_validate_values_when_given_invalid_values_raises_exception(self,
                                                                        task_storage,
                                                                        stage_storage):
        # Arrange
        task_template_id = "FIN_PR"
        stage_id = "PR_PENDING RP APPROVAL"
        stage_display_name = "Pending RP Approval"
        stage_display_logic = "Value[Status1]==Value[PR_PENDING_RP_APPROVAL]"
        value = -1
        stages_information = [StageDTO(
                task_template_id=task_template_id,
                stage_id=stage_id,
            id=None,
                stage_display_name=stage_display_name,
                stage_display_logic=stage_display_logic,
                value=value),
            StageDTO(
                task_template_id=task_template_id,
                stage_id="PR APPROVED",
                id=None,
                stage_display_name=stage_display_name,
                stage_display_logic=stage_display_logic,
                value=-4
        )]
        task_storage.get_valid_template_ids_in_given_template_ids.return_value = ["FIN_PR"]
        stage_storage.get_valid_stage_ids.return_value = []
        stage_storage.validate_stages_related_task_template_ids.return_value = []

        stage_interactor = CreateOrUpdateStagesInterface(
            stage_storage=stage_storage, task_storage=task_storage
        )

        # Act
        with pytest.raises(InvalidStageValues) as error:
            stage_interactor.create_or_update_stages_information(
                stages_information=stages_information
            )

        # Assert

    def test_invalid_task_template_id_with_valid_stage_id_raises_exception(
            self, valid_stages_dto, stage_storage, task_storage):
        # Arrange
        task_template_id = "FIN_PR"
        stage_id = "PR_PENDING RP APPROVAL"
        stage_display_name = "Pending RP Approval"
        stage_display_logic = "Value[Status1]==Value[PR_PENDING_RP_APPROVAL]"
        value = 2
        stages_information = [StageDTO(
            task_template_id=task_template_id,
            stage_id=stage_id,
            id=None,
            stage_display_name=stage_display_name,
            stage_display_logic=stage_display_logic,
            value=value
        )]
        stage_storage.get_valid_stage_ids.return_value = valid_stages_dto
        stage_storage.validate_stages_related_task_template_ids.\
            return_value = ["PR_PENDING RP APPROVAL"]
        task_stages_dto = [TaskStagesDTO(
            task_template_id=task_template_id,
            stage_id=stage_id
        )]
        stage_interactor = CreateOrUpdateStagesInterface(
            stage_storage=stage_storage, task_storage=task_storage
        )
        task_storage.get_valid_template_ids_in_given_template_ids.return_value = ["FIN_PR"]

        # Act
        with pytest.raises(InvalidStagesTaskTemplateId) as err:
            stage_interactor.create_or_update_stages_information(
                stages_information=stages_information
            )

        # Assert
        task_storage.get_valid_template_ids_in_given_template_ids.assert_called_once()
        stage_storage.validate_stages_related_task_template_ids.\
            assert_called_once_with(
                task_stages_dto
            )


    def test_check_for_duplicate_stage_ids_raises_exception(self,
                                                            stage_storage,
                                                            task_storage):
        task_template_id = "FIN_PR"
        stage_id = "PR_PENDING RP APPROVAL"
        stage_display_name = "Pending RP Approval"
        stage_display_logic = "Value[Status1]==Value[PR_PENDING_RP_APPROVAL]"
        value = 3
        stages_information = [StageDTO(
            task_template_id=task_template_id,
            stage_id=stage_id,
            id=None,
            stage_display_name=stage_display_name,
            stage_display_logic=stage_display_logic,
            value=value),
            StageDTO(
                task_template_id=task_template_id,
                stage_id=stage_id,
                id=None,
                stage_display_name=stage_display_name,
                stage_display_logic=stage_display_logic,
                value=4
            )]
        stage_storage.get_valid_stage_ids.return_value = []
        task_storage.get_valid_template_ids_in_given_template_ids.return_value = ["FIN_PR"]
        stage_storage.validate_stages_related_task_template_ids.return_value = []

        stage_interactor = CreateOrUpdateStagesInterface(
            stage_storage=stage_storage, task_storage=task_storage
        )

        # Act
        with pytest.raises(DuplicateStageIds) as error:
            stage_interactor.create_or_update_stages_information(
                stages_information=stages_information
            )

        # Assert

    def test_validate_task_template_ids_if_doesnot_exists_raises_exception(
            self, task_storage, stage_storage):
        task_template_id = "FIN_PR"
        stage_id = "PR_PENDING RP APPROVAL"
        stage_display_name = "Pending RP Approval"
        stage_display_logic = "Value[Status1]==Value[PR_PENDING_RP_APPROVAL]"
        value = 3
        stages_information = [StageDTO(
            task_template_id=task_template_id,
            stage_id=stage_id,
            id=None,
            stage_display_name=stage_display_name,
            stage_display_logic=stage_display_logic,
            value=value)]

        task_storage.get_valid_template_ids_in_given_template_ids.return_value = ["BACKEND"]

        stage_interactor = CreateOrUpdateStagesInterface(
            stage_storage=stage_storage, task_storage=task_storage
        )

        # Act
        with pytest.raises(InvalidTaskTemplateIds) as error:
            stage_interactor.create_or_update_stages_information(
                stages_information=stages_information
            )

        # Assert
        task_storage.get_valid_template_ids_in_given_template_ids.assert_called_once()

    def test_validate_stage_display_logic_invalid_stage_display_logic_raises_exception(
            self, stage_storage, task_storage):
        task_template_id = "FIN_PR"
        stage_id = "PR_PENDING RP APPROVAL"
        stage_display_name = "Pending RP Approval"
        stage_display_logic = ""
        value = 3
        stages_information = [StageDTO(
            task_template_id=task_template_id,
            stage_id=stage_id,
            id=None,
            stage_display_name=stage_display_name,
            stage_display_logic=stage_display_logic,
            value=value)]
        task_storage.get_valid_template_ids_in_given_template_ids.return_value = ["FIN_PR"]

        stage_interactor = CreateOrUpdateStagesInterface(
            stage_storage=stage_storage, task_storage=task_storage
        )

        # Act
        with pytest.raises(InvalidStageDisplayLogic) as error:
            stage_interactor.create_or_update_stages_information(
                stages_information=stages_information
            )

        # Assert
