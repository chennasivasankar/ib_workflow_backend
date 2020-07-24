

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "596ace0c-1c24-47db-a217-f13e37e8ade4",
    "team_ids": [
        "f1efb907-c550-43d4-a995-7b9260528b49"
    ],
    "role_ids": [
        "string"
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

