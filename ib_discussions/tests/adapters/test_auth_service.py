class TestAuthService:

    def prepare_get_user_profile_dtos_mock(self, mocker):
        mock = mocker.patch(
            "ib_users.interfaces.service_interface.ServiceInterface.get_user_profile_bulk"
        )

    def test_with_invalid_user_id_raise_exception(self, mocker):
        # Arrange
