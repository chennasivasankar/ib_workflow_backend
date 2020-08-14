

REQUEST_BODY_JSON = """
{
    "entity_id": "5d188d96-756b-4775-8761-c1ac0eb784b6",
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

