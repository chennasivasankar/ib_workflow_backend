from unittest.mock import create_autospec

import pytest
from mock import Mock

from ib_tasks.exceptions.stage_custom_exceptions import InvalidTaskStageIds
from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskIds
from ib_tasks.interactors.get_task_fields_and_actions import GetTaskFieldsAndActionsInteractor
from ib_tasks.interactors.storage_interfaces.fields_dtos import TaskTemplateStageFieldsDTO
from ib_tasks.interactors.storage_interfaces.fields_storage_interface import FieldsStorageInterface
from ib_tasks.interactors.storage_interfaces.stage_dtos import GetTaskStageCompleteDetailsDTO
from ib_tasks.interactors.storage_interfaces.stages_storage_interface import StageStorageInterface
from ib_tasks.tests.factories.interactor_dtos import GetTaskDetailsDTOFactory
from ib_tasks.tests.factories.storage_dtos import (
    ActionDetailsDTOFactory, FieldDetailsDTOFactory, TaskFieldsDTOFactory, TaskTemplateStagesDTOFactory,
    FieldDetailsDTOWithTaskIdFactory)


class TestGetFieldsAndActionsInteractor:

    @pytest.fixture()
    def get_task_dtos(self):
        GetTaskDetailsDTOFactory.reset_sequence()
        return GetTaskDetailsDTOFactory.create_batch(size=2, task_id=1)

    @pytest.fixture()
    def get_task_template_stage_dtos(self):
        TaskTemplateStagesDTOFactory.reset_sequence()
        return TaskTemplateStagesDTOFactory.create_batch(size=2, task_template_id="task_template_id_1", task_id=1)

    @pytest.fixture()
    def get_task_template_stage_dtos_for_two_tasks(self):
        TaskTemplateStagesDTOFactory.reset_sequence()
        return TaskTemplateStagesDTOFactory.create_batch(size=2, task_template_id="task_template_id_1")

    @pytest.fixture()
    def get_actions_dtos(self):
        ActionDetailsDTOFactory.reset_sequence()
        actions = ActionDetailsDTOFactory.create_batch(size=2, stage_id="stage_id_1")
        actions.append(ActionDetailsDTOFactory(stage_id="stage_id_2"))
        actions.append(ActionDetailsDTOFactory(stage_id="stage_id_2"))
        return actions

    @pytest.fixture()
    def get_fields_dtos(self):
        FieldDetailsDTOWithTaskIdFactory.reset_sequence()
        fields = FieldDetailsDTOWithTaskIdFactory.create_batch(size=2, task_id=1)
        fields.append(FieldDetailsDTOWithTaskIdFactory(task_id=2))
        fields.append(FieldDetailsDTOWithTaskIdFactory(task_id=2))
        return fields

    @pytest.fixture()
    def get_fields_dtos_for_a_tasks_with_two_stage(self):
        FieldDetailsDTOWithTaskIdFactory.reset_sequence()
        fields = FieldDetailsDTOWithTaskIdFactory.create_batch(size=4, task_id=1)
        return fields

    @pytest.fixture()
    def expected_response(self):
        ActionDetailsDTOFactory.reset_sequence()
        FieldDetailsDTOFactory.reset_sequence()
        response = [GetTaskStageCompleteDetailsDTO(
            task_id=1,
            stage_id="stage_id_1",
            field_dtos=[FieldDetailsDTOFactory()],
            action_dtos=[ActionDetailsDTOFactory()]
        ),
            GetTaskStageCompleteDetailsDTO(
                task_id=1,
                stage_id="stage_id_2",
                field_dtos=[FieldDetailsDTOFactory()],
                action_dtos=[ActionDetailsDTOFactory()]
            )
        ]
        return response

    @pytest.fixture()
    def get_field_ids(self):
        return [TaskTemplateStageFieldsDTO(
            task_template_id="task_template_id_1",
            task_id=1,
            stage_id="stage_id_1",
            field_ids=["FIELD-ID-1", "FIELD-ID-2"]
        ),
            TaskTemplateStageFieldsDTO(
                task_template_id="task_template_id_1",
                task_id=1,
                stage_id="stage_id_2",
                field_ids=["FIELD-ID-3", "FIELD-ID-4"]
            )
        ]

    @pytest.fixture()
    def get_field_ids_for_two_tasks(self):
        return [TaskTemplateStageFieldsDTO(
            task_template_id="task_template_id_1",
            task_id=1,
            stage_id="stage_id_1",
            field_ids=["FIELD-ID-1", "FIELD-ID-2"]
        ),
            TaskTemplateStageFieldsDTO(
                task_template_id="task_template_id_1",
                task_id=2,
                stage_id="stage_id_2",
                field_ids=["FIELD-ID-3", "FIELD-ID-4"]
            )
        ]

    @pytest.fixture()
    def task_with_no_fields(self):
        return [TaskTemplateStageFieldsDTO(
            task_template_id="task_template_id_1",
            task_id=1,
            stage_id="stage_id_1",
            field_ids=[]
        ),
            TaskTemplateStageFieldsDTO(
                task_template_id="task_template_id_1",
                task_id=1,
                stage_id="stage_id_2",
                field_ids=[]
            )
        ]

    @pytest.fixture()
    def task_fields_dtos_with_same_task_id(self):
        TaskFieldsDTOFactory.reset_sequence()
        tasks = [TaskFieldsDTOFactory(task_id=1),
                 TaskFieldsDTOFactory(field_ids=['FIELD-ID-3', 'FIELD-ID-4'], task_id=1)]
        return tasks

    @pytest.fixture()
    def task_fields_dtos(self):
        TaskFieldsDTOFactory.reset_sequence()
        tasks = [TaskFieldsDTOFactory(), TaskFieldsDTOFactory(field_ids=['FIELD-ID-3', 'FIELD-ID-4'])]
        return tasks

    @pytest.fixture()
    def get_task_dtos_for_two_tasks_in_same_stage(self):
        GetTaskDetailsDTOFactory.reset_sequence()
        return GetTaskDetailsDTOFactory.create_batch(size=2, stage_id="stage_id_1")

    @pytest.fixture()
    def get_task_template_stage_dtos_for_two_tasks_in_same_stage(self):
        TaskTemplateStagesDTOFactory.reset_sequence()
        return TaskTemplateStagesDTOFactory.create_batch(size=2, stage_id="stage_id_1")

    @pytest.fixture()
    def get_actions_dtos_for_a_stage(self):
        ActionDetailsDTOFactory.reset_sequence()
        actions = ActionDetailsDTOFactory.create_batch(size=2, stage_id="stage_id_1")
        return actions

    @pytest.fixture()
    def get_field_ids_for_two_tasks_in_same_stage(self):
        return [TaskTemplateStageFieldsDTO(
            task_template_id="task_template_id_1",
            task_id=1,
            stage_id="stage_id_1",
            field_ids=["FIELD-ID-1", "FIELD-ID-2"]
        ),
            TaskTemplateStageFieldsDTO(
                task_template_id="task_template_id_2",
                task_id=2,
                stage_id="stage_id_1",
                field_ids=["FIELD-ID-3", "FIELD-ID-4"]
            )
        ]

    @pytest.fixture()
    def get_fields_dtos_for_two_tasks_in_same_stage(self):
        FieldDetailsDTOWithTaskIdFactory.reset_sequence()
        fields = FieldDetailsDTOWithTaskIdFactory.create_batch(size=2, task_id=1)
        fields.append(FieldDetailsDTOWithTaskIdFactory(task_id=2))
        fields.append(FieldDetailsDTOWithTaskIdFactory(task_id=2))
        return fields

    def test_get_actions_and_fields_when_two_tasks_are_in_same_stage(
            self, snapshot, get_task_dtos_for_two_tasks_in_same_stage,
            get_task_template_stage_dtos_for_two_tasks_in_same_stage,
            get_actions_dtos_for_a_stage, get_field_ids_for_two_tasks_in_same_stage,
            get_fields_dtos_for_two_tasks_in_same_stage, task_fields_dtos):

        # Arrange
        user_id = "user_id_1"
        task_dtos = get_task_dtos_for_two_tasks_in_same_stage
        storage = create_autospec(FieldsStorageInterface)
        stage_storage = create_autospec(StageStorageInterface)
        interactor = GetTaskFieldsAndActionsInteractor(
            storage=storage, stage_storage=stage_storage
        )
        task_ids = [1, 2]
        task_template_stages_dtos = get_task_template_stage_dtos_for_two_tasks_in_same_stage
        stage_ids = ["stage_id_1"]
        action_dtos = get_actions_dtos_for_a_stage
        field_dtos = get_fields_dtos_for_two_tasks_in_same_stage
        storage.get_valid_task_ids.return_value = task_ids
        stage_storage.get_existing_stage_ids.return_value = stage_ids
        storage.validate_task_related_stage_ids.return_value = task_dtos
        storage.get_stage_details.return_value = task_template_stages_dtos
        storage.get_field_ids.return_value = get_field_ids_for_two_tasks_in_same_stage
        storage.get_actions_details.return_value = action_dtos
        storage.get_fields_details.return_value = field_dtos

        # Act
        response = interactor.get_task_fields_and_action(task_dtos, user_id)

        # Assert
        storage.get_stage_details.assert_called_once_with(task_dtos)
        storage.get_actions_details.assert_called_once_with(stage_ids)
        storage.get_field_ids.assert_called()
        storage.validate_task_related_stage_ids.assert_called_once_with(task_dtos)
        storage.get_fields_details.assert_called_once_with(task_fields_dtos)

        snapshot.assert_match(response, "response")

    def test_get_actions_and_fields_given_valid_task_template_id_and_stage_id(
            self, get_task_template_stage_dtos_for_two_tasks,
            get_actions_dtos,
            get_fields_dtos, expected_response,
            get_field_ids_for_two_tasks, task_fields_dtos, snapshot):
        # Arrange
        user_id = "user_id_1"
        GetTaskDetailsDTOFactory.reset_sequence()
        task_dtos = GetTaskDetailsDTOFactory.create_batch(size=2)

        storage = create_autospec(FieldsStorageInterface)
        stage_storage = create_autospec(StageStorageInterface)
        interactor = GetTaskFieldsAndActionsInteractor(
            storage=storage, stage_storage=stage_storage
        )
        task_ids = [1, 2]
        task_template_stages_dtos = get_task_template_stage_dtos_for_two_tasks
        stage_ids = ["stage_id_1", "stage_id_2"]
        action_dtos = get_actions_dtos
        field_dtos = get_fields_dtos
        storage.get_valid_task_ids.return_value = task_ids
        stage_storage.get_existing_stage_ids.return_value = stage_ids
        storage.validate_task_related_stage_ids.return_value = task_dtos
        storage.get_stage_details.return_value = task_template_stages_dtos
        storage.get_field_ids.return_value = get_field_ids_for_two_tasks
        storage.get_actions_details.return_value = action_dtos
        storage.get_fields_details.return_value = field_dtos

        # Act
        response = interactor.get_task_fields_and_action(task_dtos, user_id)

        # Assert
        storage.get_stage_details.assert_called_once_with(task_dtos)
        storage.get_actions_details.assert_called_once_with(stage_ids)
        storage.get_field_ids.assert_called()
        storage.validate_task_related_stage_ids.assert_called_once_with(task_dtos)
        storage.get_fields_details.assert_called_once_with(task_fields_dtos)

        snapshot.assert_match(response, "response")

    def test_get_actions_and_fields_when_two_stages_has_same_task_id(
            self, get_task_dtos, get_task_template_stage_dtos,
            get_actions_dtos, get_fields_dtos_for_a_tasks_with_two_stage,
            get_field_ids, task_fields_dtos_with_same_task_id, snapshot):
        # Arrange
        user_id = "user_id_1"
        task_dtos = get_task_dtos
        storage = create_autospec(FieldsStorageInterface)
        stage_storage = create_autospec(StageStorageInterface)
        interactor = GetTaskFieldsAndActionsInteractor(
            storage=storage, stage_storage=stage_storage
        )
        task_ids = [1]
        task_template_stages_dtos = get_task_template_stage_dtos
        stage_ids = ["stage_id_1", "stage_id_2"]
        action_dtos = get_actions_dtos
        field_dtos = get_fields_dtos_for_a_tasks_with_two_stage
        storage.get_valid_task_ids.return_value = task_ids
        stage_storage.get_existing_stage_ids.return_value = stage_ids
        storage.validate_task_related_stage_ids.return_value = task_dtos
        storage.get_stage_details.return_value = task_template_stages_dtos
        storage.get_field_ids.return_value = get_field_ids
        storage.get_actions_details.return_value = action_dtos
        storage.get_fields_details.return_value = field_dtos

        # Act
        response = interactor.get_task_fields_and_action(task_dtos, user_id)

        # Assert
        storage.get_stage_details.assert_called_once_with(task_dtos)
        storage.get_actions_details.assert_called_once_with(stage_ids)
        storage.get_field_ids.assert_called()
        storage.validate_task_related_stage_ids.assert_called_once_with(task_dtos)
        storage.get_fields_details.assert_called_once_with(task_fields_dtos_with_same_task_id)

        snapshot.assert_match(response, "response")

    def test_with_invalid_task_ids_raises_exception(self,
                                                    get_task_dtos):
        # Arrange
        user_id = "user_id_1"
        storage = create_autospec(FieldsStorageInterface)
        stage_storage = create_autospec(StageStorageInterface)
        interactor = GetTaskFieldsAndActionsInteractor(
            storage=storage, stage_storage=stage_storage
        )
        task_ids = [1]
        storage.get_valid_task_ids.return_value = []

        # Act
        with pytest.raises(InvalidTaskIds):
            interactor.get_task_fields_and_action(get_task_dtos, user_id)

        # Assert
        storage.get_valid_task_ids.assert_called_once_with(task_ids)

    def test_with_invalid_stage_ids_raises_exception(self,
                                                     get_task_dtos):
        # Arrange
        user_id = "user_id_1"
        storage = create_autospec(FieldsStorageInterface)
        stage_storage = create_autospec(StageStorageInterface)
        interactor = GetTaskFieldsAndActionsInteractor(
            storage=storage, stage_storage=stage_storage
        )
        task_ids = [1]
        stage_ids = ["stage_id_1", "stage_id_2"]
        storage.get_valid_task_ids.return_value = task_ids
        stage_storage.get_existing_stage_ids.return_value = []

        # Act
        from ib_tasks.exceptions.stage_custom_exceptions import \
            InvalidStageIdsListException
        with pytest.raises(InvalidStageIdsListException):
            interactor.get_task_fields_and_action(get_task_dtos, user_id)

        # Assert
        stage_storage.get_existing_stage_ids.assert_called_once_with(stage_ids)

    def test_with_invalid_stage_related_task_ids_raises_exception(self,
                                                                  get_task_dtos):
        # Arrange
        user_id = "user_id_1"
        storage = create_autospec(FieldsStorageInterface)
        stage_storage = create_autospec(StageStorageInterface)
        interactor = GetTaskFieldsAndActionsInteractor(
            storage=storage, stage_storage=stage_storage
        )
        task_ids = [1]
        stage_ids = ["stage_id_1", "stage_id_2"]
        storage.get_valid_task_ids.return_value = task_ids
        storage.validate_task_related_stage_ids.return_value = []
        stage_storage.get_existing_stage_ids.return_value = stage_ids

        # Act
        with pytest.raises(InvalidTaskStageIds):
            interactor.get_task_fields_and_action(get_task_dtos, user_id)

        # Assert
        stage_storage.get_existing_stage_ids.assert_called_once_with(stage_ids)
        storage.validate_task_related_stage_ids.assert_called_once_with(get_task_dtos)

    def test_get_actions_and_fields_when_task_has_no_actions_or_fields_returns_empty_list(
            self, get_task_dtos, get_task_template_stage_dtos,
            get_actions_dtos, get_fields_dtos, expected_response,
            task_with_no_fields, snapshot):
        # Arrange
        user_id = "user_id_1"
        task_dtos = [get_task_dtos[0]]
        storage = create_autospec(FieldsStorageInterface)
        stage_storage = create_autospec(StageStorageInterface)
        interactor = GetTaskFieldsAndActionsInteractor(
            storage=storage, stage_storage=stage_storage
        )
        task_ids = [1]
        task_template_stages_dtos = get_task_template_stage_dtos
        stage_ids = ["stage_id_1"]

        storage.get_valid_task_ids.return_value = task_ids
        stage_storage.get_existing_stage_ids.return_value = stage_ids
        storage.validate_task_related_stage_ids.return_value = task_dtos
        storage.get_stage_details.return_value = task_template_stages_dtos
        storage.get_field_ids.side_effect = [task_with_no_fields]
        storage.get_actions_details.return_value = []
        storage.get_fields_details.return_value = []

        # Act
        response = interactor.get_task_fields_and_action(task_dtos, user_id)

        # Assert
        storage.get_stage_details.assert_called_once_with(task_dtos)
        storage.get_actions_details.assert_called_once_with(stage_ids)
        storage.get_field_ids.assert_called()
        storage.validate_task_related_stage_ids.assert_called_once_with(task_dtos)
        snapshot.assert_match(response, "response")
