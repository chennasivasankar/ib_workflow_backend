# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestGetStageSearchablePossibleAssigneesPresenterImplementation.test_raise_invalid_offset_exception http_status_code'] = 400

snapshots['TestGetStageSearchablePossibleAssigneesPresenterImplementation.test_raise_invalid_offset_exception res_status'] = 'OFFSET_SHOULD_BE_GREATER_THAN_OR_EQUAL_TO_ZERO'

snapshots['TestGetStageSearchablePossibleAssigneesPresenterImplementation.test_raise_invalid_offset_exception response'] = 'Offset should be greater than or equal to zero'

snapshots['TestGetStageSearchablePossibleAssigneesPresenterImplementation.test_raise_invalid_limit_exception http_status_code'] = 400

snapshots['TestGetStageSearchablePossibleAssigneesPresenterImplementation.test_raise_invalid_limit_exception res_status'] = 'LIMIT_SHOULD_BE_GREATER_THAN_ZERO'

snapshots['TestGetStageSearchablePossibleAssigneesPresenterImplementation.test_raise_invalid_limit_exception response'] = 'Limit value should be greater than zero'

snapshots['TestGetStageSearchablePossibleAssigneesPresenterImplementation.test_raise_invalid_stage_id_exception http_status_code'] = 404

snapshots['TestGetStageSearchablePossibleAssigneesPresenterImplementation.test_raise_invalid_stage_id_exception res_status'] = 'INVALID_STAGE_ID'

snapshots['TestGetStageSearchablePossibleAssigneesPresenterImplementation.test_raise_invalid_stage_id_exception response'] = 'please give a valid stage id, 100 is invalid stage id'
