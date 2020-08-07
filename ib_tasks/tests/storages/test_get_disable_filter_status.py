import pytest


@pytest.mark.django_db
class TestGetFiltersDetails:

    def test_get_filter_details(self):

        # Arrange
        from ib_tasks.tests.factories.models import FilterFactory
        FilterFactory.reset_sequence(1)
        from ib_tasks.constants.enum import Status
        FilterFactory(is_selected=Status.ENABLED.value)
        from ib_tasks.storages.filter_storage_implementation \
            import FilterStorageImplementation
        storage = FilterStorageImplementation()
        filter_id = 1

        # Act
        response = storage.enable_filter_status(filter_id=filter_id)

        # Assert
        from ib_tasks.models import Filter
        filter_obj = Filter.objects.get(id=filter_id)
        assert response == filter_obj.is_selected