

REQUEST_BODY_JSON = """
{
    "project_id": "string",
    "task_template_id": "string",
    "action_id": 1,
    "title": "string",
    "description": "string",
    "start_date": "2099-12-31",
    "due_date": {
        "date": "2099-12-31",
        "time": "string"
    },
    "priority": "HIGH",
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


RESPONSE_201_JSON = """
{
    "task_current_stage_details": {
        "task_id": "string",
        "stages": [
            {
                "stage_id": "string",
                "stage_display_name": "string"
            }
        ],
        "user_has_permission": true
    },
    "task_details": {
        "task_id": "string",
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

