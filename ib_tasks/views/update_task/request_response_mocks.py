

REQUEST_BODY_JSON = """
{
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
    "task_details": {
        "template_id": "string",
        "task_id": "string",
        "title": "string",
        "start_date": "2099-12-31 00:00:00",
        "due_date": "2099-12-31 00:00:00",
        "priority": "string",
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

