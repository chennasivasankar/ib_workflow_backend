

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "e7dcf6ce-f30a-44f4-a404-e94de0866a84",
    "team_ids": [
        "3fb44fa5-da94-45ad-a4ca-a5ba658c6532"
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

