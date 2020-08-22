

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
    "task_id": "string",
    "stages": [
        {
            "stage_id": "string",
            "stage_display_name": "string"
        }
    ],
    "user_has_permission": true
}
"""

RESPONSE_400_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "string"
}
"""

