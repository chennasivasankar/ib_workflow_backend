

REQUEST_BODY_JSON = """
{
    "task_id": "string",
    "stage_id": 1
}
"""


RESPONSE_200_JSON = """
[
    {
        "user_id": "string",
        "profile_pic_url": "string",
        "name": "string"
    }
]
"""

RESPONSE_404_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "INVALID_STAGE_ID"
}
"""

RESPONSE_403_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "USER_IS_NOT_ASSIGNED_TO_TASK"
}
"""

