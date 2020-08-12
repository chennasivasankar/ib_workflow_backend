

REQUEST_BODY_JSON = """
{
    "task_id": "string",
    "stage_id": "string"
}
"""


RESPONSE_200_JSON = """
[
    {
        "id": "string",
        "name": "string",
        "profile_pic": "string"
    }
]
"""

RESPONSE_400_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "LIMIT_SHOULD_BE_GREATER_THAN_ZERO"
}
"""

RESPONSE_404_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "INVALID_TASK_ID"
}
"""

