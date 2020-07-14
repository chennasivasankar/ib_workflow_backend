# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestAddListOfRolesPresenter.test_raise_role_id_should_not_be_empty role_id_exception'] = {
    'http_status_code': 400,
    'res_status': 'ROLE_ID_SHOULD_NOT_BE_EMPTY',
    'response': 'role id should not be empty, try with valid role id'
}
