from unittest.mock import Mock

import pytest


class TestGetTeamMembersOfLevelHierarchyInteractor:

    @pytest.fixture()
    def team_member_level_storage_mock(self):
        from unittest.mock import create_autospec

        from ib_iam.interactors.storage_interfaces.team_member_level_storage_interface import \
            TeamMemberLevelStorageInterface
        storage = create_autospec(TeamMemberLevelStorageInterface)
        return storage

    @pytest.fixture()
    def user_storage_mock(self):
        from unittest.mock import create_autospec
        from ib_iam.interactors.storage_interfaces.user_storage_interface import \
            UserStorageInterface
        storage = create_autospec(UserStorageInterface)
        return storage

    @pytest.fixture()
    def presenter_mock(self):
        from unittest.mock import create_autospec

        from ib_iam.interactors.presenter_interfaces.level_presenter_interface \
            import GetTeamMembersOfLevelHierarchyPresenterInterface
        presenter = create_autospec(
            GetTeamMembersOfLevelHierarchyPresenterInterface)
        return presenter

    @pytest.fixture()
    def interactor(self, team_member_level_storage_mock, user_storage_mock):
        from ib_iam.interactors.get_team_members_of_level_hierarchy_interactor import \
            GetTeamMembersOfLevelHierarchyInteractor
        interactor = GetTeamMembersOfLevelHierarchyInteractor(
            team_member_level_storage=team_member_level_storage_mock,
            user_storage=user_storage_mock
        )
        return interactor

    def test_with_user_not_admin_return_response(
            self, team_member_level_storage_mock, presenter_mock, interactor,
            user_storage_mock
    ):
        # Arrange
        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        level_hierarchy = 0
        expected_presenter_response_for_user_is_not_admin_mock = Mock()
        user_id = "00be920b-7b4c-49e7-8adb-41a0c18da848"

        user_storage_mock.is_user_admin.return_value = False

        presenter_mock.response_for_user_is_not_admin.return_value \
            = expected_presenter_response_for_user_is_not_admin_mock

        # Act
        response = interactor.get_team_members_of_level_hierarchy_wrapper(
            team_id=team_id, level_hierarchy=level_hierarchy,
            presenter=presenter_mock, user_id=user_id
        )

        # Assert
        assert response == \
               expected_presenter_response_for_user_is_not_admin_mock
        user_storage_mock.is_user_admin.assert_called_with(user_id=user_id)
        presenter_mock.response_for_user_is_not_admin.assert_called_once()

    def test_with_invalid_team_id_return_response(
            self, team_member_level_storage_mock, presenter_mock, interactor,
            user_storage_mock
    ):
        # Arrange
        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        level_hierarchy = 0
        expected_presenter_response_for_invalid_team_id_mock = Mock()
        user_id = "00be920b-7b4c-49e7-8adb-41a0c18da848"

        from ib_iam.exceptions.custom_exceptions import InvalidTeamId
        team_member_level_storage_mock.validate_team_id.side_effect = \
            InvalidTeamId
        user_storage_mock.is_user_admin.return_value = True

        presenter_mock.response_for_invalid_team_id.return_value \
            = expected_presenter_response_for_invalid_team_id_mock

        # Act
        response = interactor.get_team_members_of_level_hierarchy_wrapper(
            team_id=team_id, level_hierarchy=level_hierarchy,
            presenter=presenter_mock, user_id=user_id
        )

        # Assert
        assert response == \
               expected_presenter_response_for_invalid_team_id_mock
        team_member_level_storage_mock.validate_team_id.assert_called_with(
            team_id=team_id)
        presenter_mock.response_for_invalid_team_id.assert_called_once()

    def test_with_invalid_level_hierarchy_return_response(
            self, team_member_level_storage_mock, presenter_mock, interactor,
            user_storage_mock
    ):
        # Arrange
        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        level_hierarchy = -1
        expected_presenter_response_for_invalid_level_hierarchy_of_team_mock = \
            Mock()
        user_id = "00be920b-7b4c-49e7-8adb-41a0c18da848"

        from ib_iam.exceptions.custom_exceptions import \
            InvalidLevelHierarchyOfTeam
        team_member_level_storage_mock.validate_level_hierarchy_of_team.side_effect = \
            InvalidLevelHierarchyOfTeam
        user_storage_mock.is_user_admin.return_value = True

        presenter_mock.response_for_invalid_level_hierarchy_of_team.return_value \
            = expected_presenter_response_for_invalid_level_hierarchy_of_team_mock

        # Act
        response = interactor.get_team_members_of_level_hierarchy_wrapper(
            team_id=team_id, level_hierarchy=level_hierarchy,
            presenter=presenter_mock, user_id=user_id
        )

        # Assert
        assert response == \
               expected_presenter_response_for_invalid_level_hierarchy_of_team_mock
        team_member_level_storage_mock.validate_level_hierarchy_of_team.assert_called_with(
            team_id=team_id, level_hierarchy=level_hierarchy
        )
        presenter_mock.response_for_invalid_level_hierarchy_of_team. \
            assert_called_once()

    def test_with_valid_details_return_response(
            self, team_member_level_storage_mock, presenter_mock, interactor,
            user_storage_mock
    ):
        # Arrange
        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        level_hierarchy = 0
        user_id = "00be920b-7b4c-49e7-8adb-41a0c18da848"

        expected_presenter_prepare_success_response_for_get_team_members_of_level_hierarchy = Mock()
        user_storage_mock.is_user_admin.return_value = True

        presenter_mock.prepare_success_response_for_get_team_members_of_level_hierarchy. \
            return_value = expected_presenter_prepare_success_response_for_get_team_members_of_level_hierarchy

        # Act
        response = interactor.get_team_members_of_level_hierarchy_wrapper(
            team_id=team_id, level_hierarchy=level_hierarchy,
            presenter=presenter_mock, user_id=user_id
        )

        # Assert
        assert response == expected_presenter_prepare_success_response_for_get_team_members_of_level_hierarchy

        presenter_mock.prepare_success_response_for_get_team_members_of_level_hierarchy. \
            assert_called_once()
        team_member_level_storage_mock.get_member_details.assert_called_once_with(
            team_id=team_id, level_hierarchy=level_hierarchy
        )


class TestGetImmediateSuperiorUserId:

    @pytest.fixture()
    def team_member_level_storage_mock(self):
        from unittest.mock import create_autospec

        from ib_iam.interactors.storage_interfaces.team_member_level_storage_interface import \
            TeamMemberLevelStorageInterface
        storage = create_autospec(TeamMemberLevelStorageInterface)
        return storage

    @pytest.fixture()
    def user_storage_mock(self):
        from unittest.mock import create_autospec
        from ib_iam.interactors.storage_interfaces.user_storage_interface import \
            UserStorageInterface
        storage = create_autospec(UserStorageInterface)
        return storage

    @pytest.fixture()
    def interactor(self, team_member_level_storage_mock, user_storage_mock):
        from ib_iam.interactors.get_team_members_of_level_hierarchy_interactor import \
            GetTeamMembersOfLevelHierarchyInteractor
        interactor = GetTeamMembersOfLevelHierarchyInteractor(
            team_member_level_storage=team_member_level_storage_mock,
            user_storage=user_storage_mock
        )
        return interactor

    def test_with_invalid_team_id_raise_exception(
            self, team_member_level_storage_mock, interactor):
        # Arrange
        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        user_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"

        from ib_iam.exceptions.custom_exceptions import InvalidTeamId
        team_member_level_storage_mock.validate_team_id.side_effect = InvalidTeamId

        # Assert
        with pytest.raises(InvalidTeamId):
            interactor.get_immediate_superior_user_id(
                team_id=team_id, user_id=user_id
            )

        team_member_level_storage_mock.validate_team_id.assert_called_with(team_id=team_id)

    def test_with_user_not_belong_to_team_raise_exception(
            self, team_member_level_storage_mock, interactor
    ):
        # Arrange
        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        user_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"

        from ib_iam.exceptions.custom_exceptions import UserNotBelongToTeam
        team_member_level_storage_mock.validate_user_in_a_team.side_effect = UserNotBelongToTeam

        # Assert
        with pytest.raises(UserNotBelongToTeam):
            interactor.get_immediate_superior_user_id(
                team_id=team_id, user_id=user_id
            )

        team_member_level_storage_mock.validate_user_in_a_team.assert_called_with(
            team_id=team_id, user_id=user_id
        )

    def test_with_valid_details_return_response(self, team_member_level_storage_mock, interactor):
        # Arrange
        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        user_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        immediate_superior_user_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"

        team_member_level_storage_mock.get_immediate_superior_user_id.return_value = \
            immediate_superior_user_id

        # Act
        response = interactor.get_immediate_superior_user_id(
            team_id=team_id, user_id=user_id
        )

        # Assert
        assert response == immediate_superior_user_id

        team_member_level_storage_mock.get_immediate_superior_user_id.assert_called_with(
            team_id=team_id, user_id=user_id
        )
