import pytest

from ib_tasks.tests.factories.models import CurrentTaskStageModelFactory


@pytest.fixture
def task_storage():
    from ib_tasks.storages.task_stage_storage_implementation import \
        TaskStageStorageImplementation
    task_storage = TaskStageStorageImplementation()
    return task_storage


@pytest.fixture
def reset_sequence():
    CurrentTaskStageModelFactory.reset_sequence()
