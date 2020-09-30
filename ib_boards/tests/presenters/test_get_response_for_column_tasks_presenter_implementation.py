"""
Created on: 03/08/20
Author: Pavankumar Pamuru

"""

import pytest

from ib_boards.interactors.presenter_interfaces.presenter_interface import \
    CompleteTasksDetailsDTO
from ib_boards.presenters.presenter_implementation import \
    GetColumnTasksPresenterImplementation
from ib_boards.tests.factories.interactor_dtos import AssigneeDetailsDTOFactory
from ib_boards.tests.factories.presenter_dtos import TaskDisplayIdDTOFactory
from ib_boards.tests.factories.storage_dtos import (
    TaskActionsDTOFactory, TaskFieldsDTOFactory, TaskStageDTOFactory)


class TestGetColumnDetails:

    @pytest.fixture
    def task_stage_dtos(self):
        TaskStageDTOFactory.stage_color.reset()
        TaskStageDTOFactory.reset_sequence()
        return TaskStageDTOFactory.create_batch(size=3)

    @pytest.fixture()
    def get_task_actions_dtos_with_duplicates(self):
        TaskActionsDTOFactory.reset_sequence()
        return TaskActionsDTOFactory.create_batch(size=3) + [TaskActionsDTOFactory(
            task_id=0
        )]

    @pytest.fixture()
    def get_task_fields_dtos_with_duplicates(self):
        TaskFieldsDTOFactory.reset_sequence()
        return TaskFieldsDTOFactory.create_batch(size=3) + [TaskFieldsDTOFactory(
            task_id=0
        )]

    @pytest.fixture()
    def get_task_actions_dtos_with_duplicate_fields(self):
        TaskActionsDTOFactory.reset_sequence()
        return TaskActionsDTOFactory.create_batch(size=3) + [
            TaskActionsDTOFactory(
                task_id=0, action_id='action_id_0'
            )]

    @pytest.fixture()
    def get_task_fields_dtos_with_duplicates_fields(self):
        TaskFieldsDTOFactory.reset_sequence()
        return TaskFieldsDTOFactory.create_batch(size=3) + [
            TaskFieldsDTOFactory(
                task_id=0, field_id='field_id_0'
            )]

    @pytest.fixture()
    def get_task_actions_dtos(self):
        TaskActionsDTOFactory.reset_sequence()
        return TaskActionsDTOFactory.create_batch(size=3)

    @pytest.fixture()
    def get_task_fields_dtos(self):
        TaskFieldsDTOFactory.reset_sequence()
        tasks = TaskFieldsDTOFactory.create_batch(size=3, task_id=1,
                                                  stage_id="stage_id_1")
        tasks.append(
            TaskFieldsDTOFactory(task_id=2, stage_id="stage_id_2",
                                 key="key_0"))
        tasks.append(
            TaskFieldsDTOFactory(task_id=2, stage_id="stage_id_2",
                                 key="key_4"))
        tasks.append(
            TaskFieldsDTOFactory(task_id=2, stage_id="stage_id_2",
                                 key="key_1"))
        tasks.append(
            TaskFieldsDTOFactory(task_id=0, stage_id="stage_id_0"))
        return tasks

    @pytest.fixture
    def assignee_dtos(self):
        from ib_boards.tests.factories.interactor_dtos import \
            StageAssigneesDTOFactory
        AssigneeDetailsDTOFactory.reset_sequence()
        StageAssigneesDTOFactory.reset_sequence()
        return StageAssigneesDTOFactory.create_batch(4)

    @pytest.fixture
    def task_id_dtos(self):
        TaskDisplayIdDTOFactory.reset_sequence()
        task_ids_dtos = TaskDisplayIdDTOFactory.create_batch(3)
        return task_ids_dtos

    @staticmethod
    def column_details(total_tasks, task_fields_dtos,
                       task_actions_dtos, task_stage_dtos, assignee_dtos,
                       task_id_dtos):
        column_details = CompleteTasksDetailsDTO(total_tasks=total_tasks,
                                                 task_fields_dtos=task_fields_dtos,
                                                 task_actions_dtos=task_actions_dtos,
                                                 task_id_dtos=task_id_dtos,
                                                 task_stage_dtos=task_stage_dtos,
                                                 assignees_dtos=assignee_dtos)
        return column_details

    def test_get_response_for_column_details_with_duplicate_tasks_in_same_column(
            self, get_task_fields_dtos_with_duplicates, assignee_dtos,
            get_task_actions_dtos_with_duplicates, snapshot, task_stage_dtos,
            task_id_dtos):
        total_tasks = 10

        # Arrange
        task_fields_dtos = get_task_fields_dtos_with_duplicates
        task_actions_dtos = get_task_actions_dtos_with_duplicates
        presenter = GetColumnTasksPresenterImplementation()
        column_details = self.column_details(total_tasks, task_fields_dtos,
                                             task_actions_dtos,
                                             task_stage_dtos, assignee_dtos,
                                             task_id_dtos)
        # Act
        response = presenter.get_response_for_column_tasks(
            column_details
        )

        # Assert
        import json
        result = json.loads(response.content)

        snapshot.assert_match(result, "column_details_with_duplicates")

    def test_with_duplicate_tasks_in_same_column_and_duplicate_fields(
            self, get_task_fields_dtos_with_duplicates_fields,
            get_task_actions_dtos_with_duplicate_fields, snapshot,
            task_stage_dtos, assignee_dtos, task_id_dtos):
        # Arrange
        task_fields_dtos = get_task_fields_dtos_with_duplicates_fields
        task_actions_dtos = get_task_actions_dtos_with_duplicate_fields
        total_tasks = 10
        presenter = GetColumnTasksPresenterImplementation()

        column_details = self.column_details(total_tasks, task_fields_dtos,
                                             task_actions_dtos,
                                             task_stage_dtos, assignee_dtos,
                                             task_id_dtos)
        # Act
        response = presenter.get_response_for_column_tasks(
            column_details
        )

        # Assert
        import json
        result = json.loads(response.content)

        snapshot.assert_match(result, "column_details_with_duplicates_fields")

    def test_get_response_for_column_details_with_proper_data(
            self, get_task_fields_dtos, assignee_dtos, task_id_dtos,
            get_task_actions_dtos, snapshot, task_stage_dtos):
        # Arrange
        total_tasks = 10
        task_fields_dtos = get_task_fields_dtos
        task_actions_dtos = get_task_actions_dtos
        presenter = GetColumnTasksPresenterImplementation()
        column_details = self.column_details(total_tasks, task_fields_dtos,
                                             task_actions_dtos,
                                             task_stage_dtos, assignee_dtos,
                                             task_id_dtos)

        # Act
        response = presenter.get_response_for_column_tasks(
            column_details
        )

        # Assert
        import json
        result = json.loads(response.content)

        snapshot.assert_match(result, "column_details_with_proper_data")
