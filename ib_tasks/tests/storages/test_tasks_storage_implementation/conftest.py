import pytest

from ib_tasks.tests.factories.interactor_dtos import CreateTaskLogDTOFactory
from ib_tasks.tests.factories.models import TaskTemplateFactory, \
    StageModelFactory, TaskTemplateInitialStageFactory, TaskFactory, \
    StageActionFactory


@pytest.fixture(autouse=True)
def reset_sequence():
    TaskFactory.reset_sequence(1)
    CreateTaskLogDTOFactory.reset_sequence(1)
    StageActionFactory.reset_sequence(1)
    TaskTemplateFactory.reset_sequence(1)
    StageModelFactory.reset_sequence(1)
    TaskTemplateInitialStageFactory.reset_sequence(1)


@pytest.fixture
def storage():
    from ib_tasks.storages.tasks_storage_implementation import \
        TasksStorageImplementation
    task_storage = TasksStorageImplementation()
    return task_storage
