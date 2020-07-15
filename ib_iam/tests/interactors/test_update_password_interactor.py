class TestUpdateUserPasswordInteractor:
    def test_with_weak_password_raise_exception(self):
        # Arrange
        token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
        password = "sankar"

        from ib_iam.interactors.update_user_password_interactor import \
            UpdateUserPasswordInteractor
        interactor = UpdateUserPasswordInteractor()

        # Act
        response = interactor.update_user_password_wrapper(
            token=token, password=password
        )

        # Assert