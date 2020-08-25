

REQUEST_BODY_JSON = """
{
    "entity_id": "463473ec-6c6f-4945-b0c3-7a862df1e66d",
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

