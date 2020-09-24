# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestGetChildGroupsInGroupPresenterImplementation.test_prepare_response_for_get_child_groups_in_group response_for_get_child_groups_in_group'] = {
    'child_groups': [
        {
            'group_by_display_name': 'display_name_0',
            'group_by_value': 'value_0',
            'tasks': [
                {
                    'description': 'description_0',
                    'due_date': '2020-10-10 05:30:00',
                    'priority': 'HIGH',
                    'stage_with_actions': {
                        'actions': [
                            {
                                'action_id': 'action0',
                                'action_type': 'NO_VALIDATIONS',
                                'button_color': 'button_color0',
                                'button_text': 'button_text0'
                            }
                        ],
                        'assignee': {
                            'assignee_id': 'assignee_0',
                            'name': 'name_0',
                            'profile_pic_url': 'profile_pic_0',
                            'team_info': {
                                'team_id': 'team_0',
                                'team_name': 'name_0'
                            }
                        },
                        'stage_color': 'stage_color0',
                        'stage_display_name': 'stage_name0',
                        'stage_id': 0
                    },
                    'start_date': '2020-09-10 05:30:00',
                    'task_id': 'task_display0',
                    'task_overview_fields': [
                        {
                            'field_display_name': 'key_0',
                            'field_id': 'field_0',
                            'field_response': 'value_0',
                            'field_type': 'field_type0'
                        },
                        {
                            'field_display_name': 'key_1',
                            'field_id': 'field_1',
                            'field_response': 'value_1',
                            'field_type': 'field_type1'
                        },
                        {
                            'field_display_name': 'key_2',
                            'field_id': 'field_2',
                            'field_response': 'value_2',
                            'field_type': 'field_type2'
                        }
                    ],
                    'title': 'title_0'
                },
                {
                    'description': 'description_1',
                    'due_date': '2020-10-10 05:30:00',
                    'priority': 'LOW',
                    'stage_with_actions': {
                        'actions': [
                            {
                                'action_id': 'action0',
                                'action_type': 'NO_VALIDATIONS',
                                'button_color': 'button_color0',
                                'button_text': 'button_text0'
                            }
                        ],
                        'assignee': {
                            'assignee_id': 'assignee_1',
                            'name': 'name_1',
                            'profile_pic_url': 'profile_pic_1',
                            'team_info': {
                                'team_id': 'team_1',
                                'team_name': 'name_1'
                            }
                        },
                        'stage_color': 'stage_color1',
                        'stage_display_name': 'stage_name1',
                        'stage_id': 1
                    },
                    'start_date': '2020-09-10 05:30:00',
                    'task_id': 'task_display1',
                    'task_overview_fields': [
                        {
                            'field_display_name': 'key_0',
                            'field_id': 'field_0',
                            'field_response': 'value_0',
                            'field_type': 'field_type0'
                        },
                        {
                            'field_display_name': 'key_1',
                            'field_id': 'field_1',
                            'field_response': 'value_1',
                            'field_type': 'field_type1'
                        },
                        {
                            'field_display_name': 'key_2',
                            'field_id': 'field_2',
                            'field_response': 'value_2',
                            'field_type': 'field_type2'
                        }
                    ],
                    'title': 'title_1'
                },
                {
                    'description': 'description_2',
                    'due_date': '2020-10-10 05:30:00',
                    'priority': 'MEDIUM',
                    'stage_with_actions': {
                        'actions': [
                            {
                                'action_id': 'action0',
                                'action_type': 'NO_VALIDATIONS',
                                'button_color': 'button_color0',
                                'button_text': 'button_text0'
                            }
                        ],
                        'assignee': {
                            'assignee_id': 'assignee_2',
                            'name': 'name_2',
                            'profile_pic_url': 'profile_pic_2',
                            'team_info': {
                                'team_id': 'team_2',
                                'team_name': 'name_2'
                            }
                        },
                        'stage_color': 'stage_color2',
                        'stage_display_name': 'stage_name2',
                        'stage_id': 2
                    },
                    'start_date': '2020-09-10 05:30:00',
                    'task_id': 'task_display2',
                    'task_overview_fields': [
                        {
                            'field_display_name': 'key_0',
                            'field_id': 'field_0',
                            'field_response': 'value_0',
                            'field_type': 'field_type0'
                        },
                        {
                            'field_display_name': 'key_1',
                            'field_id': 'field_1',
                            'field_response': 'value_1',
                            'field_type': 'field_type1'
                        },
                        {
                            'field_display_name': 'key_2',
                            'field_id': 'field_2',
                            'field_response': 'value_2',
                            'field_type': 'field_type2'
                        }
                    ],
                    'title': 'title_2'
                },
                {
                    'description': 'description_3',
                    'due_date': '2020-10-10 05:30:00',
                    'priority': 'HIGH',
                    'stage_with_actions': {
                        'actions': [
                            {
                                'action_id': 'action0',
                                'action_type': 'NO_VALIDATIONS',
                                'button_color': 'button_color0',
                                'button_text': 'button_text0'
                            }
                        ],
                        'assignee': {
                            'assignee_id': 'assignee_3',
                            'name': 'name_3',
                            'profile_pic_url': 'profile_pic_3',
                            'team_info': {
                                'team_id': 'team_3',
                                'team_name': 'name_3'
                            }
                        },
                        'stage_color': 'stage_color3',
                        'stage_display_name': 'stage_name3',
                        'stage_id': 3
                    },
                    'start_date': '2020-09-10 05:30:00',
                    'task_id': 'task_display3',
                    'task_overview_fields': [
                        {
                            'field_display_name': 'key_0',
                            'field_id': 'field_0',
                            'field_response': 'value_0',
                            'field_type': 'field_type0'
                        },
                        {
                            'field_display_name': 'key_1',
                            'field_id': 'field_1',
                            'field_response': 'value_1',
                            'field_type': 'field_type1'
                        },
                        {
                            'field_display_name': 'key_2',
                            'field_id': 'field_2',
                            'field_response': 'value_2',
                            'field_type': 'field_type2'
                        }
                    ],
                    'title': 'title_3'
                },
                {
                    'description': 'description_4',
                    'due_date': '2020-10-10 05:30:00',
                    'priority': 'LOW',
                    'stage_with_actions': {
                        'actions': [
                            {
                                'action_id': 'action0',
                                'action_type': 'NO_VALIDATIONS',
                                'button_color': 'button_color0',
                                'button_text': 'button_text0'
                            }
                        ],
                        'assignee': {
                            'assignee_id': 'assignee_4',
                            'name': 'name_4',
                            'profile_pic_url': 'profile_pic_4',
                            'team_info': {
                                'team_id': 'team_4',
                                'team_name': 'name_4'
                            }
                        },
                        'stage_color': 'stage_color4',
                        'stage_display_name': 'stage_name4',
                        'stage_id': 4
                    },
                    'start_date': '2020-09-10 05:30:00',
                    'task_id': 'task_display4',
                    'task_overview_fields': [
                        {
                            'field_display_name': 'key_0',
                            'field_id': 'field_0',
                            'field_response': 'value_0',
                            'field_type': 'field_type0'
                        },
                        {
                            'field_display_name': 'key_1',
                            'field_id': 'field_1',
                            'field_response': 'value_1',
                            'field_type': 'field_type1'
                        },
                        {
                            'field_display_name': 'key_2',
                            'field_id': 'field_2',
                            'field_response': 'value_2',
                            'field_type': 'field_type2'
                        }
                    ],
                    'title': 'title_4'
                }
            ],
            'total_tasks': 5
        },
        {
            'group_by_display_name': 'display_name_1',
            'group_by_value': 'value_1',
            'tasks': [
                {
                    'description': 'description_5',
                    'due_date': '2020-10-10 05:30:00',
                    'priority': 'MEDIUM',
                    'stage_with_actions': {
                        'actions': [
                            {
                                'action_id': 'action0',
                                'action_type': 'NO_VALIDATIONS',
                                'button_color': 'button_color0',
                                'button_text': 'button_text0'
                            }
                        ],
                        'assignee': {
                            'assignee_id': 'assignee_5',
                            'name': 'name_5',
                            'profile_pic_url': 'profile_pic_5',
                            'team_info': {
                                'team_id': 'team_5',
                                'team_name': 'name_5'
                            }
                        },
                        'stage_color': 'stage_color5',
                        'stage_display_name': 'stage_name5',
                        'stage_id': 5
                    },
                    'start_date': '2020-09-10 05:30:00',
                    'task_id': 'task_display5',
                    'task_overview_fields': [
                        {
                            'field_display_name': 'key_0',
                            'field_id': 'field_0',
                            'field_response': 'value_0',
                            'field_type': 'field_type0'
                        },
                        {
                            'field_display_name': 'key_1',
                            'field_id': 'field_1',
                            'field_response': 'value_1',
                            'field_type': 'field_type1'
                        },
                        {
                            'field_display_name': 'key_2',
                            'field_id': 'field_2',
                            'field_response': 'value_2',
                            'field_type': 'field_type2'
                        }
                    ],
                    'title': 'title_5'
                },
                {
                    'description': 'description_6',
                    'due_date': '2020-10-10 05:30:00',
                    'priority': 'HIGH',
                    'stage_with_actions': {
                        'actions': [
                            {
                                'action_id': 'action0',
                                'action_type': 'NO_VALIDATIONS',
                                'button_color': 'button_color0',
                                'button_text': 'button_text0'
                            }
                        ],
                        'assignee': {
                            'assignee_id': 'assignee_6',
                            'name': 'name_6',
                            'profile_pic_url': 'profile_pic_6',
                            'team_info': {
                                'team_id': 'team_6',
                                'team_name': 'name_6'
                            }
                        },
                        'stage_color': 'stage_color6',
                        'stage_display_name': 'stage_name6',
                        'stage_id': 6
                    },
                    'start_date': '2020-09-10 05:30:00',
                    'task_id': 'task_display6',
                    'task_overview_fields': [
                        {
                            'field_display_name': 'key_0',
                            'field_id': 'field_0',
                            'field_response': 'value_0',
                            'field_type': 'field_type0'
                        },
                        {
                            'field_display_name': 'key_1',
                            'field_id': 'field_1',
                            'field_response': 'value_1',
                            'field_type': 'field_type1'
                        },
                        {
                            'field_display_name': 'key_2',
                            'field_id': 'field_2',
                            'field_response': 'value_2',
                            'field_type': 'field_type2'
                        }
                    ],
                    'title': 'title_6'
                },
                {
                    'description': 'description_7',
                    'due_date': '2020-10-10 05:30:00',
                    'priority': 'LOW',
                    'stage_with_actions': {
                        'actions': [
                            {
                                'action_id': 'action0',
                                'action_type': 'NO_VALIDATIONS',
                                'button_color': 'button_color0',
                                'button_text': 'button_text0'
                            }
                        ],
                        'assignee': {
                            'assignee_id': 'assignee_7',
                            'name': 'name_7',
                            'profile_pic_url': 'profile_pic_7',
                            'team_info': {
                                'team_id': 'team_7',
                                'team_name': 'name_7'
                            }
                        },
                        'stage_color': 'stage_color7',
                        'stage_display_name': 'stage_name7',
                        'stage_id': 7
                    },
                    'start_date': '2020-09-10 05:30:00',
                    'task_id': 'task_display7',
                    'task_overview_fields': [
                        {
                            'field_display_name': 'key_0',
                            'field_id': 'field_0',
                            'field_response': 'value_0',
                            'field_type': 'field_type0'
                        },
                        {
                            'field_display_name': 'key_1',
                            'field_id': 'field_1',
                            'field_response': 'value_1',
                            'field_type': 'field_type1'
                        },
                        {
                            'field_display_name': 'key_2',
                            'field_id': 'field_2',
                            'field_response': 'value_2',
                            'field_type': 'field_type2'
                        }
                    ],
                    'title': 'title_7'
                },
                {
                    'description': 'description_8',
                    'due_date': '2020-10-10 05:30:00',
                    'priority': 'MEDIUM',
                    'stage_with_actions': {
                        'actions': [
                            {
                                'action_id': 'action0',
                                'action_type': 'NO_VALIDATIONS',
                                'button_color': 'button_color0',
                                'button_text': 'button_text0'
                            }
                        ],
                        'assignee': {
                            'assignee_id': 'assignee_8',
                            'name': 'name_8',
                            'profile_pic_url': 'profile_pic_8',
                            'team_info': {
                                'team_id': 'team_8',
                                'team_name': 'name_8'
                            }
                        },
                        'stage_color': 'stage_color8',
                        'stage_display_name': 'stage_name8',
                        'stage_id': 8
                    },
                    'start_date': '2020-09-10 05:30:00',
                    'task_id': 'task_display8',
                    'task_overview_fields': [
                        {
                            'field_display_name': 'key_0',
                            'field_id': 'field_0',
                            'field_response': 'value_0',
                            'field_type': 'field_type0'
                        },
                        {
                            'field_display_name': 'key_1',
                            'field_id': 'field_1',
                            'field_response': 'value_1',
                            'field_type': 'field_type1'
                        },
                        {
                            'field_display_name': 'key_2',
                            'field_id': 'field_2',
                            'field_response': 'value_2',
                            'field_type': 'field_type2'
                        }
                    ],
                    'title': 'title_8'
                },
                {
                    'description': 'description_9',
                    'due_date': '2020-10-10 05:30:00',
                    'priority': 'HIGH',
                    'stage_with_actions': {
                        'actions': [
                            {
                                'action_id': 'action0',
                                'action_type': 'NO_VALIDATIONS',
                                'button_color': 'button_color0',
                                'button_text': 'button_text0'
                            }
                        ],
                        'assignee': {
                            'assignee_id': 'assignee_9',
                            'name': 'name_9',
                            'profile_pic_url': 'profile_pic_9',
                            'team_info': {
                                'team_id': 'team_9',
                                'team_name': 'name_9'
                            }
                        },
                        'stage_color': 'stage_color9',
                        'stage_display_name': 'stage_name9',
                        'stage_id': 9
                    },
                    'start_date': '2020-09-10 05:30:00',
                    'task_id': 'task_display9',
                    'task_overview_fields': [
                        {
                            'field_display_name': 'key_0',
                            'field_id': 'field_0',
                            'field_response': 'value_0',
                            'field_type': 'field_type0'
                        },
                        {
                            'field_display_name': 'key_1',
                            'field_id': 'field_1',
                            'field_response': 'value_1',
                            'field_type': 'field_type1'
                        },
                        {
                            'field_display_name': 'key_2',
                            'field_id': 'field_2',
                            'field_response': 'value_2',
                            'field_type': 'field_type2'
                        }
                    ],
                    'title': 'title_9'
                }
            ],
            'total_tasks': 5
        },
        {
            'group_by_display_name': 'display_name_2',
            'group_by_value': 'value_2',
            'tasks': [
                {
                    'description': 'description_10',
                    'due_date': '2020-10-10 05:30:00',
                    'priority': 'LOW',
                    'stage_with_actions': {
                        'actions': [
                            {
                                'action_id': 'action0',
                                'action_type': 'NO_VALIDATIONS',
                                'button_color': 'button_color0',
                                'button_text': 'button_text0'
                            }
                        ],
                        'assignee': {
                            'assignee_id': 'assignee_10',
                            'name': 'name_10',
                            'profile_pic_url': 'profile_pic_10',
                            'team_info': {
                                'team_id': 'team_10',
                                'team_name': 'name_10'
                            }
                        },
                        'stage_color': 'stage_color10',
                        'stage_display_name': 'stage_name10',
                        'stage_id': 10
                    },
                    'start_date': '2020-09-10 05:30:00',
                    'task_id': 'task_display10',
                    'task_overview_fields': [
                        {
                            'field_display_name': 'key_0',
                            'field_id': 'field_0',
                            'field_response': 'value_0',
                            'field_type': 'field_type0'
                        },
                        {
                            'field_display_name': 'key_1',
                            'field_id': 'field_1',
                            'field_response': 'value_1',
                            'field_type': 'field_type1'
                        },
                        {
                            'field_display_name': 'key_2',
                            'field_id': 'field_2',
                            'field_response': 'value_2',
                            'field_type': 'field_type2'
                        }
                    ],
                    'title': 'title_10'
                },
                {
                    'description': 'description_11',
                    'due_date': '2020-10-10 05:30:00',
                    'priority': 'MEDIUM',
                    'stage_with_actions': {
                        'actions': [
                            {
                                'action_id': 'action0',
                                'action_type': 'NO_VALIDATIONS',
                                'button_color': 'button_color0',
                                'button_text': 'button_text0'
                            }
                        ],
                        'assignee': {
                            'assignee_id': 'assignee_11',
                            'name': 'name_11',
                            'profile_pic_url': 'profile_pic_11',
                            'team_info': {
                                'team_id': 'team_11',
                                'team_name': 'name_11'
                            }
                        },
                        'stage_color': 'stage_color11',
                        'stage_display_name': 'stage_name11',
                        'stage_id': 11
                    },
                    'start_date': '2020-09-10 05:30:00',
                    'task_id': 'task_display11',
                    'task_overview_fields': [
                        {
                            'field_display_name': 'key_0',
                            'field_id': 'field_0',
                            'field_response': 'value_0',
                            'field_type': 'field_type0'
                        },
                        {
                            'field_display_name': 'key_1',
                            'field_id': 'field_1',
                            'field_response': 'value_1',
                            'field_type': 'field_type1'
                        },
                        {
                            'field_display_name': 'key_2',
                            'field_id': 'field_2',
                            'field_response': 'value_2',
                            'field_type': 'field_type2'
                        }
                    ],
                    'title': 'title_11'
                },
                {
                    'description': 'description_12',
                    'due_date': '2020-10-10 05:30:00',
                    'priority': 'HIGH',
                    'stage_with_actions': {
                        'actions': [
                            {
                                'action_id': 'action0',
                                'action_type': 'NO_VALIDATIONS',
                                'button_color': 'button_color0',
                                'button_text': 'button_text0'
                            }
                        ],
                        'assignee': {
                            'assignee_id': 'assignee_12',
                            'name': 'name_12',
                            'profile_pic_url': 'profile_pic_12',
                            'team_info': {
                                'team_id': 'team_12',
                                'team_name': 'name_12'
                            }
                        },
                        'stage_color': 'stage_color12',
                        'stage_display_name': 'stage_name12',
                        'stage_id': 12
                    },
                    'start_date': '2020-09-10 05:30:00',
                    'task_id': 'task_display12',
                    'task_overview_fields': [
                        {
                            'field_display_name': 'key_0',
                            'field_id': 'field_0',
                            'field_response': 'value_0',
                            'field_type': 'field_type0'
                        },
                        {
                            'field_display_name': 'key_1',
                            'field_id': 'field_1',
                            'field_response': 'value_1',
                            'field_type': 'field_type1'
                        },
                        {
                            'field_display_name': 'key_2',
                            'field_id': 'field_2',
                            'field_response': 'value_2',
                            'field_type': 'field_type2'
                        }
                    ],
                    'title': 'title_12'
                },
                {
                    'description': 'description_13',
                    'due_date': '2020-10-10 05:30:00',
                    'priority': 'LOW',
                    'stage_with_actions': {
                        'actions': [
                            {
                                'action_id': 'action0',
                                'action_type': 'NO_VALIDATIONS',
                                'button_color': 'button_color0',
                                'button_text': 'button_text0'
                            }
                        ],
                        'assignee': {
                            'assignee_id': 'assignee_13',
                            'name': 'name_13',
                            'profile_pic_url': 'profile_pic_13',
                            'team_info': {
                                'team_id': 'team_13',
                                'team_name': 'name_13'
                            }
                        },
                        'stage_color': 'stage_color13',
                        'stage_display_name': 'stage_name13',
                        'stage_id': 13
                    },
                    'start_date': '2020-09-10 05:30:00',
                    'task_id': 'task_display13',
                    'task_overview_fields': [
                        {
                            'field_display_name': 'key_0',
                            'field_id': 'field_0',
                            'field_response': 'value_0',
                            'field_type': 'field_type0'
                        },
                        {
                            'field_display_name': 'key_1',
                            'field_id': 'field_1',
                            'field_response': 'value_1',
                            'field_type': 'field_type1'
                        },
                        {
                            'field_display_name': 'key_2',
                            'field_id': 'field_2',
                            'field_response': 'value_2',
                            'field_type': 'field_type2'
                        }
                    ],
                    'title': 'title_13'
                },
                {
                    'description': 'description_14',
                    'due_date': '2020-10-10 05:30:00',
                    'priority': 'MEDIUM',
                    'stage_with_actions': {
                        'actions': [
                            {
                                'action_id': 'action0',
                                'action_type': 'NO_VALIDATIONS',
                                'button_color': 'button_color0',
                                'button_text': 'button_text0'
                            }
                        ],
                        'assignee': {
                            'assignee_id': 'assignee_14',
                            'name': 'name_14',
                            'profile_pic_url': 'profile_pic_14',
                            'team_info': {
                                'team_id': 'team_14',
                                'team_name': 'name_14'
                            }
                        },
                        'stage_color': 'stage_color14',
                        'stage_display_name': 'stage_name14',
                        'stage_id': 14
                    },
                    'start_date': '2020-09-10 05:30:00',
                    'task_id': 'task_display14',
                    'task_overview_fields': [
                        {
                            'field_display_name': 'key_0',
                            'field_id': 'field_0',
                            'field_response': 'value_0',
                            'field_type': 'field_type0'
                        },
                        {
                            'field_display_name': 'key_1',
                            'field_id': 'field_1',
                            'field_response': 'value_1',
                            'field_type': 'field_type1'
                        },
                        {
                            'field_display_name': 'key_2',
                            'field_id': 'field_2',
                            'field_response': 'value_2',
                            'field_type': 'field_type2'
                        }
                    ],
                    'title': 'title_14'
                }
            ],
            'total_tasks': 5
        }
    ],
    'total_child_groups': 3
}
