# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestPopulateStageGoFs.test_with_duplicate_stage_ids_raises_exception message'] = [
    'stage_1'
]

snapshots['TestPopulateStageGoFs.test_with_duplicate_gof_ids_for_same_stage_raises_exception message'] = [
    'gof_1'
]

snapshots['TestPopulateStageGoFs.test_with_invalid_stage_ids_raises_exception message'] = [
    'stage_1',
    'stage_2',
    'stage_3',
    'stage_4'
]

snapshots['TestPopulateStageGoFs.test_with_invalid_gof_ids_raises_exception message'] = [
    'gof_1',
    'gof_2',
    'gof_3',
    'gof_4'
]

snapshots['TestPopulateStageGoFs.test_with_valid_details_create_stage_gofs stage_id_for_stage_gof_obj_1'] = 1

snapshots['TestPopulateStageGoFs.test_with_valid_details_create_stage_gofs gof_id_for_stage_gof_obj_1'] = 'gof_1'

snapshots['TestPopulateStageGoFs.test_with_valid_details_create_stage_gofs stage_id_for_stage_gof_obj_2'] = 1

snapshots['TestPopulateStageGoFs.test_with_valid_details_create_stage_gofs gof_id_for_stage_gof_obj_2'] = 'gof_2'

snapshots['TestPopulateStageGoFs.test_with_valid_details_create_stage_gofs stage_id_for_stage_gof_obj_3'] = 2

snapshots['TestPopulateStageGoFs.test_with_valid_details_create_stage_gofs gof_id_for_stage_gof_obj_3'] = 'gof_1'

snapshots['TestPopulateStageGoFs.test_with_valid_details_create_stage_gofs stage_id_for_stage_gof_obj_4'] = 2

snapshots['TestPopulateStageGoFs.test_with_valid_details_create_stage_gofs gof_id_for_stage_gof_obj_4'] = 'gof_2'

snapshots['TestPopulateStageGoFs.test_with_existing_stage_gofs_skips_those_stage_gofs_to_create stage_id_for_stage_gof_obj_1'] = 1

snapshots['TestPopulateStageGoFs.test_with_existing_stage_gofs_skips_those_stage_gofs_to_create gof_id_for_stage_gof_obj_1'] = 'gof_1'

snapshots['TestPopulateStageGoFs.test_with_existing_stage_gofs_skips_those_stage_gofs_to_create stage_id_for_stage_gof_obj_2'] = 1

snapshots['TestPopulateStageGoFs.test_with_existing_stage_gofs_skips_those_stage_gofs_to_create gof_id_for_stage_gof_obj_2'] = 'gof_2'

snapshots['TestPopulateStageGoFs.test_with_existing_stage_gofs_skips_those_stage_gofs_to_create stage_id_for_stage_gof_obj_3'] = 2

snapshots['TestPopulateStageGoFs.test_with_existing_stage_gofs_skips_those_stage_gofs_to_create gof_id_for_stage_gof_obj_3'] = 'gof_1'

snapshots['TestPopulateStageGoFs.test_with_existing_stage_gofs_skips_those_stage_gofs_to_create stage_id_for_stage_gof_obj_4'] = 2

snapshots['TestPopulateStageGoFs.test_with_existing_stage_gofs_skips_those_stage_gofs_to_create gof_id_for_stage_gof_obj_4'] = 'gof_2'
