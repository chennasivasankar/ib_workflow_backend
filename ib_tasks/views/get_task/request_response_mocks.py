


RESPONSE_200_JSON = """
{
    "task_id": 1,
    "template_id": "string",
    "title": "string",
    "description": "string",
    "start_date": "string",
    "due_date": "string",
    "priority": "HIGH",
    "gofs": [
        {
            "gof_id": "string",
            "same_gof_order": 1.1,
            "gof_fields": [
                {
                    "field_id": "string",
                    "field_response": "string"
                }
            ]
        }
    ],
    "stages_with_actions": [
        {
            "stage_id": "string",
            "stage_display_name": "string",
            "stage_color": "string",
            "assignee": {
                "id": "string",
                "name": "string",
                "profile_pic": "string"
            },
            "actions": [
                {
                    "action_id": 1,
                    "button_text": "string",
                    "button_color": "string",
                    "action_type": "NO_VALIDATIONS",
                    "transition_template_id": "string"
                }
            ]
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

