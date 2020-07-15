# pylint: disable=wrong-import-position

APP_NAME = "ib_iam"
OPERATION_NAME = "user_reset_password_link"
REQUEST_METHOD = "post"
URL_SUFFIX = "rest_password_link/v1/"

from .test_case_01 import TestCase01UserResetPasswordLinkAPITestCase
from .test_case_02 import TestCase02UserResetPasswordLinkAPITestCase

__all__ = [
    "TestCase01UserResetPasswordLinkAPITestCase",
    "TestCase02UserResetPasswordLinkAPITestCase"
]
