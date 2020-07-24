from unittest.mock import create_autospec

import pytest

from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskIds, InvalidStageIds
from ib_tasks.interactors.get_task_fields_and_actions import GetTaskFieldsAndActionsInteractor
from ib_tasks.interactors.storage_interfaces.actions_dtos import ActionDTO
from ib_tasks.interactors.storage_interfaces.fields_dtos import FieldDetailsDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import GetTaskStageCompleteDetailsDTO
from ib_tasks.interactors.storage_interfaces.stages_storage_interface import StageStorageInterface
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface

from ib_tasks.tests.factories.interactor_dtos import GetTaskDetailsDTOFactory


class TestGetFieldsAndActionsInteractor:

    @pytest.fixture()
    def get_task_dtos(self):
        GetTaskDetailsDTOFactory.reset_sequence()
        return GetTaskDetailsDTOFactory.create_batch(size=3)

    @pytest.fixture()
    def expected_response(self):
        response = GetTaskStageCompleteDetailsDTO(
            fields_dto=[FieldDetailsDTO(
                field_type="Text field",
                stage_id="stage_id_2",
                field_id=1,
                key="requester",
                value="KC"
            )],
            actions_dto=[ActionDTO(
                action_id="action_id_1",
                name="action_name_1",
                stage_id="stage_id_1",
                button_text="text",
                button_color=None
            )]
        )

    def test_get_actions_given_valid_task_template_id_and_stage_id(self,
                                                                   get_task_dtos,
                                                                   expected_response):
        # Arrange
        storage = create_autospec(TaskStorageInterface)
        stage_storage = create_autospec(StageStorageInterface)
        interactor = GetTaskFieldsAndActionsInteractor(
            storage=storage, stage_storage=stage_storage
        )
        task_ids = ["task_id_1", "task_id_2", "task_id_3"]
        stage_ids = ["stage_id_1", "stage_id_2", "stage_id_3"]
        storage.get_valid_task_ids.return_value = task_ids
        stage_storage.get_existing_stage_ids.return_value = stage_ids
        storage.get_task_details.return_value = expected_response

        # Act
        response = interactor.get_task_fields_and_action(get_task_dtos)

        # Assert
        assert response == expected_response


    def test_with_invalid_task_ids_raises_exception(self,
                                   get_task_dtos):
        # Arrange
        storage = create_autospec(TaskStorageInterface)
        stage_storage = create_autospec(StageStorageInterface)
        interactor = GetTaskFieldsAndActionsInteractor(
            storage=storage, stage_storage=stage_storage
        )
        task_ids = ["task_id_1", "task_id_2", "task_id_3"]
        storage.get_valid_task_ids.return_value = []

        # Act
        with pytest.raises(InvalidTaskIds):
            interactor.get_task_fields_and_action(get_task_dtos)

        # Assert
        storage.get_valid_task_ids.assert_called_once_with(task_ids)


    def test_with_invalid_stage_ids_raises_exception(self,
                                   get_task_dtos):
        # Arrange
        storage = create_autospec(TaskStorageInterface)
        stage_storage = create_autospec(StageStorageInterface)
        interactor = GetTaskFieldsAndActionsInteractor(
            storage=storage, stage_storage=stage_storage
        )
        task_ids = ["task_id_1", "task_id_2", "task_id_3"]
        stage_ids = ["stage_id_1", "stage_id_2", "stage_id_3"]
        storage.get_valid_task_ids.return_value = task_ids
        stage_storage.get_existing_stage_ids.return_value = []

        # Act
        with pytest.raises(InvalidStageIds):
            interactor.get_task_fields_and_action(get_task_dtos)

        # Assert
        stage_storage.get_existing_stage_ids.assert_called_once_with(stage_ids)
