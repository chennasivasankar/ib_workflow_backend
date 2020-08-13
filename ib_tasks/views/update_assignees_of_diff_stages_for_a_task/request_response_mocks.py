

REQUEST_BODY_JSON = """
{
    "task_id": "string",
    "stage_assignees": [
        {
            "stage_id": 1,
            "assignee_id": "string"
        }
    ]
}
"""


RESPONSE_400_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "DUPLICATE_STAGE_IDS"
}
"""

RESPONSE_404_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "INVALID_TASK_ID"
}
"""

