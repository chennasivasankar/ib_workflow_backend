# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['TestGetTaskTemplateFieldIds.test_given_template_ids_get_their_related_field_ids task_fields'] = [
    GenericRepr("TemplateFieldsDTO(task_template_id='template_1', field_ids=['FIELD_ID-0', 'FIELD_ID-1', 'FIELD_ID-2', 'FIELD_ID-3'])"),
    GenericRepr("TemplateFieldsDTO(task_template_id='template_2', field_ids=['FIELD_ID-0', 'FIELD_ID-1', 'FIELD_ID-2', 'FIELD_ID-3'])")
]
