


RESPONSE_403_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "USER_DONOT_HAVE_ACCESS"
}
"""

RESPONSE_400_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "INVALID_OFFSET_VALUE"
}
"""

RESPONSE_404_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "INVALID_COLUMN_ID"
}
"""

RESPONSE_200_JSON = """
{
    "total_tasks_count": 1,
    "tasks": [
        {
            "task_id": "string",
            "fields": [
                {
                    "field_type": "string",
                    "key": "string",
                    "value": "string"
                }
            ],
            "actions": [
                {
                    "action_id": "string",
                    "display_name": "string",
                    "button_text": "string",
                    "button_color": "string"
                }
            ]
        }
    ]
}
"""

