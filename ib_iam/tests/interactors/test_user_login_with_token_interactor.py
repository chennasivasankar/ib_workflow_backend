from unittest import mock
from unittest.mock import create_autospec

import pytest

from ib_iam.adapters.dtos import UserProfileDTO
from ib_iam.constants.config import DEFAULT_TEAM_ID, DEFAULT_TEAM_NAME, \
    LEVEL_0_HIERARCHY, LEVEL_0_NAME, DEFAULT_PASSWORD
from ib_iam.interactors.dtos.dtos import TeamMemberLevelIdWithMemberIdsDTO
from ib_iam.tests.factories.adapter_dtos import UserTokensDTOFactory
from ib_workflows_backend.settings.base_swagger_utils import \
    JGC_DRIVE_PROJECT_ID



class TestLoginWithTokenInteractor:

    @pytest.fixture()
    def user_storage_mock(self):
        from ib_iam.interactors.storage_interfaces.user_storage_interface import \
            UserStorageInterface
        return create_autospec(UserStorageInterface)

    @pytest.fixture()
    def team_storage_mock(self):
        from ib_iam.interactors.storage_interfaces \
            .team_storage_interface import TeamStorageInterface
        return create_autospec(TeamStorageInterface)

    @pytest.fixture()
    def project_storage_mock(self):
        from ib_iam.interactors.storage_interfaces \
            .project_storage_interface import ProjectStorageInterface
        return create_autospec(ProjectStorageInterface)

    @pytest.fixture()
    def elastic_storage_mock(self):
        from ib_iam.interactors.storage_interfaces.elastic_storage_interface import \
            ElasticSearchStorageInterface
        return create_autospec(ElasticSearchStorageInterface)

    @pytest.fixture()
    def team_member_level_storage_mock(self):
        from ib_iam.interactors.storage_interfaces.team_member_level_storage_interface import \
            TeamMemberLevelStorageInterface
        return create_autospec(TeamMemberLevelStorageInterface)

    @pytest.fixture()
    def presenter_mock(self):
        from ib_iam.interactors.presenter_interfaces.auth_presenter_interface import \
            LoginWithUserTokePresenterInterface
        return create_autospec(LoginWithUserTokePresenterInterface)

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

    def test_given_existing_token_returns_success_response(
            self, interactor_mock, user_storage_mock, presenter_mock, mocker
    ):
        # Arrange
        from django.conf import settings
        from ib_iam.tests.factories.adapter_dtos import UserTokensDTOFactory
        from ib_iam.tests.factories.interactor_dtos import \
            LoginWithTokenParameterDTOFactory
        from ib_iam.tests.common_fixtures.adapters.auth_service_adapter_mocks \
            import create_auth_tokens_for_user_mock
        token = "user_token"
        is_admin = False
        user_id = "user_id_1"
        expiry_in_seconds = settings.USER_VERIFICATION_EMAIL_EXPIRY_IN_SECONDS
        login_with_token_parameter_dto = LoginWithTokenParameterDTOFactory(
            token=token
        )
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

    def test_given_new_token_creates_user_and_returns_success_response(
            self, interactor_mock, user_storage_mock, elastic_storage_mock,
            team_storage_mock, team_member_level_storage_mock,
            project_storage_mock, presenter_mock, mocker
    ):
        # Arrange
        from ib_iam.tests.common_fixtures.adapters.auth_service_adapter_mocks \
            import create_auth_tokens_for_user_mock, create_user_profile_mock,\
            create_user_account_with_email_mock
        from django.conf import settings
        from ib_iam.tests.factories.interactor_dtos import \
            LoginWithTokenParameterDTOFactory
        token = "user_token"
        email = "user_token@gmail.com"
        name = "username"
        is_admin = False
        auth_token_user_id = "auth_token_user_id_1"
        user_id = "user_id_1"
        elastic_user_id = "elastic_user_id_1"
        team_member_level_0_id = "team_member_level_0_id_1"
        role_ids = ["ROLE_1", "ROLE_2"]
        login_with_token_parameter_dto = LoginWithTokenParameterDTOFactory(
            token=token, auth_token_user_id=auth_token_user_id, name=name
        )
        user_profile_dto = UserProfileDTO(
            user_id=user_id, email=email, name=name
        )
        team_member_level_id_with_member_ids_dtos = [
            TeamMemberLevelIdWithMemberIdsDTO(
                team_member_level_id=team_member_level_0_id,
                member_ids=[user_id]
            )
        ]
        expiry_in_seconds = settings.USER_VERIFICATION_EMAIL_EXPIRY_IN_SECONDS
        user_tokens_dto = UserTokensDTOFactory(user_id=user_id)
        user_storage_mock.get_user_id_for_given_token.return_value = None
        create_user_account_with_email_mock = create_user_account_with_email_mock(
            mocker)
        create_user_account_with_email_mock.return_value = user_id
        create_user_profile_mock = create_user_profile_mock(mocker)
        elastic_storage_mock.create_elastic_user.return_value = elastic_user_id
        team_storage_mock.get_or_create_team_with_id_and_name.return_value = False
        team_member_level_storage_mock.get_or_create_team_member_level_hierarchy \
            .return_value = team_member_level_0_id
        project_storage_mock.get_project_role_ids.return_value = role_ids
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
        create_user_account_with_email_mock.assert_called_once_with(
            email=email, password=DEFAULT_PASSWORD
        )
        create_user_profile_mock.assert_called_once_with(
            user_id=user_id, user_profile_dto=user_profile_dto
        )
        user_storage_mock.create_user.assert_called_once_with(
            user_id=user_id, is_admin=False, name=name
        )
        user_storage_mock.create_auth_user.assert_called_once_with(
            user_id=user_id, token=token,
            auth_token_user_id=auth_token_user_id
        )
        elastic_storage_mock.create_elastic_user.assert_called_once_with(
            user_id=user_id, name=name, email=email
        )
        elastic_storage_mock.create_elastic_user_intermediary \
            .assert_called_once_with(elastic_user_id=elastic_user_id,
                                     user_id=user_id)
        team_storage_mock.get_or_create_team_with_id_and_name \
            .assert_called_once_with(team_id=DEFAULT_TEAM_ID,
                                     name=DEFAULT_TEAM_NAME)
        team_storage_mock.add_users_to_team.assert_called_once_with(
            team_id=DEFAULT_TEAM_ID, user_ids=[user_id]
        )
        team_member_level_storage_mock \
            .get_or_create_team_member_level_hierarchy.assert_called_once_with(
            team_id=DEFAULT_TEAM_ID, level_hierarchy=LEVEL_0_HIERARCHY,
            level_name=LEVEL_0_NAME
        )
        team_member_level_storage_mock.add_members_to_levels_for_a_team \
            .assert_called_once_with(team_member_level_id_with_member_ids_dtos=
                                     team_member_level_id_with_member_ids_dtos)
        project_storage_mock.get_project_role_ids.assert_called_once_with(
            project_id=JGC_DRIVE_PROJECT_ID
        )
        user_storage_mock.add_roles_to_the_user.assert_called_once_with(
            user_id=user_id, role_ids=role_ids
        )
        create_auth_tokens_for_user_mock.assert_called_once_with(
            user_id=user_id, expiry_in_seconds=expiry_in_seconds
        )
        presenter_mock.prepare_response_for_user_tokens_dto_and_is_admin \
            .assert_called_once_with(
            tokens_dto=user_tokens_dto, is_admin=is_admin
        )

    def test_given_token_team_not_added_adds_and_assign_team_to_project(
            self, interactor_mock, user_storage_mock, elastic_storage_mock,
            team_storage_mock, team_member_level_storage_mock,
            project_storage_mock, presenter_mock, mocker
    ):
        # Arrange
        from ib_iam.tests.common_fixtures.adapters.auth_service_adapter_mocks \
            import create_auth_tokens_for_user_mock, create_user_profile_mock,\
            create_user_account_with_email_mock
        from ib_iam.tests.factories.interactor_dtos import \
            LoginWithTokenParameterDTOFactory
        token = "user_token"
        user_id = "user_id_1"
        elastic_user_id = "elastic_user_id_1"
        user_tokens_dto = UserTokensDTOFactory(user_id=user_id)
        login_with_token_parameter_dto = LoginWithTokenParameterDTOFactory(
            token=token
        )
        user_storage_mock.get_user_id_for_given_token.return_value = None
        create_user_account_with_email_mock = create_user_account_with_email_mock(
            mocker)
        create_user_account_with_email_mock.return_value = user_id
        create_user_profile_mock(mocker)
        elastic_storage_mock.create_elastic_user.return_value = elastic_user_id
        team_storage_mock.get_or_create_team_with_id_and_name.return_value = True
        create_auth_tokens_for_user_mock = create_auth_tokens_for_user_mock(
            mocker=mocker
        )
        create_auth_tokens_for_user_mock.return_value = user_tokens_dto

        # Act
        interactor_mock.login_with_token_wrapper(
            presenter=presenter_mock,
            login_with_token_parameter_dto=login_with_token_parameter_dto
        )

        # Assert
        user_storage_mock.get_user_id_for_given_token.assert_called_once_with(
            token=token
        )
        team_storage_mock.get_or_create_team_with_id_and_name \
            .assert_called_once_with(team_id=DEFAULT_TEAM_ID,
                                     name=DEFAULT_TEAM_NAME)
        project_storage_mock.assign_teams_to_projects.assert_called_once_with(
            project_id=JGC_DRIVE_PROJECT_ID, team_ids=[DEFAULT_TEAM_ID]
        )