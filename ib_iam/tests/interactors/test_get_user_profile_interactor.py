import pytest

from ib_iam.tests.factories.adapter_dtos import UserProfileDTOFactory
from ib_iam.tests.factories.interactor_dtos import CompleteUserProfileDTOFactory
from ib_iam.tests.factories.storage_dtos import UserDTOFactory


class TestGetUserProfileInteractor:

    @pytest.fixture
    def expected_company_dto(self):
        from ib_iam.tests.factories.storage_dtos import CompanyDTOFactory
        CompanyDTOFactory.reset_sequence(1, force=True)
        company_dto = CompanyDTOFactory(company_id="1")
        return company_dto

    @pytest.fixture
    def expected_company_employee_ids_dto(self):
        from ib_iam.tests.factories.storage_dtos import \
            CompanyIdWithEmployeeIdsDTOFactory
        CompanyIdWithEmployeeIdsDTOFactory.reset_sequence(1)
        expected_company_id_with_employee_id_dto = \
            CompanyIdWithEmployeeIdsDTOFactory(company_id="1",
                                               employee_ids=["1", "3"])
        return expected_company_id_with_employee_id_dto

    @pytest.fixture
    def expected_team_dtos(self):
        from ib_iam.tests.factories.storage_dtos import TeamDTOFactory
        TeamDTOFactory.reset_sequence(1)
        team_dtos = [TeamDTOFactory(team_id="1")]
        return team_dtos

    @pytest.fixture()
    def expected_team_user_ids_dtos(self):
        from ib_iam.tests.factories.storage_dtos import TeamUserIdsDTOFactory
        team_user_ids_dtos = [
            TeamUserIdsDTOFactory(team_id="1", user_ids=["1", "2"])
        ]
        return team_user_ids_dtos

    @pytest.fixture
    def expected_user_dtos(self):
        from ib_iam.tests.factories.adapter_dtos import UserProfileDTOFactory
        UserProfileDTOFactory.reset_sequence(1)
        user_profile_dtos = [
            UserProfileDTOFactory() for _ in range(3)
        ]
        return user_profile_dtos

    @pytest.fixture()
    def expected_role_dtos(self):
        user_id = "1"
        from ib_iam.tests.factories.storage_dtos import UserRoleDTOFactory
        role_dtos = [UserRoleDTOFactory.create_batch(size=4, user_id=user_id)]
        return role_dtos

    @pytest.fixture()
    def user_with_extra_details_dto(
            self, expected_company_dto, expected_company_employee_ids_dto,
            expected_role_dtos, expected_team_dtos,
            expected_team_user_ids_dtos, expected_user_dtos):
        user_id = "1"
        from ib_iam.interactors.presenter_interfaces.auth_presenter_interface import \
            UserWithExtraDetailsDTO
        CompleteUserProfileDTOFactory.reset_sequence(1)
        user_profile_dto = CompleteUserProfileDTOFactory(
            user_id=user_id, is_admin=True, cover_page_url="url1")
        expected_response_dto = UserWithExtraDetailsDTO(
            user_profile_dto=user_profile_dto,
            company_dto=expected_company_dto,
            team_dtos=expected_team_dtos,
            team_user_ids_dto=expected_team_user_ids_dtos,
            company_id_with_employee_ids_dto=expected_company_employee_ids_dto,
            user_dtos=expected_user_dtos,
            role_dtos=expected_role_dtos
        )
        return expected_response_dto

    @pytest.fixture()
    def presenter_mock(self):
        from ib_iam.interactors.presenter_interfaces.auth_presenter_interface import \
            GetUserProfilePresenterInterface
        from unittest.mock import create_autospec
        presenter = create_autospec(GetUserProfilePresenterInterface)
        return presenter

    @pytest.fixture()
    def storage_mock(self):
        from ib_iam.interactors.storage_interfaces.user_storage_interface import \
            UserStorageInterface
        from unittest.mock import create_autospec
        storage = create_autospec(UserStorageInterface)
        return storage

    def test_invalid_user_raise_exception(
            self, mocker, presenter_mock, storage_mock):
        # Arrange
        user_id = ""
        from unittest.mock import Mock
        expected_presenter_invalid_user_id_mock = Mock()

        from ib_iam.tests.common_fixtures.adapters.user_service import \
            prepare_get_user_profile_dto_mock
        get_user_profile_dto_mock = prepare_get_user_profile_dto_mock(mocker)
        from ib_iam.exceptions.custom_exceptions import InvalidUserId
        get_user_profile_dto_mock.side_effect = InvalidUserId

        presenter_mock.raise_exception_for_invalid_user_id.return_value \
            = expected_presenter_invalid_user_id_mock

        from ib_iam.interactors.get_user_profile_interactor import \
            GetUserProfileInteractor
        interactor = GetUserProfileInteractor(user_storage=storage_mock)

        # Act
        response = interactor.get_user_profile_wrapper(
            user_id=user_id, presenter=presenter_mock
        )

        # Assert
        assert response == expected_presenter_invalid_user_id_mock
        presenter_mock.raise_exception_for_invalid_user_id.assert_called_once()

    def test_with_user_id_which_is_does_not_exist_raise_exception(
            self, mocker, presenter_mock, storage_mock
    ):
        # Arrange
        user_id = "eca1a0c1-b9ef-4e59-b415-60a28ef17b10"
        from unittest.mock import Mock
        expected_presenter_user_account_does_not_exist_mock = Mock()

        from ib_iam.tests.common_fixtures.adapters.user_service import \
            prepare_get_user_profile_dto_mock
        get_user_profile_dto_mock = prepare_get_user_profile_dto_mock(mocker)
        from ib_iam.adapters.user_service import UserAccountDoesNotExist
        get_user_profile_dto_mock.side_effect = UserAccountDoesNotExist

        presenter_mock.raise_exception_for_user_account_does_not_exist \
            .return_value = expected_presenter_user_account_does_not_exist_mock

        from ib_iam.interactors.get_user_profile_interactor import \
            GetUserProfileInteractor
        interactor = GetUserProfileInteractor(
            user_storage=storage_mock
        )

        # Act
        response = interactor.get_user_profile_wrapper(
            user_id=user_id, presenter=presenter_mock
        )

        # Assert
        assert response == expected_presenter_user_account_does_not_exist_mock
        presenter_mock.raise_exception_for_user_account_does_not_exist. \
            assert_called_once()

    def test_with_valid_user_id_return_user_profile_details_as_response(
            self, mocker, storage_mock, presenter_mock, expected_company_dto,
            expected_company_employee_ids_dto, expected_team_dtos,
            expected_team_user_ids_dtos, expected_user_dtos,
            expected_role_dtos, user_with_extra_details_dto
    ):
        # Arrange
        user_id = "1"
        from unittest.mock import Mock
        UserProfileDTOFactory.reset_sequence(1)
        UserDTOFactory.reset_sequence(1)
        user_profile_dto = UserProfileDTOFactory(user_id=user_id)
        user_detail_dto = UserDTOFactory(user_id=user_id)
        from ib_iam.tests.common_fixtures.adapters.user_service import \
            prepare_get_user_profile_dto_mock
        get_user_profile_dto_mock = prepare_get_user_profile_dto_mock(mocker)
        get_user_profile_dto_mock.return_value = user_profile_dto
        storage_mock.get_user_details.return_value = user_detail_dto
        storage_mock.get_user_related_team_dtos \
            .return_value = expected_team_dtos
        storage_mock.get_team_user_ids_dtos \
            .return_value = expected_team_user_ids_dtos
        storage_mock.get_role_details_of_users_bulk \
            .return_value = expected_role_dtos
        storage_mock.get_user_related_company_dto \
            .return_value = expected_company_dto
        storage_mock.get_company_employee_ids_dto \
            .return_value = expected_company_employee_ids_dto
        from ib_iam.tests.common_fixtures.adapters.user_service_mocks import \
            prepare_user_profile_dtos_mock
        user_profile_dtos_mock = prepare_user_profile_dtos_mock(mocker)
        user_profile_dtos_mock.return_value = expected_user_dtos
        presenter_mock.prepare_response_for_get_user_profile \
            .return_value = Mock()

        from ib_iam.interactors.get_user_profile_interactor import \
            GetUserProfileInteractor
        interactor = GetUserProfileInteractor(user_storage=storage_mock)

        # Act
        interactor.get_user_profile_wrapper(user_id=user_id,
                                            presenter=presenter_mock)

        # Assert
        storage_mock.get_user_details.assert_called_once_with(user_id=user_id)
        storage_mock.get_user_related_team_dtos \
            .assert_called_once_with(user_id=user_id)
        storage_mock.get_team_user_ids_dtos \
            .assert_called_once_with(team_ids=["1"])
        storage_mock.get_role_details_of_users_bulk \
            .assert_called_once_with(user_ids=[user_id])
        storage_mock.get_user_related_company_dto \
            .assert_called_once_with(user_id=user_id)
        storage_mock.get_company_employee_ids_dto \
            .assert_called_once_with(company_id="1")
        presenter_mock.prepare_response_for_get_user_profile. \
            assert_called_once_with(
            user_with_extra_details_dto=user_with_extra_details_dto)
