from unittest.mock import create_autospec, Mock

import pytest

from ib_tasks.exceptions.stage_custom_exceptions import InvalidTaskStageIds
from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskIds, InvalidStageIds
from ib_tasks.interactors.get_task_fields_and_actions import GetTaskFieldsAndActionsInteractor
from ib_tasks.interactors.storage_interfaces.fields_dtos import FieldDetailsDTO, TaskTemplateStageFieldsDTO
from ib_tasks.interactors.storage_interfaces.fields_storage_interface import FieldsStorageInterface
from ib_tasks.interactors.storage_interfaces.stage_dtos import GetTaskStageCompleteDetailsDTO
from ib_tasks.interactors.storage_interfaces.stages_storage_interface import StageStorageInterface
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface

from ib_tasks.tests.factories.interactor_dtos import GetTaskDetailsDTOFactory
from ib_tasks.tests.factories.storage_dtos import (
    ActionDetailsDTOFactory, FieldDetailsDTOFactory, TaskFieldsDTOFactory, TaskTemplateStagesDTOFactory)


class TestGetFieldsAndActionsInteractor:

    @pytest.fixture()
    def get_task_dtos(self):
        GetTaskDetailsDTOFactory.reset_sequence()
        return GetTaskDetailsDTOFactory()

    @pytest.fixture()
    def get_task_template_stage_dtos(self):
        TaskTemplateStagesDTOFactory.reset_sequence()
        return TaskTemplateStagesDTOFactory()

    @pytest.fixture()
    def get_actions_dtos(self):
        ActionDetailsDTOFactory.reset_sequence()
        return ActionDetailsDTOFactory()

    @pytest.fixture()
    def get_fields_dtos(self):
        FieldDetailsDTOFactory.reset_sequence()
        return FieldDetailsDTOFactory()

    @pytest.fixture()
    def expected_response(self):
        ActionDetailsDTOFactory.reset_sequence()
        FieldDetailsDTOFactory.reset_sequence()
        response = [GetTaskStageCompleteDetailsDTO(
            task_id="task_id_1",
            stage_id="stage_id_1",
            field_dtos=[FieldDetailsDTOFactory()],
            action_dtos=[ActionDetailsDTOFactory()]
        )]
        return response

    @pytest.fixture()
    def get_field_ids(self):
        return [TaskTemplateStageFieldsDTO(
            task_template_id="task_template_id_1",
            stage_id="stage_id_1",
            field_ids=["field_id_1"]
        )]

    @pytest.fixture()
    def task_fields_dtos(self):
        TaskFieldsDTOFactory.reset_sequence()
        return [TaskFieldsDTOFactory()]

    def test_get_actions_and_fields_given_valid_task_template_id_and_stage_id(
            self, get_task_dtos, get_task_template_stage_dtos,
            get_actions_dtos, get_fields_dtos, expected_response,
            get_field_ids, task_fields_dtos):
        # Arrange
        task_dtos = [get_task_dtos]
        storage = create_autospec(FieldsStorageInterface)
        stage_storage = create_autospec(StageStorageInterface)
        interactor = GetTaskFieldsAndActionsInteractor(
            storage=storage, stage_storage=stage_storage
        )
        task_ids = ["task_id_1"]
        task_template_stages_dtos = [get_task_template_stage_dtos]
        stage_ids = ["stage_id_1"]
        action_dtos = [get_actions_dtos]
        field_dtos = [get_fields_dtos]
        storage.get_valid_task_ids.return_value = task_ids
        stage_storage.get_existing_stage_ids.return_value = stage_ids
        storage.validate_task_related_stage_ids.return_value = task_dtos
        storage.get_stage_details.return_value = task_template_stages_dtos
        storage.get_field_ids.side_effect = [get_field_ids]
        storage.get_actions_details.return_value = action_dtos
        storage.get_fields_details.return_value = field_dtos

        # Act
        response = interactor.get_task_fields_and_action(task_dtos)

        # Assert
        storage.get_stage_details.assert_called_once_with(task_dtos)
        storage.get_actions_details.assert_called_once_with(stage_ids)
        storage.get_field_ids.assert_called()
        storage.validate_task_related_stage_ids.assert_called_once_with(task_dtos)
        storage.get_fields_details.assert_called_once_with(task_fields_dtos)
        assert response == expected_response

    def test_with_invalid_task_ids_raises_exception(self,
                                                    get_task_dtos):
        # Arrange
        storage = create_autospec(FieldsStorageInterface)
        stage_storage = create_autospec(StageStorageInterface)
        interactor = GetTaskFieldsAndActionsInteractor(
            storage=storage, stage_storage=stage_storage
        )
        task_ids = ["task_id_1"]
        storage.get_valid_task_ids.return_value = []

        # Act
        with pytest.raises(InvalidTaskIds):
            interactor.get_task_fields_and_action([get_task_dtos])

        # Assert
        storage.get_valid_task_ids.assert_called_once_with(task_ids)

    def test_with_invalid_stage_ids_raises_exception(self,
                                                     get_task_dtos):
        # Arrange
        storage = create_autospec(FieldsStorageInterface)
        stage_storage = create_autospec(StageStorageInterface)
        interactor = GetTaskFieldsAndActionsInteractor(
            storage=storage, stage_storage=stage_storage
        )
        task_ids = ["task_id_1"]
        stage_ids = ["stage_id_1"]
        storage.get_valid_task_ids.return_value = task_ids
        stage_storage.get_existing_stage_ids.return_value = []

        # Act
        with pytest.raises(InvalidStageIds):
            interactor.get_task_fields_and_action([get_task_dtos])

        # Assert
        stage_storage.get_existing_stage_ids.assert_called_once_with(stage_ids)

    def test_with_invalid_stage_related_task_ids_raises_exception(self,
                                                                  get_task_dtos):
        # Arrange
        storage = create_autospec(FieldsStorageInterface)
        stage_storage = create_autospec(StageStorageInterface)
        interactor = GetTaskFieldsAndActionsInteractor(
            storage=storage, stage_storage=stage_storage
        )
        task_ids = ["task_id_1"]
        stage_ids = ["stage_id_1"]
        storage.get_valid_task_ids.return_value = task_ids
        storage.validate_task_related_stage_ids.return_value = []
        stage_storage.get_existing_stage_ids.return_value = ["stage_id_1"]

        # Act
        with pytest.raises(InvalidTaskStageIds):
            interactor.get_task_fields_and_action([get_task_dtos])

        # Assert
        stage_storage.get_existing_stage_ids.assert_called_once_with(stage_ids)
        storage.validate_task_related_stage_ids.assert_called_once_with([get_task_dtos])
