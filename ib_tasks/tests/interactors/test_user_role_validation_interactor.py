import pytest
from ib_tasks.interactors.user_role_validation_interactor import \
    UserRoleValidationInteractor
from ib_tasks.tests.common_fixtures.adapters.roles_service import \
    get_user_role_ids


class TestUserRoleValidationInteractor:
    @pytest.fixture
    def field_storage_mock(self):
        from mock import create_autospec
        from ib_tasks.interactors.storage_interfaces.fields_storage_interface \
            import FieldsStorageInterface
        field_storage_mock = create_autospec(FieldsStorageInterface)
        return field_storage_mock

    @pytest.fixture
    def gof_storage_mock(self):
        from mock import create_autospec
        from ib_tasks.interactors.storage_interfaces.gof_storage_interface \
            import GoFStorageInterface
        gof_storage_mock = create_autospec(GoFStorageInterface)
        return gof_storage_mock

    def test_given_all_roles_id_return_true(self, mocker):
        # Arrange
        user_id = "user_1"
        role_ids = ["ALL_ROLES", "FIN_PAYMENT_REQUESTER", "FIN_PAYMENT_POC"]
        get_user_role_ids_mock_method = \
            get_user_role_ids(mocker)

        interactor = UserRoleValidationInteractor()

        # Act
        result = \
            interactor.does_user_has_required_permission(user_id=user_id,
                                                         role_ids=role_ids)

        # Assert
        assert result is True
        get_user_role_ids_mock_method.assert_not_called()

    def test_given_valid_user_roles_return_true(self, mocker):
        # Arrange
        user_id = "user_1"
        role_ids = ["FIN_PAYMENTS_LEVEL3_VERIFIER", "FIN_PAYMENT_REQUESTER"]
        get_user_role_ids_mock_method = \
            get_user_role_ids(mocker)

        interactor = UserRoleValidationInteractor()

        # Act
        result = \
            interactor.does_user_has_required_permission(user_id=user_id,
                                                         role_ids=role_ids)

        # Assert
        assert result is True
        get_user_role_ids_mock_method.assert_called_once_with(user_id=user_id)

    def test_given_invalid_user_roles_return_false(self, mocker):
        # Arrange
        user_id = "user_1"
        role_ids = ["user_role_1", "user_role_2"]
        get_user_role_ids_mock_method = get_user_role_ids(mocker)
        interactor = UserRoleValidationInteractor()

        # Act
        result = \
            interactor.does_user_has_required_permission(user_id=user_id,
                                                         role_ids=role_ids)

        # Assert
        assert result is False
        get_user_role_ids_mock_method.assert_called_once_with(user_id=user_id)

    def test_get_gof_ids_having_read_permission_for_user(
            self, mocker, gof_storage_mock):
        # Arrange
        user_id = "user_1"
        gof_ids = ["gof_1", "gof_2", "gof_3"]
        expected_gof_ids = ["gof_1", "gof_2"]
        get_user_role_ids_mock_method = get_user_role_ids(mocker)
        gof_storage_mock.get_gof_ids_having_read_permission_for_user. \
            return_value = expected_gof_ids

        interactor = UserRoleValidationInteractor()

        # Act
        result = interactor.get_gof_ids_having_read_permission_for_user(
            user_id=user_id, gof_ids=gof_ids, gof_storage=gof_storage_mock)

        # Assert
        assert result == expected_gof_ids
        get_user_role_ids_mock_method.assert_called_once_with(user_id=user_id)

    def test_get_gof_ids_having_write_permission_for_user(
            self, mocker, gof_storage_mock):
        # Arrange
        user_id = "user_1"
        gof_ids = ["gof_1", "gof_2", "gof_3"]
        expected_gof_ids = ["gof_1", "gof_2"]
        get_user_role_ids_mock_method = get_user_role_ids(mocker)
        gof_storage_mock.get_gof_ids_having_write_permission_for_user. \
            return_value = expected_gof_ids

        interactor = UserRoleValidationInteractor()

        # Act
        result = interactor.get_gof_ids_having_write_permission_for_user(
            user_id=user_id, gof_ids=gof_ids, gof_storage=gof_storage_mock)

        # Assert
        assert result == expected_gof_ids
        get_user_role_ids_mock_method.assert_called_once_with(user_id=user_id)

    def test_get_field_ids_having_read_permission_for_user(
            self, mocker, field_storage_mock):
        # Arrange
        user_id = "user_1"
        field_ids = ["field_1", "field_2", "field_3"]
        expected_field_ids = ["field_1", "field_2"]
        get_user_role_ids_mock_method = get_user_role_ids(mocker)
        field_storage_mock.get_field_ids_having_read_permission_for_user. \
            return_value = expected_field_ids

        interactor = UserRoleValidationInteractor()

        # Act
        result = interactor.get_field_ids_having_read_permission_for_user(
            user_id=user_id, field_ids=field_ids,
            field_storage=field_storage_mock)

        # Assert
        assert result == expected_field_ids
        get_user_role_ids_mock_method.assert_called_once_with(user_id=user_id)

    def test_get_field_ids_having_write_permission_for_user(
            self, mocker, field_storage_mock):
        # Arrange
        user_id = "user_1"
        field_ids = ["field_1", "field_2", "field_3"]
        expected_field_ids = ["field_1", "field_2"]
        get_user_role_ids_mock_method = get_user_role_ids(mocker)
        field_storage_mock.get_field_ids_having_write_permission_for_user. \
            return_value = expected_field_ids

        interactor = UserRoleValidationInteractor()

        # Act
        result = interactor.get_field_ids_having_write_permission_for_user(
            user_id=user_id, field_ids=field_ids,
            field_storage=field_storage_mock)

        # Assert
        assert result == expected_field_ids
        get_user_role_ids_mock_method.assert_called_once_with(user_id=user_id)

    def test_check_is_user_has_read_permission_for_field_when_user_does_not_have_returns_false(
            self, mocker, field_storage_mock):
        # Arrange
        user_id = "user_1"
        field_id = "field_1"
        get_user_role_ids_mock_method = get_user_role_ids(mocker)
        field_storage_mock.check_is_user_has_read_permission_for_field. \
            return_value = False

        interactor = UserRoleValidationInteractor()

        # Act
        result = interactor.check_is_user_has_read_permission_for_field(
            user_id=user_id, field_id=field_id,
            field_storage=field_storage_mock)

        # Assert
        assert result is False
        get_user_role_ids_mock_method.assert_called_once_with(user_id=user_id)

    def test_check_is_user_has_read_permission_for_field_when_user_have_permission_returns_true(
            self, mocker, field_storage_mock):
        # Arrange
        user_id = "user_1"
        field_id = "field_1"
        get_user_role_ids_mock_method = get_user_role_ids(mocker)
        field_storage_mock.check_is_user_has_read_permission_for_field. \
            return_value = True

        interactor = UserRoleValidationInteractor()

        # Act
        result = interactor.check_is_user_has_read_permission_for_field(
            user_id=user_id, field_id=field_id,
            field_storage=field_storage_mock)

        # Assert
        assert result is True
        get_user_role_ids_mock_method.assert_called_once_with(user_id=user_id)

    def test_check_is_user_has_write_permission_for_field_when_user_does_not_have_returns_false(
            self, mocker, field_storage_mock):
        # Arrange
        user_id = "user_1"
        field_id = "field_1"
        get_user_role_ids_mock_method = get_user_role_ids(mocker)
        field_storage_mock.check_is_user_has_write_permission_for_field. \
            return_value = False

        interactor = UserRoleValidationInteractor()

        # Act
        result = interactor.check_is_user_has_write_permission_for_field(
            user_id=user_id, field_id=field_id,
            field_storage=field_storage_mock)

        # Assert
        assert result is False
        get_user_role_ids_mock_method.assert_called_once_with(user_id=user_id)

    def test_check_is_user_has_write_permission_for_field_when_user_have_permission_returns_true(
            self, mocker, field_storage_mock):
        # Arrange
        user_id = "user_1"
        field_id = "field_1"
        get_user_role_ids_mock_method = get_user_role_ids(mocker)
        field_storage_mock.check_is_user_has_write_permission_for_field. \
            return_value = True

        interactor = UserRoleValidationInteractor()

        # Act
        result = interactor.check_is_user_has_write_permission_for_field(
            user_id=user_id, field_id=field_id,
            field_storage=field_storage_mock)

        # Assert
        assert result is True
        get_user_role_ids_mock_method.assert_called_once_with(user_id=user_id)
