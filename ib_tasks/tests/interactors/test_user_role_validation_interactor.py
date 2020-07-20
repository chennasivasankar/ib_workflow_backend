from ib_tasks.interactors.user_role_validation_interactor import \
    UserRoleValidationInteractor


class TestUserRoleValidationInteractor:
    def test_given_all_roles_id_return_true(self, mocker):
        from ib_tasks.tests.common_fixtures.adapters.roles_service import \
            get_user_role_ids
        user_id = "user_1"
        role_ids = ["ALL_ROLES", "FIN_PAYMENT_REQUESTER", "FIN_PAYMENT_POC"]
        get_user_role_ids_mock_method = \
            get_user_role_ids(mocker)

        interactor = UserRoleValidationInteractor()

        # Act
        result = interactor.user_role_validation(user_id=user_id,
                                                 role_ids=role_ids)
        assert result is True
        get_user_role_ids_mock_method.assert_not_called()

    def test_given_valid_user_roles_return_true(self, mocker):
        from ib_tasks.tests.common_fixtures.adapters.roles_service import \
            get_user_role_ids
        user_id = "user_1"
        role_ids = ["FIN_PAYMENTS_LEVEL3_VERIFIER", "FIN_PAYMENT_REQUESTER"]
        get_user_role_ids_mock_method = \
            get_user_role_ids(mocker)

        interactor = UserRoleValidationInteractor()

        # Act
        result = interactor.user_role_validation(user_id=user_id,
                                                 role_ids=role_ids)
        assert result is True
        get_user_role_ids_mock_method.assert_called_once_with(user_id=user_id)

    def test_given_invalid_user_roles_return_false(self, mocker):
        from ib_tasks.tests.common_fixtures.adapters.roles_service import \
            get_user_role_ids
        user_id = "user_1"
        role_ids = ["FIN_PAYMENTS_LEVEL3_VERIFIER", "FIN_PAYMENT_APPROVER"]
        get_user_role_ids_mock_method = \
            get_user_role_ids(mocker)

        interactor = UserRoleValidationInteractor()

        # Act
        result = interactor.user_role_validation(user_id=user_id,
                                                 role_ids=role_ids)
        assert result is False
        get_user_role_ids_mock_method.assert_called_once_with(user_id=user_id)
