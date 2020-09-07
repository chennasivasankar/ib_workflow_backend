import pytest

from ib_tasks.tests.factories.filter_dtos import CreateFilterDTOFactory, \
    UpdateFilterDTOFactory, CreateConditionDTOFactory, FilterDTOFactory, \
    ConditionDTOFactory
from ib_tasks.tests.factories.models import TaskTemplateFactory, FilterFactory, \
    FieldFactory, GoFToTaskTemplateFactory


@pytest.fixture(autouse=True)
def reset_sequence():
    CreateFilterDTOFactory.reset_sequence()
    UpdateFilterDTOFactory.reset_sequence()
    CreateConditionDTOFactory.reset_sequence()
    FilterDTOFactory.reset_sequence()
    ConditionDTOFactory.reset_sequence()
    TaskTemplateFactory.reset_sequence()
    FilterFactory.reset_sequence()
    FieldFactory.reset_sequence()
    GoFToTaskTemplateFactory.reset_sequence()


@pytest.fixture
def storage():
    from ib_tasks.storages.filter_storage_implementation import \
        FilterStorageImplementation
    return FilterStorageImplementation()


@pytest.fixture
def filter_dto():
    return CreateFilterDTOFactory()


@pytest.fixture
def update_filter_dto():
    return UpdateFilterDTOFactory()


@pytest.fixture
def condition_dtos():
    return CreateConditionDTOFactory.create_batch(3)


@pytest.fixture
def new_filter_dto():
    return FilterDTOFactory()


@pytest.fixture
def new_condition_dtos():
    return ConditionDTOFactory.create_batch(3)
