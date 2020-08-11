

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "6a7bb1e2-1558-4462-a1e0-1c0ff80ff70e",
    "team_ids": [
        "19da7494-3f22-424f-9477-a7323f56723a"
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

