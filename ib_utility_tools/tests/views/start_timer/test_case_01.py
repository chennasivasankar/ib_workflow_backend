"""
It returns duration in seconds and is running true
This usecase is, if the user starting time
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils
from freezegun import freeze_time

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase01StartTimerAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    @freeze_time("2020-08-07 18:00:00")
    @pytest.mark.django_db
    def test_case(self, setup, snapshot):
        entity_id, entity_type = setup
        body = {'entity_id': entity_id, 'entity_type': entity_type}
        path_params = {}
        query_params = {}
        headers = {}
        response = self.make_api_call(body=body,
                                      path_params=path_params,
                                      query_params=query_params,
                                      headers=headers,
                                      snapshot=snapshot)

        from ib_utility_tools.models import Timer
        timer_object = Timer.objects.get(entity_id=entity_id,
                                         entity_type=entity_type)
        snapshot.assert_match(timer_object.start_datetime, "start_datetime")

    @pytest.fixture
    def setup(self):
        from ib_utility_tools.constants.enum import TimerEntityType
        from ib_utility_tools.tests.factories.models import TimerFactory
        entity_id = "09b6cf6d-90ea-43ac-b0ee-3cee3c59ce5a"
        entity_type = TimerEntityType.STAGE_TASK.value
        TimerFactory.create(entity_id=entity_id,
                            entity_type=entity_type,
                            duration_in_seconds=0)
        return entity_id, entity_type
