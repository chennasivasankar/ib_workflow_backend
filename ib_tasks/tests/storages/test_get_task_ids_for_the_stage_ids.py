"""
Created on: 24/07/20
Author: Pavankumar Pamuru

"""

import pytest

from ib_tasks.storages.tasks_storage_implementation import TasksStorageImplementation
from ib_tasks.tests.factories.models import StageModelFactory, StageActionFactory, CurrentTaskStageModelFactory, TaskFactory


@pytest.mark.django_db
class TestGetTaskStageIds:

    @pytest.fixture()
    def populate_data(self):
        StageModelFactory.reset_sequence()
        stages = StageModelFactory.create_batch(size=10)
        StageActionFactory.reset_sequence()
        StageActionFactory.create_batch(size=3, stage=stages[0])
        TaskFactory.reset_sequence()
        tasks = TaskFactory.create_batch(size=3)
        CurrentTaskStageModelFactory.reset_sequence()
        CurrentTaskStageModelFactory(stage=stages[0], task=tasks[0])
        CurrentTaskStageModelFactory(stage=stages[0], task=tasks[1])
        CurrentTaskStageModelFactory(stage=stages[0], task=tasks[2])

    def test_with_valid_details_returns_task_details_dtos(self,
                                                          snapshot,
                                                          populate_data):
        # Arrange
        storage = TasksStorageImplementation()
        stage_ids = ['stage_id_1', 'stage_id_1']

        # Act
        result = storage.get_task_ids_for_the_stage_ids(
            stage_ids=stage_ids,
            offset=0,
            limit=1
        )

        # Assert
        snapshot.assert_match(result, "result")