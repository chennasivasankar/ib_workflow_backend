# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCreateOrUpdateTaskPresenterImplementation.test_raise_exception_for_invalid_board invalid_board'] = {
    'http_status_code': 404,
    'res_status': 'INVALID_BOARD_ID',
    'response': 'invalid board id is: board_1, please send valid board id'
}

snapshots['TestCreateOrUpdateTaskPresenterImplementation.test_raise_exception_for_invalid_action invalid_action'] = {
    'http_status_code': 404,
    'res_status': 'INVALID_ACTION_ID',
    'response': 'invalid action id is: 1, please send valid action id'
}

snapshots['TestCreateOrUpdateTaskPresenterImplementation.test_raise_exception_for_invalid_user_permission invalid_user_permission'] = {
    'http_status_code': 403,
    'res_status': 'USER_DO_NOT_HAVE_ACCESS',
    'response': 'User do not have access to the action: 1'
}

snapshots['TestCreateOrUpdateTaskPresenterImplementation.test_raise_exception_for_invalid_task invalid_task'] = {
    'http_status_code': 404,
    'res_status': 'INVALID_TASK_ID',
    'response': 'invalid task id is: 1, please send valid task id'
}

snapshots['TestCreateOrUpdateTaskPresenterImplementation.test_raise_exception_for_invalid_user_board_permission invalid_user_board_permission'] = {
    'http_status_code': 403,
    'res_status': 'USER_DO_NOT_HAVE_ACCESS',
    'response': 'User do not have access to the board: board_1'
}
