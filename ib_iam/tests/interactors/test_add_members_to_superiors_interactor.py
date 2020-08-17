from unittest.mock import Mock

import pytest


class TestAddMembersToSuperiorsInteractor:

    @pytest.fixture()
    def storage_mock(self):
        from unittest.mock import create_autospec

        from ib_iam.interactors.storage_interfaces.level_storage_interface import \
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

    def test_with_valid_details_return_response(
            self, storage_mock, presenter_mock, interactor,
            prepare_immediate_superior_id_with_member_ids_dtos
    ):
        # Arrange
        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        level_hierarchy = 0
        immediate_superior_id_with_member_ids_dtos = \
            prepare_immediate_superior_id_with_member_ids_dtos

        expected_presenter_prepare_success_response_for_add_members_superiors = \
            Mock()

        presenter_mock.prepare_success_response_for_add_members_superiors. \
            return_value = expected_presenter_prepare_success_response_for_add_members_superiors

        # Act
        response = interactor.add_members_to_superiors_wrapper(
            team_id=team_id, level_hierarchy=level_hierarchy,
            presenter=presenter_mock,
            immediate_superior_user_id_with_member_ids_dtos=immediate_superior_id_with_member_ids_dtos
        )

        # Assert
        assert response == \
               expected_presenter_prepare_success_response_for_add_members_superiors

        presenter_mock.prepare_success_response_for_add_members_superiors. \
            assert_called_once()
        storage_mock.add_members_to_superiors.assert_called_with(
            team_id=team_id, level_hierarchy=level_hierarchy,
            immediate_superior_user_id_with_member_ids_dtos=immediate_superior_id_with_member_ids_dtos
        )

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
