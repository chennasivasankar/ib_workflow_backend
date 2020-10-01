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
    'response': 'user not have access to update the filter status'
}

snapshots['TestGetFiltersDetailsPresenter.test_create_filter_details filters'] = {
    'conditions': [
        {
            'field_id': 'field_1',
            'field_name': 'field_name1',
            'operator': 'GTE',
            'value': 'value_1'
        },
        {
            'field_id': 'field_2',
            'field_name': 'field_name2',
            'operator': 'GTE',
            'value': 'value_2'
        }
    ],
    'filter_id': 'field_1',
    'name': 'filed_name_1',
    'status': False,
    'template_id': 'template_1',
    'template_name': 'template_name_1'
}

snapshots['TestGetFiltersDetailsPresenter.test_update_filter_details filters'] = {
    'conditions': [
        {
            'field_id': 'field_1',
            'field_name': 'field_name1',
            'operator': 'GTE',
            'value': 'value_1'
        },
        {
            'field_id': 'field_2',
            'field_name': 'field_name2',
            'operator': 'GTE',
            'value': 'value_2'
        }
    ],
    'filter_id': 'field_1',
    'name': 'filed_name_1',
    'status': False,
    'template_id': 'template_1',
    'template_name': 'template_name_1'
}

snapshots['TestGetFiltersDetailsPresenter.test_get_response_for_invalid_filter_id filters'] = {
    'http_status_code': 404,
    'res_status': 'INVALID_FILTER_ID',
    'response': 'invalid filter id'
}

snapshots['TestGetFiltersDetailsPresenter.test_get_response_for_invalid_user_to_update_filter_status filters'] = {
    'http_status_code': 403,
    'res_status': 'USER_DO_NOT_ACCESS_TO_UPDATE_FILTER_STATUS',
    'response': 'user not have access to update the filter status'
}

snapshots['TestGetFiltersDetailsPresenter.test_get_response_for_invalid_task_template_id filters'] = {
    'http_status_code': 404,
    'res_status': 'TASK_TEMPLATES_DOES_NOT_EXISTS',
    'response': 'No Task Templates are exists'
}

snapshots['TestGetFiltersDetailsPresenter.test_get_response_for_invalid_field_ids filters'] = {
    'http_status_code': 403,
    'res_status': 'FIELDS_NOT_BELONGS_TO_TASK_TEMPLATE',
    'response': 'fields not belongs to task template: [1, 2]'
}

snapshots['TestGetFiltersDetailsPresenter.test_get_response_for_user_not_have_access_to_fields filters'] = {
    'http_status_code': 403,
    'res_status': 'USER_NOT_ACCESS_TO_FIELDS',
    'response': 'user not have access to fields'
}

snapshots['TestGetFiltersDetailsPresenter.test_get_response_for_user_not_have_access_to_update_filter filters'] = {
    'http_status_code': 403,
    'res_status': 'USER_NOT_HAVE_PERMISSIONS_TO_UPDATE',
    'response': 'user not have access to update the filter'
}

snapshots['TestGetFiltersDetailsPresenter.test_get_response_for_user_not_have_access_to_delete_filter filters'] = {
    'http_status_code': 403,
    'res_status': 'USER_NOT_HAVE_PERMISSIONS_TO_DELETE',
    'response': 'user not have access to delete the filter'
}

snapshots['TestGetFiltersDetailsPresenter.test_returns_templates_fields filters'] = {
    'operators': [
        'GTE',
        'LTE',
        'GT',
        'LT',
        'NE',
        'EQ',
        'CONTAINS'
    ],
    'task_template_fields_details': [
        {
            'fields': [
                {
                    'field_id': 'field_0',
                    'name': 'display_name_0'
                }
            ],
            'name': 'Task Template 0',
            'task_template_id': 'template_0'
        }
    ]
}
