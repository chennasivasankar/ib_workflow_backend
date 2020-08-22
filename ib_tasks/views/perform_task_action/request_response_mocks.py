

REQUEST_BODY_JSON = """
{
    "board_id": "string",
    "task_id": "string",
    "action_id": "string"
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
                        "team_info": [
                            {
                                "team_id": "string",
                                "team_name": "string"
                            }
                        ]
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
    }
}
"""

RESPONSE_403_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "USER_DONOT_HAVE_ACCESS"
}
"""

RESPONSE_404_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "INVALID_ACTION_ID"
}
"""

