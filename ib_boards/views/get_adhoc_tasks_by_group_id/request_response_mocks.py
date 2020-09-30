


RESPONSE_200_JSON = """
{
    "total_tasks": 1,
    "tasks": [
        {
            "task_id": "string",
            "title": "string",
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
                        "transition_template_id": "string",
                        "button_text": "string",
                        "button_color": "string"
                    }
                ]
            }
        }
    ]
}
"""

