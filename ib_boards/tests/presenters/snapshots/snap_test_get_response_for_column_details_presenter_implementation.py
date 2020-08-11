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
                    'actions': [
                        {
                            'action_id': 'action_id_0',
                            'button_color': None,
                            'button_text': 'button_text_0',
                            'name': 'name_0',
                            'transition_template_id': 'template_0'
                        },
                        {
                            'action_id': 'action_id_3',
                            'button_color': None,
                            'button_text': 'button_text_3',
                            'name': 'name_3',
                            'transition_template_id': None
                        }
                    ],
                    'fields': [
                        {
                            'field_type': 'field_type_0',
                            'key': 'key_0',
                            'value': 'value_0'
                        },
                        {
                            'field_type': 'field_type_3',
                            'key': 'key_3',
                            'value': 'value_3'
                        }
                    ],
                    'stage_color': 'blue',
                    'task_id': 'task_id_0'
                }
            ],
            'total_tasks_count': 1
        },
        {
            'column_id': 'COLUMN_ID_2',
            'name': 'COLUMN_DISPLAY_NAME_2',
            'tasks': [
                {
                    'actions': [
                        {
                            'action_id': 'action_id_1',
                            'button_color': None,
                            'button_text': 'button_text_1',
                            'name': 'name_1',
                            'transition_template_id': 'template_1'
                        }
                    ],
                    'fields': [
                        {
                            'field_type': 'field_type_1',
                            'key': 'key_1',
                            'value': 'value_1'
                        }
                    ],
                    'stage_color': 'orange',
                    'task_id': 'task_id_1'
                }
            ],
            'total_tasks_count': 1
        },
        {
            'column_id': 'COLUMN_ID_3',
            'name': 'COLUMN_DISPLAY_NAME_3',
            'tasks': [
                {
                    'actions': [
                        {
                            'action_id': 'action_id_2',
                            'button_color': None,
                            'button_text': 'button_text_2',
                            'name': 'name_2',
                            'transition_template_id': 'template_2'
                        }
                    ],
                    'fields': [
                        {
                            'field_type': 'field_type_2',
                            'key': 'key_2',
                            'value': 'value_2'
                        }
                    ],
                    'stage_color': 'green',
                    'task_id': 'task_id_2'
                }
            ],
            'total_tasks_count': 1
        }
    ],
    'total_columns_count': 4
}

snapshots['TestGetColumnDetails.test_with_duplicate_tasks_in_same_column_and_duplicate_fields column_details_with_duplicates_fields'] = {
    'columns': [
        {
            'column_id': 'COLUMN_ID_1',
            'name': 'COLUMN_DISPLAY_NAME_1',
            'tasks': [
                {
                    'actions': [
                        {
                            'action_id': 'action_id_0',
                            'button_color': None,
                            'button_text': 'button_text_0',
                            'name': 'name_0',
                            'transition_template_id': 'template_0'
                        }
                    ],
                    'fields': [
                        {
                            'field_type': 'field_type_0',
                            'key': 'key_0',
                            'value': 'value_0'
                        }
                    ],
                    'stage_color': 'blue',
                    'task_id': 'task_id_0'
                }
            ],
            'total_tasks_count': 1
        },
        {
            'column_id': 'COLUMN_ID_2',
            'name': 'COLUMN_DISPLAY_NAME_2',
            'tasks': [
                {
                    'actions': [
                        {
                            'action_id': 'action_id_1',
                            'button_color': None,
                            'button_text': 'button_text_1',
                            'name': 'name_1',
                            'transition_template_id': 'template_1'
                        }
                    ],
                    'fields': [
                        {
                            'field_type': 'field_type_1',
                            'key': 'key_1',
                            'value': 'value_1'
                        }
                    ],
                    'stage_color': 'orange',
                    'task_id': 'task_id_1'
                }
            ],
            'total_tasks_count': 1
        },
        {
            'column_id': 'COLUMN_ID_3',
            'name': 'COLUMN_DISPLAY_NAME_3',
            'tasks': [
                {
                    'actions': [
                        {
                            'action_id': 'action_id_2',
                            'button_color': None,
                            'button_text': 'button_text_2',
                            'name': 'name_2',
                            'transition_template_id': 'template_2'
                        }
                    ],
                    'fields': [
                        {
                            'field_type': 'field_type_2',
                            'key': 'key_2',
                            'value': 'value_2'
                        }
                    ],
                    'stage_color': 'green',
                    'task_id': 'task_id_2'
                }
            ],
            'total_tasks_count': 1
        }
    ],
    'total_columns_count': 4
}

snapshots['TestGetColumnDetails.test_get_response_for_column_details_with_proper_data column_details_with_proper_data'] = {
    'columns': [
        {
            'column_id': 'COLUMN_ID_1',
            'name': 'COLUMN_DISPLAY_NAME_1',
            'tasks': [
                {
                    'actions': [
                        {
                            'action_id': 'action_id_0',
                            'button_color': None,
                            'button_text': 'button_text_0',
                            'name': 'name_0',
                            'transition_template_id': 'template_0'
                        }
                    ],
                    'fields': [
                        {
                            'field_type': 'field_type_6',
                            'key': 'key_6',
                            'value': 'value_6'
                        }
                    ],
                    'stage_color': 'blue',
                    'task_id': 'task_id_0'
                }
            ],
            'total_tasks_count': 1
        },
        {
            'column_id': 'COLUMN_ID_2',
            'name': 'COLUMN_DISPLAY_NAME_2',
            'tasks': [
                {
                    'actions': [
                        {
                            'action_id': 'action_id_1',
                            'button_color': None,
                            'button_text': 'button_text_1',
                            'name': 'name_1',
                            'transition_template_id': 'template_1'
                        }
                    ],
                    'fields': [
                        {
                            'field_type': 'field_type_0',
                            'key': 'key_0',
                            'value': 'value_0'
                        },
                        {
                            'field_type': 'field_type_1',
                            'key': 'key_1',
                            'value': 'value_1'
                        },
                        {
                            'field_type': 'field_type_2',
                            'key': 'key_2',
                            'value': 'value_2'
                        }
                    ],
                    'stage_color': 'orange',
                    'task_id': 'task_id_1'
                }
            ],
            'total_tasks_count': 1
        },
        {
            'column_id': 'COLUMN_ID_3',
            'name': 'COLUMN_DISPLAY_NAME_3',
            'tasks': [
                {
                    'actions': [
                        {
                            'action_id': 'action_id_2',
                            'button_color': None,
                            'button_text': 'button_text_2',
                            'name': 'name_2',
                            'transition_template_id': 'template_2'
                        }
                    ],
                    'fields': [
                        {
                            'field_type': 'field_type_3',
                            'key': 'key_0',
                            'value': 'value_3'
                        },
                        {
                            'field_type': 'field_type_5',
                            'key': 'key_1',
                            'value': 'value_5'
                        },
                        {
                            'field_type': 'field_type_4',
                            'key': 'key_4',
                            'value': 'value_4'
                        }
                    ],
                    'stage_color': 'green',
                    'task_id': 'task_id_2'
                }
            ],
            'total_tasks_count': 1
        }
    ],
    'total_columns_count': 4
}

snapshots['TestGetColumnDetails.test_get_response_for_column_details_with_no_tasks column_details_with_proper_data'] = {
    'columns': [
        {
            'column_id': 'COLUMN_ID_1',
            'name': 'COLUMN_DISPLAY_NAME_1',
            'tasks': [
            ],
            'total_tasks_count': 1
        },
        {
            'column_id': 'COLUMN_ID_2',
            'name': 'COLUMN_DISPLAY_NAME_2',
            'tasks': [
            ],
            'total_tasks_count': 1
        },
        {
            'column_id': 'COLUMN_ID_3',
            'name': 'COLUMN_DISPLAY_NAME_3',
            'tasks': [
            ],
            'total_tasks_count': 1
        }
    ],
    'total_columns_count': 4
}
