# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['TestCreateFieldOrderAndStatus.test_fields_display_order_and_status_creates field_ids'] = '{"field_ids": ["field_id_0", "field_id_1", "field_id_2"]}'

snapshots['TestCreateFieldOrderAndStatus.test_fields_display_order_and_status_creates display_objects'] = GenericRepr('<QuerySet [<FieldDisplayStatus: FieldDisplayStatus object (1)>, <FieldDisplayStatus: FieldDisplayStatus object (2)>, <FieldDisplayStatus: FieldDisplayStatus object (3)>]>')
