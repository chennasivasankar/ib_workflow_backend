

REQUEST_BODY_JSON = """
{
    "checklist_item_ids": [
        "89d96f4b-c19d-4e69-8eae-e818f3123b09"
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

