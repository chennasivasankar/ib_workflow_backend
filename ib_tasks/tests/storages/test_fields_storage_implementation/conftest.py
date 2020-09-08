import pytest

from ib_tasks.tests.factories.models import FieldRoleFactory, TaskGoFFactory, \
    TaskFactory, TaskGoFFieldFactory
from ib_tasks.tests.factories.storage_dtos import \
    FieldCompleteDetailsDTOFactory


@pytest.fixture(autouse=True)
def reset_sequence():
    from ib_tasks.tests.factories.models import GoFFactory, FieldFactory
    GoFFactory.reset_sequence()
    FieldFactory.reset_sequence(1)
    FieldCompleteDetailsDTOFactory.reset_sequence()
    FieldRoleFactory.reset_sequence()
    TaskGoFFactory.reset_sequence()
    TaskFactory.reset_sequence()
    TaskGoFFieldFactory.reset_sequence()


@pytest.fixture
def storage():
    from ib_tasks.storages.fields_storage_implementation import \
        FieldsStorageImplementation
    return FieldsStorageImplementation()
