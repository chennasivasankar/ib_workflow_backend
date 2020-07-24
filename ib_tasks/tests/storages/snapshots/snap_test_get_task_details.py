# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot, GenericRepr


snapshots = Snapshot()

snapshots['TestGetTaskDetails.test_with_valid_details_returns_task_details_dtos result'] = GenericRepr("GetTaskStageCompleteDetailsDTO(fields_dto=[], actions_dto=[])")
