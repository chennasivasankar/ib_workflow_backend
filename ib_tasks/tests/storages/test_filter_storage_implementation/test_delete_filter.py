import pytest

from ib_tasks.tests.factories.models import FilterFactory


@pytest.mark.django_db
class TestDeleteFilter:

    def test_delete_filter_with_valid_filter_id(self, storage):
        # Arrange
        filter_id = 1
        user_id = '3'
        FilterFactory()

        # Act
        storage.delete_filter(
            filter_id=filter_id,
            user_id=user_id
        )

        # Assert
        from ib_tasks.models import Filter
        is_deleted = not Filter.objects.filter(id=filter_id).exists()

        assert is_deleted is True
