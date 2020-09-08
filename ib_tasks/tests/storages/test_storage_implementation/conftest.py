import pytest

from ib_tasks.tests.factories.storage_dtos import TaskTemplateStagesDTOFactory


@pytest.fixture()
def task_template_stages_dtos():
    TaskTemplateStagesDTOFactory.reset_sequence(1)
    return TaskTemplateStagesDTOFactory.create_batch(size=2)
