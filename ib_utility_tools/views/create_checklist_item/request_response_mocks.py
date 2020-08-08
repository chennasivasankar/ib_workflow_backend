

REQUEST_BODY_JSON = """
{
    "entity_id": "string",
    "entity_type": "TASK",
    "text": "string",
    "is_checked": true
}
"""


RESPONSE_201_JSON = """
{
    "checklist_item_id": "string"
}
"""

RESPONSE_400_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "EMPTY_CHECKLIST_ITEM_TEXT"
}
"""

