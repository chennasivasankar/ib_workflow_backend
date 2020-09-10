import pytest

from ib_tasks.tests.factories.models import TaskTemplateFactory, \
    ProjectTaskTemplateFactory


@pytest.fixture
def storage():
    from ib_tasks.storages.task_template_storage_implementation import \
        TaskTemplateStorageImplementation
    return TaskTemplateStorageImplementation()


@pytest.fixture(autouse=True)
def reset_sequence():
    from ib_tasks.tests.factories.interactor_dtos import \
        GoFWithOrderAndAddAnotherDTOFactory, GlobalConstantsDTOFactory
    from ib_tasks.tests.factories.models import GoFFactory, \
        GlobalConstantFactory, GoFToTaskTemplateFactory
    GoFWithOrderAndAddAnotherDTOFactory.reset_sequence()
    TaskTemplateFactory.reset_sequence()
    GoFFactory.reset_sequence()
    GlobalConstantFactory.reset_sequence()
    GlobalConstantsDTOFactory.reset_sequence()
    GoFToTaskTemplateFactory.reset_sequence()
    GoFToTaskTemplateFactory.enable_add_another_gof.reset()
    ProjectTaskTemplateFactory.reset_sequence(1)
