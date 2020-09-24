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
                    "group_by_value": "value_0",
                    "group_by_display_name": "display_name_0",
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
                                    "field_type": "field_type0",
                                    "field_display_name": "key_0",
                                    "field_response": "value_0",
                                    "field_id": "field_0"
                                },
                                {
                                    "field_type": "field_type1",
                                    "field_display_name": "key_1",
                                    "field_response": "value_1",
                                    "field_id": "field_1"
                                },
                                {
                                    "field_type": "field_type2",
                                    "field_display_name": "key_2",
                                    "field_response": "value_2",
                                    "field_id": "field_2"
                                }
                            ],
                            "stage_with_actions": {
                                "stage_id": 0,
                                "stage_display_name": "stage_name0",
                                "stage_color": "stage_color0",
                                "assignee": {
                                    "assignee_id": "assignee_0",
                                    "name": "name_0",
                                    "profile_pic_url": "profile_pic_0",
                                    "team_info": {
                                        "team_id": "team_0",
                                        "team_name": "name_0"
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
                                    "field_type": "field_type0",
                                    "field_display_name": "key_0",
                                    "field_response": "value_0",
                                    "field_id": "field_0"
                                },
                                {
                                    "field_type": "field_type1",
                                    "field_display_name": "key_1",
                                    "field_response": "value_1",
                                    "field_id": "field_1"
                                },
                                {
                                    "field_type": "field_type2",
                                    "field_display_name": "key_2",
                                    "field_response": "value_2",
                                    "field_id": "field_2"
                                }
                            ],
                            "stage_with_actions": {
                                "stage_id": 1,
                                "stage_display_name": "stage_name1",
                                "stage_color": "stage_color1",
                                "assignee": {
                                    "assignee_id": "assignee_1",
                                    "name": "name_1",
                                    "profile_pic_url": "profile_pic_1",
                                    "team_info": {
                                        "team_id": "team_1",
                                        "team_name": "name_1"
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
                                    "field_type": "field_type0",
                                    "field_display_name": "key_0",
                                    "field_response": "value_0",
                                    "field_id": "field_0"
                                },
                                {
                                    "field_type": "field_type1",
                                    "field_display_name": "key_1",
                                    "field_response": "value_1",
                                    "field_id": "field_1"
                                },
                                {
                                    "field_type": "field_type2",
                                    "field_display_name": "key_2",
                                    "field_response": "value_2",
                                    "field_id": "field_2"
                                }
                            ],
                            "stage_with_actions": {
                                "stage_id": 2,
                                "stage_display_name": "stage_name2",
                                "stage_color": "stage_color2",
                                "assignee": {
                                    "assignee_id": "assignee_2",
                                    "name": "name_2",
                                    "profile_pic_url": "profile_pic_2",
                                    "team_info": {
                                        "team_id": "team_2",
                                        "team_name": "name_2"
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
                    "group_by_value": "value_1",
                    "group_by_display_name": "display_name_1",
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
                                    "field_type": "field_type0",
                                    "field_display_name": "key_0",
                                    "field_response": "value_0",
                                    "field_id": "field_0"
                                },
                                {
                                    "field_type": "field_type1",
                                    "field_display_name": "key_1",
                                    "field_response": "value_1",
                                    "field_id": "field_1"
                                },
                                {
                                    "field_type": "field_type2",
                                    "field_display_name": "key_2",
                                    "field_response": "value_2",
                                    "field_id": "field_2"
                                }
                            ],
                            "stage_with_actions": {
                                "stage_id": 3,
                                "stage_display_name": "stage_name3",
                                "stage_color": "stage_color3",
                                "assignee": {
                                    "assignee_id": "assignee_3",
                                    "name": "name_3",
                                    "profile_pic_url": "profile_pic_3",
                                    "team_info": {
                                        "team_id": "team_3",
                                        "team_name": "name_3"
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
                                    "field_type": "field_type0",
                                    "field_display_name": "key_0",
                                    "field_response": "value_0",
                                    "field_id": "field_0"
                                },
                                {
                                    "field_type": "field_type1",
                                    "field_display_name": "key_1",
                                    "field_response": "value_1",
                                    "field_id": "field_1"
                                },
                                {
                                    "field_type": "field_type2",
                                    "field_display_name": "key_2",
                                    "field_response": "value_2",
                                    "field_id": "field_2"
                                }
                            ],
                            "stage_with_actions": {
                                "stage_id": 4,
                                "stage_display_name": "stage_name4",
                                "stage_color": "stage_color4",
                                "assignee": {
                                    "assignee_id": "assignee_4",
                                    "name": "name_4",
                                    "profile_pic_url": "profile_pic_4",
                                    "team_info": {
                                        "team_id": "team_4",
                                        "team_name": "name_4"
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
                                    "field_type": "field_type0",
                                    "field_display_name": "key_0",
                                    "field_response": "value_0",
                                    "field_id": "field_0"
                                },
                                {
                                    "field_type": "field_type1",
                                    "field_display_name": "key_1",
                                    "field_response": "value_1",
                                    "field_id": "field_1"
                                },
                                {
                                    "field_type": "field_type2",
                                    "field_display_name": "key_2",
                                    "field_response": "value_2",
                                    "field_id": "field_2"
                                }
                            ],
                            "stage_with_actions": {
                                "stage_id": 5,
                                "stage_display_name": "stage_name5",
                                "stage_color": "stage_color5",
                                "assignee": {
                                    "assignee_id": "assignee_5",
                                    "name": "name_5",
                                    "profile_pic_url": "profile_pic_5",
                                    "team_info": {
                                        "team_id": "team_5",
                                        "team_name": "name_5"
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
