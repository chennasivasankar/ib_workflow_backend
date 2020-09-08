from unittest.mock import Mock

import pytest


class TestAddMembersToSuperiorsInteractor:

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
            AddMembersToSuperiorsPresenterInterface
        presenter = create_autospec(AddMembersToSuperiorsPresenterInterface)
        return presenter

    @pytest.fixture()
    def interactor(self, storage_mock):
        from ib_iam.interactors.add_members_to_superiors_interactor import \
            AddMembersToSuperiorsInteractor
        interactor = AddMembersToSuperiorsInteractor(
            team_member_level_storage=storage_mock)
        return interactor

    def test_with_invalid_team_id_return_response(
            self, storage_mock, presenter_mock, interactor,
            prepare_immediate_superior_id_with_member_ids_dtos
    ):
        # Arrange
        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        member_level_hierarchy = 0
        immediate_superior_id_with_member_ids_dtos = \
            prepare_immediate_superior_id_with_member_ids_dtos
        expected_presenter_response_for_invalid_team_id_mock = Mock()

        from ib_iam.exceptions.custom_exceptions import InvalidTeamId
        storage_mock.validate_team_id.side_effect = InvalidTeamId

        presenter_mock.response_for_invalid_team_id.return_value \
            = expected_presenter_response_for_invalid_team_id_mock

        # Act
        response = interactor.add_members_to_superiors_wrapper(
            team_id=team_id, member_level_hierarchy=member_level_hierarchy,
            presenter=presenter_mock,
            immediate_superior_user_id_with_member_ids_dtos=immediate_superior_id_with_member_ids_dtos
        )

        # Assert
        assert response == \
               expected_presenter_response_for_invalid_team_id_mock
        storage_mock.validate_team_id.assert_called_with(team_id=team_id)
        presenter_mock.response_for_invalid_team_id.assert_called_once()

    def test_with_valid_details_return_response(
            self, storage_mock, presenter_mock, interactor,
            prepare_immediate_superior_id_with_member_ids_dtos
    ):
        # Arrange
        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        member_level_hierarchy = 0
        immediate_superior_id_with_member_ids_dtos = \
            prepare_immediate_superior_id_with_member_ids_dtos
        team_member_ids_in_database = [
            'e73b5841-ec73-433b-9f60-fead97b0cf03',
            '223c90e6-3a65-4e09-91f7-873e32cd8856',
            'ccdfa4c5-31ec-45ce-820a-a31b73b02b7d',
            'f5253a19-3924-4d38-a263-567dae36808d',
            'd96e90ef-44d6-43b8-b3bb-6a291c8abd32',
            '71a79d50-c4e7-4a67-8abf-f1a986b46957',
            "60e77608-f798-4ca8-b395-777e5e998f5d",
            "6e9817f5-baff-44fe-aeb8-bb17fdd4735c"
        ]

        expected_presenter_prepare_success_response_for_add_members_superiors = \
            Mock()

        storage_mock.get_team_member_ids.return_value = \
            team_member_ids_in_database
        presenter_mock.prepare_success_response_for_add_members_superiors. \
            return_value = expected_presenter_prepare_success_response_for_add_members_superiors

        # Act
        response = interactor.add_members_to_superiors_wrapper(
            team_id=team_id, member_level_hierarchy=member_level_hierarchy,
            presenter=presenter_mock,
            immediate_superior_user_id_with_member_ids_dtos=immediate_superior_id_with_member_ids_dtos
        )

        # Assert
        assert response == \
               expected_presenter_prepare_success_response_for_add_members_superiors

        presenter_mock.prepare_success_response_for_add_members_superiors. \
            assert_called_once()
        storage_mock.add_members_to_superiors.assert_called_with(
            team_id=team_id, member_level_hierarchy=member_level_hierarchy,
            immediate_superior_user_id_with_member_ids_dtos=immediate_superior_id_with_member_ids_dtos
        )

    def test_with_invalid_level_hierarchy_return_response(
            self, storage_mock, presenter_mock, interactor,
            prepare_immediate_superior_id_with_member_ids_dtos
    ):
        # Arrange
        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        member_level_hierarchy = -1
        immediate_superior_id_with_member_ids_dtos = \
            prepare_immediate_superior_id_with_member_ids_dtos
        expected_presenter_response_for_invalid_level_hierarchy_of_team_mock = \
            Mock()

        from ib_iam.exceptions.custom_exceptions import \
            InvalidLevelHierarchyOfTeam
        storage_mock.validate_level_hierarchy_of_team.side_effect = \
            InvalidLevelHierarchyOfTeam

        presenter_mock.response_for_invalid_level_hierarchy_of_team.return_value \
            = expected_presenter_response_for_invalid_level_hierarchy_of_team_mock

        # Act
        response = interactor.add_members_to_superiors_wrapper(
            team_id=team_id, member_level_hierarchy=member_level_hierarchy,
            presenter=presenter_mock,
            immediate_superior_user_id_with_member_ids_dtos=immediate_superior_id_with_member_ids_dtos
        )

        # Assert
        assert response == \
               expected_presenter_response_for_invalid_level_hierarchy_of_team_mock
        storage_mock.validate_level_hierarchy_of_team.assert_called_with(
            team_id=team_id, level_hierarchy=member_level_hierarchy
        )
        presenter_mock.response_for_invalid_level_hierarchy_of_team. \
            assert_called_once()

    def test_with_team_member_ids_not_found_return_response(
            self, storage_mock, presenter_mock, interactor,
            prepare_immediate_superior_id_with_member_ids_dtos
    ):
        # Arrange
        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        member_level_hierarchy = 2
        immediate_superior_id_with_member_ids_dtos = \
            prepare_immediate_superior_id_with_member_ids_dtos
        team_member_level_ids_in_database = [
            "b52d31f3-7359-4a5a-b81d-579acd460942",
            '5aba9060-0714-4857-bd78-8689ec585b10',
            '4fb31acf-c73e-43db-b561-60ee38597608'
        ]
        team_member_ids_in_database = [
            'ccdfa4c5-31ec-45ce-820a-a31b73b02b7d',
            'f5253a19-3924-4d38-a263-567dae36808d',
            'd96e90ef-44d6-43b8-b3bb-6a291c8abd32',
            '71a79d50-c4e7-4a67-8abf-f1a986b46957'
        ]
        team_member_ids_not_found = [
            'e73b5841-ec73-433b-9f60-fead97b0cf03',
            '223c90e6-3a65-4e09-91f7-873e32cd8856',
            "60e77608-f798-4ca8-b395-777e5e998f5d",
            "6e9817f5-baff-44fe-aeb8-bb17fdd4735c"
        ]

        expected_presenter_response_for_team_member_ids_not_found_mock = Mock()

        storage_mock.get_team_member_level_ids.return_value = \
            team_member_level_ids_in_database
        storage_mock.get_team_member_ids.return_value = \
            team_member_ids_in_database

        presenter_mock.response_for_team_member_ids_not_found.return_value = \
            expected_presenter_response_for_team_member_ids_not_found_mock

        # Act
        response = interactor.add_members_to_superiors_wrapper(
            team_id=team_id, member_level_hierarchy=member_level_hierarchy,
            presenter=presenter_mock,
            immediate_superior_user_id_with_member_ids_dtos=immediate_superior_id_with_member_ids_dtos
        )

        # Assert
        assert response == \
               expected_presenter_response_for_team_member_ids_not_found_mock

        call_obj = presenter_mock.response_for_team_member_ids_not_found.call_args
        error_object = call_obj.args[0]

        assert error_object.team_member_ids == team_member_ids_not_found
        presenter_mock.response_for_team_member_ids_not_found. \
            assert_called_once()
        storage_mock.get_team_member_ids.assert_called_with(team_id=team_id)

    def test_with_users_not_belong_to_given_team_member_level_return_response(
            self, storage_mock, presenter_mock, interactor,
            prepare_immediate_superior_id_with_member_ids_dtos
    ):
        # Arrange
        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        member_level_hierarchy = 2
        immediate_superior_id_with_member_ids_dtos = \
            prepare_immediate_superior_id_with_member_ids_dtos
        team_member_ids_in_database = [
            'e73b5841-ec73-433b-9f60-fead97b0cf03',
            '223c90e6-3a65-4e09-91f7-873e32cd8856',
            'ccdfa4c5-31ec-45ce-820a-a31b73b02b7d',
            'f5253a19-3924-4d38-a263-567dae36808d',
            'd96e90ef-44d6-43b8-b3bb-6a291c8abd32',
            '71a79d50-c4e7-4a67-8abf-f1a986b46957',
            "60e77608-f798-4ca8-b395-777e5e998f5d",
            "6e9817f5-baff-44fe-aeb8-bb17fdd4735c"
        ]
        subordinate_user_ids = [
            'e73b5841-ec73-433b-9f60-fead97b0cf03',
            '223c90e6-3a65-4e09-91f7-873e32cd8856',
            'ccdfa4c5-31ec-45ce-820a-a31b73b02b7d',
            'f5253a19-3924-4d38-a263-567dae36808d',
            'd96e90ef-44d6-43b8-b3bb-6a291c8abd32',
            '71a79d50-c4e7-4a67-8abf-f1a986b46957'
        ]

        expected_presenter_response_for_users_not_belong_to_team_member_level_mock = \
            Mock()

        storage_mock.get_team_member_ids.return_value = \
            team_member_ids_in_database
        from ib_iam.exceptions.custom_exceptions import UsersNotBelongToGivenLevelHierarchy
        storage_mock.validate_users_belong_to_given_level_hierarchy_in_a_team.side_effect = \
            UsersNotBelongToGivenLevelHierarchy(
                user_ids=subordinate_user_ids,
                level_hierarchy=member_level_hierarchy
            )
        presenter_mock.response_for_users_not_belong_to_team_member_level. \
            return_value = expected_presenter_response_for_users_not_belong_to_team_member_level_mock

        # Act
        response = interactor.add_members_to_superiors_wrapper(
            team_id=team_id, member_level_hierarchy=member_level_hierarchy,
            presenter=presenter_mock,
            immediate_superior_user_id_with_member_ids_dtos=immediate_superior_id_with_member_ids_dtos
        )

        # Assert
        assert response == \
               expected_presenter_response_for_users_not_belong_to_team_member_level_mock

        storage_mock.validate_users_belong_to_given_level_hierarchy_in_a_team. \
            assert_called_once_with(
            team_id=team_id, level_hierarchy=member_level_hierarchy,
            user_ids=subordinate_user_ids
        )

        call_obj = presenter_mock.response_for_users_not_belong_to_team_member_level.call_args
        error_object = call_obj.args[0]
        assert error_object.user_ids == subordinate_user_ids
        assert error_object.level_hierarchy == member_level_hierarchy

    @pytest.fixture()
    def prepare_immediate_superior_id_with_member_ids_dtos(self):
        immediate_superior_id_with_member_ids_list = [{
            'immediate_superior_user_id': '60e77608-f798-4ca8-b395-777e5e998f5d',
            'member_ids': ['e73b5841-ec73-433b-9f60-fead97b0cf03',
                           '223c90e6-3a65-4e09-91f7-873e32cd8856',
                           'ccdfa4c5-31ec-45ce-820a-a31b73b02b7d']
        }, {
            'immediate_superior_user_id': '6e9817f5-baff-44fe-aeb8-bb17fdd4735c',
            'member_ids': ['f5253a19-3924-4d38-a263-567dae36808d',
                           'd96e90ef-44d6-43b8-b3bb-6a291c8abd32',
                           '71a79d50-c4e7-4a67-8abf-f1a986b46957']
        }]
        from ib_iam.tests.factories.interactor_dtos import \
            ImmediateSuperiorUserIdWithUserIdsDTOFactory
        immediate_superior_id_with_member_ids_dtos = [
            ImmediateSuperiorUserIdWithUserIdsDTOFactory(
                immediate_superior_user_id=details_dict[
                    "immediate_superior_user_id"],
                member_ids=details_dict["member_ids"]
            )
            for details_dict in immediate_superior_id_with_member_ids_list
        ]
        return immediate_superior_id_with_member_ids_dtos
