# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestGetTasksForKanbanViewPresenterImplementation.test_given_task_details_group_by_info_dto_returns_group_info_task_details group_by_task_details'] = '''{
    "total_groups": 2,
    "groups": [
        {
            "total_groups": 2,
            "group_by_value": "group_by_value1",
            "group_by_display_name": "group_by_display_name",
            "child_groups": [
                {
                    "group_by_value": "value_15",
                    "group_by_display_name": "display_name_15",
                    "total_tasks": 3,
                    "tasks": [
                        {
                            "task_id": "task_display0",
                            "title": "title_0",
                            "description": "description_0",
                            "start_date": "2020-09-10 05:30:00",
                            "due_date": "2020-10-10 05:30:00",
                            "priority": "HIGH",
                            "task_overview_fields": [
                                {
                                    "field_type": "field_type6",
                                    "field_display_name": "key_6",
                                    "field_response": "value_6",
                                    "field_id": "field_6"
                                },
                                {
                                    "field_type": "field_type7",
                                    "field_display_name": "key_7",
                                    "field_response": "value_7",
                                    "field_id": "field_7"
                                },
                                {
                                    "field_type": "field_type8",
                                    "field_display_name": "key_8",
                                    "field_response": "value_8",
                                    "field_id": "field_8"
                                }
                            ],
                            "stage_with_actions": {
                                "stage_id": 0,
                                "stage_display_name": "stage_name0",
                                "stage_color": "stage_color0",
                                "assignee": {
                                    "assignee_id": "assignee_30",
                                    "name": "name_30",
                                    "profile_pic_url": "profile_pic_30",
                                    "team_info": {
                                        "team_id": "team_30",
                                        "team_name": "name_30"
                                    }
                                },
                                "actions": [
                                    {
                                        "action_id": "action0",
                                        "action_type": "NO_VALIDATIONS",
                                        "button_text": "button_text0",
                                        "button_color": "button_color0"
                                    }
                                ]
                            }
                        },
                        {
                            "task_id": "task_display1",
                            "title": "title_1",
                            "description": "description_1",
                            "start_date": "2020-09-10 05:30:00",
                            "due_date": "2020-10-10 05:30:00",
                            "priority": "LOW",
                            "task_overview_fields": [
                                {
                                    "field_type": "field_type6",
                                    "field_display_name": "key_6",
                                    "field_response": "value_6",
                                    "field_id": "field_6"
                                },
                                {
                                    "field_type": "field_type7",
                                    "field_display_name": "key_7",
                                    "field_response": "value_7",
                                    "field_id": "field_7"
                                },
                                {
                                    "field_type": "field_type8",
                                    "field_display_name": "key_8",
                                    "field_response": "value_8",
                                    "field_id": "field_8"
                                }
                            ],
                            "stage_with_actions": {
                                "stage_id": 1,
                                "stage_display_name": "stage_name1",
                                "stage_color": "stage_color1",
                                "assignee": {
                                    "assignee_id": "assignee_31",
                                    "name": "name_31",
                                    "profile_pic_url": "profile_pic_31",
                                    "team_info": {
                                        "team_id": "team_31",
                                        "team_name": "name_31"
                                    }
                                },
                                "actions": [
                                    {
                                        "action_id": "action0",
                                        "action_type": "NO_VALIDATIONS",
                                        "button_text": "button_text0",
                                        "button_color": "button_color0"
                                    }
                                ]
                            }
                        },
                        {
                            "task_id": "task_display2",
                            "title": "title_2",
                            "description": "description_2",
                            "start_date": "2020-09-10 05:30:00",
                            "due_date": "2020-10-10 05:30:00",
                            "priority": "MEDIUM",
                            "task_overview_fields": [
                                {
                                    "field_type": "field_type6",
                                    "field_display_name": "key_6",
                                    "field_response": "value_6",
                                    "field_id": "field_6"
                                },
                                {
                                    "field_type": "field_type7",
                                    "field_display_name": "key_7",
                                    "field_response": "value_7",
                                    "field_id": "field_7"
                                },
                                {
                                    "field_type": "field_type8",
                                    "field_display_name": "key_8",
                                    "field_response": "value_8",
                                    "field_id": "field_8"
                                }
                            ],
                            "stage_with_actions": {
                                "stage_id": 2,
                                "stage_display_name": "stage_name2",
                                "stage_color": "stage_color2",
                                "assignee": {
                                    "assignee_id": "assignee_32",
                                    "name": "name_32",
                                    "profile_pic_url": "profile_pic_32",
                                    "team_info": {
                                        "team_id": "team_32",
                                        "team_name": "name_32"
                                    }
                                },
                                "actions": [
                                    {
                                        "action_id": "action0",
                                        "action_type": "NO_VALIDATIONS",
                                        "button_text": "button_text0",
                                        "button_color": "button_color0"
                                    }
                                ]
                            }
                        }
                    ]
                }
            ]
        },
        {
            "total_groups": 2,
            "group_by_value": "group_by_value2",
            "group_by_display_name": "group_by_display_name",
            "child_groups": [
                {
                    "group_by_value": "value_16",
                    "group_by_display_name": "display_name_16",
                    "total_tasks": 3,
                    "tasks": [
                        {
                            "task_id": "task_display3",
                            "title": "title_3",
                            "description": "description_3",
                            "start_date": "2020-09-10 05:30:00",
                            "due_date": "2020-10-10 05:30:00",
                            "priority": "HIGH",
                            "task_overview_fields": [
                                {
                                    "field_type": "field_type6",
                                    "field_display_name": "key_6",
                                    "field_response": "value_6",
                                    "field_id": "field_6"
                                },
                                {
                                    "field_type": "field_type7",
                                    "field_display_name": "key_7",
                                    "field_response": "value_7",
                                    "field_id": "field_7"
                                },
                                {
                                    "field_type": "field_type8",
                                    "field_display_name": "key_8",
                                    "field_response": "value_8",
                                    "field_id": "field_8"
                                }
                            ],
                            "stage_with_actions": {
                                "stage_id": 3,
                                "stage_display_name": "stage_name3",
                                "stage_color": "stage_color3",
                                "assignee": {
                                    "assignee_id": "assignee_33",
                                    "name": "name_33",
                                    "profile_pic_url": "profile_pic_33",
                                    "team_info": {
                                        "team_id": "team_33",
                                        "team_name": "name_33"
                                    }
                                },
                                "actions": [
                                    {
                                        "action_id": "action0",
                                        "action_type": "NO_VALIDATIONS",
                                        "button_text": "button_text0",
                                        "button_color": "button_color0"
                                    }
                                ]
                            }
                        },
                        {
                            "task_id": "task_display4",
                            "title": "title_4",
                            "description": "description_4",
                            "start_date": "2020-09-10 05:30:00",
                            "due_date": "2020-10-10 05:30:00",
                            "priority": "LOW",
                            "task_overview_fields": [
                                {
                                    "field_type": "field_type6",
                                    "field_display_name": "key_6",
                                    "field_response": "value_6",
                                    "field_id": "field_6"
                                },
                                {
                                    "field_type": "field_type7",
                                    "field_display_name": "key_7",
                                    "field_response": "value_7",
                                    "field_id": "field_7"
                                },
                                {
                                    "field_type": "field_type8",
                                    "field_display_name": "key_8",
                                    "field_response": "value_8",
                                    "field_id": "field_8"
                                }
                            ],
                            "stage_with_actions": {
                                "stage_id": 4,
                                "stage_display_name": "stage_name4",
                                "stage_color": "stage_color4",
                                "assignee": {
                                    "assignee_id": "assignee_34",
                                    "name": "name_34",
                                    "profile_pic_url": "profile_pic_34",
                                    "team_info": {
                                        "team_id": "team_34",
                                        "team_name": "name_34"
                                    }
                                },
                                "actions": [
                                    {
                                        "action_id": "action0",
                                        "action_type": "NO_VALIDATIONS",
                                        "button_text": "button_text0",
                                        "button_color": "button_color0"
                                    }
                                ]
                            }
                        },
                        {
                            "task_id": "task_display5",
                            "title": "title_5",
                            "description": "description_5",
                            "start_date": "2020-09-10 05:30:00",
                            "due_date": "2020-10-10 05:30:00",
                            "priority": "MEDIUM",
                            "task_overview_fields": [
                                {
                                    "field_type": "field_type6",
                                    "field_display_name": "key_6",
                                    "field_response": "value_6",
                                    "field_id": "field_6"
                                },
                                {
                                    "field_type": "field_type7",
                                    "field_display_name": "key_7",
                                    "field_response": "value_7",
                                    "field_id": "field_7"
                                },
                                {
                                    "field_type": "field_type8",
                                    "field_display_name": "key_8",
                                    "field_response": "value_8",
                                    "field_id": "field_8"
                                }
                            ],
                            "stage_with_actions": {
                                "stage_id": 5,
                                "stage_display_name": "stage_name5",
                                "stage_color": "stage_color5",
                                "assignee": {
                                    "assignee_id": "assignee_35",
                                    "name": "name_35",
                                    "profile_pic_url": "profile_pic_35",
                                    "team_info": {
                                        "team_id": "team_35",
                                        "team_name": "name_35"
                                    }
                                },
                                "actions": [
                                    {
                                        "action_id": "action0",
                                        "action_type": "NO_VALIDATIONS",
                                        "button_text": "button_text0",
                                        "button_color": "button_color0"
                                    }
                                ]
                            }
                        }
                    ]
                }
            ]
        }
    ]
}'''

snapshots['TestGetTasksForKanbanViewPresenterImplementation.test_raise_invalid_offset_value exception_object'] = b'{"response": "Invalid offset value, please send valid offset value", "http_status_code": 400, "res_status": "INVALID_OFFSET_VALUE"}'

snapshots['TestGetTasksForKanbanViewPresenterImplementation.test_raise_invalid_limit_value exception_object'] = b'{"response": "Invalid limit value, please send valid limit values", "http_status_code": 400, "res_status": "INVALID_LIMIT_VALUE"}'

snapshots['TestGetTasksForKanbanViewPresenterImplementation.test_raise_invalid_project_id exception_object'] = b'{"response": "Invalid project id, please send valid project id", "http_status_code": 404, "res_status": "INVALID_PROJECT_ID"}'

snapshots['TestGetTasksForKanbanViewPresenterImplementation.test_raise_invalid_user_id exception_object'] = b'{"response": "Invalid user_id, please send valid user_id", "http_status_code": 404, "res_status": "INVALID_USER_ID"}'

snapshots['TestGetTasksForKanbanViewPresenterImplementation.test_raise_invalid_user_for_project exception_object'] = b'{"response": "User not the member of project", "http_status_code": 404, "res_status": "INVALID_USER_ID_FOR_PROJECT"}'
