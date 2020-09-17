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
        response_object = presenter.response_for_invalid_user_id_exception()

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
            presenter.response_for_user_account_does_not_exist_exception()

        # Assert
        response_data = json.loads(response_object.content)

        assert response_data["response"] == expected_response
        assert response_data["http_status_code"] == expected_http_status_code
        assert response_data["res_status"] == expected_res_status

    def test_prepare_response_for_user_profile_dto(
            self, presenter, user_dtos, user_role_dtos, company_dto,
            company_employee_ids_dtos, team_dtos, team_user_ids_dtos,
            snapshot):
        # Arrange
        user_ids = ['eca1a0c1-b9ef-4e59-b415-60a28ef17b10',
                    '4b8fb6eb-fa7d-47c1-8726-cd917901104e',
                    '548a803c-7b48-47ba-a700-24f2ea0d1280']
        from ib_iam.interactors.presenter_interfaces.dtos \
            import UserWithExtraDetailsDTO
        from ib_iam.tests.factories.interactor_dtos import \
            CompleteUserProfileDTOFactory
        CompleteUserProfileDTOFactory.reset_sequence(1)
        user_profile_dto = CompleteUserProfileDTOFactory(
            user_id=user_ids[0], is_admin=False)
        user_with_extra_details_dto = \
            UserWithExtraDetailsDTO(
                user_profile_dto=user_profile_dto,
                company_dto=company_dto,
                team_dtos=team_dtos,
                team_user_ids_dto=team_user_ids_dtos,
                user_dtos=user_dtos,
                company_id_with_employee_ids_dto=company_employee_ids_dtos,
                role_dtos=user_role_dtos
            )

        # Act
        response_object = presenter.response_for_get_user_profile(
            user_with_extra_details_dto=user_with_extra_details_dto)

        # Assert
        response_data = json.loads(response_object.content)
        snapshot.assert_match(response_data, "get_user_profile_response")

    @pytest.fixture
    def user_dtos(self):
        user_ids = ['eca1a0c1-b9ef-4e59-b415-60a28ef17b10',
                    '4b8fb6eb-fa7d-47c1-8726-cd917901104e',
                    '548a803c-7b48-47ba-a700-24f2ea0d1280']
        from ib_iam.tests.factories.adapter_dtos import UserProfileDTOFactory
        UserProfileDTOFactory.reset_sequence(1)
        user_dtos = [UserProfileDTOFactory(user_id=user_id)
                     for user_id in user_ids]
        return user_dtos

    @pytest.fixture
    def user_role_dtos(self):
        user_id = 'eca1a0c1-b9ef-4e59-b415-60a28ef17b10'
        from ib_iam.tests.factories.storage_dtos import UserRoleDTOFactory
        UserRoleDTOFactory.reset_sequence(1)
        role_dtos = UserRoleDTOFactory.create_batch(2, user_id=user_id)
        return role_dtos

    @pytest.fixture
    def team_dtos(self):
        team_id = '2bdb417e-4632-419a-8ddd-085ea272c6eb'
        from ib_iam.tests.factories.storage_dtos import TeamDTOFactory
        TeamDTOFactory.reset_sequence(1)
        team_dtos = [TeamDTOFactory(team_id=team_id)]
        return team_dtos

    @pytest.fixture
    def team_user_ids_dtos(self):
        team_id = '2bdb417e-4632-419a-8ddd-085ea272c6eb'
        user_ids = ['eca1a0c1-b9ef-4e59-b415-60a28ef17b10',
                    '4b8fb6eb-fa7d-47c1-8726-cd917901104e']
        from ib_iam.tests.factories.storage_dtos import TeamUserIdsDTOFactory
        TeamUserIdsDTOFactory.reset_sequence(1)
        team_user_ids_dtos = [TeamUserIdsDTOFactory(team_id=team_id,
                                                    user_ids=user_ids)]
        return team_user_ids_dtos

    @pytest.fixture
    def company_dto(self):
        company_id = 'f2c02d98-f311-4ab2-8673-3daa00757002'
        from ib_iam.tests.factories.storage_dtos import CompanyDTOFactory
        CompanyDTOFactory.reset_sequence(1, force=True)
        company_dto = CompanyDTOFactory(company_id=company_id)
        return company_dto

    @pytest.fixture
    def company_employee_ids_dtos(self):
        company_id = 'f2c02d98-f311-4ab2-8673-3daa00757002'
        user_ids = ['eca1a0c1-b9ef-4e59-b415-60a28ef17b10',
                    '548a803c-7b48-47ba-a700-24f2ea0d1280']
        from ib_iam.tests.factories.storage_dtos import \
            CompanyIdWithEmployeeIdsDTOFactory
        CompanyIdWithEmployeeIdsDTOFactory.reset_sequence(1)
        company_id_with_employee_ids_dto = CompanyIdWithEmployeeIdsDTOFactory(
            company_id=company_id, employee_ids=user_ids)
        return company_id_with_employee_ids_dto
