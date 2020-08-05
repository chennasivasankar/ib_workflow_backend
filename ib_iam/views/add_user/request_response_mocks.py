

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "921fa61a-e552-49c4-9db4-5a11ac577975",
    "team_ids": [
        "e93f61c0-b229-4e14-abdb-b9c67c365329"
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

