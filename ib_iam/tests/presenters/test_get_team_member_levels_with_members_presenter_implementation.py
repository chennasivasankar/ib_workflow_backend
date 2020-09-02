import json

import pytest

from ib_iam.constants.enums import StatusCode


class TestGetTeamMemberLevelsWithMembersPresenterImplementation:

    @pytest.fixture()
    def presenter(self):
        from ib_iam.presenters.get_team_member_levels_with_members_presenter_implementation import \
            GetTeamMemberLevelsWithMembersPresenterImplementation
        presenter = GetTeamMemberLevelsWithMembersPresenterImplementation()
        return presenter

    def test_prepare_success_response_for_team_member_levels_with_members(
            self, presenter, prepare_complete_team_member_levels_details_dto,
            snapshot
    ):
        # Arrange
        complete_team_member_levels_details_dto = \
            prepare_complete_team_member_levels_details_dto

        # Act
        response = presenter.prepare_success_response_for_team_member_levels_with_members(
            complete_team_member_levels_details_dto=complete_team_member_levels_details_dto
        )

        # Assert
        response_dict = json.loads(response.content)

        snapshot.assert_match(
            response_dict, "complete_team_member_levels_details")

    @pytest.fixture()
    def prepare_team_member_level_details_dtos(self):
        team_member_level_details_list = [{
            'level_id': 'd6264b89-df8d-4b08-9ce1-f61004a0fbcc',
            'level_name': 'Developer',
            'level_hierarchy': 0
        }, {
            'level_id': '55b28aac-db47-44b4-a76a-c42084979a83',
            'level_name': 'SDL',
            'level_hierarchy': 1
        }, {
            'level_id': 'a762f699-a9b4-42c7-82b8-b702296ff764',
            'level_name': 'PM',
            'level_hierarchy': 2
        }, {
            'level_id': '7e82dc48-0fde-4aad-9e82-7b1f9d77378d',
            'level_name': 'EM',
            'level_hierarchy': 3
        }, {
            'level_id': '615ef7d5-c142-46b4-acd7-f37ab35bf83f',
            'level_name': 'Chairman',
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

    @pytest.fixture()
    def prepare_user_profile_dtos(self):
        user_profile_list = [
            {
                "user_id": '2b8f68ed-82cb-47ea-bf92-5a970d0c1109',
                "profile_pic_url": "https://picsum.photos/200",
                "email": "test@gmail.com",
                "name": "user_1"
            },
            {
                "user_id": "e5fd217b-a1c6-4b43-aea0-6e9cf17117a4",
                "profile_pic_url": "https://picsum.photos/200",
                "email": "test@gmail.com",
                "name": "user_2"
            },
            {
                "user_id": "216cc13f-5446-493b-a2f7-90aaaeecaef1",
                "profile_pic_url": "https://picsum.photos/200",
                "email": "test@gmail.com",
                "name": "user_3"
            },
            {
                "user_id": 'bc96292f-0e09-46ec-b90f-bf28c09e9365',
                "profile_pic_url": "https://picsum.photos/200",
                "email": "test@gmail.com",
                "name": "user_4"
            },
            {
                "user_id": "86de39e4-e85d-4650-b78e-65f9bdc69719",
                "profile_pic_url": "https://picsum.photos/200",
                "email": "test@gmail.com",
                "name": "user_5"
            },
            {
                "user_id": "a7178219-7559-45c4-8c90-d25807820f20",
                "profile_pic_url": "https://picsum.photos/200",
                "email": "test@gmail.com",
                "name": "user_6"
            },
            {
                "user_id": "4b5fd9ba-64a2-4ee2-8868-5e1d00bd83c8",
                "profile_pic_url": "https://picsum.photos/200",
                "email": "test@gmail.com",
                "name": "user_6"
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

    @pytest.fixture()
    def prepare_member_dtos(self):
        members_list = [
            {
                'member_id': '2b8f68ed-82cb-47ea-bf92-5a970d0c1109',
                'immediate_superior_team_user_id': 'bc96292f-0e09-46ec-b90f-bf28c09e9365'
            },
            {
                'member_id': 'e5fd217b-a1c6-4b43-aea0-6e9cf17117a4',
                'immediate_superior_team_user_id': 'bc96292f-0e09-46ec-b90f-bf28c09e9365'
            },
            {
                'member_id': '216cc13f-5446-493b-a2f7-90aaaeecaef1',
                'immediate_superior_team_user_id': '86de39e4-e85d-4650-b78e-65f9bdc69719'
            },
            {
                'member_id': 'bc96292f-0e09-46ec-b90f-bf28c09e9365',
                'immediate_superior_team_user_id': '4b5fd9ba-64a2-4ee2-8868-5e1d00bd83c8'
            },
            {
                'member_id': '86de39e4-e85d-4650-b78e-65f9bdc69719',
                'immediate_superior_team_user_id': '4b5fd9ba-64a2-4ee2-8868-5e1d00bd83c8'
            },
            {
                'member_id': 'a7178219-7559-45c4-8c90-d25807820f20',
                'immediate_superior_team_user_id': '4b5fd9ba-64a2-4ee2-8868-5e1d00bd83c8'
            },
            {
                'member_id': '4b5fd9ba-64a2-4ee2-8868-5e1d00bd83c8',
                'immediate_superior_team_user_id': None
            }
        ]
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
    def prepare_team_member_level_id_with_member_ids_dtos(self):
        level_id_with_member_ids_list = [{
            'level_id': 'd6264b89-df8d-4b08-9ce1-f61004a0fbcc',
            'member_ids': ['2b8f68ed-82cb-47ea-bf92-5a970d0c1109',
                           'e5fd217b-a1c6-4b43-aea0-6e9cf17117a4',
                           '216cc13f-5446-493b-a2f7-90aaaeecaef1'
                           ]
        }, {
            'level_id': '55b28aac-db47-44b4-a76a-c42084979a83',
            'member_ids': ['bc96292f-0e09-46ec-b90f-bf28c09e9365',
                           '86de39e4-e85d-4650-b78e-65f9bdc69719',
                           'a7178219-7559-45c4-8c90-d25807820f20']
        }, {
            'level_id': 'a762f699-a9b4-42c7-82b8-b702296ff764',
            'member_ids': ['4b5fd9ba-64a2-4ee2-8868-5e1d00bd83c8']
        }]

        from ib_iam.tests.factories.interactor_dtos import \
            TeamMemberLevelIdWithMemberIdsDTOFactory
        team_member_level_id_with_member_ids_dtos = [
            TeamMemberLevelIdWithMemberIdsDTOFactory(
                team_member_level_id=level_id_with_member_ids_dict["level_id"],
                member_ids=level_id_with_member_ids_dict["member_ids"]
            )
            for level_id_with_member_ids_dict in level_id_with_member_ids_list
        ]
        return team_member_level_id_with_member_ids_dtos

    @pytest.fixture()
    def prepare_member_id_with_subordinate_member_ids_dtos(self):
        member_id_with_subordinate_member_ids_list = [
            {
                "member_id": "2b8f68ed-82cb-47ea-bf92-5a970d0c1109",
                "subordinate_member_ids": []
            },
            {
                "member_id": "e5fd217b-a1c6-4b43-aea0-6e9cf17117a4",
                "subordinate_member_ids": []
            },
            {
                "member_id": "216cc13f-5446-493b-a2f7-90aaaeecaef1",
                "subordinate_member_ids": []
            },
            {
                "member_id": "bc96292f-0e09-46ec-b90f-bf28c09e9365",
                "subordinate_member_ids": [
                    '2b8f68ed-82cb-47ea-bf92-5a970d0c1109',
                    'e5fd217b-a1c6-4b43-aea0-6e9cf17117a4',
                ]
            },
            {
                "member_id": "86de39e4-e85d-4650-b78e-65f9bdc69719",
                "subordinate_member_ids": [
                    '216cc13f-5446-493b-a2f7-90aaaeecaef1'
                ]
            },
            {
                "member_id": "a7178219-7559-45c4-8c90-d25807820f20",
                "subordinate_member_ids": []
            },
            {
                "member_id": "4b5fd9ba-64a2-4ee2-8868-5e1d00bd83c8",
                "subordinate_member_ids": [
                    "bc96292f-0e09-46ec-b90f-bf28c09e9365",
                    '86de39e4-e85d-4650-b78e-65f9bdc69719',
                    'a7178219-7559-45c4-8c90-d25807820f20'
                ]
            },
        ]
        from ib_iam.tests.factories.storage_dtos import \
            MemberIdWithSubordinateMemberIdsDTOFactory
        member_id_with_subordinate_member_ids_dtos = [
            MemberIdWithSubordinateMemberIdsDTOFactory(
                member_id=member_id_with_subordinate_member_ids_dict[
                    "member_id"],
                subordinate_member_ids=
                member_id_with_subordinate_member_ids_dict[
                    "subordinate_member_ids"]
            )
            for member_id_with_subordinate_member_ids_dict in
            member_id_with_subordinate_member_ids_list
        ]
        return member_id_with_subordinate_member_ids_dtos

    @pytest.fixture()
    def prepare_complete_team_member_levels_details_dto(
            self, prepare_member_dtos, prepare_user_profile_dtos,
            prepare_team_member_level_details_dtos,
            prepare_team_member_level_id_with_member_ids_dtos,
            prepare_member_id_with_subordinate_member_ids_dtos
    ):
        from ib_iam.tests.factories.interactor_dtos import \
            CompleteTeamMemberLevelsDetailsDTOFactory
        complete_team_member_levels_details_dto = \
            CompleteTeamMemberLevelsDetailsDTOFactory(
                member_dtos=prepare_member_dtos,
                user_profile_dtos=prepare_user_profile_dtos,
                team_member_level_details_dtos=prepare_team_member_level_details_dtos,
                team_member_level_id_with_member_ids_dtos=prepare_team_member_level_id_with_member_ids_dtos,
                member_id_with_subordinate_member_ids_dtos=prepare_member_id_with_subordinate_member_ids_dtos
            )
        return complete_team_member_levels_details_dto

    def test_response_for_invalid_team_id(self, presenter):
        # Arrange
        from ib_iam.presenters.get_team_member_levels_with_members_presenter_implementation import \
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
