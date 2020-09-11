from unittest.mock import Mock

import pytest


class TestAddMembersToLevelsInteractor:

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
        from ib_iam.interactors.presenter_interfaces.level_presenter_interface import \
            AddMembersToTeamMemberLevelsPresenterInterface
        presenter = create_autospec(AddMembersToTeamMemberLevelsPresenterInterface)
        return presenter

    @pytest.fixture()
    def interactor(self, team_member_level_storage_mock, user_storage_mock):
        from ib_iam.interactors.add_members_to_team_member_levels_interactor import \
            AddMembersToTeamMemberLevelsInteractor
        interactor = AddMembersToTeamMemberLevelsInteractor(
            team_member_level_storage=team_member_level_storage_mock,
            user_storage=user_storage_mock
        )
        return interactor

    @pytest.fixture()
    def prepare_level_id_with_member_ids_dtos(self):
        level_id_with_member_ids_list = [{
            'level_id': 'b52d31f3-7359-4a5a-b81d-579acd460942',
            'member_ids': ['2b8f68ed-82cb-47ea-bf92-5a970d0c1109',
                           'e5fd217b-a1c6-4b43-aea0-6e9cf17117a4',
                           '221f0318-7231-428a-9bd5-1e68c2b41672']
        }, {
            'level_id': '5aba9060-0714-4857-bd78-8689ec585b10',
            'member_ids': ['bc96292f-0e09-46ec-b90f-bf28c09e9365',
                           '86de39e4-e85d-4650-b78e-65f9bdc69719']
        }, {
            'level_id': '4fb31acf-c73e-43db-b561-60ee38597608',
            'member_ids': ['4b5fd9ba-64a2-4ee2-8868-5e1d00bd83c8',
                           'a7178219-7559-45c4-8c90-d25807820f20',
                           'd17f65b0-9c9a-4a0a-8280-bfc278ff3c13',
                           '216cc13f-5446-493b-a2f7-90aaaeecaef1' ]
        }]

        from ib_iam.tests.factories.interactor_dtos import \
            TeamMemberLevelIdWithMemberIdsDTOFactory
        level_id_with_member_ids_dtos = [
            TeamMemberLevelIdWithMemberIdsDTOFactory(
                team_member_level_id=level_id_with_member_ids_dict["level_id"],
                member_ids=level_id_with_member_ids_dict["member_ids"]
            )
            for level_id_with_member_ids_dict in level_id_with_member_ids_list
        ]
        return level_id_with_member_ids_dtos

    def test_with_user_not_admin_return_response(
            self, team_member_level_storage_mock, presenter_mock, interactor,
            prepare_level_id_with_member_ids_dtos, user_storage_mock
    ):
        # Arrange
        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        team_member_level_id_with_member_ids_dtos = \
            prepare_level_id_with_member_ids_dtos
        expected_presenter_response_for_invalid_project_id_mock = Mock()
        user_id = "00be920b-7b4c-49e7-8adb-41a0c18da848"

        user_storage_mock.is_user_admin.return_value = False

        presenter_mock.response_for_user_is_not_admin.return_value \
            = expected_presenter_response_for_invalid_project_id_mock

        # Act
        response = interactor.add_members_to_team_member_levels_wrapper(
            team_member_level_id_with_member_ids_dtos=team_member_level_id_with_member_ids_dtos,
            presenter=presenter_mock, team_id=team_id, user_id=user_id
        )

        # Assert
        assert response == \
               expected_presenter_response_for_invalid_project_id_mock
        user_storage_mock.is_user_admin.assert_called_with(user_id=user_id)
        presenter_mock.response_for_user_is_not_admin.assert_called_once()

    def test_with_invalid_team_id_return_response(
            self, team_member_level_storage_mock, presenter_mock, interactor,
            prepare_level_id_with_member_ids_dtos, user_storage_mock
    ):
        # Arrange
        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        team_member_level_id_with_member_ids_dtos = \
            prepare_level_id_with_member_ids_dtos
        expected_presenter_response_for_invalid_team_id_mock = Mock()
        user_id = "00be920b-7b4c-49e7-8adb-41a0c18da848"

        from ib_iam.exceptions.custom_exceptions import InvalidTeamId
        team_member_level_storage_mock.validate_team_id.side_effect = InvalidTeamId
        user_storage_mock.is_user_admin.return_value = True

        presenter_mock.response_for_invalid_team_id.return_value \
            = expected_presenter_response_for_invalid_team_id_mock

        # Act
        response = interactor.add_members_to_team_member_levels_wrapper(
            team_member_level_id_with_member_ids_dtos=team_member_level_id_with_member_ids_dtos,
            presenter=presenter_mock, team_id=team_id, user_id=user_id
        )

        # Assert
        assert response == \
               expected_presenter_response_for_invalid_team_id_mock
        team_member_level_storage_mock.validate_team_id.assert_called_with(team_id=team_id)
        presenter_mock.response_for_invalid_team_id.assert_called_once()

    def test_invalid_team_member_level_ids_return_response(
            self, team_member_level_storage_mock, presenter_mock, interactor,
            prepare_level_id_with_member_ids_dtos, user_storage_mock
    ):
        # Arrange
        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        team_member_level_id_with_member_ids_dtos = \
            prepare_level_id_with_member_ids_dtos
        expected_presenter_response_for_team_member_level_ids_not_found_mock = \
            Mock()
        team_member_level_ids_in_database = [
            "b52d31f3-7359-4a5a-b81d-579acd460942"
        ]
        expected_team_member_level_ids_not_found = [
            '5aba9060-0714-4857-bd78-8689ec585b10',
            '4fb31acf-c73e-43db-b561-60ee38597608'
        ]
        user_id = "00be920b-7b4c-49e7-8adb-41a0c18da848"

        presenter_mock.response_for_team_member_level_ids_not_found. \
            return_value = expected_presenter_response_for_team_member_level_ids_not_found_mock

        team_member_level_storage_mock.get_team_member_level_ids.return_value = \
            team_member_level_ids_in_database
        user_storage_mock.is_user_admin.return_value = True

        # Act
        response = interactor.add_members_to_team_member_levels_wrapper(
            team_member_level_id_with_member_ids_dtos=team_member_level_id_with_member_ids_dtos,
            presenter=presenter_mock, team_id=team_id, user_id=user_id
        )

        # Assert
        assert response == \
               expected_presenter_response_for_team_member_level_ids_not_found_mock

        call_args = \
            presenter_mock.response_for_team_member_level_ids_not_found.call_args
        error_object = call_args[0][0]

        assert error_object.team_member_level_ids == \
               expected_team_member_level_ids_not_found
        presenter_mock.response_for_team_member_level_ids_not_found.\
            assert_called_once()
        team_member_level_storage_mock.get_team_member_level_ids.assert_called_once_with(
            team_id=team_id
        )

    def test_with_team_member_ids_not_found_return_response(
            self, team_member_level_storage_mock, presenter_mock, interactor,
            prepare_level_id_with_member_ids_dtos, user_storage_mock
    ):
        # Arrange
        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        team_member_level_id_with_member_ids_dtos = \
            prepare_level_id_with_member_ids_dtos
        team_member_level_ids_in_database = [
            "b52d31f3-7359-4a5a-b81d-579acd460942",
            '5aba9060-0714-4857-bd78-8689ec585b10',
            '4fb31acf-c73e-43db-b561-60ee38597608'
        ]
        team_member_ids_in_database = [
            '2b8f68ed-82cb-47ea-bf92-5a970d0c1109',
            'e5fd217b-a1c6-4b43-aea0-6e9cf17117a4',
            '221f0318-7231-428a-9bd5-1e68c2b41672',
            'bc96292f-0e09-46ec-b90f-bf28c09e9365',
            '86de39e4-e85d-4650-b78e-65f9bdc69719'
        ]
        team_member_ids_not_found = [
            '4b5fd9ba-64a2-4ee2-8868-5e1d00bd83c8',
            'a7178219-7559-45c4-8c90-d25807820f20',
            'd17f65b0-9c9a-4a0a-8280-bfc278ff3c13',
            '216cc13f-5446-493b-a2f7-90aaaeecaef1'
        ]
        user_id = "00be920b-7b4c-49e7-8adb-41a0c18da848"

        expected_presenter_response_for_team_member_ids_not_found_mock = Mock()

        team_member_level_storage_mock.get_team_member_level_ids.return_value = \
            team_member_level_ids_in_database
        team_member_level_storage_mock.get_team_member_ids.return_value = \
            team_member_ids_in_database
        user_storage_mock.is_user_admin.return_value = True

        presenter_mock.response_for_team_member_ids_not_found.return_value = \
            expected_presenter_response_for_team_member_ids_not_found_mock

        # Act
        response = interactor.add_members_to_team_member_levels_wrapper(
            team_member_level_id_with_member_ids_dtos=team_member_level_id_with_member_ids_dtos,
            presenter=presenter_mock, team_id=team_id, user_id=user_id
        )

        # Assert
        assert response == \
            expected_presenter_response_for_team_member_ids_not_found_mock

        call_args = presenter_mock.response_for_team_member_ids_not_found.call_args
        error_object = call_args[0][0]

        assert error_object.team_member_ids == team_member_ids_not_found
        presenter_mock.response_for_team_member_ids_not_found.\
            assert_called_once()
        team_member_level_storage_mock.get_team_member_ids.assert_called_with(team_id=team_id)

    def test_with_valid_details_return_response(
            self, team_member_level_storage_mock, presenter_mock, interactor,
            prepare_level_id_with_member_ids_dtos, user_storage_mock
    ):
        # Arrange
        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        team_member_level_id_with_member_ids_dtos = \
            prepare_level_id_with_member_ids_dtos
        team_member_level_ids_in_database = [
            "b52d31f3-7359-4a5a-b81d-579acd460942",
            '5aba9060-0714-4857-bd78-8689ec585b10',
            '4fb31acf-c73e-43db-b561-60ee38597608'
        ]
        team_member_ids_in_database = [
            '2b8f68ed-82cb-47ea-bf92-5a970d0c1109',
            'e5fd217b-a1c6-4b43-aea0-6e9cf17117a4',
            '221f0318-7231-428a-9bd5-1e68c2b41672',
            'bc96292f-0e09-46ec-b90f-bf28c09e9365',
            '86de39e4-e85d-4650-b78e-65f9bdc69719',
            '4b5fd9ba-64a2-4ee2-8868-5e1d00bd83c8',
            'a7178219-7559-45c4-8c90-d25807820f20',
            'd17f65b0-9c9a-4a0a-8280-bfc278ff3c13',
            '216cc13f-5446-493b-a2f7-90aaaeecaef1'
        ]
        user_id = "00be920b-7b4c-49e7-8adb-41a0c18da848"

        expected_presenter_prepare_success_response_for_add_members_to_levels = \
            Mock()

        team_member_level_storage_mock.get_team_member_level_ids.return_value = \
            team_member_level_ids_in_database
        team_member_level_storage_mock.get_team_member_ids.return_value = \
            team_member_ids_in_database
        user_storage_mock.is_user_admin.return_value = True

        presenter_mock.prepare_success_response_for_add_members_to_team_member_levels. \
            return_value = expected_presenter_prepare_success_response_for_add_members_to_levels

        # Act
        response = interactor.add_members_to_team_member_levels_wrapper(
            team_member_level_id_with_member_ids_dtos=team_member_level_id_with_member_ids_dtos,
            presenter=presenter_mock, team_id=team_id, user_id=user_id
        )

        # Assert
        assert response == \
               expected_presenter_prepare_success_response_for_add_members_to_levels

        presenter_mock.prepare_success_response_for_add_members_to_team_member_levels. \
            assert_called_once()
