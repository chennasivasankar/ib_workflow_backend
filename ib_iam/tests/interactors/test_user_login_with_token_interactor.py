from unittest import mock

import pytest


class TestLoginWithTokenInteractor:

    @pytest.fixture()
    def user_storage_mock(self):
        from unittest.mock import create_autospec

        from ib_iam.interactors.storage_interfaces.user_storage_interface import \
            UserStorageInterface
        storage = create_autospec(UserStorageInterface)
        return storage

    @pytest.fixture()
    def team_storage_mock(self):
        from unittest.mock import create_autospec

        from ib_iam.interactors.storage_interfaces \
            .team_storage_interface import TeamStorageInterface
        storage = create_autospec(TeamStorageInterface)
        return storage

    @pytest.fixture()
    def project_storage_mock(self):
        from unittest.mock import create_autospec

        from ib_iam.interactors.storage_interfaces \
            .project_storage_interface import ProjectStorageInterface
        storage = create_autospec(ProjectStorageInterface)
        return storage

    @pytest.fixture()
    def elastic_storage_mock(self):
        from unittest.mock import create_autospec

        from ib_adhoc_tasks.interactors.storage_interfaces \
            .elastic_storage_interface import ElasticStorageInterface
        storage = create_autospec(ElasticStorageInterface)
        return storage

    @pytest.fixture()
    def team_member_level_storage_mock(self):
        from unittest.mock import create_autospec

        from ib_iam.interactors.storage_interfaces.team_member_level_storage_interface import \
            TeamMemberLevelStorageInterface
        storage = create_autospec(TeamMemberLevelStorageInterface)
        return storage

    @pytest.fixture()
    def presenter_mock(self):
        from unittest.mock import create_autospec

        from ib_iam.interactors.presenter_interfaces.auth_presenter_interface import \
            LoginWithUserTokePresenterInterface
        presenter = create_autospec(LoginWithUserTokePresenterInterface)
        return presenter

    @pytest.fixture
    def interactor_mock(
            self, user_storage_mock, team_storage_mock, project_storage_mock,
            elastic_storage_mock, team_member_level_storage_mock
    ):
        from ib_iam.interactors.auth.user_login_with_token_interactor import \
            LoginWithTokenInteractor
        return LoginWithTokenInteractor(
            team_storage=team_storage_mock,
            user_storage=user_storage_mock,
            project_storage=project_storage_mock,
            elastic_storage=elastic_storage_mock,
            team_member_level_storage=team_member_level_storage_mock
        )

    def test_given_valid_token_returns_success_response(
            self, interactor_mock, user_storage_mock, presenter_mock, mocker
    ):
        # Arrange
        from django.conf import settings
        from ib_iam.tests.common_fixtures.adapters \
            .auth_service_adapter_mocks import create_auth_tokens_for_user_mock
        from ib_iam.tests.factories.adapter_dtos import UserTokensDTOFactory
        token = "user_token"
        name = "username"
        auth_token_user_id = "auth_token_user_id"
        is_admin = False
        user_id = "user_id_1"
        from ib_iam.interactors.dtos.dtos import LoginWithTokenParameterDTO
        login_with_token_parameter_dto = LoginWithTokenParameterDTO(
            token=token, auth_token_user_id=auth_token_user_id, name=name
        )
        expiry_in_seconds = settings.USER_VERIFICATION_EMAIL_EXPIRY_IN_SECONDS
        user_tokens_dto = UserTokensDTOFactory(user_id=user_id)
        user_storage_mock.get_user_id_for_given_token.return_value = user_id
        create_auth_tokens_for_user_mock = create_auth_tokens_for_user_mock(
            mocker=mocker
        )
        create_auth_tokens_for_user_mock.return_value = user_tokens_dto
        mock_object = mock.Mock
        presenter_mock.prepare_response_for_user_tokens_dto_and_is_admin \
            .return_value = mock_object

        # Act
        response = interactor_mock.login_with_token_wrapper(
            presenter=presenter_mock,
            login_with_token_parameter_dto=login_with_token_parameter_dto
        )

        # Assert
        assert response == mock_object
        user_storage_mock.get_user_id_for_given_token.assert_called_once_with(
            token=token
        )
        create_auth_tokens_for_user_mock.assert_called_once_with(
            user_id=user_id, expiry_in_seconds=expiry_in_seconds
        )
        presenter_mock.prepare_response_for_user_tokens_dto_and_is_admin \
            .assert_called_once_with(
            tokens_dto=user_tokens_dto, is_admin=is_admin
        )
        # TODO improve the test
