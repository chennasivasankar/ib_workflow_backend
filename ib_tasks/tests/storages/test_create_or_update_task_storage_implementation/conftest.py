import pytest


@pytest.fixture
def storage():
    from ib_tasks.storages.create_or_update_task_storage_implementation \
        import CreateOrUpdateTaskStorageImplementation
    storage = CreateOrUpdateTaskStorageImplementation()
    return storage
