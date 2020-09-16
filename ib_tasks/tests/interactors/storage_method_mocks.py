from unittest.mock import create_autospec

import pytest

from ib_tasks.interactors.storage_interfaces.action_storage_interface import \
    ActionStorageInterface
from ib_tasks.interactors.storage_interfaces.fields_storage_interface import \
    FieldsStorageInterface
from ib_tasks.interactors.storage_interfaces.stages_storage_interface import \
    StageStorageInterface
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface
from ib_tasks.interactors.storage_interfaces.task_template_storage_interface \
    import \
    TaskTemplateStorageInterface


class StorageMethodsMock:
    @pytest.fixture
    def field_storage(self):
        return create_autospec(FieldsStorageInterface)

    @pytest.fixture
    def stage_storage(self):
        stage_storage = create_autospec(StageStorageInterface)
        return stage_storage

    @pytest.fixture
    def task_storage(self):
        task_storage = create_autospec(TaskStorageInterface)
        return task_storage

    @pytest.fixture
    def action_storage(self):
        action_storage = create_autospec(ActionStorageInterface)
        return action_storage

    @pytest.fixture
    def storage_mock(self):
        storage = create_autospec(FieldsStorageInterface)
        return storage

    @pytest.fixture()
    def task_template_storage(self):
        return create_autospec(TaskTemplateStorageInterface)
