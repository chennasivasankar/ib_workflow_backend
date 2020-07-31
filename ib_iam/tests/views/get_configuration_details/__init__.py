# pylint: disable=wrong-import-position

APP_NAME = "ib_iam"
OPERATION_NAME = "get_configuration_details"
REQUEST_METHOD = "get"
URL_SUFFIX = "configuration_details/v1/"

from .test_case_01 import TestCase01GetConfigurationDetailsAPITestCase
from .test_case_02 import TestCase02GetConfigurationDetailsAPITestCase

__all__ = [
    "TestCase01GetConfigurationDetailsAPITestCase",
    "TestCase02GetConfigurationDetailsAPITestCase"
]
