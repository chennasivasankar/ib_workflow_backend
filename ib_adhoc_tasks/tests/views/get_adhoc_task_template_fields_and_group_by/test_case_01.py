"""
given valid data it returns group_by_fields and all_fields successfully
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase01GetAdhocTaskTemplateFieldsAndGroupByAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read']}}

    @pytest.mark.django_db
    def test_case(self, setup, snapshot):
        body = {}
        path_params = {}
        query_params = {'project_id': 'string', 'view_type': 'LIST'}
        headers = {}
        self.make_api_call(body=body,
                           path_params=path_params,
                           query_params=query_params,
                           headers=headers,
                           snapshot=snapshot)

    @pytest.fixture
    def setup(self, mocker, group_by_fields_dtos):
        from ib_adhoc_tasks.tests.common_fixtures.interactors import \
            get_group_by_interactor_mock, \
            get_adhoc_template_fields_interactor_mock
        get_group_by_interactor_mock(
            mocker=mocker, response=group_by_fields_dtos
        )
        from ib_adhoc_tasks.tests.factories.adapter_dtos import \
            FieldIdAndNameDTOFactory
        field_dtos = FieldIdAndNameDTOFactory.create_batch(size=2)
        get_adhoc_template_fields_interactor_mock(
            mocker=mocker, response=field_dtos
        )

    @pytest.fixture
    def group_by_fields_dtos(self):
        from ib_adhoc_tasks.tests.factories.storage_dtos import \
            GroupByResponseDTOFactory
        GroupByResponseDTOFactory.reset_sequence(0)
        GroupByResponseDTOFactory.order.reset()
        GroupByResponseDTOFactory.group_by_key.reset()
        GroupByResponseDTOFactory.display_name.reset()
        return GroupByResponseDTOFactory.create_batch(size=2)
