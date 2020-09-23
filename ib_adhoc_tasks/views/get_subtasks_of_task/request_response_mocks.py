

REQUEST_BODY_JSON = """
{
    "task_id": "string",
    "view_type": "LIST"
}
"""


RESPONSE_200_JSON = """
{
    "parent_task_id": "string",
    "tasks": [
        {
            "task_id": "string",
            "title": "string",
            "description": "string",
            "start_date": "2099-12-31 00:00:00",
            "due_date": "2099-12-31 00:00:00",
            "priority": "string",
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
                        "button_text": "string",
                        "button_color": "string"
                    }
                ]
            }
        }
    ]
}
"""

RESPONSE_404_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "INVALID_TASK_ID"
}
"""

RESPONSE_400_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "INVALID_OFFSET_VALUE"
}
"""

