import pytest


class TestGetUserDetailsForGivenRoleIds:
    @pytest.fixture
    def user_storage_mock(self):
        from ib_iam.interactors.storage_interfaces.user_storage_interface import \
            UserStorageInterface
        from unittest.mock import create_autospec
        user_storage_mock = create_autospec(UserStorageInterface)
        return user_storage_mock

    def test_given_valid_details_then_return_user_details(
            self, user_storage_mock, mocker):
        project_id = "FA"
        role_ids = ["1", "2", "3"]
        user_ids = ["1", "2", "3"]
        from ib_iam.tests.factories.adapter_dtos import UserProfileDTOFactory
        user_profile_dtos = [UserProfileDTOFactory(user_id=user_id) for user_id
                             in user_ids]
        from ib_iam.tests.common_fixtures.adapters.user_service_mocks import \
            prepare_user_profile_dtos_mock
        get_user_profile_mock = prepare_user_profile_dtos_mock(mocker)

        get_user_profile_mock.return_value = user_profile_dtos
        user_storage_mock.get_valid_role_ids.return_value = role_ids
        user_storage_mock.get_user_ids.return_value = user_ids
        interactor = self.interactor_init(user_storage_mock=user_storage_mock)

        interactor.get_user_details_for_given_role_ids(
            role_ids=role_ids, project_id=project_id)

        user_storage_mock.get_valid_role_ids.assert_called_once_with(
            role_ids=role_ids)
        user_storage_mock.get_user_ids.assert_called_once_with(
            role_ids=role_ids)
        get_user_profile_mock.assert_called_once_with(user_ids=user_ids)

    def test_given_invalid_role_ids_then_raise_exception(
            self, user_storage_mock):
        project_id = "FA"
        invalid_role_ids = ["1", "2", "3"]
        interactor = self.interactor_init(user_storage_mock=user_storage_mock)
        user_storage_mock.get_valid_role_ids.return_value = []

        from ib_iam.exceptions.custom_exceptions import RoleIdsAreInvalid
        with pytest.raises(RoleIdsAreInvalid):
            interactor.get_user_details_for_given_role_ids(
                role_ids=invalid_role_ids, project_id=project_id)
        user_storage_mock.get_valid_role_ids.assert_called_once_with(
            role_ids=invalid_role_ids)

    def test_given_valid_role_ids_with_contains_all_role_id_then_return_all_users(
            self, user_storage_mock, mocker):
        project_id = "FA"
        role_ids = ["1", "2", "ALL_ROLES"]
        user_ids = ["1", "2", "3", "4"]
        from ib_iam.tests.factories.adapter_dtos import UserProfileDTOFactory
        user_profile_dtos = [UserProfileDTOFactory(user_id=user_id) for user_id
                             in user_ids]
        from ib_iam.tests.common_fixtures.adapters.user_service_mocks import \
            prepare_user_profile_dtos_mock
        get_user_profile_mock = prepare_user_profile_dtos_mock(mocker)

        get_user_profile_mock.return_value = user_profile_dtos
        user_storage_mock.get_user_ids_for_given_project.return_value = user_ids
        interactor = self.interactor_init(user_storage_mock=user_storage_mock)

        interactor.get_user_details_for_given_role_ids(
            role_ids=role_ids, project_id=project_id)

        user_storage_mock.get_user_ids_for_given_project.assert_called_once_with(
            project_id=project_id)
        get_user_profile_mock.assert_called_once_with(user_ids=user_ids)

    @staticmethod
    def interactor_init(user_storage_mock):
        from ib_iam.interactors.get_users_list_interactor import \
            GetListOfUsersInteractor
        interactor = GetListOfUsersInteractor(user_storage=user_storage_mock)
        return interactor

    # TODO check the project id is invalid or not test case
