# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot, GenericRepr


snapshots = Snapshot()

snapshots['TestGetTaskIdsOfUserBasedOnStagesInteractor.test_given_valid_stage_ids_get_tasks_with_max_stage_value_dtos stage_details_for_task_ids'] = [
    GenericRepr("TaskWithCompleteStageDetailsDTO(task_with_stage_details_dto=TaskIdWithStageDetailsDTO(db_stage_id=1, task_id=1, task_display_id='iBWF-1', stage_id='stage_1', stage_display_name='stage_display_1', stage_color='color_1'), stage_assignee_dto=[TaskStageAssigneeDetailsDTO(task_id=1, stage_id='stage_1', assignee_details=AssigneeWithTeamDetailsDTO(assignee_id='123e4567-e89b-12d3-a456-426614174000', name='name_0', profile_pic_url='https://www.google.com/search?q=ibhubs&client=ubuntu&hs=DI7&channel=fs&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjZqYjthYfrAhUF4zgGHevjDZUQ_AUoA3oECAsQBQ&biw=1848&bih=913#imgrc=Kg3TRY0jmx3udM', team_info_dto=TeamInfoDTO(team_id='team_0', team_name='team_name0')))])"),
    GenericRepr("TaskWithCompleteStageDetailsDTO(task_with_stage_details_dto=TaskIdWithStageDetailsDTO(db_stage_id=2, task_id=2, task_display_id='iBWF-2', stage_id='stage_2', stage_display_name='stage_display_2', stage_color='color_2'), stage_assignee_dto=[TaskStageAssigneeDetailsDTO(task_id=2, stage_id='stage_2', assignee_details=AssigneeWithTeamDetailsDTO(assignee_id='123e4567-e89b-12d3-a456-426614174001', name='name_1', profile_pic_url='https://www.google.com/search?q=ibhubs&client=ubuntu&hs=DI7&channel=fs&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjZqYjthYfrAhUF4zgGHevjDZUQ_AUoA3oECAsQBQ&biw=1848&bih=913#imgrc=Kg3TRY0jmx3udM', team_info_dto=TeamInfoDTO(team_id='team_1', team_name='team_name1')))])")
]

snapshots['TestGetTaskIdsOfUserBasedOnStagesInteractor.test_given_valid_stage_ids_get_tasks_with_max_stage_value_dtos_with_no_assignees stage_details_for_task_ids'] = [
    GenericRepr("TaskWithCompleteStageDetailsDTO(task_with_stage_details_dto=TaskIdWithStageDetailsDTO(db_stage_id=1, task_id=1, task_display_id='iBWF-1', stage_id='stage_1', stage_display_name='stage_display_1', stage_color='color_1'), stage_assignee_dto=[])"),
    GenericRepr("TaskWithCompleteStageDetailsDTO(task_with_stage_details_dto=TaskIdWithStageDetailsDTO(db_stage_id=2, task_id=2, task_display_id='iBWF-2', stage_id='stage_2', stage_display_name='stage_display_2', stage_color='color_2'), stage_assignee_dto=[])")
]
