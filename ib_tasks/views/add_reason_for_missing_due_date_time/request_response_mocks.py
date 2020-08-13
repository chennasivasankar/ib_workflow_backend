

REQUEST_BODY_JSON = """
{
    "updated_due_date_time": "2099-12-31 00:00:00",
    "reason_id": 1,
    "reason": "string"
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
    "res_status": "INVALID_REASON_ID"
}
"""

RESPONSE_403_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "USER_IS_NOT_ASSIGNED_TO_TASK"
}
"""

