

REQUEST_BODY_JSON = """
{
    "group_by_values": [
        "string"
    ],
    "view_type": "LIST"
}
"""


RESPONSE_200_JSON = """
{
    "total_tasks": 1,
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
    "res_status": "INVALID_PROJECT_ID"
}
"""

RESPONSE_403_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "INVALID_OFFSET_VALUE"
}
"""

