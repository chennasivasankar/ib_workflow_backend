def prepare_send_email_to_user_mock(mocker):
    mock = mocker.patch(
        "ib_iam.adapters.email_service.EmailService.send_email_to_user"
    )
    return mock
