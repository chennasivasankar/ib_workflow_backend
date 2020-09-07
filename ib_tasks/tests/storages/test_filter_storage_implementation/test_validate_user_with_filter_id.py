import pytest

from ib_tasks.tests.factories.models import FilterFactory


@pytest.mark.django_db
class TestValidateUserFilterId:

    def test_validate_user_with_filter_id_with_invalid_user_id(self, storage):
        # Arrange
        filter_id = 1
        user_id = '2'
        FilterFactory()

        # Act
        from ib_tasks.exceptions.filter_exceptions import \
            UserNotHaveAccessToFilter
        with pytest.raises(UserNotHaveAccessToFilter):
            storage.validate_user_with_filter_id(
                filter_id=filter_id,
                user_id=user_id
            )

    def test_validate_user_with_filter_id_with_valid_filter_id(self, storage):
        # Arrange
        filter_id = 1
        user_id = '2'
        FilterFactory(id=filter_id, created_by=user_id)

        # Act
        storage.validate_user_with_filter_id(
            filter_id=filter_id,
            user_id=user_id
        )
