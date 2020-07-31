# pylint: disable=wrong-import-position

APP_NAME = "ib_iam"
OPERATION_NAME = "send_user_reset_password_link"
REQUEST_METHOD = "post"
URL_SUFFIX = "send/reset_password_link/v1/"

from .test_case_01 import TestCase01SendUserResetPasswordLinkAPITestCase
from .test_case_02 import TestCase02SendUserResetPasswordLinkAPITestCase
from .test_case_03 import TestCase03SendUserResetPasswordLinkAPITestCase

__all__ = [
    "TestCase01SendUserResetPasswordLinkAPITestCase",
    "TestCase02SendUserResetPasswordLinkAPITestCase",
    "TestCase03SendUserResetPasswordLinkAPITestCase"
]
