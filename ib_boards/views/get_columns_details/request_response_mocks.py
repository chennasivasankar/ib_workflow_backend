

REQUEST_BODY_JSON = """
{
    "view_type": "LIST"
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
    "res_status": "INVALID_BOARD_ID"
}
"""

RESPONSE_400_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "INVALID_OFFSET_VALUE"
}
"""

RESPONSE_200_JSON = """
{
    "total_columns_count": 1,
    "columns": [
        {
            "column_id": "string",
            "name": "string",
            "total_tasks": 1,
            "tasks": [
                {
                    "task_id": "string",
                    "task_overview_fields": [
                        {
                            "field_type": "PLAIN_TEXT",
                            "field_display_name": "string",
                            "field_response": "string",
                            "field_id": "string"
                        }
                    ],
                    "stage_with_actions": {
                        "stage_id": 1,
                        "stage_display_name": "string",
                        "stage_color": "string",
                        "assignee": {
                            "assignee_id": "string",
                            "name": "string",
                            "profile_pic_url": "string"
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
            ]
        }
    ]
}
"""

