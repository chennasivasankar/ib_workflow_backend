

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "f22eb559-b83c-4fe0-b097-caf3a2b8883b",
    "team_ids": [
        "afacb5f7-5de3-4804-ab87-dd7fba471871"
    ]
}
"""


RESPONSE_400_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "INVALID_EMAIL"
}
"""

RESPONSE_403_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "USER_DOES_NOT_HAVE_PERMISSION"
}
"""

RESPONSE_404_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "INVALID_COMPANY_ID"
}
"""

