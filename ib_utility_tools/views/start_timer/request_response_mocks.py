

REQUEST_BODY_JSON = """
{
    "entity_id": "c5353b5c-be83-462e-a258-d69bb0d500bf",
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

