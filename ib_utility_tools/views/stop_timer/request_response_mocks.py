

REQUEST_BODY_JSON = """
{
    "entity_id": "ba8984b0-43c6-4353-8f48-fd4656e03139",
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

