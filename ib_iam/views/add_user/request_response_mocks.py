

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "15ce662f-344b-496d-9e2f-5d9063bc1a97",
    "team_ids": [
        "f8d7ca60-e2cc-4701-b133-5d701dd44720"
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

