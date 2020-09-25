"""
As Given valid data it returns group_by_key and display_names
"""
import mock
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from ib_adhoc_tasks.adapters.task_service import TaskService
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase01GetAdhocTaskTemplateFieldsAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read']}}

    @pytest.mark.django_db
    @mock.patch.object(TaskService, "get_task_template_field_dtos")
    def test_given_valid_data_returns_group_by_key_and_display_names(
            self, get_task_template_field_dtos_mock, snapshot
    ):
        from ib_adhoc_tasks.tests.factories.adapter_dtos import \
            FieldIdAndNameDTOFactory
        FieldIdAndNameDTOFactory.reset_sequence(1)
        field_dtos = FieldIdAndNameDTOFactory.create_batch(size=1)
        get_task_template_field_dtos_mock.return_value = field_dtos
        body = {}
        path_params = {}
        query_params = {'project_id': 'string'}
        headers = {}
        self.make_api_call(body=body,
                           path_params=path_params,
                           query_params=query_params,
                           headers=headers,
                           snapshot=snapshot)
