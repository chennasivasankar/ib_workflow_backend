

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "f0dd8842-1b17-4958-879e-02bb99ac6da1",
    "team_ids": [
        "6961c3ba-28bb-4c71-8c74-84e089100f43"
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

