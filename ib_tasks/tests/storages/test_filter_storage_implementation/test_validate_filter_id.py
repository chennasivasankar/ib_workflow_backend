import pytest

from ib_tasks.tests.factories.models import FilterFactory


@pytest.mark.django_db
class TestValidateFilterId:

    def test_validate_filter_id_with_invalid_filter_id(self, storage):
        # Arrange
        filter_id = 1

        # Act
        from ib_tasks.exceptions.filter_exceptions import InvalidFilterId
        with pytest.raises(InvalidFilterId):
            storage.validate_filter_id(filter_id=filter_id)

    def test_validate_filter_id_with_valid_filter_id(self, storage):
        # Arrange
        filter_id = 1
        FilterFactory()

        # Act
        storage.validate_filter_id(filter_id=filter_id)
