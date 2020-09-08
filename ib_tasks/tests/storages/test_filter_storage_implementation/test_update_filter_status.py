import pytest


@pytest.mark.django_db
class TestGetFiltersDetails:

    def test_get_filter_details_with_is_selected_enabled(self):
        # Arrange
        from ib_tasks.tests.factories.models import FilterFactory
        FilterFactory.reset_sequence(1)
        from ib_tasks.constants.enum import Status
        FilterFactory(is_selected=Status.DISABLED.value)
        from ib_tasks.storages.filter_storage_implementation \
            import FilterStorageImplementation
        storage = FilterStorageImplementation()
        filter_id = 1

        # Act
        response = storage.update_filter_status(
            filter_id=filter_id, is_selected=Status.ENABLED.value
        )

        # Assert
        from ib_tasks.models import Filter
        filter_obj = Filter.objects.get(id=filter_id)
        assert response == filter_obj.is_selected

    def test_get_filter_details(self):
        # Arrange
        from ib_tasks.tests.factories.models import FilterFactory
        FilterFactory.reset_sequence(1)
        from ib_tasks.constants.enum import Status
        FilterFactory(is_selected=Status.ENABLED.value)
        from ib_tasks.storages.filter_storage_implementation \
            import FilterStorageImplementation
        storage = FilterStorageImplementation()
        action_enum = Status.ENABLED.value
        filter_id = 1

        # Act
        response = storage.update_filter_status(
            filter_id=filter_id, is_selected=action_enum
        )

        # Assert
        from ib_tasks.models import Filter
        filter_obj = Filter.objects.get(id=filter_id)
        assert response == filter_obj.is_selected
