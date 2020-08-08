import pytest


@pytest.mark.django_db
class TestGetConditionsToFilter:

    def test_get_conditions_to_filter(self):

        # Arrange
        from ib_tasks.tests.factories.models import FilterConditionFactory, FieldFactory
        FilterConditionFactory.reset_sequence(1)
        FieldFactory.reset_sequence(1)
        FilterConditionFactory()
        from ib_tasks.storages.filter_storage_implementation \
            import FilterStorageImplementation
        from ib_tasks.tests.factories.storage_dtos import ConditionDTOFactory
        ConditionDTOFactory.reset_sequence(1)
        conditions_dto = [ConditionDTOFactory()]
        storage = FilterStorageImplementation()
        filter_ids = [1]

        # Act
        response = storage.get_conditions_to_filters(filter_ids=filter_ids)

        # Assert
        assert response == conditions_dto