

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "f3f9bb71-f65d-431a-b8d8-0c3f31f9d7a4",
    "team_ids": [
        "c1035f74-0c83-4edf-b589-4213a50775cd"
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

