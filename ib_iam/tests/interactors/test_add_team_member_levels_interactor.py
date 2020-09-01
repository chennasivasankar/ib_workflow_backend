from unittest.mock import Mock

import pytest


class TestAddTeamMemberLevelsInteractor:

    @pytest.fixture()
    def storage_mock(self):
        from unittest.mock import create_autospec
        from ib_iam.interactors.storage_interfaces.team_member_level_storage_interface import \
            TeamMemberLevelStorageInterface
        storage = create_autospec(TeamMemberLevelStorageInterface)
        return storage

    @pytest.fixture()
    def presenter_mock(self):
        from unittest.mock import create_autospec

        from ib_iam.interactors.presenter_interfaces.level_presenter_interface import \
            AddTeamMemberLevelsPresenterInterface
        presenter = create_autospec(AddTeamMemberLevelsPresenterInterface)
        return presenter

    @pytest.fixture()
    def interactor(self, storage_mock):
        from ib_iam.interactors.add_team_member_levels_interactor import \
            AddTeamMemberLevelsInteractor
        interactor = AddTeamMemberLevelsInteractor(
            team_member_level_storage=storage_mock)
        return interactor

    @pytest.fixture()
    def prepare_team_member_level_dtos(self):
        team_member_level_list = [
            {
                "level_name": "Developer",
                "level_hierarchy": 0
            },
            {
                "level_name": "Software Developer Lead",
                "level_hierarchy": 1
            },
            {
                "level_name": "Engineer Manager",
                "level_hierarchy": 2
            },
            {
                "level_name": "Product Owner",
                "level_hierarchy": 3
            }
        ]

        from ib_iam.tests.factories.interactor_dtos import \
            TeamMemberLevelDTOFactory
        team_member_level_dtos = [
            TeamMemberLevelDTOFactory(
                team_member_level_name=level_dict["level_name"],
                level_hierarchy=level_dict["level_hierarchy"]
            )
            for level_dict in team_member_level_list
        ]
        return team_member_level_dtos

    def test_with_invalid_team_id_return_response(
            self, storage_mock, presenter_mock, interactor,
            prepare_team_member_level_dtos
    ):
        # Arrange
        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        team_member_level_dtos = prepare_team_member_level_dtos
        expected_presenter_response_for_invalid_team_id_mock = Mock()

        from ib_iam.exceptions.custom_exceptions import InvalidTeamId
        storage_mock.validate_team_id.side_effect = InvalidTeamId

        presenter_mock.response_for_invalid_team_id.return_value \
            = expected_presenter_response_for_invalid_team_id_mock

        # Act
        response = interactor.add_team_member_levels_wrapper(
            team_id=team_id, team_member_level_dtos=team_member_level_dtos,
            presenter=presenter_mock
        )

        # Assert
        assert response == \
               expected_presenter_response_for_invalid_team_id_mock
        storage_mock.validate_team_id.assert_called_with(team_id=team_id)
        presenter_mock.response_for_invalid_team_id.assert_called_once()

    def test_with_duplicate_level_hierarchies_return_response(
            self, storage_mock, presenter_mock, interactor,
            prepare_team_member_level_dtos
    ):
        # Arrange
        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        team_member_level_dtos = prepare_team_member_level_dtos
        team_member_level_dtos[0].level_hierarchy = 2
        team_member_level_dtos[3].level_hierarchy = 1
        expected_duplicate_level_hierarchies = [1, 2]

        expected_presenter_response_for_duplicate_level_hierarchies_mock = Mock()

        presenter_mock.response_for_duplicate_level_hierarchies.return_value = \
            expected_presenter_response_for_duplicate_level_hierarchies_mock

        # Act
        response = interactor.add_team_member_levels_wrapper(
            team_id=team_id, team_member_level_dtos=team_member_level_dtos,
            presenter=presenter_mock
        )

        # Assert
        assert response == \
               expected_presenter_response_for_duplicate_level_hierarchies_mock

        presenter_mock.response_for_duplicate_level_hierarchies. \
            assert_called_once()
        call_args = \
            presenter_mock.response_for_duplicate_level_hierarchies.call_args
        error_object = call_args[0][0]
        duplicate_level_hierarchies = error_object.level_hierarchies
        assert sorted(duplicate_level_hierarchies) == \
               sorted(expected_duplicate_level_hierarchies)

    def test_with_negative_level_hierarchies_return_response(
            self, storage_mock, presenter_mock, interactor,
            prepare_team_member_level_dtos
    ):
        # Arrange
        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        team_member_level_dtos = prepare_team_member_level_dtos
        team_member_level_dtos[0].level_hierarchy = -2
        team_member_level_dtos[3].level_hierarchy = -1
        expected_negative_level_hierarchies = [-1, -2]

        expected_presenter_response_for_negative_level_hierarchies_mock = Mock()

        presenter_mock.response_for_negative_level_hierarchies.return_value = \
            expected_presenter_response_for_negative_level_hierarchies_mock

        # Act
        response = interactor.add_team_member_levels_wrapper(
            team_id=team_id, team_member_level_dtos=team_member_level_dtos,
            presenter=presenter_mock
        )

        # Assert
        assert response == \
               expected_presenter_response_for_negative_level_hierarchies_mock

        presenter_mock.response_for_negative_level_hierarchies. \
            assert_called_once()
        call_args = \
            presenter_mock.response_for_negative_level_hierarchies.call_args
        error_object = call_args[0][0]
        negative_level_hierarchies = error_object.level_hierarchies
        assert sorted(negative_level_hierarchies) == \
               sorted(expected_negative_level_hierarchies)

    def test_with_duplicate_team_member_level_names_return_response(
            self, storage_mock, presenter_mock, interactor,
            prepare_team_member_level_dtos
    ):
        # Arrange
        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        team_member_level_dtos = prepare_team_member_level_dtos
        team_member_level_dtos[1].team_member_level_name = "Developer"
        team_member_level_dtos[3].team_member_level_name = "Engineer Manager"
        expected_duplicate_team_member_level_names = [
            "Developer",
            "Engineer Manager"
        ]

        expected_presenter_response_for_duplicate_team_member_levels_mock = \
            Mock()

        presenter_mock.response_for_duplicate_team_member_levels.return_value = \
            expected_presenter_response_for_duplicate_team_member_levels_mock

        # Act
        response = interactor.add_team_member_levels_wrapper(
            team_id=team_id, team_member_level_dtos=team_member_level_dtos,
            presenter=presenter_mock
        )

        # Assert
        assert response == \
               expected_presenter_response_for_duplicate_team_member_levels_mock

        presenter_mock.response_for_duplicate_team_member_levels. \
            assert_called_once()
        call_args = \
            presenter_mock.response_for_duplicate_team_member_levels.call_args
        error_object = call_args[0][0]
        duplicate_team_member_level_names = error_object.team_member_level_names
        assert sorted(duplicate_team_member_level_names) == \
               sorted(expected_duplicate_team_member_level_names)

    def test_with_valid_details_return_response(
            self, storage_mock, presenter_mock, interactor,
            prepare_team_member_level_dtos):
        # Arrange
        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        team_member_level_dtos = prepare_team_member_level_dtos

        expected_presenter_response_for_add_levels_to_team_mock = Mock()

        presenter_mock.prepare_success_response_for_add_team_member_levels_to_team.return_value = \
            expected_presenter_response_for_add_levels_to_team_mock

        # Act
        response = interactor.add_team_member_levels_wrapper(
            team_id=team_id, team_member_level_dtos=team_member_level_dtos,
            presenter=presenter_mock
        )

        # Assert
        assert response == \
               expected_presenter_response_for_add_levels_to_team_mock

        presenter_mock.prepare_success_response_for_add_team_member_levels_to_team. \
            assert_called_once()
        storage_mock.add_team_member_levels.assert_called_once_with(
            team_id=team_id, team_member_level_dtos=team_member_level_dtos
        )
