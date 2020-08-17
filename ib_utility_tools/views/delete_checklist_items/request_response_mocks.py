

REQUEST_BODY_JSON = """
{
    "checklist_item_ids": [
        "7363c18d-64d4-46ed-8e7f-346168f0ab04"
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

