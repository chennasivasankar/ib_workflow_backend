"""
Created on: 22/07/20
Author: Pavankumar Pamuru

"""
import pytest


@pytest.mark.django_db
class TestInvalidUserRoleForColumn:

    @pytest.fixture
    def storage(self):
        from ib_boards.storages.storage_implementation import \
            StorageImplementation
        return StorageImplementation()

    @pytest.fixture
    def reset_sequence(self):
        from ib_boards.tests.factories.models import BoardFactory, ColumnFactory
        BoardFactory.reset_sequence()
        ColumnFactory.reset_sequence()
        from ib_boards.tests.factories.interactor_dtos import BoardDTOFactory
        BoardDTOFactory.reset_sequence()

    def test_with_valid_user_role_for_the_column(self, storage, reset_sequence):
        # Arrange
        user_role = 'USER'
        column_id = 'COLUMN_ID_1'
        from ib_boards.tests.factories.models import BoardFactory, ColumnFactory
        BoardFactory.create_batch(2)
        ColumnFactory.create_batch(3, board_id='BOARD_ID_1')
        from ib_boards.tests.factories.models import ColumnPermissionFactory
        ColumnPermissionFactory(column_id='COLUMN_ID_1', user_role_id='USER')
        ColumnPermissionFactory(column_id='COLUMN_ID_1', user_role_id='ADMIN')

        # Act
        storage.validate_user_role_with_column_roles(user_role=user_role)

    def test_with_invalid_user_role_for_the_column(self, storage, reset_sequence):
        # Arrange
        user_role = 'USER'
        column_id = 'COLUMN_ID_1'
        from ib_boards.tests.factories.models import BoardFactory, ColumnFactory
        BoardFactory.create_batch(2)
        ColumnFactory.create_batch(3, board_id='BOARD_ID_1')
        from ib_boards.tests.factories.models import ColumnPermissionFactory
        ColumnPermissionFactory(column_id='COLUMN_ID_1', user_role_id='ADMIN')

        # Act
        from ib_boards.exceptions.custom_exceptions import \
            UserDoNotHaveAccessToColumn
        with pytest.raises(UserDoNotHaveAccessToColumn):
            storage.validate_user_role_with_column_roles(user_role=user_role)

    def test_with_all_user_roles_for_the_column(self, storage, reset_sequence):
        # Arrange
        user_role = 'USER'
        column_id = 'COLUMN_ID_1'
        from ib_boards.tests.factories.models import BoardFactory, ColumnFactory
        BoardFactory.create_batch(2)
        ColumnFactory.create_batch(3, board_id='BOARD_ID_1')
        from ib_boards.tests.factories.models import ColumnPermissionFactory
        ColumnPermissionFactory(column_id='COLUMN_ID_1', user_role_id='ALL_ROLES')

        # Act
        storage.validate_user_role_with_column_roles(user_role=user_role)

