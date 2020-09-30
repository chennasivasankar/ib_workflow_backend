import pytest


class TestAuthUsersInteractor:

    @pytest.fixture()
    def user_storage_mock(self):
        from unittest.mock import create_autospec
        from ib_iam.interactors.storage_interfaces.user_storage_interface import \
            UserStorageInterface
        storage = create_autospec(UserStorageInterface)
        return storage

    @pytest.fixture()
    def elastic_storage(self):
        from unittest import mock
        from ib_iam.interactors.storage_interfaces.elastic_storage_interface \
            import ElasticSearchStorageInterface
        storage = mock.create_autospec(ElasticSearchStorageInterface)
        return storage

    @pytest.fixture()
    def interactor(self, user_storage_mock, elastic_storage):
        from ib_iam.interactors.auth_users_interactor import AuthUsersInteractor
        interactor = AuthUsersInteractor(
            user_storage=user_storage_mock,
            elastic_storage=elastic_storage
        )
        return interactor

    def test_with_valid_details_create_data(
            self, interactor, user_storage_mock, elastic_storage, mocker
    ):
        # Arrange
        from ib_iam.tests.factories.interactor_dtos import AuthUserDTOFactory
        auth_user_dtos = AuthUserDTOFactory.create_batch(size=3)

        from ib_iam.tests.common_fixtures.adapters.auth_service_adapter_mocks import \
            create_user_account_with_email_mock, create_user_profile_mock
        create_user_account_with_email_mock = \
            create_user_account_with_email_mock(mocker)
        create_user_profile_mock = create_user_profile_mock(mocker)

        # Act
        interactor.auth_user_dtos(auth_user_dtos=auth_user_dtos)

        # Assert
        assert create_user_account_with_email_mock.call_count == 3
        assert create_user_profile_mock.call_count == 3
        assert user_storage_mock.create_user.call_count == 3
        assert user_storage_mock.create_auth_user.call_count == 3
        assert elastic_storage.create_elastic_user.call_count == 3
