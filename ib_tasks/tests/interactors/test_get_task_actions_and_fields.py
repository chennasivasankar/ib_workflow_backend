import pytest

from ib_tasks.constants.enum import ViewType
from ib_tasks.exceptions.stage_custom_exceptions import InvalidTaskStageIds
from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskIds
from ib_tasks.interactors.get_task_fields_and_actions \
    .get_task_fields_and_actions import \
    GetTaskFieldsAndActionsInteractor
from ib_tasks.interactors.storage_interfaces.fields_dtos import \
    TaskTemplateStageFieldsDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import \
    GetTaskStageCompleteDetailsDTO
from ib_tasks.tests.common_fixtures.interactors import \
    (prepare_get_permitted_action_ids_for_project,
     prepare_get_field_ids_having_permission_for_user_projects,
     prepare_actions_for_get_task_fields_and_actions,
     prepare_fields_for_get_task_fields_and_actions)
from ib_tasks.tests.factories.interactor_dtos import \
    GetTaskDetailsDTOFactory
from ib_tasks.tests.factories.storage_dtos import (
    StageActionDetailsDTOFactory, FieldDetailsDTOFactory,
    TaskFieldsDTOFactory, TaskTemplateStagesDTOFactory,
    FieldDetailsDTOWithTaskIdFactory)
from ib_tasks.tests.interactors.storage_method_mocks import StorageMethodsMock


class TestGetFieldsAndActionsInteractor(StorageMethodsMock):

    @pytest.fixture()
    def get_task_dtos(self):
        GetTaskDetailsDTOFactory.reset_sequence()
        return GetTaskDetailsDTOFactory.create_batch(size=2, task_id=1)

    @pytest.fixture()
    def get_task_template_stage_dtos(self):
        TaskTemplateStagesDTOFactory.reset_sequence()
        return TaskTemplateStagesDTOFactory.create_batch(
                size=2, task_template_id="task_template_id_1", task_id=1)

    @pytest.fixture()
    def get_task_template_stage_dtos_for_two_tasks(self):
        TaskTemplateStagesDTOFactory.reset_sequence()
        return TaskTemplateStagesDTOFactory.create_batch(
                size=2, task_template_id="task_template_id_1")

    @pytest.fixture()
    def get_actions_dtos(self):
        StageActionDetailsDTOFactory.reset_sequence()
        actions = StageActionDetailsDTOFactory.create_batch(
                size=2, stage_id="stage_id_1")
        actions.append(StageActionDetailsDTOFactory(stage_id="stage_id_2"))
        actions.append(StageActionDetailsDTOFactory(stage_id="stage_id_2"))
        return actions

    @pytest.fixture()
    def get_fields_dtos(self):
        FieldDetailsDTOWithTaskIdFactory.reset_sequence()
        fields = FieldDetailsDTOWithTaskIdFactory.create_batch(size=2,
                                                               task_id=1)
        fields.append(FieldDetailsDTOWithTaskIdFactory(task_id=2))
        fields.append(FieldDetailsDTOWithTaskIdFactory(task_id=2))
        return fields

    @pytest.fixture()
    def get_fields_dtos_for_kanban(self):
        FieldDetailsDTOWithTaskIdFactory.reset_sequence()
        FieldDetailsDTOWithTaskIdFactory()
        fields = FieldDetailsDTOWithTaskIdFactory.create_batch(size=2,
                                                               task_id=1)
        fields.append(FieldDetailsDTOWithTaskIdFactory(task_id=2))
        return fields

    @pytest.fixture()
    def get_fields_dtos_for_a_tasks_with_two_stage(self):
        FieldDetailsDTOWithTaskIdFactory.reset_sequence()
        fields = FieldDetailsDTOWithTaskIdFactory.create_batch(
                size=4, task_id=1)
        return fields

    @pytest.fixture()
    def expected_response(self):
        StageActionDetailsDTOFactory.reset_sequence()
        FieldDetailsDTOFactory.reset_sequence()

        response = [GetTaskStageCompleteDetailsDTO(
                task_id=1,
                stage_id="stage_id_1",
                db_stage_id=1,
                display_name="name",
                stage_color="blue",
                field_dtos=[FieldDetailsDTOFactory()],
                action_dtos=[StageActionDetailsDTOFactory()]
        ),
                GetTaskStageCompleteDetailsDTO(
                        task_id=1,
                        stage_id="stage_id_2",
                        db_stage_id=20,
                        display_name="name",
                        stage_color="blue",
                        field_dtos=[FieldDetailsDTOFactory()],
                        action_dtos=[StageActionDetailsDTOFactory()]
                )
        ]
        return response

    @pytest.fixture()
    def get_field_ids(self):
        return [TaskTemplateStageFieldsDTO(
                task_template_id="task_template_id_1",
                task_id=1,
                db_stage_id=1,
                stage_color="blue",
                display_name="display_name_1",
                stage_id="stage_id_1",
                field_ids=["FIELD-ID-1", "FIELD-ID-2"]
        ),
                TaskTemplateStageFieldsDTO(
                        task_template_id="task_template_id_1",
                        task_id=2,
                        db_stage_id=2,
                        stage_color="blue",
                        display_name="display_name_2",
                        stage_id="stage_id_2",
                        field_ids=["FIELD-ID-3", "FIELD-ID-4"]
                )
        ]

    @pytest.fixture()
    def get_field_ids_for_two_tasks(self):
        return [TaskTemplateStageFieldsDTO(
                task_template_id="task_template_id_1",
                task_id=1,
                db_stage_id=1,
                display_name="display_name_1",
                stage_color="blue",
                stage_id="stage_id_1",
                field_ids=["FIELD-ID-1", "FIELD-ID-2"]
        ),
                TaskTemplateStageFieldsDTO(
                        task_template_id="task_template_id_1",
                        task_id=2,
                        db_stage_id=2,
                        display_name="display_name_2",
                        stage_color="blue",
                        stage_id="stage_id_2",
                        field_ids=["FIELD-ID-3", "FIELD-ID-4"]
                )
        ]

    @pytest.fixture()
    def get_field_ids_for_a_tasks_in_two_stage(self):
        return [TaskTemplateStageFieldsDTO(
                task_template_id="task_template_id_1",
                task_id=1,
                db_stage_id=1,
                display_name="display_name_1",
                stage_color="blue",
                stage_id="stage_id_1",
                field_ids=["FIELD-ID-1", "FIELD-ID-2"]
        ),
                TaskTemplateStageFieldsDTO(
                        task_template_id="task_template_id_1",
                        task_id=1,
                        db_stage_id=2,
                        display_name="display_name_2",
                        stage_color="blue",
                        stage_id="stage_id_2",
                        field_ids=["FIELD-ID-3", "FIELD-ID-4"]
                )
        ]

    @pytest.fixture()
    def task_with_no_fields(self):
        return [TaskTemplateStageFieldsDTO(
                task_template_id="task_template_id_1",
                task_id=1,
                db_stage_id=1,
                display_name="display_name_1",
                stage_color="orange",
                stage_id="stage_id_1",
                field_ids=[]
        ),
                TaskTemplateStageFieldsDTO(
                        task_template_id="task_template_id_1",
                        task_id=1,
                        db_stage_id=2,
                        display_name="display_name_2",
                        stage_color="blue",
                        stage_id="stage_id_2",
                        field_ids=[]
                )
        ]

    @pytest.fixture()
    def task_fields_dtos_with_same_task_id(self):
        TaskFieldsDTOFactory.reset_sequence()
        tasks = [TaskFieldsDTOFactory(task_id=1),
                 TaskFieldsDTOFactory(field_ids=['FIELD-ID-3', 'FIELD-ID-4'],
                                      task_id=1)]
        return tasks

    @pytest.fixture()
    def task_fields_dtos(self):
        TaskFieldsDTOFactory.reset_sequence()
        tasks = [TaskFieldsDTOFactory(), TaskFieldsDTOFactory(
                field_ids=['FIELD-ID-3', 'FIELD-ID-4'])]
        return tasks

    @pytest.fixture()
    def get_task_dtos_for_two_tasks_in_same_stage(self):
        GetTaskDetailsDTOFactory.reset_sequence()
        return GetTaskDetailsDTOFactory.create_batch(size=2,
                                                     stage_id="stage_id_1")

    @pytest.fixture()
    def get_task_template_stage_dtos_for_two_tasks_in_same_stage(self):
        TaskTemplateStagesDTOFactory.reset_sequence()
        return TaskTemplateStagesDTOFactory.create_batch(
                size=2,
                stage_id="stage_id_1", task_template_id="task_template_id_1")

    @pytest.fixture()
    def get_actions_dtos_for_a_stage(self):
        StageActionDetailsDTOFactory.reset_sequence()
        actions = StageActionDetailsDTOFactory.create_batch(
                size=2, stage_id="stage_id_1")
        return actions

    @pytest.fixture()
    def get_field_ids_for_two_tasks_in_same_stage(self):
        return [TaskTemplateStageFieldsDTO(
                task_template_id="task_template_id_1",
                task_id=1,
                db_stage_id=1,
                stage_color="green",
                display_name="display_name_1",
                stage_id="stage_id_1",
                field_ids=["FIELD-ID-1", "FIELD-ID-2"]
        ),
                TaskTemplateStageFieldsDTO(
                        task_template_id="task_template_id_1",
                        task_id=2,
                        db_stage_id=2,
                        stage_color="blue",
                        display_name="display_name_2",
                        stage_id="stage_id_1",
                        field_ids=["FIELD-ID-1", "FIELD-ID-2"]
                )
        ]

    @pytest.fixture
    def interactor_mock(self, action_storage, field_storage, stage_storage,
                        task_storage):
        interactor = GetTaskFieldsAndActionsInteractor(
                field_storage=field_storage, stage_storage=stage_storage,
                task_storage=task_storage, action_storage=action_storage)
        return interactor

    @pytest.fixture()
    def task_fields_dtos_with_for_same_stage_tasks(self):
        TaskFieldsDTOFactory.reset_sequence()
        tasks = TaskFieldsDTOFactory.create_batch(size=2,
                                                  stage_id="stage_id_1")
        return tasks

    @pytest.fixture()
    def get_fields_dtos_for_two_tasks_in_same_stage(self):
        FieldDetailsDTOWithTaskIdFactory.reset_sequence()
        fields = FieldDetailsDTOWithTaskIdFactory.create_batch(size=2,
                                                               task_id=1)
        FieldDetailsDTOWithTaskIdFactory.reset_sequence()
        fields.append(FieldDetailsDTOWithTaskIdFactory(task_id=2))
        fields.append(FieldDetailsDTOWithTaskIdFactory(task_id=2))
        return fields

    @staticmethod
    def storage_method_mocks(field_storage,
                             stage_ids, stage_storage, task_dtos,
                             task_ids, task_storage,
                             task_template_stages_dtos):
        task_storage.get_valid_task_ids.return_value = task_ids
        stage_storage.get_existing_stage_ids.return_value = stage_ids
        task_storage.validate_task_related_stage_ids.return_value = task_dtos
        stage_storage.get_stage_details.return_value = \
            task_template_stages_dtos

    @staticmethod
    def interactor_mocks(mocker, action_dtos, field_ids, field_dtos):
        prepare_actions_for_get_task_fields_and_actions(mocker, action_dtos)
        prepare_fields_for_get_task_fields_and_actions(mocker, field_dtos,
                                                       field_ids)

    def test_get_user_permitted_fields_and_actions(
            self, action_storage, stage_storage, task_storage, field_storage,
            mocker, get_task_template_stage_dtos_for_two_tasks, snapshot,
            get_actions_dtos, get_field_ids, interactor_mock,
            get_fields_dtos, expected_response,
            get_field_ids_for_two_tasks, task_fields_dtos):
        # Arrange
        user_id = "user_id_1"
        view_type = ViewType.LIST.value
        GetTaskDetailsDTOFactory.reset_sequence()
        task_dtos = GetTaskDetailsDTOFactory.create_batch(size=2)

        interactor = interactor_mock
        task_ids = [1, 2]
        task_template_stages_dtos = get_task_template_stage_dtos_for_two_tasks
        stage_ids = ["stage_id_1", "stage_id_2"]
        action_dtos = get_actions_dtos
        field_dtos = get_fields_dtos
        get_field_ids_for_storage = get_field_ids_for_two_tasks
        self.storage_method_mocks(
                field_storage, stage_ids, stage_storage,
                task_dtos, task_ids, task_storage, task_template_stages_dtos)
        field_storage.get_field_ids.return_value = get_field_ids_for_storage
        self.interactor_mocks(mocker, action_dtos, get_field_ids, field_dtos)

        # Act
        response = interactor.get_task_fields_and_action(task_dtos, user_id,
                                                         view_type)

        # Assert
        stage_storage.get_stage_details.assert_called_once_with(task_dtos)
        task_storage.validate_task_related_stage_ids.assert_called_once_with(
                task_dtos)

        snapshot.assert_match(response, "response")

    def test_get_actions_and_fields_when_two_tasks_are_in_same_stage(
            self, action_storage, stage_storage, task_storage, field_storage,
            mocker, interactor_mock, snapshot,
            get_task_dtos_for_two_tasks_in_same_stage,
            get_task_template_stage_dtos_for_two_tasks_in_same_stage,
            get_actions_dtos_for_a_stage,
            get_field_ids_for_two_tasks_in_same_stage,
            get_fields_dtos_for_two_tasks_in_same_stage,
            task_fields_dtos_with_for_same_stage_tasks):
        # Arrange
        user_id = "user_id_1"
        view_type = ViewType.LIST.value

        stage_ids = ["stage_id_1"]
        action_dtos = get_actions_dtos_for_a_stage
        field_dtos = get_fields_dtos_for_two_tasks_in_same_stage
        task_dtos = get_task_dtos_for_two_tasks_in_same_stage
        action_ids = [1, 2, 3, 4]
        task_ids = [1, 2]
        prepare_get_permitted_action_ids_for_project(mocker,
                                                     action_ids=action_ids)
        field_ids = ["FIELD-ID-1", "FIELD-ID-2", "FIELD-ID-3", "FIELD-ID-4"]
        prepare_get_field_ids_having_permission_for_user_projects(mocker,
                                                                  field_ids)
        interactor = interactor_mock

        task_template_stages_dtos = \
            get_task_template_stage_dtos_for_two_tasks_in_same_stage

        self.storage_method_mocks(
                field_storage, stage_ids, stage_storage,
                task_dtos, task_ids, task_storage, task_template_stages_dtos)

        self.interactor_mocks(mocker, action_dtos,
                              get_field_ids_for_two_tasks_in_same_stage,
                              field_dtos)

        # Act
        response = interactor.get_task_fields_and_action(task_dtos, user_id,
                                                         view_type)

        # Assert
        stage_storage.get_stage_details.assert_called_once_with(task_dtos)
        task_storage.validate_task_related_stage_ids.assert_called_once_with(
                task_dtos)

        snapshot.assert_match(response, "response")

    def test_get_actions_and_fields_given_valid_task_template_id_and_stage_id(
            self, action_storage, stage_storage, task_storage, field_storage,
            mocker, interactor_mock,
            get_task_template_stage_dtos_for_two_tasks,
            get_actions_dtos,
            get_fields_dtos, expected_response,
            get_field_ids_for_two_tasks, task_fields_dtos, snapshot):
        # Arrange
        user_id = "user_id_1"
        view_type = ViewType.LIST.value

        GetTaskDetailsDTOFactory.reset_sequence()
        task_dtos = GetTaskDetailsDTOFactory.create_batch(size=2)

        interactor = interactor_mock
        task_ids = [1, 2]
        action_ids = [1, 2, 3, 4]
        prepare_get_permitted_action_ids_for_project(mocker,
                                                     action_ids=action_ids)
        field_ids = ["FIELD-ID-1", "FIELD-ID-2", "FIELD-ID-3", "FIELD-ID-4"]
        prepare_get_field_ids_having_permission_for_user_projects(mocker,
                                                                  field_ids)
        task_template_stages_dtos = get_task_template_stage_dtos_for_two_tasks
        stage_ids = ["stage_id_1", "stage_id_2"]
        action_dtos = get_actions_dtos
        field_dtos = get_fields_dtos
        self.storage_method_mocks(
                field_storage, stage_ids, stage_storage,
                task_dtos, task_ids, task_storage, task_template_stages_dtos)
        self.interactor_mocks(mocker, action_dtos,
                              get_field_ids_for_two_tasks, field_dtos)
        # Act
        response = interactor.get_task_fields_and_action(task_dtos, user_id,
                                                         view_type)

        # Assert
        stage_storage.get_stage_details.assert_called_once_with(task_dtos)
        task_storage.validate_task_related_stage_ids.assert_called_once_with(
                task_dtos)

        snapshot.assert_match(response, "response")

    def test_get_actions_and_fields_given_valid_task_template_id_and_stage_id_and_field_type_is_kanban(
            self, action_storage, stage_storage, task_storage, field_storage,
            mocker, interactor_mock,
            get_task_template_stage_dtos_for_two_tasks,
            get_actions_dtos,
            get_fields_dtos_for_kanban, expected_response,
            get_field_ids_for_two_tasks, task_fields_dtos, snapshot):
        # Arrange
        user_id = "user_id_1"
        view_type = ViewType.KANBAN.value
        action_ids = [1, 2, 3, 4]
        prepare_get_permitted_action_ids_for_project(mocker,
                                                     action_ids=action_ids)
        GetTaskDetailsDTOFactory.reset_sequence()
        task_dtos = GetTaskDetailsDTOFactory.create_batch(size=2)

        interactor = interactor_mock
        task_ids = [1, 2]
        task_template_stages_dtos = get_task_template_stage_dtos_for_two_tasks
        stage_ids = ["stage_id_1", "stage_id_2"]
        field_ids = ["FIELD-ID-1", "FIELD-ID-2", "FIELD-ID-3", "FIELD-ID-4"]
        prepare_get_field_ids_having_permission_for_user_projects(mocker,
                                                                  field_ids)
        action_dtos = get_actions_dtos
        field_dtos = get_fields_dtos_for_kanban
        self.storage_method_mocks(
                field_storage, stage_ids, stage_storage,
                task_dtos, task_ids, task_storage, task_template_stages_dtos)

        self.interactor_mocks(mocker, action_dtos,
                              get_field_ids_for_two_tasks, field_dtos)

        # Act
        response = interactor.get_task_fields_and_action(task_dtos, user_id,
                                                         view_type)

        # Assert
        stage_storage.get_stage_details.assert_called_once_with(task_dtos)
        task_storage.validate_task_related_stage_ids.assert_called_once_with(
                task_dtos)

        snapshot.assert_match(response, "response")

    def test_get_actions_and_fields_when_task_is_in_two_stages(
            self, action_storage, stage_storage, task_storage, field_storage,
            mocker, interactor_mock, get_task_dtos,
            get_task_template_stage_dtos,
            get_actions_dtos, get_fields_dtos_for_a_tasks_with_two_stage,
            get_field_ids_for_a_tasks_in_two_stage, snapshot):
        # Arrange
        user_id = "user_id_1"
        view_type = ViewType.LIST.value

        task_dtos = get_task_dtos
        action_ids = [1, 2, 3, 4]
        prepare_get_permitted_action_ids_for_project(mocker,
                                                     action_ids=action_ids)
        field_ids = ["FIELD-ID-1", "FIELD-ID-2", "FIELD-ID-3", "FIELD-ID-4"]
        prepare_get_field_ids_having_permission_for_user_projects(mocker,
                                                                  field_ids)
        interactor = interactor_mock
        task_ids = [1]

        task_template_stages_dtos = get_task_template_stage_dtos
        stage_ids = ["stage_id_1", "stage_id_2"]
        action_dtos = get_actions_dtos
        field_dtos = get_fields_dtos_for_a_tasks_with_two_stage
        self.storage_method_mocks(
                field_storage, stage_ids, stage_storage,
                task_dtos, task_ids, task_storage, task_template_stages_dtos)

        self.interactor_mocks(mocker, action_dtos,
                              get_field_ids_for_a_tasks_in_two_stage,
                              field_dtos)

        # Act
        response = interactor.get_task_fields_and_action(task_dtos, user_id,
                                                         view_type)

        # Assert
        stage_storage.get_stage_details.assert_called_once_with(task_dtos)
        task_storage.validate_task_related_stage_ids.assert_called_once_with(
                task_dtos)

        snapshot.assert_match(response, "response")

    def test_with_invalid_task_ids_raises_exception(
            self, action_storage, stage_storage, task_storage, field_storage,
            interactor_mock, get_task_dtos):
        # Arrange
        user_id = "user_id_1"
        view_type = ViewType.LIST.value
        interactor = interactor_mock
        task_ids = [1]
        task_storage.get_valid_task_ids.return_value = []

        # Act
        with pytest.raises(InvalidTaskIds):
            interactor.get_task_fields_and_action(get_task_dtos, user_id,
                                                  view_type)

        # Assert
        task_storage.get_valid_task_ids.assert_called_once_with(task_ids)

    def test_with_invalid_stage_ids_raises_exception(
            self, action_storage, stage_storage, task_storage, field_storage,
            interactor_mock, get_task_dtos):
        # Arrange
        user_id = "user_id_1"
        view_type = ViewType.LIST.value

        interactor = interactor_mock
        task_ids = [1]
        stage_ids = ["stage_id_1", "stage_id_2"]
        task_storage.get_valid_task_ids.return_value = task_ids
        stage_storage.get_existing_stage_ids.return_value = []

        # Act
        from ib_tasks.exceptions.stage_custom_exceptions import \
            InvalidStageIdsListException
        with pytest.raises(InvalidStageIdsListException):
            interactor.get_task_fields_and_action(get_task_dtos, user_id,
                                                  view_type)

        # Assert
        stage_storage.get_existing_stage_ids.assert_called_once_with(
                stage_ids)

    def test_with_invalid_stage_related_task_ids_raises_exception(
            self, interactor_mock,
            action_storage, stage_storage, task_storage, field_storage,
            get_task_dtos):
        # Arrange
        user_id = "user_id_1"
        view_type = ViewType.LIST.value

        interactor = interactor_mock
        task_ids = [1]
        stage_ids = ["stage_id_1", "stage_id_2"]
        task_storage.get_valid_task_ids.return_value = task_ids
        task_storage.validate_task_related_stage_ids.return_value = []
        stage_storage.get_existing_stage_ids.return_value = stage_ids

        # Act
        with pytest.raises(InvalidTaskStageIds):
            interactor.get_task_fields_and_action(get_task_dtos, user_id,
                                                  view_type)

        # Assert
        stage_storage.get_existing_stage_ids.assert_called_once_with(
                stage_ids)
        task_storage.validate_task_related_stage_ids.assert_called_once_with(
                get_task_dtos)

    def test_get_actions_and_fields_when_task_has_no_actions_or_fields_returns_empty_list(
            self, interactor_mock, action_storage, stage_storage,
            task_storage, field_storage, mocker,
            get_task_dtos, get_task_template_stage_dtos,
            get_actions_dtos, get_fields_dtos, expected_response,
            task_with_no_fields, snapshot):
        # Arrange
        user_id = "user_id_1"
        view_type = ViewType.LIST.value
        task_dtos = [get_task_dtos[0]]
        action_ids = [1, 2, 3, 4]
        prepare_get_permitted_action_ids_for_project(mocker,
                                                     action_ids=action_ids)

        interactor = interactor_mock
        task_ids = [1]
        task_template_stages_dtos = get_task_template_stage_dtos
        stage_ids = ["stage_id_1"]

        self.storage_method_mocks(
                field_storage, stage_ids, stage_storage,
                task_dtos, task_ids, task_storage, task_template_stages_dtos)
        self.interactor_mocks(mocker, [], task_with_no_fields, [])

        # Act
        response = interactor.get_task_fields_and_action(task_dtos, user_id,
                                                         view_type)

        # Assert
        stage_storage.get_stage_details.assert_called_once_with(task_dtos)
        task_storage.validate_task_related_stage_ids.assert_called_once_with(
                task_dtos)
        snapshot.assert_match(response, "response")
