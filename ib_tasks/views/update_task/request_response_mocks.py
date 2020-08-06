

REQUEST_BODY_JSON = """
{
    "task_id": 1,
    "title": "string",
    "description": "string",
    "start_date": "2099-12-31",
    "due_date": "2099-12-31",
    "priority": "HIGH",
    "stage_assignee": {
        "stage_id": 1,
        "assignee_id": "string"
    },
    "task_gofs": [
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
    ]
}
"""


RESPONSE_400_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "INVALID_TASK_ID"
}
"""

