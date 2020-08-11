


RESPONSE_200_JSON = """
[
    {
        "task_id": 1,
        "due_date_time": "2099-12-31 00:00:00",
        "due_missed_count": 1,
        "reason": "string",
        "user": {
            "user_id": "string",
            "name": "string",
            "profile_pic": "string"
        }
    }
]
"""

RESPONSE_404_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "INVALID_TASK_ID"
}
"""

RESPONSE_403_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "USER_IS_NOT_ASSIGNED_TO_TASK"
}
"""

