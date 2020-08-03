"""
Created on: 03/08/20
Author: Pavankumar Pamuru

"""

import pytest

from ib_boards.presenters.presenter_implementation import \
    GetColumnTasksPresenterImplementation
from ib_boards.tests.factories.storage_dtos import (
    TaskActionsDTOFactory, TaskFieldsDTOFactory)


class TestGetColumnDetails:

    @pytest.fixture()
    def get_task_actions_dtos_with_duplicates(self):
        TaskActionsDTOFactory.reset_sequence()
        return TaskActionsDTOFactory.create_batch(size=3) + [TaskActionsDTOFactory(
            task_id='task_id_0'
        )]

    @pytest.fixture()
    def get_task_fields_dtos_with_duplicates(self):
        TaskFieldsDTOFactory.reset_sequence()
        return TaskFieldsDTOFactory.create_batch(size=3) + [TaskFieldsDTOFactory(
            task_id='task_id_0'
        )]

    @pytest.fixture()
    def get_task_actions_dtos(self):
        TaskActionsDTOFactory.reset_sequence()
        return TaskActionsDTOFactory.create_batch(size=3)

    @pytest.fixture()
    def get_task_fields_dtos(self):
        TaskFieldsDTOFactory.reset_sequence()
        return TaskFieldsDTOFactory.create_batch(size=3)

    def test_get_response_for_column_details_with_duplicate_tasks_in_same_column(
            self, get_task_fields_dtos_with_duplicates,
            get_task_actions_dtos_with_duplicates, snapshot):
        total_tasks = 10
        task_ids = ['task_id_0', 'task_id_0', 'task_id_1', 'task_id_2']
        # Arrange
        task_fields_dtos = get_task_fields_dtos_with_duplicates
        task_actions_dtos = get_task_actions_dtos_with_duplicates
        presenter = GetColumnTasksPresenterImplementation()

        # Act
        response = presenter.get_response_for_column_tasks(
            total_tasks=total_tasks, task_fields_dtos=task_fields_dtos,
            task_actions_dtos=task_actions_dtos,
            task_ids=task_ids
        )

        # Assert
        import json
        result = json.loads(response.content)

        snapshot.assert_match(result, "column_details_with_duplicates")

    def test_get_response_for_column_details_with_proper_data(
            self, get_task_fields_dtos,
            get_task_actions_dtos, snapshot):
        # Arrange
        total_tasks = 10
        task_ids = ['task_id_0', 'task_id_1', 'task_id_2']
        task_fields_dtos = get_task_fields_dtos
        task_actions_dtos = get_task_actions_dtos
        presenter = GetColumnTasksPresenterImplementation()

        # Act
        response = presenter.get_response_for_column_tasks(
            total_tasks=total_tasks, task_fields_dtos=task_fields_dtos,
            task_actions_dtos=task_actions_dtos,
            task_ids=task_ids
        )

        # Assert
        import json
        result = json.loads(response.content)

        snapshot.assert_match(result, "column_details_with_proper_data")