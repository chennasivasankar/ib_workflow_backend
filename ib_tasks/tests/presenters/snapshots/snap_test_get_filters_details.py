# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestGetFiltersDetailsPresenter.test_get_filter_details filters'] = [
    {
        'conditions': [
            {
                'field_id': 'FIELD_ID-1',
                'field_name': 'DISPLAY_NAME-1',
                'operator': 'GTE',
                'value': 'value_1'
            }
        ],
        'filter_id': 1,
        'name': 'filter_name_1',
        'status': 'ENABLED',
        'template_id': 'template_1',
        'template_name': 'Template 1'
    },
    {
        'conditions': [
            {
                'field_id': 'FIELD_ID-2',
                'field_name': 'DISPLAY_NAME-2',
                'operator': 'GTE',
                'value': 'value_2'
            }
        ],
        'filter_id': 2,
        'name': 'filter_name_2',
        'status': 'ENABLED',
        'template_id': 'template_2',
        'template_name': 'Template 2'
    }
]

snapshots['TestGetFiltersDetailsPresenter.test_get_update_filter_status filters'] = {
    'action': 'ENABLED',
    'filter_id': 1
}

snapshots['TestGetFiltersDetailsPresenter.test_get_raises_exception filters'] = {
    'http_status_code': 403,
    'res_status': 'USER_DO_NOT_ACCESS_TO_UPDATE_FILTER_STATUS',
    'response': 'user do not have access to change filter status'
}
