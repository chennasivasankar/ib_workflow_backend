def send_email_to_user_mock(mocker):
    mock = mocker.patch(
        "ib_iam.adapters.email_service.EmailService.send_email_to_user"
    )
    return mock


def send_email_mock(mocker):
    mock = mocker.patch(
        "ib_iam.services.email_service_implementation.EmailSenderImpl.send_email"
    )
    return mock
