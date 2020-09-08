import pytest


@pytest.mark.django_db
class TestGetFiltersDetails:

    def test_get_filter_details(self):
        # Arrange
        project_id = "project_1"
        from ib_tasks.tests.factories.models \
            import FilterFactory, TaskTemplateFactory
        TaskTemplateFactory.reset_sequence(0)
        FilterFactory.reset_sequence(1)
        FilterFactory(project_id=project_id)
        from ib_tasks.storages.filter_storage_implementation \
            import FilterStorageImplementation
        from ib_tasks.tests.factories.storage_dtos import FilterDTOFactory
        FilterDTOFactory.reset_sequence(1)
        filter_dtos = [FilterDTOFactory()]
        storage = FilterStorageImplementation()
        user_id = "1"

        # Act
        response = storage.get_filters_dto_to_user(
            user_id=user_id, project_id=project_id)

        # Assert
        assert response == filter_dtos
