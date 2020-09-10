# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestGetColumnDetails.test_get_response_for_column_details_with_duplicate_tasks_in_same_column column_details_with_duplicates'] = {
    'columns': [
        {
            'column_id': 'COLUMN_ID_1',
            'name': 'COLUMN_DISPLAY_NAME_1',
            'tasks': [
                {
                    'stage_with_actions': {
                        'actions': [
                            {
                                'action_id': 'action_id_0',
                                'action_type': 'action_type_0',
                                'button_color': None,
                                'button_text': 'button_text_0',
                                'transition_template_id': 'template_0'
                            },
                            {
                                'action_id': 'action_id_3',
                                'action_type': 'action_type_3',
                                'button_color': None,
                                'button_text': 'button_text_3',
                                'transition_template_id': None
                            }
                        ],
                        'assignee': {
                            'assignee_id': '123e4567-e89b-12d3-a456-426614174000',
                            'name': 'name_0',
                            'profile_pic_url': 'https://www.google.com/search?q=ibhubs&client=ubuntu&hs=DI7&channel=fs&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjZqYjthYfrAhUF4zgGHevjDZUQ_AUoA3oECAsQBQ&biw=1848&bih=913#imgrc=Kg3TRY0jmx3udM'
                        },
                        'stage_color': 'blue',
                        'stage_display_name': 'stage',
                        'stage_id': 0
                    },
                    'task_id': 'task_id_0',
                    'task_overview_fields': [
                        {
                            'field_display_name': 'key_0',
                            'field_response': 'value_0'
                        },
                        {
                            'field_display_name': 'key_3',
                            'field_response': 'value_3'
                        }
                    ]
                }
            ],
            'total_tasks': 1
        },
        {
            'column_id': 'COLUMN_ID_2',
            'name': 'COLUMN_DISPLAY_NAME_2',
            'tasks': [
                {
                    'stage_with_actions': {
                        'actions': [
                            {
                                'action_id': 'action_id_1',
                                'action_type': 'action_type_1',
                                'button_color': None,
                                'button_text': 'button_text_1',
                                'transition_template_id': 'template_1'
                            }
                        ],
                        'assignee': {
                            'assignee_id': '123e4567-e89b-12d3-a456-426614174001',
                            'name': 'name_1',
                            'profile_pic_url': 'https://www.google.com/search?q=ibhubs&client=ubuntu&hs=DI7&channel=fs&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjZqYjthYfrAhUF4zgGHevjDZUQ_AUoA3oECAsQBQ&biw=1848&bih=913#imgrc=Kg3TRY0jmx3udM'
                        },
                        'stage_color': 'orange',
                        'stage_display_name': 'stage',
                        'stage_id': 1
                    },
                    'task_id': 'task_id_1',
                    'task_overview_fields': [
                        {
                            'field_display_name': 'key_1',
                            'field_response': 'value_1'
                        }
                    ]
                }
            ],
            'total_tasks': 1
        },
        {
            'column_id': 'COLUMN_ID_3',
            'name': 'COLUMN_DISPLAY_NAME_3',
            'tasks': [
                {
                    'stage_with_actions': {
                        'actions': [
                            {
                                'action_id': 'action_id_2',
                                'action_type': 'action_type_2',
                                'button_color': None,
                                'button_text': 'button_text_2',
                                'transition_template_id': 'template_2'
                            }
                        ],
                        'assignee': {
                            'assignee_id': '123e4567-e89b-12d3-a456-426614174002',
                            'name': 'name_2',
                            'profile_pic_url': 'https://www.google.com/search?q=ibhubs&client=ubuntu&hs=DI7&channel=fs&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjZqYjthYfrAhUF4zgGHevjDZUQ_AUoA3oECAsQBQ&biw=1848&bih=913#imgrc=Kg3TRY0jmx3udM'
                        },
                        'stage_color': 'green',
                        'stage_display_name': 'stage',
                        'stage_id': 2
                    },
                    'task_id': 'task_id_2',
                    'task_overview_fields': [
                        {
                            'field_display_name': 'key_2',
                            'field_response': 'value_2'
                        }
                    ]
                }
            ],
            'total_tasks': 1
        }
    ],
    'total_columns_count': 3
}

snapshots['TestGetColumnDetails.test_with_duplicate_tasks_in_same_column_and_duplicate_fields column_details_with_duplicates_fields'] = {
    'columns': [
        {
            'column_id': 'COLUMN_ID_1',
            'name': 'COLUMN_DISPLAY_NAME_1',
            'tasks': [
                {
                    'stage_with_actions': {
                        'actions': [
                            {
                                'action_id': 'action_id_0',
                                'action_type': 'action_type_0',
                                'button_color': None,
                                'button_text': 'button_text_0',
                                'transition_template_id': 'template_0'
                            }
                        ],
                        'assignee': {
                            'assignee_id': '123e4567-e89b-12d3-a456-426614174004',
                            'name': 'name_4',
                            'profile_pic_url': 'https://www.google.com/search?q=ibhubs&client=ubuntu&hs=DI7&channel=fs&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjZqYjthYfrAhUF4zgGHevjDZUQ_AUoA3oECAsQBQ&biw=1848&bih=913#imgrc=Kg3TRY0jmx3udM'
                        },
                        'stage_color': 'blue',
                        'stage_display_name': 'stage',
                        'stage_id': 0
                    },
                    'task_id': 'task_id_0',
                    'task_overview_fields': [
                        {
                            'field_display_name': 'key_0',
                            'field_response': 'value_0'
                        }
                    ]
                }
            ],
            'total_tasks': 1
        },
        {
            'column_id': 'COLUMN_ID_2',
            'name': 'COLUMN_DISPLAY_NAME_2',
            'tasks': [
                {
                    'stage_with_actions': {
                        'actions': [
                            {
                                'action_id': 'action_id_1',
                                'action_type': 'action_type_1',
                                'button_color': None,
                                'button_text': 'button_text_1',
                                'transition_template_id': 'template_1'
                            }
                        ],
                        'assignee': {
                            'assignee_id': '123e4567-e89b-12d3-a456-426614174005',
                            'name': 'name_5',
                            'profile_pic_url': 'https://www.google.com/search?q=ibhubs&client=ubuntu&hs=DI7&channel=fs&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjZqYjthYfrAhUF4zgGHevjDZUQ_AUoA3oECAsQBQ&biw=1848&bih=913#imgrc=Kg3TRY0jmx3udM'
                        },
                        'stage_color': 'orange',
                        'stage_display_name': 'stage',
                        'stage_id': 1
                    },
                    'task_id': 'task_id_1',
                    'task_overview_fields': [
                        {
                            'field_display_name': 'key_1',
                            'field_response': 'value_1'
                        }
                    ]
                }
            ],
            'total_tasks': 1
        },
        {
            'column_id': 'COLUMN_ID_3',
            'name': 'COLUMN_DISPLAY_NAME_3',
            'tasks': [
                {
                    'stage_with_actions': {
                        'actions': [
                            {
                                'action_id': 'action_id_2',
                                'action_type': 'action_type_2',
                                'button_color': None,
                                'button_text': 'button_text_2',
                                'transition_template_id': 'template_2'
                            }
                        ],
                        'assignee': {
                            'assignee_id': '123e4567-e89b-12d3-a456-426614174006',
                            'name': 'name_6',
                            'profile_pic_url': 'https://www.google.com/search?q=ibhubs&client=ubuntu&hs=DI7&channel=fs&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjZqYjthYfrAhUF4zgGHevjDZUQ_AUoA3oECAsQBQ&biw=1848&bih=913#imgrc=Kg3TRY0jmx3udM'
                        },
                        'stage_color': 'green',
                        'stage_display_name': 'stage',
                        'stage_id': 2
                    },
                    'task_id': 'task_id_2',
                    'task_overview_fields': [
                        {
                            'field_display_name': 'key_2',
                            'field_response': 'value_2'
                        }
                    ]
                }
            ],
            'total_tasks': 1
        }
    ],
    'total_columns_count': 3
}

snapshots['TestGetColumnDetails.test_get_response_for_column_details_with_proper_data column_details_with_proper_data'] = {
    'columns': [
        {
            'column_id': 'COLUMN_ID_1',
            'name': 'COLUMN_DISPLAY_NAME_1',
            'tasks': [
                {
                    'stage_with_actions': {
                        'actions': [
                            {
                                'action_id': 'action_id_0',
                                'action_type': 'action_type_0',
                                'button_color': None,
                                'button_text': 'button_text_0',
                                'transition_template_id': 'template_0'
                            }
                        ],
                        'assignee': {
                            'assignee_id': '123e4567-e89b-12d3-a456-426614174008',
                            'name': 'name_8',
                            'profile_pic_url': 'https://www.google.com/search?q=ibhubs&client=ubuntu&hs=DI7&channel=fs&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjZqYjthYfrAhUF4zgGHevjDZUQ_AUoA3oECAsQBQ&biw=1848&bih=913#imgrc=Kg3TRY0jmx3udM'
                        },
                        'stage_color': 'blue',
                        'stage_display_name': 'stage',
                        'stage_id': 0
                    },
                    'task_id': 'task_id_0',
                    'task_overview_fields': [
                        {
                            'field_display_name': 'key_0',
                            'field_response': 'value_0'
                        }
                    ]
                }
            ],
            'total_tasks': 1
        },
        {
            'column_id': 'COLUMN_ID_2',
            'name': 'COLUMN_DISPLAY_NAME_2',
            'tasks': [
                {
                    'stage_with_actions': {
                        'actions': [
                            {
                                'action_id': 'action_id_1',
                                'action_type': 'action_type_1',
                                'button_color': None,
                                'button_text': 'button_text_1',
                                'transition_template_id': 'template_1'
                            }
                        ],
                        'assignee': {
                            'assignee_id': '123e4567-e89b-12d3-a456-426614174009',
                            'name': 'name_9',
                            'profile_pic_url': 'https://www.google.com/search?q=ibhubs&client=ubuntu&hs=DI7&channel=fs&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjZqYjthYfrAhUF4zgGHevjDZUQ_AUoA3oECAsQBQ&biw=1848&bih=913#imgrc=Kg3TRY0jmx3udM'
                        },
                        'stage_color': 'orange',
                        'stage_display_name': 'stage',
                        'stage_id': 1
                    },
                    'task_id': 'task_id_1',
                    'task_overview_fields': [
                        {
                            'field_display_name': 'key_1',
                            'field_response': 'value_1'
                        }
                    ]
                }
            ],
            'total_tasks': 1
        },
        {
            'column_id': 'COLUMN_ID_3',
            'name': 'COLUMN_DISPLAY_NAME_3',
            'tasks': [
                {
                    'stage_with_actions': {
                        'actions': [
                            {
                                'action_id': 'action_id_2',
                                'action_type': 'action_type_2',
                                'button_color': None,
                                'button_text': 'button_text_2',
                                'transition_template_id': 'template_2'
                            }
                        ],
                        'assignee': {
                            'assignee_id': '123e4567-e89b-12d3-a456-4266141740010',
                            'name': 'name_10',
                            'profile_pic_url': 'https://www.google.com/search?q=ibhubs&client=ubuntu&hs=DI7&channel=fs&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjZqYjthYfrAhUF4zgGHevjDZUQ_AUoA3oECAsQBQ&biw=1848&bih=913#imgrc=Kg3TRY0jmx3udM'
                        },
                        'stage_color': 'green',
                        'stage_display_name': 'stage',
                        'stage_id': 2
                    },
                    'task_id': 'task_id_2',
                    'task_overview_fields': [
                        {
                            'field_display_name': 'key_2',
                            'field_response': 'value_2'
                        }
                    ]
                }
            ],
            'total_tasks': 1
        }
    ],
    'total_columns_count': 3
}

snapshots['TestGetColumnDetails.test_get_response_for_column_details_with_no_tasks column_details_with_proper_data'] = {
    'columns': [
        {
            'column_id': 'COLUMN_ID_1',
            'name': 'COLUMN_DISPLAY_NAME_1',
            'tasks': [
            ],
            'total_tasks': 1
        },
        {
            'column_id': 'COLUMN_ID_2',
            'name': 'COLUMN_DISPLAY_NAME_2',
            'tasks': [
            ],
            'total_tasks': 1
        },
        {
            'column_id': 'COLUMN_ID_3',
            'name': 'COLUMN_DISPLAY_NAME_3',
            'tasks': [
            ],
            'total_tasks': 1
        }
    ],
    'total_columns_count': 3
}
