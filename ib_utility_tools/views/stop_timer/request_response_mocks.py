

REQUEST_BODY_JSON = """
{
    "entity_id": "f50969ce-79d5-4986-a868-92efd46b7592",
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

