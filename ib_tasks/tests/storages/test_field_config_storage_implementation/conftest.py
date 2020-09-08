import pytest

from ib_tasks.tests.factories.models import GoFFactory, TaskTemplateFactory, \
    FieldFactory, GoFRoleFactory, FieldRoleFactory
from ib_tasks.tests.factories.storage_dtos import GoFDTOFactory, \
    GoFRolesDTOFactory, CompleteGoFDetailsDTOFactory, GoFRoleDTOFactory, \
    FieldCompleteDetailsDTOFactory, FieldDTOFactory, FieldRoleDTOFactory


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
    FieldDTOFactory.reset_sequence()
    FieldRoleDTOFactory.reset_sequence()
    FieldRoleFactory.reset_sequence()


@pytest.fixture
def storage():
    from ib_tasks.storages.field_config_storage_implementation import \
        FieldConfigStorageImplementation
    return FieldConfigStorageImplementation()


@pytest.fixture
def gof_storage():
    from ib_tasks.storages.gof_storage_implementation import \
        GoFStorageImplementation
    return GoFStorageImplementation()
