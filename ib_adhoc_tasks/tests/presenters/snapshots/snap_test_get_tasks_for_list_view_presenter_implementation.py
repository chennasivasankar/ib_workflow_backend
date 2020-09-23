# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestGetTasksForListViewPresenterImplementation.test_given_group_details_dtos_and_task_details_dtos_returns_group_info_task_details_dtos group_by_task_details'] = '''{
    "total_groups": 3,
    "groups": [
        {
            "group_by_value": "value_4",
            "group_by_display_name": "display_name_4",
            "total_tasks": 5,
            "tasks": [
                {
                    "task_id": "task_display5",
                    "title": "title_5",
                    "description": "description_5",
                    "start_date": "2020-09-10 05:30:00",
                    "due_date": "2020-10-10 05:30:00",
                    "priority": "LOW",
                    "task_overview_fields": [
                        {
                            "field_type": "field_type5",
                            "field_display_name": "key_5",
                            "field_response": "value_5",
                            "field_id": "field_5"
                        },
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
                        }
                    ],
                    "stage_with_actions": {
                        "stage_id": 5,
                        "stage_display_name": "stage_name5",
                        "stage_color": "stage_color5",
                        "assignee": {
                            "assignee_id": "assignee_22",
                            "name": "name_22",
                            "profile_pic_url": "profile_pic_22",
                            "team_info": {
                                "team_id": "team_22",
                                "team_name": "name_22"
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
                    "task_id": "task_display6",
                    "title": "title_6",
                    "description": "description_6",
                    "start_date": "2020-09-10 05:30:00",
                    "due_date": "2020-10-10 05:30:00",
                    "priority": "MEDIUM",
                    "task_overview_fields": [
                        {
                            "field_type": "field_type5",
                            "field_display_name": "key_5",
                            "field_response": "value_5",
                            "field_id": "field_5"
                        },
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
                        }
                    ],
                    "stage_with_actions": {
                        "stage_id": 6,
                        "stage_display_name": "stage_name6",
                        "stage_color": "stage_color6",
                        "assignee": {
                            "assignee_id": "assignee_23",
                            "name": "name_23",
                            "profile_pic_url": "profile_pic_23",
                            "team_info": {
                                "team_id": "team_23",
                                "team_name": "name_23"
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
                    "task_id": "task_display7",
                    "title": "title_7",
                    "description": "description_7",
                    "start_date": "2020-09-10 05:30:00",
                    "due_date": "2020-10-10 05:30:00",
                    "priority": "HIGH",
                    "task_overview_fields": [
                        {
                            "field_type": "field_type5",
                            "field_display_name": "key_5",
                            "field_response": "value_5",
                            "field_id": "field_5"
                        },
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
                        }
                    ],
                    "stage_with_actions": {
                        "stage_id": 7,
                        "stage_display_name": "stage_name7",
                        "stage_color": "stage_color7",
                        "assignee": {
                            "assignee_id": "assignee_24",
                            "name": "name_24",
                            "profile_pic_url": "profile_pic_24",
                            "team_info": {
                                "team_id": "team_24",
                                "team_name": "name_24"
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
                    "task_id": "task_display8",
                    "title": "title_8",
                    "description": "description_8",
                    "start_date": "2020-09-10 05:30:00",
                    "due_date": "2020-10-10 05:30:00",
                    "priority": "LOW",
                    "task_overview_fields": [
                        {
                            "field_type": "field_type5",
                            "field_display_name": "key_5",
                            "field_response": "value_5",
                            "field_id": "field_5"
                        },
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
                        }
                    ],
                    "stage_with_actions": {
                        "stage_id": 8,
                        "stage_display_name": "stage_name8",
                        "stage_color": "stage_color8",
                        "assignee": {
                            "assignee_id": "assignee_25",
                            "name": "name_25",
                            "profile_pic_url": "profile_pic_25",
                            "team_info": {
                                "team_id": "team_25",
                                "team_name": "name_25"
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
                    "task_id": "task_display9",
                    "title": "title_9",
                    "description": "description_9",
                    "start_date": "2020-09-10 05:30:00",
                    "due_date": "2020-10-10 05:30:00",
                    "priority": "MEDIUM",
                    "task_overview_fields": [
                        {
                            "field_type": "field_type5",
                            "field_display_name": "key_5",
                            "field_response": "value_5",
                            "field_id": "field_5"
                        },
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
                        }
                    ],
                    "stage_with_actions": {
                        "stage_id": 9,
                        "stage_display_name": "stage_name9",
                        "stage_color": "stage_color9",
                        "assignee": {
                            "assignee_id": "assignee_26",
                            "name": "name_26",
                            "profile_pic_url": "profile_pic_26",
                            "team_info": {
                                "team_id": "team_26",
                                "team_name": "name_26"
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
        },
        {
            "group_by_value": "value_5",
            "group_by_display_name": "display_name_5",
            "total_tasks": 5,
            "tasks": [
                {
                    "task_id": "task_display10",
                    "title": "title_10",
                    "description": "description_10",
                    "start_date": "2020-09-10 05:30:00",
                    "due_date": "2020-10-10 05:30:00",
                    "priority": "HIGH",
                    "task_overview_fields": [
                        {
                            "field_type": "field_type5",
                            "field_display_name": "key_5",
                            "field_response": "value_5",
                            "field_id": "field_5"
                        },
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
                        }
                    ],
                    "stage_with_actions": {
                        "stage_id": 10,
                        "stage_display_name": "stage_name10",
                        "stage_color": "stage_color10",
                        "assignee": {
                            "assignee_id": "assignee_27",
                            "name": "name_27",
                            "profile_pic_url": "profile_pic_27",
                            "team_info": {
                                "team_id": "team_27",
                                "team_name": "name_27"
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
                    "task_id": "task_display11",
                    "title": "title_11",
                    "description": "description_11",
                    "start_date": "2020-09-10 05:30:00",
                    "due_date": "2020-10-10 05:30:00",
                    "priority": "LOW",
                    "task_overview_fields": [
                        {
                            "field_type": "field_type5",
                            "field_display_name": "key_5",
                            "field_response": "value_5",
                            "field_id": "field_5"
                        },
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
                        }
                    ],
                    "stage_with_actions": {
                        "stage_id": 11,
                        "stage_display_name": "stage_name11",
                        "stage_color": "stage_color11",
                        "assignee": {
                            "assignee_id": "assignee_28",
                            "name": "name_28",
                            "profile_pic_url": "profile_pic_28",
                            "team_info": {
                                "team_id": "team_28",
                                "team_name": "name_28"
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
                    "task_id": "task_display12",
                    "title": "title_12",
                    "description": "description_12",
                    "start_date": "2020-09-10 05:30:00",
                    "due_date": "2020-10-10 05:30:00",
                    "priority": "MEDIUM",
                    "task_overview_fields": [
                        {
                            "field_type": "field_type5",
                            "field_display_name": "key_5",
                            "field_response": "value_5",
                            "field_id": "field_5"
                        },
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
                        }
                    ],
                    "stage_with_actions": {
                        "stage_id": 12,
                        "stage_display_name": "stage_name12",
                        "stage_color": "stage_color12",
                        "assignee": {
                            "assignee_id": "assignee_29",
                            "name": "name_29",
                            "profile_pic_url": "profile_pic_29",
                            "team_info": {
                                "team_id": "team_29",
                                "team_name": "name_29"
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
                    "task_id": "task_display13",
                    "title": "title_13",
                    "description": "description_13",
                    "start_date": "2020-09-10 05:30:00",
                    "due_date": "2020-10-10 05:30:00",
                    "priority": "HIGH",
                    "task_overview_fields": [
                        {
                            "field_type": "field_type5",
                            "field_display_name": "key_5",
                            "field_response": "value_5",
                            "field_id": "field_5"
                        },
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
                        }
                    ],
                    "stage_with_actions": {
                        "stage_id": 13,
                        "stage_display_name": "stage_name13",
                        "stage_color": "stage_color13",
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
                    "task_id": "task_display14",
                    "title": "title_14",
                    "description": "description_14",
                    "start_date": "2020-09-10 05:30:00",
                    "due_date": "2020-10-10 05:30:00",
                    "priority": "LOW",
                    "task_overview_fields": [
                        {
                            "field_type": "field_type5",
                            "field_display_name": "key_5",
                            "field_response": "value_5",
                            "field_id": "field_5"
                        },
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
                        }
                    ],
                    "stage_with_actions": {
                        "stage_id": 14,
                        "stage_display_name": "stage_name14",
                        "stage_color": "stage_color14",
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
                }
            ]
        },
        {
            "group_by_value": "value_6",
            "group_by_display_name": "display_name_6",
            "total_tasks": 5,
            "tasks": [
                {
                    "task_id": "task_display0",
                    "title": "title_0",
                    "description": "description_0",
                    "start_date": "2020-09-10 05:30:00",
                    "due_date": "2020-10-10 05:30:00",
                    "priority": "MEDIUM",
                    "task_overview_fields": [
                        {
                            "field_type": "field_type5",
                            "field_display_name": "key_5",
                            "field_response": "value_5",
                            "field_id": "field_5"
                        },
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
                        }
                    ],
                    "stage_with_actions": {
                        "stage_id": 0,
                        "stage_display_name": "stage_name0",
                        "stage_color": "stage_color0",
                        "assignee": {
                            "assignee_id": "assignee_17",
                            "name": "name_17",
                            "profile_pic_url": "profile_pic_17",
                            "team_info": {
                                "team_id": "team_17",
                                "team_name": "name_17"
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
                    "priority": "HIGH",
                    "task_overview_fields": [
                        {
                            "field_type": "field_type5",
                            "field_display_name": "key_5",
                            "field_response": "value_5",
                            "field_id": "field_5"
                        },
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
                        }
                    ],
                    "stage_with_actions": {
                        "stage_id": 1,
                        "stage_display_name": "stage_name1",
                        "stage_color": "stage_color1",
                        "assignee": {
                            "assignee_id": "assignee_18",
                            "name": "name_18",
                            "profile_pic_url": "profile_pic_18",
                            "team_info": {
                                "team_id": "team_18",
                                "team_name": "name_18"
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
                    "priority": "LOW",
                    "task_overview_fields": [
                        {
                            "field_type": "field_type5",
                            "field_display_name": "key_5",
                            "field_response": "value_5",
                            "field_id": "field_5"
                        },
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
                        }
                    ],
                    "stage_with_actions": {
                        "stage_id": 2,
                        "stage_display_name": "stage_name2",
                        "stage_color": "stage_color2",
                        "assignee": {
                            "assignee_id": "assignee_19",
                            "name": "name_19",
                            "profile_pic_url": "profile_pic_19",
                            "team_info": {
                                "team_id": "team_19",
                                "team_name": "name_19"
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
                    "task_id": "task_display3",
                    "title": "title_3",
                    "description": "description_3",
                    "start_date": "2020-09-10 05:30:00",
                    "due_date": "2020-10-10 05:30:00",
                    "priority": "MEDIUM",
                    "task_overview_fields": [
                        {
                            "field_type": "field_type5",
                            "field_display_name": "key_5",
                            "field_response": "value_5",
                            "field_id": "field_5"
                        },
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
                        }
                    ],
                    "stage_with_actions": {
                        "stage_id": 3,
                        "stage_display_name": "stage_name3",
                        "stage_color": "stage_color3",
                        "assignee": {
                            "assignee_id": "assignee_20",
                            "name": "name_20",
                            "profile_pic_url": "profile_pic_20",
                            "team_info": {
                                "team_id": "team_20",
                                "team_name": "name_20"
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
                    "priority": "HIGH",
                    "task_overview_fields": [
                        {
                            "field_type": "field_type5",
                            "field_display_name": "key_5",
                            "field_response": "value_5",
                            "field_id": "field_5"
                        },
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
                        }
                    ],
                    "stage_with_actions": {
                        "stage_id": 4,
                        "stage_display_name": "stage_name4",
                        "stage_color": "stage_color4",
                        "assignee": {
                            "assignee_id": "assignee_21",
                            "name": "name_21",
                            "profile_pic_url": "profile_pic_21",
                            "team_info": {
                                "team_id": "team_21",
                                "team_name": "name_21"
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
}'''

snapshots['TestGetTasksForListViewPresenterImplementation.test_raise_invalid_offset_value exception_object'] = b'{"response": "Invalid offset value, please send valid offset value", "http_status_code": 400, "res_status": "INVALID_OFFSET_VALUE"}'

snapshots['TestGetTasksForListViewPresenterImplementation.test_raise_invalid_limit_value exception_object'] = b'{"response": "Invalid limit value, please send valid limit values", "http_status_code": 400, "res_status": "INVALID_LIMIT_VALUE"}'

snapshots['TestGetTasksForListViewPresenterImplementation.test_raise_invalid_project_id exception_object'] = b'{"response": "Invalid project id, please send valid project id", "http_status_code": 404, "res_status": "INVALID_PROJECT_ID"}'

snapshots['TestGetTasksForListViewPresenterImplementation.test_raise_invalid_user_id exception_object'] = b'{"response": "Invalid user_id, please send valid user_id", "http_status_code": 404, "res_status": "INVALID_USER_ID"}'

snapshots['TestGetTasksForListViewPresenterImplementation.test_raise_invalid_user_for_project exception_object'] = b'{"response": "User not the member of project", "http_status_code": 404, "res_status": "INVALID_USER_ID_FOR_PROJECT"}'
