

REQUEST_BODY_JSON = """
{
    "checklist_item_ids": [
        "f1da5a88-bce5-4e01-958f-bdc8e8b2f96f"
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

