

REQUEST_BODY_JSON = """
{
    "checklist_item_ids": [
        "12f23eec-8a8e-444c-b3d2-0a202677d431"
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

