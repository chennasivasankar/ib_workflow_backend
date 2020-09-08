import pytest


@pytest.fixture
def storage():
    from ib_tasks.storages.action_storage_implementation import \
        ActionsStorageImplementation
    return ActionsStorageImplementation()
