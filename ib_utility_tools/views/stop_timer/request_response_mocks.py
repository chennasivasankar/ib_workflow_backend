

REQUEST_BODY_JSON = """
{
    "entity_id": "7e507b1e-e979-4167-b242-ed2927d42e7a",
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
    "res_status": "TIMER_IS_ALREADY_STOPPED"
}
"""

