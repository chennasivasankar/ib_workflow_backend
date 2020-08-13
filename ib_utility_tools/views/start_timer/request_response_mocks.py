

REQUEST_BODY_JSON = """
{
    "entity_id": "9cc13508-9755-4a7f-a1f9-217cbc31a742",
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

