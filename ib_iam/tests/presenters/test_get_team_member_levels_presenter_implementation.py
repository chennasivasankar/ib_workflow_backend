import json

import pytest

from ib_iam.constants.enums import StatusCode


class TestGetTeamMemberLevelsPresenterImplementation:

    @pytest.fixture()
    def presenter(self):
        from ib_iam.presenters.get_team_member_levels_presenter_implementation import \
            GetTeamMemberLevelsPresenterImplementation
        presenter = GetTeamMemberLevelsPresenterImplementation()
        return presenter

    @pytest.fixture()
    def prepare_team_member_level_details_dtos(self):
        team_member_level_details_list = [{
            'level_id': 'd6264b89-df8d-4b08-9ce1-f61004a0fbcc',
            'level_name': 'Geoffrey Barnes',
            'level_hierarchy': 0
        }, {
            'level_id': '55b28aac-db47-44b4-a76a-c42084979a83',
            'level_name': 'Scott Baker',
            'level_hierarchy': 1
        }, {
            'level_id': 'a762f699-a9b4-42c7-82b8-b702296ff764',
            'level_name': 'Dan Ramos',
            'level_hierarchy': 2
        }, {
            'level_id': '7e82dc48-0fde-4aad-9e82-7b1f9d77378d',
            'level_name': 'Jeffrey Clark',
            'level_hierarchy': 3
        }, {
            'level_id': '615ef7d5-c142-46b4-acd7-f37ab35bf83f',
            'level_name': 'Sarah Mason',
            'level_hierarchy': 4
        }]

        from ib_iam.tests.factories.storage_dtos import \
            TeamMemberLevelDetailsDTOFactory
        team_member_level_details_dtos = [
            TeamMemberLevelDetailsDTOFactory(
                team_member_level_id=level_details_dict["level_id"],
                team_member_level_name=level_details_dict["level_name"],
                level_hierarchy=level_details_dict["level_hierarchy"]
            )
            for level_details_dict in team_member_level_details_list
        ]
        return team_member_level_details_dtos

    def test_response_for_level_details_dtos(
            self, presenter, snapshot, prepare_team_member_level_details_dtos):
        # Arrange
        team_member_level_details_dtos = prepare_team_member_level_details_dtos

        # Act
        response = presenter.response_for_team_member_level_details_dtos(
            team_member_level_details_dtos=team_member_level_details_dtos
        )

        # Assert
        response_data = json.loads(response.content)

        snapshot.assert_match(response_data, "level_details_dtos_response")

    def test_response_for_invalid_team_id(self, presenter):
        # Arrange
        from ib_iam.presenters.get_team_member_levels_presenter_implementation import \
            INVALID_TEAM_ID
        expected_response = INVALID_TEAM_ID[0]
        expected_http_status_code = StatusCode.BAD_REQUEST.value
        expected_res_status = INVALID_TEAM_ID[1]

        # Act
        response_obj = presenter.response_for_invalid_team_id()

        # Assert
        response_data = json.loads(response_obj.content)

        assert response_data["response"] == expected_response
        assert response_data["http_status_code"] == expected_http_status_code
        assert response_data["res_status"] == expected_res_status
