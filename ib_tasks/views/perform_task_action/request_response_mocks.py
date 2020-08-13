

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
                "actions": [
                    {
                        "action_id": "string",
                        "name": "string",
                        "button_text": "string",
                        "button_color": "string"
                    }
                ],
                "fields": [
                    {
                        "field_type": "string",
                        "key": "string",
                        "value": "string"
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

