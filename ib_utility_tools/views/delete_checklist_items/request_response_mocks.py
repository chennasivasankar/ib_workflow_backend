

REQUEST_BODY_JSON = """
{
    "checklist_item_ids": [
        "5deebcc2-e0bf-489e-879d-a27f13341a90"
    ]
}
"""


RESPONSE_400_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "DUPLICATE_CHECKLIST_ITEM_IDS"
}
"""

RESPONSE_404_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "CHECKLIST_ITEM_IDS_NOT_FOUND"
}
"""

