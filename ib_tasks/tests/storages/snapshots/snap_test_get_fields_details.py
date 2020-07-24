# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['TestGetFieldDetails.test_get_field_details response'] = [
    GenericRepr("FieldDetailsDTO(field_type='PLAIN_TEXT', field_id='FIELD_ID-1', key='DISPLAY_NAME-1', value='response')"),
    GenericRepr("FieldDetailsDTO(field_type='PLAIN_TEXT', field_id='FIELD_ID-2', key='DISPLAY_NAME-2', value='response')")
]
