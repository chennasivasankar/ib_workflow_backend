import pytest

from ib_tasks.tests.factories.models import FilterFactory, \
    FilterConditionFactory


@pytest.mark.django_db
class TestGetEnableFiltersDTO:

    def test_get_enabled_filters_dto_to_user_with(self, snapshot, storage):
        # Arrange
        user_id = '1'
        project_id = "project_1"
        from ib_tasks.constants.enum import Status
        filter_1 = FilterFactory(
            created_by=user_id, is_selected=Status.DISABLED.value,
            project_id=project_id
        )
        filter_2 = FilterFactory(created_by=user_id, project_id=project_id)

        FilterConditionFactory.create_batch(3, filter=filter_1)
        FilterConditionFactory.create_batch(3, filter=filter_2)

        # Act
        response = storage.get_enabled_filters_dto_to_user(
            user_id=user_id, project_id=project_id
        )

        # Assert
        snapshot.assert_match(response, 'enabled_filters')

    def test_get_enabled_filters_dto_to_user_with_all_filters_enabled(
            self, snapshot, storage):
        # Arrange
        user_id = '1'
        project_id = "project_1"
        filter_1 = FilterFactory(
            created_by=user_id, project_id=project_id)
        filter_2 = FilterFactory(created_by=user_id, project_id=project_id)

        FilterConditionFactory.create_batch(3, filter=filter_1)
        FilterConditionFactory.create_batch(3, filter=filter_2)

        # Act
        response = storage.get_enabled_filters_dto_to_user(
            user_id=user_id, project_id=project_id)

        # Assert
        snapshot.assert_match(response, 'enabled_filters')

    def test_get_enabled_filters_dto_to_user_with_no_filters_enabled(
            self, snapshot, storage):
        # Arrange
        user_id = '1'
        project_id = "project_1"
        from ib_tasks.constants.enum import Status
        filter_1 = FilterFactory(
            created_by=user_id,
            is_selected=Status.DISABLED.value,
            project_id=project_id
        )
        filter_2 = FilterFactory(
            created_by=user_id,
            is_selected=Status.DISABLED.value,
            project_id=project_id
        )

        FilterConditionFactory.create_batch(3, filter=filter_1)
        FilterConditionFactory.create_batch(3, filter=filter_2)

        # Act
        response = storage.get_enabled_filters_dto_to_user(
            user_id=user_id, project_id=project_id)

        # Assert
        snapshot.assert_match(response, 'enabled_filters')
