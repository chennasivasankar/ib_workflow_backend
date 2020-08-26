import json

import pytest


class TestGetSpecificProjectDetailsPresenterImplementation:

    @pytest.fixture()
    def presenter(self):
        from ib_iam.presenters.get_specific_project_details_presenter_implementation import \
            GetSpecificProjectDetailsPresenterImplementation
        presenter = GetSpecificProjectDetailsPresenterImplementation()
        return presenter

    def test_prepare_success_response_for_get_specific_team_details(
            self, presenter, prepare_basic_user_details_dtos,
            prepare_user_role_dtos, snapshot
    ):
        # Arrange
        basic_user_details_dtos = prepare_basic_user_details_dtos
        user_role_dtos = prepare_user_role_dtos

        # Act
        response = presenter.prepare_success_response_for_get_specific_team_details(
            user_role_dtos=user_role_dtos,
            basic_user_details_dtos=basic_user_details_dtos
        )

        # Assert
        response_dict = json.loads(response.content)

        snapshot.assert_match(response_dict, "get_team_specific_details")

    @pytest.fixture()
    def prepare_basic_user_details_dtos(self):
        basic_user_details_list = [
            {
                "user_id": "31be920b-7b4c-49e7-8adb-41a0c18da848",
                "name": "user_1",
                "profile_pic_url": None
            },
            {
                "user_id": "01be920b-7b4c-49e7-8adb-41a0c18da848",
                "name": "user_2",
                "profile_pic_url": None
            },
            {
                "user_id": "77be920b-7b4c-49e7-8adb-41a0c18da848",
                "name": "user_3",
                "profile_pic_url": None
            }
        ]
        from ib_iam.tests.factories.storage_dtos import \
            BasicUserDetailsDTOFactory
        basic_user_details_dtos = [
            BasicUserDetailsDTOFactory(
                user_id=basic_user_details_dict["user_id"],
                name=basic_user_details_dict["name"],
                profile_pic_url=basic_user_details_dict["profile_pic_url"]
            )
            for basic_user_details_dict in basic_user_details_list
        ]
        return basic_user_details_dtos

    @pytest.fixture()
    def prepare_user_role_dtos(self):
        user_roles_list = [
            {
                "user_id": "31be920b-7b4c-49e7-8adb-41a0c18da848",
                "role_id": "ROLE_1",
                "name": "NAME_1",
                "description": "description"
            },
            {
                "user_id": "31be920b-7b4c-49e7-8adb-41a0c18da848",
                "role_id": "ROLE_2",
                "name": "NAME_2",
                "description": "description"
            },
            {
                "user_id": "01be920b-7b4c-49e7-8adb-41a0c18da848",
                "role_id": "ROLE_3",
                "name": "NAME_3",
                "description": "description"
            }
        ]
        from ib_iam.tests.factories.storage_dtos import UserRoleDTOFactory
        user_roles_dtos = [
            UserRoleDTOFactory(
                user_id=user_roles_dict["user_id"],
                role_id=user_roles_dict["role_id"],
                name=user_roles_dict["name"],
                description=user_roles_dict["description"]
            )
            for user_roles_dict in user_roles_list
        ]
        return user_roles_dtos
