import pytest

from ib_boards.presenters.presenter_implementation import \
    PresenterImplementation
from ib_boards.tests.factories.interactor_dtos import TaskColumnDTOFactory, \
    StageAssigneesDTOFactory
from ib_boards.tests.factories.storage_dtos import (
    TaskActionsDTOFactory, TaskFieldsDTOFactory,
    ColumnCompleteDetailsDTOFactory, TaskStageDTOFactory)


class TestGetColumnDetails:

    @pytest.fixture()
    def get_task_actions_dtos_with_duplicates(self):
        TaskActionsDTOFactory.reset_sequence()
        return TaskActionsDTOFactory.create_batch(size=3) + [TaskActionsDTOFactory(
            task_id='task_id_0', transition_template_id=None
        )]

    @pytest.fixture()
    def get_task_fields_dtos_with_duplicates(self):
        TaskFieldsDTOFactory.reset_sequence()
        return TaskFieldsDTOFactory.create_batch(size=3) + [TaskFieldsDTOFactory(
            task_id='task_id_0'
        )]

    @pytest.fixture()
    def get_column_task_details_with_duplicates(self):
        TaskColumnDTOFactory.reset_sequence()
        return TaskColumnDTOFactory.create_batch(size=3) + [TaskColumnDTOFactory(
            column_id='COLUMN_ID_1', task_id=1
        )]

    @pytest.fixture()
    def get_task_actions_dtos_with_duplicate_fields(self):
        TaskActionsDTOFactory.reset_sequence()
        return TaskActionsDTOFactory.create_batch(size=3) + [
            TaskActionsDTOFactory(
                task_id='task_id_0', action_id='action_id_0'
            )]

    @pytest.fixture()
    def get_task_fields_dtos_with_duplicates_fields(self):
        TaskFieldsDTOFactory.reset_sequence()
        return TaskFieldsDTOFactory.create_batch(size=3) + [
            TaskFieldsDTOFactory(
                task_id='task_id_0', field_id='field_id_0'
            )]

    @pytest.fixture
    def task_stage_dtos(self):
        TaskStageDTOFactory.reset_sequence()
        return TaskStageDTOFactory.create_batch(size=3)

    @pytest.fixture()
    def get_task_actions_dtos(self):
        TaskActionsDTOFactory.reset_sequence()
        return TaskActionsDTOFactory.create_batch(size=3)

    @pytest.fixture()
    def get_task_fields_dtos(self):
        TaskFieldsDTOFactory.reset_sequence()
        tasks = TaskFieldsDTOFactory.create_batch(size=3, task_id="task_id_1", stage_id="stage_id_1")
        tasks.append(TaskFieldsDTOFactory(task_id="task_id_2", stage_id="stage_id_2", key="key_0"))
        tasks.append(TaskFieldsDTOFactory(task_id="task_id_2", stage_id="stage_id_2", key="key_4"))
        tasks.append(TaskFieldsDTOFactory(task_id="task_id_2", stage_id="stage_id_2", key="key_1"))
        tasks.append(TaskFieldsDTOFactory(task_id="task_id_0", stage_id="stage_id_0"))
        return tasks

    @pytest.fixture()
    def get_column_task_details(self):
        TaskColumnDTOFactory.reset_sequence()
        return TaskColumnDTOFactory.create_batch(size=3)

    @pytest.fixture()
    def get_column_details(self):
        ColumnCompleteDetailsDTOFactory.reset_sequence()
        return ColumnCompleteDetailsDTOFactory.create_batch(size=3)

    @pytest.fixture
    def assignee_dtos(self):
        StageAssigneesDTOFactory.reset_sequence()
        return StageAssigneesDTOFactory.create_batch(4)

    def test_get_response_for_column_details_with_duplicate_tasks_in_same_column(
            self, get_task_fields_dtos_with_duplicates, assignee_dtos,
            get_column_task_details_with_duplicates, task_stage_dtos,
            get_task_actions_dtos_with_duplicates, get_column_details, snapshot):
        # Arrange
        task_fields_dtos = get_task_fields_dtos_with_duplicates
        task_actions_dtos = get_task_actions_dtos_with_duplicates
        task_details = get_column_task_details_with_duplicates
        column_details = get_column_details
        presenter = PresenterImplementation()

        # Act
        response = presenter.get_response_for_column_details(
            column_details=column_details,
            column_tasks=task_details, task_fields_dtos=task_fields_dtos,
            task_actions_dtos=task_actions_dtos,
            task_stage_dtos=task_stage_dtos,
            assignees_dtos=assignee_dtos
        )

        # Assert
        import json
        result = json.loads(response.content)

        snapshot.assert_match(result, "column_details_with_duplicates")

    def test_with_duplicate_tasks_in_same_column_and_duplicate_fields(
            self, get_task_fields_dtos_with_duplicates_fields,
            get_column_task_details_with_duplicates,
            task_stage_dtos, assignee_dtos,
            get_task_actions_dtos_with_duplicate_fields, get_column_details, snapshot):
        # Arrange
        task_fields_dtos = get_task_fields_dtos_with_duplicates_fields
        task_actions_dtos = get_task_actions_dtos_with_duplicate_fields
        task_details = get_column_task_details_with_duplicates
        column_details = get_column_details
        presenter = PresenterImplementation()

        # Act
        response = presenter.get_response_for_column_details(
            column_details=column_details,
            column_tasks=task_details, task_fields_dtos=task_fields_dtos,
            task_actions_dtos=task_actions_dtos,
            task_stage_dtos=task_stage_dtos,
            assignees_dtos=assignee_dtos
        )

        # Assert
        import json
        result = json.loads(response.content)

        snapshot.assert_match(result, "column_details_with_duplicates_fields")

    def test_get_response_for_column_details_with_proper_data(
            self, get_task_fields_dtos, get_column_task_details,
            get_task_actions_dtos, get_column_details, snapshot,
            task_stage_dtos, assignee_dtos):
        # Arrange
        task_fields_dtos = get_task_fields_dtos
        task_actions_dtos = get_task_actions_dtos
        task_details = get_column_task_details
        column_details = get_column_details
        presenter = PresenterImplementation()

        # Act
        response = presenter.get_response_for_column_details(
            column_details=column_details,
            column_tasks=task_details, task_fields_dtos=task_fields_dtos,
            task_actions_dtos=task_actions_dtos,
            task_stage_dtos=task_stage_dtos,
            assignees_dtos=assignee_dtos
        )

        # Assert
        import json
        result = json.loads(response.content)

        snapshot.assert_match(result, "column_details_with_proper_data")

    def test_get_response_for_column_details_with_no_tasks(
            self, get_task_fields_dtos, get_column_task_details,
            get_task_actions_dtos, get_column_details, snapshot,
            task_stage_dtos, assignee_dtos):
        # Arrange
        task_fields_dtos = []
        task_actions_dtos = []
        task_details = []
        column_details = get_column_details
        presenter = PresenterImplementation()

        # Act
        response = presenter.get_response_for_column_details(
            column_details=column_details,
            column_tasks=task_details, task_fields_dtos=task_fields_dtos,
            task_actions_dtos=task_actions_dtos,
            task_stage_dtos=task_stage_dtos,
            assignees_dtos=assignee_dtos
        )

        # Assert
        import json
        result = json.loads(response.content)

        snapshot.assert_match(result, "column_details_with_proper_data")
