

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "e8ef9fe2-cb19-41c9-8f77-34f04c0a27be",
    "team_ids": [
        "6d8f38c3-cf17-479f-a1de-7f43fbf80f65"
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

