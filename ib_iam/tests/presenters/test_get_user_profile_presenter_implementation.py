import json

import pytest


class TestGetUserProfilePresenterImplementation:

    @pytest.fixture()
    def presenter(self):
        from ib_iam.presenters.get_user_profile_presenter_implementation \
            import GetUserProfilePresenterImplementation
        presenter = GetUserProfilePresenterImplementation()
        return presenter

    def test_raise_exception_for_invalid_user_id(self, presenter):
        # Arrange
        from ib_iam.presenters.get_user_profile_presenter_implementation \
            import INVALID_USER_ID
        expected_response = INVALID_USER_ID[0]
        from ib_iam.constants.enums import StatusCode
        expected_http_status_code = StatusCode.BAD_REQUEST.value
        expected_res_status = INVALID_USER_ID[1]

        # Act
        response_object = presenter.raise_exception_for_invalid_user_id()

        # Assert
        response_data = json.loads(response_object.content)

        assert response_data["response"] == expected_response
        assert response_data["http_status_code"] == expected_http_status_code
        assert response_data["res_status"] == expected_res_status

    def test_raise_exception_for_user_account_does_not_exist(self, presenter):
        # Arrange
        from ib_iam.presenters.get_user_profile_presenter_implementation \
            import USER_ACCOUNT_DOES_NOT_EXIST
        expected_response = USER_ACCOUNT_DOES_NOT_EXIST[0]
        from ib_iam.constants.enums import StatusCode
        expected_http_status_code = StatusCode.NOT_FOUND.value
        expected_res_status = USER_ACCOUNT_DOES_NOT_EXIST[1]

        # Act
        response_object = \
            presenter.raise_exception_for_user_account_does_not_exist()

        # Assert
        response_data = json.loads(response_object.content)

        assert response_data["response"] == expected_response
        assert response_data["http_status_code"] == expected_http_status_code
        assert response_data["res_status"] == expected_res_status

    def test_prepare_response_for_user_profile_dto(
            self, presenter, snapshot):
        # Arrange
        user_ids = ['eca1a0c1-b9ef-4e59-b415-60a28ef17b10',
                    '4b8fb6eb-fa7d-47c1-8726-cd917901104e',
                    '548a803c-7b48-47ba-a700-24f2ea0d1280', ]
        company_id = 'f2c02d98-f311-4ab2-8673-3daa00757002'
        team_id = '2bdb417e-4632-419a-8ddd-085ea272c6eb'
        from ib_iam.tests.factories.adapter_dtos import UserProfileDTOFactory
        from ib_iam.interactors.presenter_interfaces.auth_presenter_interface \
            import UserProfileWithTeamsAndCompanyAndTheirUsersDTO
        from ib_iam.tests.factories.storage_dtos import (
            CompanyDTOFactory, TeamDTOFactory, TeamUserIdsDTOFactory,
            CompanyIdWithEmployeeIdsDTOFactory)
        UserProfileDTOFactory.reset_sequence(1)
        TeamDTOFactory.reset_sequence(1)
        CompanyDTOFactory.reset_sequence(1, force=True)
        user_profile_dto = UserProfileDTOFactory(user_id=user_ids[0])
        UserProfileDTOFactory.reset_sequence(1)
        user_dtos = [UserProfileDTOFactory(user_id=user_id)
                     for user_id in user_ids]
        company_dto = CompanyDTOFactory(company_id=company_id)
        team_dtos = [TeamDTOFactory(team_id=team_id)]
        team_user_ids_dtos = [TeamUserIdsDTOFactory(
            team_id=team_id, user_ids=[user_ids[0], user_ids[1]])]

        company_id_with_employee_ids_dto = CompanyIdWithEmployeeIdsDTOFactory(
            company_id=company_id, employee_ids=[user_ids[0], user_ids[2]])
        user_profile_response_dto = \
            UserProfileWithTeamsAndCompanyAndTheirUsersDTO(
                user_profile_dto=user_profile_dto,
                company_dto=company_dto,
                team_dtos=team_dtos,
                team_user_ids_dto=team_user_ids_dtos,
                user_dtos=user_dtos,
                company_id_with_employee_ids_dto=
                company_id_with_employee_ids_dto
            )

        # Act
        response_object = presenter.prepare_response_for_get_user_profile(
            user_profile_response_dto=user_profile_response_dto)

        # Assert
        response_data = json.loads(response_object.content)
        snapshot.assert_match(response_data, "get_user_profile_response")
