"""
This will create a timer for given entity details as
there is no created timer previously
And returns duration_in_seconds and is_running
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils
from freezegun import freeze_time

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase03GetTimerAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    @pytest.mark.django_db
    def test_case(self, setup, snapshot):
        entity_id, entity_type = setup
        body = {'entity_id': entity_id,
                'entity_type': entity_type}
        path_params = {}
        query_params = {}
        headers = {}
        response = self.make_api_call(body=body,
                                      path_params=path_params,
                                      query_params=query_params,
                                      headers=headers,
                                      snapshot=snapshot)

    @pytest.fixture
    def setup(self):
        from ib_utility_tools.constants.enum import TimerEntityType
        from ib_utility_tools.tests.factories.models import TimerFactory
        entity_id = "09b6cf6d-90ea-43ac-b0ee-3cee3c59ce5a"
        entity_type = TimerEntityType.STAGE_TASK.value

        import datetime
        TimerFactory.create(entity_id=entity_id,
                            entity_type=entity_type,
                            start_datetime=None,
                            duration_in_seconds=100,
                            is_running=False)
        return entity_id, entity_type
