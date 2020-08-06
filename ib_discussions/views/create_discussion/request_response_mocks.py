

REQUEST_BODY_JSON = """
{
    "entity_id": "string",
    "entity_type": "TASK",
    "title": "string",
    "description": "string"
}
"""


RESPONSE_404_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "ENTITY_ID_NOT_FOUND"
}
"""

RESPONSE_400_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "EMPTY_TITLE"
}
"""

