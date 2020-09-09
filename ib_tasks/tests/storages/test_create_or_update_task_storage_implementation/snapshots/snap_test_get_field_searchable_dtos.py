# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['TestGetFieldSearchableDTOS.test_given_field_ids_returns_field_searchable_dtos field_searchable_dtos'] = [
    GenericRepr("FieldSearchableDTO(field_id='FIELD_ID-25', field_value='CITY', field_response='1')"),
    GenericRepr("FieldSearchableDTO(field_id='FIELD_ID-26', field_value='USER', field_response='123e4567-e89b-12d3-a456-426614174000')"),
    GenericRepr("FieldSearchableDTO(field_id='FIELD_ID-27', field_value='COUNTRY', field_response='India')"),
    GenericRepr("FieldSearchableDTO(field_id='FIELD_ID-28', field_value='CITY', field_response='5')")
]
