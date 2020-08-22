

REQUEST_BODY_JSON = """
{
    "entity_id": "ecf2a227-7852-45f6-9ba0-ed0a46fc3cf5",
    "entity_type": "STAGE_TASK"
}
"""


RESPONSE_200_JSON = """
{
    "duration_in_seconds": 1,
    "is_running": true
}
"""

RESPONSE_400_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "TIMER_IS_ALREADY_RUNNING"
}
"""

