

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "ac883d5f-8770-46f8-b8f1-272a3297c5d5",
    "team_ids": [
        "4b953221-3cb3-41e4-9f01-ac83db04643a"
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

