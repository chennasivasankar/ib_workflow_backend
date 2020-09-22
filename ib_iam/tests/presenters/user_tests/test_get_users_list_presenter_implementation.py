import json
import pytest

from ib_iam.constants.enums import StatusCode


class TestGetUsersListPresenter:

    @pytest.fixture
    def presenter(self):
        from ib_iam.presenters.get_users_list_presenter_implementation \
            import GetUsersListPresenterImplementation
        return GetUsersListPresenterImplementation()

    def test_raise_user_is_not_admin_exception(self, presenter):
        # Arrange
        from ib_iam.constants.exception_messages import \
            USER_DOES_NOT_HAVE_PERMISSION

        expected_response = USER_DOES_NOT_HAVE_PERMISSION[0]
        response_status_code = USER_DOES_NOT_HAVE_PERMISSION[1]

        # Act
        response_object = presenter.response_for_user_is_not_admin_exception()

        # Assert
        response = json.loads(response_object.content)
        assert response['http_status_code'] == StatusCode.FORBIDDEN.value
        assert response['res_status'] == response_status_code
        assert response['response'] == expected_response

    def test_raise_invalid_offset_value_exception(self, presenter):
        # Arrange
        from ib_iam.constants.exception_messages import INVALID_OFFSET_VALUE
        expected_response = INVALID_OFFSET_VALUE[0]
        response_status_code = INVALID_OFFSET_VALUE[1]

        # Act
        response_object = presenter.raise_invalid_offset_value_exception()

        # Assert
        response = json.loads(response_object.content)
        assert response['http_status_code'] == StatusCode.BAD_REQUEST.value
        assert response['res_status'] == response_status_code
        assert response['response'] == expected_response

    def test_raise_invalid_limit_value_exception(self, presenter):
        # Arrange
        from ib_iam.constants.exception_messages import INVALID_LIMIT_VALUE
        expected_response = INVALID_LIMIT_VALUE[0]
        response_status_code = INVALID_LIMIT_VALUE[1]

        # Act
        response_object = presenter.raise_invalid_limit_value_exception()

        # Assert
        response = json.loads(response_object.content)
        assert response['http_status_code'] == StatusCode.BAD_REQUEST.value
        assert response['res_status'] == response_status_code
        assert response['response'] == expected_response

    def test_raise_invalid_user_exception(self, presenter):
        # Arrange
        from ib_iam.constants.exception_messages import INVALID_USER
        expected_response = INVALID_USER[0]
        response_status_code = INVALID_USER[1]

        # Act
        response_object = presenter.raise_invalid_user()

        # Assert
        response = json.loads(response_object.content)
        assert response['http_status_code'] == StatusCode.NOT_FOUND.value
        assert response['res_status'] == response_status_code
        assert response['response'] == expected_response

    @pytest.fixture
    def complete_user_details_dto(self):
        from ib_iam.tests.common_fixtures.reset_fixture \
            import reset_sequence_for_dto_factory
        reset_sequence_for_dto_factory()
        from ib_iam.tests.factories.storage_dtos \
            import UserTeamDTOFactory, \
            UserRoleDTOFactory, UserCompanyDTOFactory
        user_ids = ["user1", "user2", "user3"]
        company_ids = ["company1", "company2", "company3"]
        user_teams = []
        user_roles = []
        for user_id in user_ids:
            user_teams.extend(
                UserTeamDTOFactory.create_batch(2, user_id=user_id)
            )
        user_company_dtos = [
            UserCompanyDTOFactory.create(
                company_id=company_id, user_id=user_id
            ) for company_id, user_id in zip(company_ids, user_ids)
        ]
        for user_id in user_ids:
            user_roles.extend(
                UserRoleDTOFactory.create_batch(2, user_id=user_id)
            )
        from ib_iam.tests.factories.adapter_dtos import UserProfileDTOFactory
        user_profile_dtos = [
            UserProfileDTOFactory.create(user_id=user_id)
            for user_id in user_ids
        ]
        from ib_iam.interactors.presenter_interfaces.dtos import \
            ListOfCompleteUsersWithRolesDTO
        complete_user_details_dto = ListOfCompleteUsersWithRolesDTO(
            users=user_profile_dtos, teams=user_teams, roles=user_roles,
            companies=user_company_dtos, total_no_of_users=len(user_ids)
        )
        return complete_user_details_dto

    def test_response_for_get_users(
            self, complete_user_details_dto, snapshot, presenter
    ):
        # Act
        response_object = presenter.response_for_get_users(
            complete_user_details_dto
        )

        # Assert
        response = json.loads(response_object.content)
        snapshot.assert_match(response, "get_users_response")