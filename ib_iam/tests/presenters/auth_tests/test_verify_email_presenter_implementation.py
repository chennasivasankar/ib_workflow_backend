import json

import pytest

from ib_iam.constants.enums import StatusCode


class TestVerifyEmailLinkPresenter:
    @pytest.fixture
    def presenter_mock(self):
        from ib_iam.presenters.verify_email_presenter_implementation import \
            VerifyEmailPresenterImplementation
        presenter = VerifyEmailPresenterImplementation()
        return presenter

    def test_raise_email_does_not_exist_to_verify_exception(
            self, presenter_mock):
        # Arrange
        from ib_iam.constants.exception_messages import ACCOUNT_DOES_NOT_EXISTS
        response_dict = {
            "response": ACCOUNT_DOES_NOT_EXISTS[0],
            "http_status_code": StatusCode.NOT_FOUND.value,
            "res_status": ACCOUNT_DOES_NOT_EXISTS[1]
        }

        # Act
        response = presenter_mock.response_for_email_does_not_exist_exception()

        # Assert
        actual_response_content = json.loads(response.content)
        assert response_dict == actual_response_content

    def test_raise_email_already_verified_exception(self, presenter_mock):
        # Arrange
        from ib_iam.constants.exception_messages import EMAIL_ALREADY_VERIFIED
        response_dict = {
            "response": EMAIL_ALREADY_VERIFIED[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": EMAIL_ALREADY_VERIFIED[1]
        }

        # Act
        response = presenter_mock.response_for_email_already_verified_exception()

        # Assert
        actual_response_content = json.loads(response.content)
        assert response_dict == actual_response_content

    def test_get_response_for_verified_email(self, presenter_mock):
        # Act
        response = presenter_mock.get_response_for_verified_email()

        # Assert
        assert StatusCode.SUCCESS.value == response.status_code