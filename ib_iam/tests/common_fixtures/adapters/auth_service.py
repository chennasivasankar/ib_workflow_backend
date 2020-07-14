from ib_iam.interactors.user_login_interactor import \
    EmailAndPasswordDTO

def prepare_get_user_id_mock(mocker, email_and_password_dto: EmailAndPasswordDTO):
    mock = mocker.patch(
        "ib_user.adapters.get_service_adapter"
    )
    user_id = 1
    mock.return_value = user_id
    return mock
