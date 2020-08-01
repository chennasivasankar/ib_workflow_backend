# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot, GenericRepr


snapshots = Snapshot()

snapshots['TestGetActionDetails.test_get_action_details response'] = [
    GenericRepr("ActionDetailsDTO(action_id=2, name='name_1', stage_id='stage_id_1', button_text='hey', button_color='#fafafa')"),
    GenericRepr("ActionDetailsDTO(action_id=3, name='name_2', stage_id='stage_id_2', button_text='hey', button_color='#fafafa')")
]
