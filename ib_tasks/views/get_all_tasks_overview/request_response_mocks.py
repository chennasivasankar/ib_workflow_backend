


RESPONSE_200_JSON = """
{
    "tasks": [
        {
            "task_id": 1,
            "transition_template_id": "string",
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
                "actions": [
                    {
                        "action_id": 1,
                        "action_type": "NO_VALIDATIONS",
                        "button_text": "string",
                        "button_color": "string",
                        "transition_template_id": "string"
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

