import pytest


@pytest.mark.django_db
class TestGetFiltersDetails:

    def test_get_filter_details(self):

        # Arrange
        from ib_tasks.tests.factories.models import FilterFactory
        FilterFactory.reset_sequence(1)
        FilterFactory()
        from ib_tasks.storages.filter_storage_implementation \
            import FilterStorageImplementation
        from ib_tasks.tests.factories.storage_dtos import FilterDTOFactory
        FilterDTOFactory.reset_sequence(1)
        filter_dtos = [FilterDTOFactory()]
        storage = FilterStorageImplementation()
        user_id = "1"

        # Act
        response = storage.get_filters_dto_to_user(user_id=user_id)

        # Assert
        assert response == filter_dtos