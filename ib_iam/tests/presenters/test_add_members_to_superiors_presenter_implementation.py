import json

import pytest

from ib_iam.constants.enums import StatusCode


class TestAddMembersToSuperiorsPresenterImplementation:

    @pytest.fixture()
    def presenter(self):
        from ib_iam.presenters. \
            add_members_to_superiors_presenter_implementation import \
            AddMembersToSuperiorsPresenterImplementation
        return AddMembersToSuperiorsPresenterImplementation()

    def test_prepare_success_response_for_add_members_superiors(
            self, presenter
    ):
        # Act
        response_object = presenter. \
            prepare_success_response_for_add_members_superiors()

        # Assert
        assert response_object.status_code == StatusCode.SUCCESS_CREATE.value

    def test_response_for_invalid_team_id(self, presenter):
        # Arrange
        from ib_iam.presenters. \
            add_members_to_superiors_presenter_implementation import \
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

    def test_response_for_invalid_level_hierarchy_of_team(self, presenter):
        # Arrange
        from ib_iam.presenters. \
            add_members_to_superiors_presenter_implementation import \
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

    def test_response_for_team_member_ids_not_found(self, presenter):
        # Arrange
        team_member_ids = ["1", "2"]
        from ib_iam.presenters. \
            add_members_to_superiors_presenter_implementation import \
            TEAM_MEMBER_IDS_NOT_FOUND
        expected_response = TEAM_MEMBER_IDS_NOT_FOUND[0].format(
            team_member_ids=team_member_ids
        )
        expected_http_status_code = StatusCode.NOT_FOUND.value
        expected_res_status = TEAM_MEMBER_IDS_NOT_FOUND[1]

        from ib_iam.exceptions.custom_exceptions import MemberIdsNotFoundInTeam
        error_object = MemberIdsNotFoundInTeam(
            team_member_ids=team_member_ids
        )

        # Act
        response_obj = presenter.response_for_team_member_ids_not_found(
            err=error_object
        )

        # Assert
        response_data = json.loads(response_obj.content)

        assert response_data["response"] == expected_response
        assert response_data["http_status_code"] == expected_http_status_code
        assert response_data["res_status"] == expected_res_status

    def test_response_for_users_not_belong_to_team_member_level(
            self, presenter
    ):
        # Arrange
        user_ids = ["1", "2"]
        level_hierarchy = 1
        from ib_iam.presenters. \
            add_members_to_superiors_presenter_implementation import \
            USERS_NOT_BELONG_TO_TEAM_MEMBER_LEVEL
        expected_response = USERS_NOT_BELONG_TO_TEAM_MEMBER_LEVEL[0].format(
            user_ids=user_ids, level_hierarchy=level_hierarchy
        )
        expected_http_status_code = StatusCode.NOT_FOUND.value
        expected_res_status = USERS_NOT_BELONG_TO_TEAM_MEMBER_LEVEL[1]

        from ib_iam.exceptions.custom_exceptions import \
            UsersNotBelongToGivenLevelHierarchy
        error_object = UsersNotBelongToGivenLevelHierarchy(
            user_ids=user_ids, level_hierarchy=level_hierarchy
        )

        # Act
        response_obj = presenter. \
            response_for_users_not_belong_to_team_member_level(
            err=error_object
        )

        # Assert
        response_data = json.loads(response_obj.content)

        assert response_data["response"] == expected_response
        assert response_data["http_status_code"] == expected_http_status_code
        assert response_data["res_status"] == expected_res_status

    def test_response_for_user_is_not_admin(self, presenter):
        # Arrange
        from ib_iam.presenters. \
            assign_user_roles_for_given_project_bulk_presenter_implementation \
            import USER_DOES_NOT_HAVE_ACCESS
        expected_response = USER_DOES_NOT_HAVE_ACCESS[0]
        response_status_code = USER_DOES_NOT_HAVE_ACCESS[1]

        # Act
        response_object = presenter.response_for_user_is_not_admin()

        # Assert
        response = json.loads(response_object.content)

        assert response['http_status_code'] == StatusCode.FORBIDDEN.value
        assert response['res_status'] == response_status_code
        assert response['response'] == expected_response
