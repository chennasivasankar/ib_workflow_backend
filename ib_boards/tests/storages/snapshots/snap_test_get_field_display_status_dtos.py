# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['TestCreateFieldOrderAndStatus.test_fields_display_order_and_status_creates display_status_dtos'] = [
    GenericRepr("FieldDisplayStatusDTO(field_id='field_id_0', display_status='HIDE')")
]
