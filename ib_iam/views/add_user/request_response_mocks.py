

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "1428431c-02aa-42d7-9251-11586db65832",
    "team_ids": [
        "cce106a1-33d5-4576-b5c2-327936365159"
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

