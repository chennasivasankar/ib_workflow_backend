

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "37f0f53d-7e94-438c-87e5-20266fe6e6c1",
    "team_ids": [
        "a06fda24-9331-456d-98a9-e971a6f7ee06"
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

