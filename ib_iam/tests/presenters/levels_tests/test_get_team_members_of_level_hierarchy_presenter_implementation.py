import json

import pytest

from ib_iam.constants.enums import StatusCode


class TestGetTeamMembersOfLevelHierarchyPresenterImplementation:

    @pytest.fixture()
    def presenter(self):
        from ib_iam.presenters.get_team_members_of_level_hierarchy_presenter_implementation import \
            GetTeamMembersOfLevelHierarchyPresenterImplementation
        presenter = GetTeamMembersOfLevelHierarchyPresenterImplementation()
        return presenter

    @pytest.fixture()
    def get_member_dtos(self):
        members_list = [{
            'member_id': 'e326eb71-0a81-4015-b7d0-caa2cccd338d',
            'immediate_superior_team_user_id': 'eabada6d-0f17-4638-af2e-abd2f4d11462'
        }, {
            'member_id': 'f420d920-0393-4759-bf67-8e10bb7c44bf',
            'immediate_superior_team_user_id': '967c596a-3a2c-4de7-a09d-7d28a0796f2e'
        }, {
            'member_id': '239b29fd-446a-450c-bf9d-f8c1e744ad58',
            'immediate_superior_team_user_id': None
        }]
        from ib_iam.tests.factories.storage_dtos import MemberDTOFactory
        member_dtos = [
            MemberDTOFactory(
                member_id=members_dict["member_id"],
                immediate_superior_team_user_id=members_dict[
                    "immediate_superior_team_user_id"]
            )
            for members_dict in members_list
        ]
        return member_dtos

    @pytest.fixture()
    def get_user_profile_dtos(self):
        user_profile_list = [
            {
                "user_id": "e326eb71-0a81-4015-b7d0-caa2cccd338d",
                "profile_pic_url": "https://picsum.photos/200",
                "email": "test@gmail.com",
                "name": "user_1"
            },
            {
                "user_id": "f420d920-0393-4759-bf67-8e10bb7c44bf",
                "profile_pic_url": "https://picsum.photos/200",
                "email": "test@gmail.com",
                "name": "user_2"
            },
            {
                "user_id": "239b29fd-446a-450c-bf9d-f8c1e744ad58",
                "profile_pic_url": "https://picsum.photos/200",
                "email": "test@gmail.com",
                "name": "user_3"
            }
        ]
        from ib_iam.tests.factories.adapter_dtos import UserProfileDTOFactory
        user_profile_dtos = [
            UserProfileDTOFactory(
                user_id=user_profile_dict["user_id"],
                name=user_profile_dict["name"],
                email=user_profile_dict["email"],
                profile_pic_url=user_profile_dict["profile_pic_url"]
            )
            for user_profile_dict in user_profile_list
        ]
        return user_profile_dtos

    def test_prepare_success_response_for_get_team_members_of_level_hierarchy(
            self, presenter, get_member_dtos, get_user_profile_dtos, snapshot
    ):
        # Arrange
        member_dtos = get_member_dtos
        user_profile_dtos = get_user_profile_dtos

        # Act
        response_object = \
            presenter.prepare_success_response_for_get_team_members_of_level_hierarchy(
                member_dtos=member_dtos, user_profile_dtos=user_profile_dtos
            )

        # Assert
        response_dict = json.loads(response_object.content)

        snapshot.assert_match(response_dict, "get_team_members")

    def test_response_for_invalid_team_id(self, presenter):
        # Arrange
        from ib_iam.presenters.get_team_members_of_level_hierarchy_presenter_implementation import \
            INVALID_TEAM_ID
        expected_response = INVALID_TEAM_ID[0]
        expected_http_status_code = StatusCode.BAD_REQUEST.value
        expected_res_status = INVALID_TEAM_ID[1]

        # Act
        response_obj = presenter.response_for_invalid_team_id_exception()

        # Assert
        response_data = json.loads(response_obj.content)

        assert response_data["response"] == expected_response
        assert response_data["http_status_code"] == expected_http_status_code
        assert response_data["res_status"] == expected_res_status

    def test_response_for_invalid_level_hierarchy_of_team(self, presenter):
        # Arrange
        from ib_iam.presenters.get_team_members_of_level_hierarchy_presenter_implementation import \
            INVALID_LEVEL_HIERARCHY
        expected_response = INVALID_LEVEL_HIERARCHY[0]
        expected_http_status_code = StatusCode.BAD_REQUEST.value
        expected_res_status = INVALID_LEVEL_HIERARCHY[1]

        # Act
        response_obj = presenter.response_for_invalid_level_hierarchy_of_team()

        # Assert
        response_data = json.loads(response_obj.content)

        assert response_data["response"] == expected_response
        assert response_data["http_status_code"] == expected_http_status_code
        assert response_data["res_status"] == expected_res_status

    def test_response_for_user_is_not_admin(self, presenter):
        # Arrange
        from ib_iam.presenters.assign_user_roles_for_given_project_bulk_presenter_implementation import \
            USER_DOES_NOT_HAVE_ACCESS
        expected_response = USER_DOES_NOT_HAVE_ACCESS[0]
        response_status_code = USER_DOES_NOT_HAVE_ACCESS[1]

        # Act
        response_object = presenter.response_for_user_is_not_admin_exception()

        # Assert
        response = json.loads(response_object.content)

        assert response['http_status_code'] == StatusCode.FORBIDDEN.value
        assert response['res_status'] == response_status_code
        assert response['response'] == expected_response
