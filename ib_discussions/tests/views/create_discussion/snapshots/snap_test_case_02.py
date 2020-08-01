# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02CreateDiscussionAPITestCase.test_invalid_entity_id_raise_exception status_code'] = '404'

snapshots['TestCase02CreateDiscussionAPITestCase.test_invalid_entity_id_raise_exception body'] = {
    'http_status_code': 404,
    'res_status': 'ENTITY_ID_NOT_FOUND',
    'response': 'Please send valid entity id'
}

snapshots['TestCase02CreateDiscussionAPITestCase.test_invalid_entity_type_for_entity_id_raise_exception status_code'] = '400'

snapshots['TestCase02CreateDiscussionAPITestCase.test_invalid_entity_type_for_entity_id_raise_exception body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_ENTITY_TYPE_FOR_ENTITY_ID',
    'response': 'Please valid entity type for entity id'
}
