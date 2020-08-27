

REQUEST_BODY_JSON = """
{
    "entity_id": "251b68cf-510d-4590-89e3-e2b7691fe16b",
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

