import pytest


@pytest.fixture()
def storage():
    from ib_discussions.storages.storage_implementation import \
        StorageImplementation
    storage = StorageImplementation()
    return storage
