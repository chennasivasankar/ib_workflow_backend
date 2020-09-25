# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot, GenericRepr


snapshots = Snapshot()

snapshots['TestGetUsersWithLessTasksInGivenStagesInteractor.test_given_more_task_count_for_user_get_users_with_less_tasks_for_stages 1'] = GenericRepr("StageWithUserDetailsAndTeamDetailsDTO(stages_with_user_details_dtos=[StageWithUserDetailsDTO(stage_details_dto=StageIdWithNameDTO(db_stage_id=1, stage_display_name='name_0'), assignee_details_dto=AssigneeDetailsDTO(assignee_id='123e4567-e89b-12d3-a456-426614174000', name='name_0', profile_pic_url='pic_url')), StageWithUserDetailsDTO(stage_details_dto=StageIdWithNameDTO(db_stage_id=2, stage_display_name='name_1'), assignee_details_dto=AssigneeDetailsDTO(assignee_id='123e4567-e89b-12d3-a456-426614174001', name='name_1', profile_pic_url='pic_url')), StageWithUserDetailsDTO(stage_details_dto=StageIdWithNameDTO(db_stage_id=3, stage_display_name='name_2'), assignee_details_dto=AssigneeDetailsDTO(assignee_id='123e4567-e89b-12d3-a456-426614174002', name='name_2', profile_pic_url='pic_url')), StageWithUserDetailsDTO(stage_details_dto=StageIdWithNameDTO(db_stage_id=4, stage_display_name='name_3'), assignee_details_dto=AssigneeDetailsDTO(assignee_id='123e4567-e89b-12d3-a456-426614174000', name='name_0', profile_pic_url='pic_url'))], user_with_team_details_dtos=[UserIdWIthTeamDetailsDTO(user_id='123e4567-e89b-12d3-a456-426614174000', team_details=TeamDetailsDTO(team_id='team_0', name='team_name0')), UserIdWIthTeamDetailsDTO(user_id='123e4567-e89b-12d3-a456-426614174001', team_details=TeamDetailsDTO(team_id='team_2', name='team_name2'))])")

snapshots['TestGetUsersWithLessTasksInGivenStagesInteractor.test_given_no_task_count_for_user_get_users_with_less_tasks_for_stages 1'] = GenericRepr("StageWithUserDetailsAndTeamDetailsDTO(stages_with_user_details_dtos=[StageWithUserDetailsDTO(stage_details_dto=StageIdWithNameDTO(db_stage_id=1, stage_display_name='name_0'), assignee_details_dto=AssigneeDetailsDTO(assignee_id='123e4567-e89b-12d3-a456-426614174000', name='name_0', profile_pic_url='pic_url')), StageWithUserDetailsDTO(stage_details_dto=StageIdWithNameDTO(db_stage_id=2, stage_display_name='name_1'), assignee_details_dto=AssigneeDetailsDTO(assignee_id='123e4567-e89b-12d3-a456-426614174001', name='name_1', profile_pic_url='pic_url')), StageWithUserDetailsDTO(stage_details_dto=StageIdWithNameDTO(db_stage_id=3, stage_display_name='name_2'), assignee_details_dto=AssigneeDetailsDTO(assignee_id='123e4567-e89b-12d3-a456-426614174002', name='name_2', profile_pic_url='pic_url')), StageWithUserDetailsDTO(stage_details_dto=StageIdWithNameDTO(db_stage_id=4, stage_display_name='name_3'), assignee_details_dto=AssigneeDetailsDTO(assignee_id='123e4567-e89b-12d3-a456-426614174000', name='name_0', profile_pic_url='pic_url'))], user_with_team_details_dtos=[UserIdWIthTeamDetailsDTO(user_id='123e4567-e89b-12d3-a456-426614174000', team_details=TeamDetailsDTO(team_id='team_0', name='team_name0')), UserIdWIthTeamDetailsDTO(user_id='123e4567-e89b-12d3-a456-426614174001', team_details=TeamDetailsDTO(team_id='team_2', name='team_name2'))])")

snapshots['TestGetUsersWithLessTasksInGivenStagesInteractor.test_given_equal_task_count_for_user_get_users_with_less_tasks_for_stages 1'] = GenericRepr("StageWithUserDetailsAndTeamDetailsDTO(stages_with_user_details_dtos=[StageWithUserDetailsDTO(stage_details_dto=StageIdWithNameDTO(db_stage_id=1, stage_display_name='name_0'), assignee_details_dto=AssigneeDetailsDTO(assignee_id='123e4567-e89b-12d3-a456-426614174000', name='name_0', profile_pic_url='pic_url')), StageWithUserDetailsDTO(stage_details_dto=StageIdWithNameDTO(db_stage_id=2, stage_display_name='name_1'), assignee_details_dto=AssigneeDetailsDTO(assignee_id='123e4567-e89b-12d3-a456-426614174001', name='name_1', profile_pic_url='pic_url')), StageWithUserDetailsDTO(stage_details_dto=StageIdWithNameDTO(db_stage_id=3, stage_display_name='name_2'), assignee_details_dto=AssigneeDetailsDTO(assignee_id='123e4567-e89b-12d3-a456-426614174002', name='name_2', profile_pic_url='pic_url')), StageWithUserDetailsDTO(stage_details_dto=StageIdWithNameDTO(db_stage_id=4, stage_display_name='name_3'), assignee_details_dto=AssigneeDetailsDTO(assignee_id='123e4567-e89b-12d3-a456-426614174000', name='name_0', profile_pic_url='pic_url'))], user_with_team_details_dtos=[UserIdWIthTeamDetailsDTO(user_id='123e4567-e89b-12d3-a456-426614174000', team_details=TeamDetailsDTO(team_id='team_0', name='team_name0')), UserIdWIthTeamDetailsDTO(user_id='123e4567-e89b-12d3-a456-426614174001', team_details=TeamDetailsDTO(team_id='team_2', name='team_name2'))])")
