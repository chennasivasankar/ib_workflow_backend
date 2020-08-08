

REQUEST_BODY_JSON = """
{
    "updated_due_date_time": "2099-12-31 00:00:00",
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
    "res_status": "INVALID_REASON"
}
"""

RESPONSE_403_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "TASK_IS_NOT_ASSIGNED_TO_TASK"
}
"""

