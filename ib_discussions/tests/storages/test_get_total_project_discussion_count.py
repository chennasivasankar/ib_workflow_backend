import pytest


class TestGetTotalProjectDiscussionCount:

    @pytest.fixture()
    def storage(self):
        from ib_discussions.storages.storage_implementation import \
            StorageImplementation
        storage = StorageImplementation()
        return storage

    @pytest.mark.django_db
    def test_get_project_total_discussion_count(self):
        pass
