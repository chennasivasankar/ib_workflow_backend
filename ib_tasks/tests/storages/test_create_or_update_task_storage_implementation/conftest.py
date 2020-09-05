import pytest

from ib_tasks.tests.factories.models import TaskFactory, TaskGoFFactory, \
    GoFRoleFactory, GoFFactory, FieldRoleFactory, FieldFactory, \
    TaskGoFFieldFactory
from ib_tasks.tests.factories.storage_dtos import \
    TaskGoFWithTaskIdDTOFactory, TaskGoFFieldDTOFactory


@pytest.fixture(autouse=True)
def reset_sequence():
    TaskGoFWithTaskIdDTOFactory.reset_sequence()
    TaskFactory.reset_sequence()
    TaskGoFFieldDTOFactory.reset_sequence()
    TaskGoFFactory.reset_sequence()
    GoFRoleFactory.reset_sequence()
    GoFFactory.reset_sequence()
    FieldRoleFactory.reset_sequence()
    FieldFactory.reset_sequence()
    TaskGoFFieldFactory.reset_sequence()


@pytest.fixture
def storage():
    from ib_tasks.storages.create_or_update_task_storage_implementation \
        import CreateOrUpdateTaskStorageImplementation
    storage = CreateOrUpdateTaskStorageImplementation()
    return storage
