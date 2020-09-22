

REQUEST_BODY_JSON = """
{
    "project_id": "string",
    "task_template_id": "string",
    "action_id": 1,
    "parent_task_id": "string",
    "title": "string",
    "description": "string",
    "start_datetime": "2099-12-31 00:00:00",
    "due_datetime": "2099-12-31 00:00:00",
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
    "response": "string",
    "http_status_code": 1,
    "res_status": "string"
}
"""

RESPONSE_400_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "string"
}
"""

RESPONSE_403_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "USER_DO_NOT_HAVE_ACCESS"
}
"""

