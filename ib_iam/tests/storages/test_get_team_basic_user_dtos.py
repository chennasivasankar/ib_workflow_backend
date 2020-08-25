import pytest


class TestGetTeamBasicUserDTOS:

    @pytest.fixture()
    def user_storage(self):
        from ib_iam.storages.user_storage_implementation import \
            UserStorageImplementation
        user_storage = UserStorageImplementation()
        return user_storage

    @pytest.fixture()
    def create_team(self):
        from ib_iam.tests.factories.models import TeamFactory
        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        user_id = "21be920b-7b4c-49e7-8adb-41a0c18da848"
        team_object = TeamFactory(
            team_id=team_id,
            name="name",
            description="description",
            created_by=user_id
        )
        return team_object

    @pytest.fixture()
    def create_user_teams(self, create_team):
        team_object = create_team
        user_ids = [
            "31be920b-7b4c-49e7-8adb-41a0c18da848",
            "01be920b-7b4c-49e7-8adb-41a0c18da848",
            "77be920b-7b4c-49e7-8adb-41a0c18da848"
        ]
        from ib_iam.tests.factories.models import UserTeamFactory
        user_team_objects = [
            UserTeamFactory(
                user_id=user_id,
                team=team_object
            )
            for user_id in user_ids
        ]
        return user_team_objects

    @pytest.fixture()
    def create_user_details(self):
        user_details_list = [
            {
                "user_id": "31be920b-7b4c-49e7-8adb-41a0c18da848",
                "name": "user_1",
            },
            {
                "user_id": "01be920b-7b4c-49e7-8adb-41a0c18da848",
                "name": "user_2",
            },
            {
                "user_id": "77be920b-7b4c-49e7-8adb-41a0c18da848",
                "name": "user_3",
            }
        ]
        from ib_iam.tests.factories.models import UserDetailsFactory
        user_details_objects = [
            UserDetailsFactory(
                user_id=user_details_dict["user_id"],
                name=user_details_dict["name"]
            )
            for user_details_dict in user_details_list
        ]
        return user_details_objects

    @pytest.mark.django_db
    def test_with_valid_team_id_return_response(
            self, user_storage, create_user_details, create_user_teams):
        # Arrange
        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        basic_user_details_list = [{
            'user_id': '31be920b-7b4c-49e7-8adb-41a0c18da848',
            'name': 'user_1',
            'profile_pic_url': None
        }, {
            'user_id': '01be920b-7b4c-49e7-8adb-41a0c18da848',
            'name': 'user_2',
            'profile_pic_url': None
        }, {
            'user_id': '77be920b-7b4c-49e7-8adb-41a0c18da848',
            'name': 'user_3',
            'profile_pic_url': None
        }]
        from ib_iam.tests.factories.storage_dtos import \
            BasicUserDetailsDTOFactory
        expected_basic_user_details_dtos = [
            BasicUserDetailsDTOFactory(
                user_id=basic_user_details_dict["user_id"],
                name=basic_user_details_dict["name"],
                profile_pic_url=basic_user_details_dict["profile_pic_url"]
            )
            for basic_user_details_dict in basic_user_details_list
        ]

        # Act
        response = user_storage.get_team_basic_user_dtos(
            team_id=team_id
        )

        # Assert
        assert response == expected_basic_user_details_dtos
