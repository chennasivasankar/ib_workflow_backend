# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot, GenericRepr


snapshots = Snapshot()

snapshots['TestGetStageRoleDTOsGivenDBStageIds.test_given_db_stage_ids_returns_stage_role_dtos stage_role_dtos'] = [
    GenericRepr("StageRoleDTO(db_stage_id=1, role_id='FIN_PAYMENT_REQUESTER')"),
    GenericRepr("StageRoleDTO(db_stage_id=2, role_id='FIN_PAYMENT_APPROVER')"),
    GenericRepr("StageRoleDTO(db_stage_id=3, role_id='FIN_PAYMENT_REQUESTER')"),
    GenericRepr("StageRoleDTO(db_stage_id=4, role_id='FIN_PAYMENT_APPROVER')"),
    GenericRepr("StageRoleDTO(db_stage_id=5, role_id='FIN_PAYMENT_REQUESTER')")
]
