import pytest

from ib_boards.storages.storage_implementation import StorageImplementation
from ib_boards.tests.factories.models import BoardFactory, ColumnPermissionFactory, ColumnFactory
from ib_boards.tests.factories.storage_dtos import ColumnDetailsDTOFactory


@pytest.mark.django_db
class TestColumnDetails:

    @pytest.fixture()
    def column_details(self):
        ColumnDetailsDTOFactory.reset_sequence()
        return ColumnDetailsDTOFactory.create_batch(size=4)

    @pytest.fixture()
    def create_columns(self):
        BoardFactory.reset_sequence()
        board = BoardFactory()
        ColumnFactory.reset_sequence()
        ColumnPermissionFactory.reset_sequence()
        columns = ColumnFactory.create_batch(size=4, board=board)
        ColumnPermissionFactory.create_batch(size=2, column=columns[0])
        ColumnPermissionFactory.create_batch(size=2, column=columns[1])
        ColumnPermissionFactory.create_batch(size=2, column=columns[2])
        ColumnPermissionFactory.create_batch(size=2, column=columns[3])

    def test_get_column_details_given_column_ids(self, create_columns,
                                                 column_details):
        # Arrange
        expected_column_dtos = column_details
        column_ids = ["COLUMN_ID_1", "COLUMN_ID_2", "COLUMN_ID_3", "COLUMN_ID_4"]
        storage = StorageImplementation()

        # Act
        column_details = storage.get_columns_details(column_ids)

        # Assert
        assert column_details == expected_column_dtos
