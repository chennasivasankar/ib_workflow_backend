import mock
import pytest


class TestGetTaskIdsForGroupInteractor:

    @pytest.fixture
    def elastic_storage_mock(self):
        from ib_adhoc_tasks.interactors.storage_interfaces \
            .elastic_storage_interface import ElasticStorageInterface
        return mock.create_autospec(ElasticStorageInterface)

    def test_success(self):
        pass
