# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetUserProfileAPITestCase.test_valid_user_id status_code'] = '200'

snapshots['TestCase01GetUserProfileAPITestCase.test_valid_user_id body'] = {
    'email': 'test@gmail.com',
    'is_admin': False,
    'name': 'test',
    'profile_pic_url': 'test.com',
    'user_id': 'c8939223-79a0-4566-ba13-b4fbf7db6f93'
}
