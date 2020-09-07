

REQUEST_BODY_JSON = """
{
    "field_id": "string",
    "display_order": 1,
    "field_ids": [
        "string"
    ]
}
"""


RESPONSE_200_JSON = """
[
    {
        "field_id": "string",
        "display_name": "string",
        "display_status": "HIDE",
        "display_order": 1
    }
]
"""

RESPONSE_404_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "INVALID_COLUMN_ID"
}
"""

RESPONSE_403_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "USER_NOT_HAVE_ACCESS_TO_COLUMN"
}
"""

RESPONSE_400_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "USER_NOT_HAVE_ACCESS_TO_COLUMN"
}
"""

