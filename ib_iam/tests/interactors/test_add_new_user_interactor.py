from unittest.mock import Mock

import pytest

from ib_iam.interactors.add_new_user_interactor import AddNewUserInteractor
from ib_iam.tests.factories.interactor_dtos import \
    AddUserDetailsDTOFactory


class TestAddNewUserIneractor:

    @pytest.fixture
    def storage_mock(self):
        from unittest import mock

        from ib_iam.interactors.storage_interfaces.user_storage_interface \
            import UserStorageInterface
        storage = mock.create_autospec(UserStorageInterface)
        return storage

    @pytest.fixture()
    def elastic_storage(self):
        from unittest import mock
        from ib_iam.interactors.storage_interfaces.elastic_storage_interface \
            import ElasticSearchStorageInterface
        storage = mock.create_autospec(ElasticSearchStorageInterface)
        return storage

    @pytest.fixture
    def presenter_mock(self):
        from unittest import mock
        from ib_iam.interactors.presenter_interfaces.add_new_user_presenter_inerface \
            import AddUserPresenterInterface
        storage = mock.create_autospec(AddUserPresenterInterface)
        return storage

    @pytest.fixture
    def send_verification_email_mock(self, mocker):
        mock = mocker.patch(
            "ib_iam.interactors.send_verify_email_link_interactor.SendVerifyEmailLinkInteractor.send_verification_email"
        )
        return mock

    @pytest.fixture
    def set_up(self):
        new_user_id = "user1"
        name = "namedurga"
        email = "sample@gmail.com"
        user_teams_ids = ["1", "2"]
        user_role_ids = ["1", "2"]
        user_company_id = "1"
        from ib_iam.tests.factories.adapter_dtos import UserProfileDTOFactory
        user_profile_dto = UserProfileDTOFactory(
            user_id=new_user_id, name=name, profile_pic_url=None, email=email,
            is_email_verified=None)
        add_user_details_dto = AddUserDetailsDTOFactory(
            name=name, email=email, team_ids=user_teams_ids,
            # role_ids=user_role_ids,
            company_id=user_company_id
        )
        return user_profile_dto, email, user_teams_ids, user_role_ids, \
               user_company_id, add_user_details_dto

    def test_create_user_when_user_is_not_admin_then_throw_exception(
            self, storage_mock, presenter_mock, elastic_storage, set_up,
    ):
        invalid_user_id = "user_1"
        add_user_details_dto = set_up[5]

        interactor = AddNewUserInteractor(
            user_storage=storage_mock, elastic_storage=elastic_storage
        )
        storage_mock.is_user_admin.return_value = False
        presenter_mock.response_for_user_is_not_admin_exception.return_value = Mock()

        interactor.add_new_user_wrapper(
            user_id=invalid_user_id,
            add_user_details_dto=add_user_details_dto,
            presenter=presenter_mock)

        storage_mock.is_user_admin.assert_called_once_with(
            user_id=invalid_user_id)
        presenter_mock.response_for_user_is_not_admin_exception.assert_called_once()

    def test_validate_name_when_contains_special_characters_and_numbers_throw_exception(
            self, storage_mock, presenter_mock, elastic_storage, set_up
    ):
        user_id = "user_1"
        invalid_name = "user@1"
        add_user_details_dto = set_up[5]
        add_user_details_dto.name = invalid_name
        interactor = AddNewUserInteractor(
            user_storage=storage_mock, elastic_storage=elastic_storage
        )
        storage_mock.is_user_admin.return_value = True
        presenter_mock \
            .response_for_name_contains_special_character_exception \
            .return_value = Mock()

        interactor.add_new_user_wrapper(
            user_id=user_id,
            add_user_details_dto=add_user_details_dto,
            presenter=presenter_mock)

        storage_mock.is_user_admin.assert_called_once_with(user_id=user_id)
        presenter_mock. \
            response_for_name_contains_special_character_exception. \
            assert_called_once()

    def test_validate_name_returns_should_contain_minimum_5_characters_exception(
            self, storage_mock, presenter_mock, elastic_storage, set_up
    ):
        # Arrange
        user_id = "user_1"
        invalid_name = "user"
        add_user_details_dto = set_up[5]
        add_user_details_dto.name = invalid_name
        interactor = AddNewUserInteractor(
            user_storage=storage_mock, elastic_storage=elastic_storage
        )
        storage_mock.is_user_admin.return_value = True
        presenter_mock.response_for_invalid_name_length_exception \
            .return_value = Mock()

        # Act
        interactor.add_new_user_wrapper(
            user_id=user_id,
            add_user_details_dto=add_user_details_dto,
            presenter=presenter_mock)

        # Assert
        storage_mock.is_user_admin.assert_called_once_with(user_id=user_id)
        presenter_mock.response_for_invalid_name_length_exception. \
            assert_called_once()

    def test_validate_email_and_throw_exception(
            self, storage_mock, presenter_mock, elastic_storage, set_up
    ):
        # Arrange
        user_id = "user1"
        invalid_email = "123"
        add_user_details_dto = set_up[5]
        add_user_details_dto.email = invalid_email
        interactor = AddNewUserInteractor(
            user_storage=storage_mock, elastic_storage=elastic_storage
        )
        storage_mock.is_user_admin.return_value = True
        presenter_mock.response_for_invalid_email_exception.return_value = Mock()

        # Act
        interactor.add_new_user_wrapper(
            user_id=user_id,
            add_user_details_dto=add_user_details_dto,
            presenter=presenter_mock
        )

        # Assert
        storage_mock.is_user_admin.assert_called_once_with(user_id=user_id)
        presenter_mock.response_for_invalid_email_exception.assert_called_once()

    # def test_validate_roles_and_throw_exception(
    #         self, storage_mock, presenter_mock, elastic_storage, set_up):
    #     # Arrange
    #     user_id = "user_1"
    #     add_user_details_dto = set_up[5]
    #     interactor = AddNewUserInteractor(
    #         user_storage=storage_mock, elastic_storage=elastic_storage
    #     )
    #     storage_mock.is_user_admin.return_value = True
    #     storage_mock.check_are_valid_role_ids.return_value = False
    #     presenter_mock.response_for_invalid_role_ids_exception.return_value = Mock()
    #
    #     # Act
    #     interactor.add_new_user_wrapper(
    #         user_id=user_id,
    #         add_user_details_dto=add_user_details_dto,
    #         presenter=presenter_mock)
    #
    #     # Assert
    #     storage_mock.is_user_admin.assert_called_once_with(user_id=user_id)
    #     storage_mock.check_are_valid_role_ids.assert_called_once_with(
    #         role_ids=add_user_details_dto.role_ids)
    #     presenter_mock.response_for_invalid_role_ids_exception.assert_called_once()

    def test_validate_teams_and_throw_exception(
            self, storage_mock, presenter_mock, elastic_storage, set_up
    ):
        # Arrange
        user_id = "user_1"
        add_user_details_dto = set_up[5]
        interactor = AddNewUserInteractor(
            user_storage=storage_mock, elastic_storage=elastic_storage
        )
        storage_mock.is_user_admin.return_value = True
        storage_mock.check_are_valid_team_ids.return_value = False
        # storage_mock.check_are_valid_role_ids.return_value = True
        presenter_mock.response_for_invalid_team_ids_exception.return_value = Mock()

        # Act
        interactor.add_new_user_wrapper(
            user_id=user_id,
            add_user_details_dto=add_user_details_dto,
            presenter=presenter_mock)

        # Assert
        storage_mock.check_are_valid_team_ids.assert_called_once_with(
            team_ids=add_user_details_dto.team_ids)
        storage_mock.is_user_admin.assert_called_once_with(user_id=user_id)
        # storage_mock.check_are_valid_role_ids.assert_called_once_with(
        #     role_ids=add_user_details_dto.role_ids)
        presenter_mock.response_for_invalid_team_ids_exception.assert_called_once()

    def test_validate_company_id_and_throw_exception(
            self, storage_mock, presenter_mock, elastic_storage, set_up
    ):
        # Arrange
        user_id = "user_1"
        add_user_details_dto = set_up[5]
        interactor = AddNewUserInteractor(
            user_storage=storage_mock, elastic_storage=elastic_storage
        )
        storage_mock.is_user_admin.return_value = True
        storage_mock.check_are_valid_team_ids.return_value = True
        # storage_mock.check_are_valid_role_ids.return_value = True
        storage_mock.check_is_exists_company_id.return_value = False
        presenter_mock.response_for_invalid_company_ids_exception.return_value = Mock()

        # Act
        interactor.add_new_user_wrapper(
            user_id=user_id,
            add_user_details_dto=add_user_details_dto,
            presenter=presenter_mock)

        # Assert
        storage_mock.check_are_valid_team_ids.assert_called_once_with(
            team_ids=add_user_details_dto.team_ids)
        storage_mock.is_user_admin.assert_called_once_with(user_id=user_id)
        # storage_mock.check_are_valid_role_ids.assert_called_once_with(
        #     role_ids=add_user_details_dto.role_ids)
        storage_mock.check_is_exists_company_id.assert_called_once_with(
            company_id=add_user_details_dto.company_id)
        presenter_mock.response_for_invalid_company_ids_exception.assert_called_once()

    def test_create_user_account_with_email_already_exist_throws_exception(
            self, storage_mock, presenter_mock, mocker, elastic_storage,
            set_up
    ):
        # Arrange
        user_id = "user_1"
        add_user_details_dto = set_up[5]
        interactor = AddNewUserInteractor(
            user_storage=storage_mock, elastic_storage=elastic_storage
        )
        storage_mock.is_user_admin.return_value = True
        presenter_mock.response_for_user_account_already_exists_exception. \
            return_value = Mock()
        from ib_iam.tests.common_fixtures.adapters.user_service \
            import email_exist_adapter_mock
        adapter_mock = email_exist_adapter_mock(mocker=mocker)
        # Act
        interactor.add_new_user_wrapper(
            user_id=user_id,
            add_user_details_dto=add_user_details_dto,
            presenter=presenter_mock)

        # Assert
        storage_mock.is_user_admin.assert_called_once_with(user_id=user_id)
        adapter_mock.assert_called_once_with(email=add_user_details_dto.email)
        presenter_mock.response_for_user_account_already_exists_exception. \
            assert_called_once()

    # def test_get_role_objs_ids_returns_ids_of_role(
    #         self, storage_mock, presenter_mock, mocker, elastic_storage,
    #         set_up):
    #     # Arrange
    #     user_id = "user_1"
    #     new_user_id = "user1"
    #     user_profile_dto = set_up[0]
    #     add_user_details_dto = set_up[5]
    #     ids_of_role_objs = [
    #         "ef6d1fc6-ac3f-4d2d-a983-752c992e8331",
    #         "ef6d1fc6-ac3f-4d2d-a983-752c992e8332"
    #     ]
    #     elastic_user_id = "elastic_user_1"
    #     interactor = AddNewUserInteractor(
    #         user_storage=storage_mock, elastic_storage=elastic_storage
    #     )
    #     storage_mock.is_user_admin.return_value = True
    #     storage_mock.check_are_valid_team_ids.return_value = True
    #     # storage_mock.check_are_valid_role_ids.return_value = True
    #     storage_mock.check_is_exists_company_id.return_value = True
    #     elastic_storage.create_elastic_user.return_value = elastic_user_id
    #     storage_mock.get_role_objs_ids.return_value = ids_of_role_objs
    #     from ib_iam.tests.common_fixtures.adapters.user_service \
    #         import create_user_account_adapter_mock, \
    #         create_user_profile_adapter_mock
    #     user_account_adapter_mock = \
    #         create_user_account_adapter_mock(mocker=mocker)
    #     user_profile_adapter_mock = \
    #         create_user_profile_adapter_mock(mocker=mocker)
    #     user_account_adapter_mock.return_value = new_user_id
    #     user_profile_adapter_mock.return_value = user_profile_dto
    #
    #     # Act
    #     interactor.add_new_user_wrapper(
    #         user_id=user_id,
    #         add_user_details_dto=add_user_details_dto,
    #         presenter=presenter_mock)
    #
    #     # Assert
    #     elastic_storage.create_elastic_user.assert_called_once_with(
    #         user_id=new_user_id, name=add_user_details_dto.name)
    #     elastic_storage.create_elastic_user_intermediary.assert_called_once_with(
    #         elastic_user_id=elastic_user_id, user_id=new_user_id)
    #     # storage_mock.get_role_objs_ids.assert_called_once_with(
    #     #     role_ids=add_user_details_dto.role_ids)
    #     user_account_adapter_mock.assert_called_once_with(
    #         email=add_user_details_dto.email)
    #     user_profile_adapter_mock.assert_called_once_with(
    #         user_id=new_user_id, user_profile_dto=user_profile_dto)

    def test_create_ib_user_with_given_valid_details(
            self, storage_mock, presenter_mock, mocker, elastic_storage,
            set_up, send_verification_email_mock
    ):
        # Arrange
        user_id = "user_1"
        new_user_id = "user1"
        user_profile_dto = set_up[0]
        add_user_details_dto = set_up[5]
        elastic_user_id = "elastic_user_1"
        interactor = AddNewUserInteractor(
            user_storage=storage_mock, elastic_storage=elastic_storage
        )
        storage_mock.is_user_admin.return_value = True
        elastic_storage.create_elastic_user.return_value = elastic_user_id
        from ib_iam.tests.common_fixtures.adapters.auth_service_adapter_mocks import \
            update_is_email_verified_value_mock
        update_is_email_verified_value_mock = update_is_email_verified_value_mock(
            mocker=mocker)
        update_is_email_verified_value_mock.return_value = None
        from ib_iam.tests.common_fixtures.adapters.user_service \
            import create_user_account_adapter_mock, \
            create_user_profile_adapter_mock
        user_account_adapter_mock = \
            create_user_account_adapter_mock(mocker=mocker)
        user_account_adapter_mock.return_value = new_user_id
        user_profile_adapter_mock = \
            create_user_profile_adapter_mock(mocker=mocker)
        user_profile_adapter_mock.return_value = user_profile_dto
        send_verification_email_mock.return_value = None

        # Act
        interactor.add_new_user_wrapper(
            user_id=user_id,
            add_user_details_dto=add_user_details_dto,
            presenter=presenter_mock)

        # Assert
        user_account_adapter_mock.assert_called_once_with(
            email=add_user_details_dto.email)
        user_profile_adapter_mock.assert_called_once_with(
            user_id=new_user_id, user_profile_dto=user_profile_dto)
        update_is_email_verified_value_mock.assert_called_once_with(
            user_id=new_user_id, is_email_verified=False)

    def test_add_new_user_when_company_is_none_adds_user_successfully(
            self, storage_mock, presenter_mock, mocker, elastic_storage,
            set_up, send_verification_email_mock
    ):
        # Arrange
        user_id = "user_1"
        new_user_id = "user1"
        user_profile_dto = set_up[0]
        add_user_details_dto = set_up[5]
        add_user_details_dto.company_id = None
        elastic_user_id = "elastic_user_1"
        interactor = AddNewUserInteractor(
            user_storage=storage_mock, elastic_storage=elastic_storage
        )
        storage_mock.is_user_admin.return_value = True
        elastic_storage.create_elastic_user.return_value = elastic_user_id
        from ib_iam.tests.common_fixtures.adapters.user_service \
            import create_user_account_adapter_mock, \
            create_user_profile_adapter_mock
        user_account_adapter_mock = \
            create_user_account_adapter_mock(mocker=mocker)
        user_account_adapter_mock.return_value = new_user_id
        user_profile_adapter_mock = \
            create_user_profile_adapter_mock(mocker=mocker)
        user_profile_adapter_mock.return_value = user_profile_dto
        from ib_iam.tests.common_fixtures.adapters.auth_service_adapter_mocks import \
            update_is_email_verified_value_mock
        update_is_email_verified_value_mock = update_is_email_verified_value_mock(
            mocker=mocker)
        update_is_email_verified_value_mock.return_value = None
        send_verification_email_mock.return_value = None

        # Act
        interactor.add_new_user_wrapper(
            user_id=user_id,
            add_user_details_dto=add_user_details_dto,
            presenter=presenter_mock)

        # Assert
        user_account_adapter_mock.assert_called_once_with(
            email=add_user_details_dto.email)
        user_profile_adapter_mock.assert_called_once_with(
            user_id=new_user_id, user_profile_dto=user_profile_dto)
        storage_mock.check_are_valid_team_ids.assert_called_once_with(
            team_ids=add_user_details_dto.team_ids)
        storage_mock.is_user_admin.assert_called_once_with(user_id=user_id)
        # storage_mock.check_are_valid_role_ids.assert_called_once_with(
        #     role_ids=add_user_details_dto.role_ids)
        elastic_storage.create_elastic_user.assert_called_once_with(
            user_id=new_user_id, name=add_user_details_dto.name,
            email=add_user_details_dto.email
        )
        elastic_storage.create_elastic_user_intermediary.assert_called_once_with(
            elastic_user_id=elastic_user_id, user_id=new_user_id)

    def test_add_new_user(
            self, storage_mock, presenter_mock, mocker, elastic_storage,
            set_up, send_verification_email_mock
    ):
        # Arrange
        user_id = "user_1"
        new_user_id = "user1"
        user_profile_dto = set_up[0]
        add_user_details_dto = set_up[5]
        elastic_user_id = "elastic_user_1"
        interactor = AddNewUserInteractor(
            user_storage=storage_mock, elastic_storage=elastic_storage
        )
        storage_mock.is_user_admin.return_value = True
        elastic_storage.create_elastic_user.return_value = elastic_user_id
        from ib_iam.tests.common_fixtures.adapters.user_service \
            import create_user_account_adapter_mock, \
            create_user_profile_adapter_mock
        user_account_adapter_mock = \
            create_user_account_adapter_mock(mocker=mocker)
        user_account_adapter_mock.return_value = new_user_id
        user_profile_adapter_mock = \
            create_user_profile_adapter_mock(mocker=mocker)
        user_profile_adapter_mock.return_value = user_profile_dto
        from ib_iam.tests.common_fixtures.adapters.auth_service_adapter_mocks import \
            update_is_email_verified_value_mock
        update_is_email_verified_value_mock = update_is_email_verified_value_mock(
            mocker=mocker)
        update_is_email_verified_value_mock.return_value = None
        send_verification_email_mock.return_value = None

        # Act
        interactor.add_new_user_wrapper(
            user_id=user_id,
            add_user_details_dto=add_user_details_dto,
            presenter=presenter_mock)

        # Assert
        user_account_adapter_mock.assert_called_once_with(
            email=add_user_details_dto.email)
        user_profile_adapter_mock.assert_called_once_with(
            user_id=new_user_id, user_profile_dto=user_profile_dto)
        storage_mock.check_are_valid_team_ids.assert_called_once_with(
            team_ids=add_user_details_dto.team_ids)
        storage_mock.is_user_admin.assert_called_once_with(user_id=user_id)
        # storage_mock.check_are_valid_role_ids.assert_called_once_with(
        #     role_ids=add_user_details_dto.role_ids)
        storage_mock.check_is_exists_company_id.assert_called_once_with(
            company_id=add_user_details_dto.company_id)
        elastic_storage.create_elastic_user.assert_called_once_with(
            user_id=new_user_id, name=add_user_details_dto.name,
            email=add_user_details_dto.email
        )
        elastic_storage.create_elastic_user_intermediary.assert_called_once_with(
            elastic_user_id=elastic_user_id, user_id=new_user_id)
