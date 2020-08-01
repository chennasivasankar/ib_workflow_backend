


RESPONSE_200_JSON = """
{
    "tasks": [
        {
            "task_id": 1,
            "task_overview_fields": [
                {
                    "field_type": "PLAIN_TEXT",
                    "field_display_name": "string",
                    "field_response": "string"
                }
            ],
            "stage_with_actions": {
                "stage_id": "string",
                "stage_display_name": "string",
                "actions": [
                    {
                        "action_id": 1,
                        "button_text": "string",
                        "button_color": "string"
                    }
                ]
            }
        }
    ],
    "total_tasks": 1
}
"""

RESPONSE_400_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "LIMIT_SHOULD_BE_GREATER_THAN_ZERO"
}
"""

