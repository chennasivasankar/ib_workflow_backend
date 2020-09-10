

REQUEST_BODY_JSON = """
{
    "action_id": "string",
    "board_id": "string",
    "task_id": "string",
    "title": "string",
    "description": "string",
    "start_datetime": "2099-12-31 00:00:00",
    "due_datetime": "2099-12-31 00:00:00",
    "priority": "HIGH",
    "stage_assignee": {
        "stage_id": 1,
        "assignee_id": "string",
        "team_id": "string"
    },
    "task_gofs": [
        {
            "gof_id": "string",
            "same_gof_order": 1,
            "gof_fields": [
                {
                    "field_id": "string",
                    "field_response": "string"
                }
            ]
        }
    ]
}
"""


RESPONSE_200_JSON = """
{
    "task_id": "string",
    "current_board_details": {
        "board_id": "string",
        "board_name": "string",
        "column_details": [
            {
                "column_id": "string",
                "column_name": "string",
                "stage_with_actions": {
                    "stage_id": 1,
                    "stage_display_name": "string",
                    "stage_color": "string",
                    "assignee": {
                        "assignee_id": "string",
                        "name": "string",
                        "profile_pic_url": "string",
                        "team_info": {
                            "team_id": "string",
                            "team_name": "string"
                        }
                    },
                    "actions": [
                        {
                            "action_id": 1,
                            "action_type": "NO_VALIDATIONS",
                            "transition_template_id": "string",
                            "button_text": "string",
                            "button_color": "string"
                        }
                    ]
                },
                "task_overview_fields": [
                    {
                        "field_type": "PLAIN_TEXT",
                        "field_display_name": "string",
                        "field_response": "string"
                    }
                ]
            }
        ]
    },
    "other_board_details": [
        {
            "board_id": "string",
            "board_name": "string",
            "column_details": [
                {
                    "column_id": "string",
                    "column_name": "string"
                }
            ]
        }
    ],
    "task_current_stages_details": {
        "task_id": "string",
        "stages": [
            {
                "stage_id": "string",
                "stage_display_name": "string"
            }
        ],
        "user_has_permission": true
    },
    "task_details": {
        "task_id": "string",
        "task_overview_fields": [
            {
                "field_type": "PLAIN_TEXT",
                "field_display_name": "string",
                "field_response": "string"
            }
        ],
        "stage_with_actions": {
            "stage_id": 1,
            "stage_display_name": "string",
            "stage_color": "string",
            "assignee": {
                "assignee_id": "string",
                "name": "string",
                "profile_pic_url": "string",
                "team_info": {
                    "team_id": "string",
                    "team_name": "string"
                }
            },
            "actions": [
                {
                    "action_id": 1,
                    "action_type": "NO_VALIDATIONS",
                    "transition_template_id": "string",
                    "button_text": "string",
                    "button_color": "string"
                }
            ]
        }
    }
}
"""

RESPONSE_400_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "string"
}
"""

