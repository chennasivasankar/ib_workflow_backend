# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02GetDiscussionsAPITestCase.test_invalid_offset_raise_exception status_code'] = '400'

snapshots['TestCase02GetDiscussionsAPITestCase.test_invalid_offset_raise_exception body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_OFFSET',
    'response': 'Please send the valid offset value'
}

snapshots['TestCase02GetDiscussionsAPITestCase.test_invalid_limit_raise_exception status_code'] = '400'

snapshots['TestCase02GetDiscussionsAPITestCase.test_invalid_limit_raise_exception body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_LIMIT',
    'response': 'Please send the valid limit value'
}

snapshots['TestCase02GetDiscussionsAPITestCase.test_invalid_entity_id_raise_exception status_code'] = '404'

snapshots['TestCase02GetDiscussionsAPITestCase.test_invalid_entity_id_raise_exception body'] = {
    'http_status_code': 404,
    'res_status': 'ENTITY_ID_NOT_FOUND',
    'response': 'Please send valid entity id'
}

snapshots['TestCase02GetDiscussionsAPITestCase.test_invalid_entity_type_for_entity_id_raise_exception status_code'] = '400'

snapshots['TestCase02GetDiscussionsAPITestCase.test_invalid_entity_type_for_entity_id_raise_exception body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_ENTITY_TYPE_FOR_ENTITY_ID',
    'response': 'Please valid entity type for entity id'
}

snapshots['TestCase02GetDiscussionsAPITestCase.test_user_profile_does_not_exist_raise_exception status_code'] = '400'

snapshots['TestCase02GetDiscussionsAPITestCase.test_user_profile_does_not_exist_raise_exception body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_USER_ID',
    'response': 'Please send the valid user id'
}
