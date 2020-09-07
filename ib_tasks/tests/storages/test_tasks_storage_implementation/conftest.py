import pytest


@pytest.fixture(autouse=True)
def reset_sequence():
    from ib_tasks.tests.factories.models import TaskFactory, \
        StageActionFactory
    from ib_tasks.tests.factories.interactor_dtos import \
        CreateTaskLogDTOFactory

    TaskFactory.reset_sequence(1)
    CreateTaskLogDTOFactory.reset_sequence(1)
    StageActionFactory.reset_sequence(1)


@pytest.fixture
def task_storage():
    from ib_tasks.storages.tasks_storage_implementation import \
        TasksStorageImplementation
    task_storage = TasksStorageImplementation()
    return task_storage
