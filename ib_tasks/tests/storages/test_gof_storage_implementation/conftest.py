import pytest

from ib_tasks.tests.factories.models import GoFFactory, TaskTemplateFactory, \
    FieldFactory, GoFRoleFactory, TaskTemplateWith2GoFsFactory
from ib_tasks.tests.factories.storage_dtos import GoFDTOFactory, \
    GoFRolesDTOFactory, CompleteGoFDetailsDTOFactory, GoFRoleDTOFactory, \
    FieldCompleteDetailsDTOFactory


@pytest.fixture
def storage():
    from ib_tasks.storages.gof_storage_implementation import \
        GoFStorageImplementation
    return GoFStorageImplementation()


@pytest.fixture(autouse=True)
def reset_sequence():
    GoFFactory.reset_sequence(1)
    TaskTemplateFactory.reset_sequence(1)
    FieldFactory.reset_sequence(1)
    GoFRoleFactory.reset_sequence(1)
    GoFDTOFactory.reset_sequence(1)
    GoFRolesDTOFactory.reset_sequence(1)
    CompleteGoFDetailsDTOFactory.reset_sequence(1)
    GoFRoleDTOFactory.reset_sequence(1)
    FieldCompleteDetailsDTOFactory.reset_sequence(1)
