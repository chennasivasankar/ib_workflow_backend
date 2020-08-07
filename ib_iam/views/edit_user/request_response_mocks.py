

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "c2bfb414-90bd-4719-a2a8-0050e50baffe",
    "team_ids": [
        "df470182-0f03-4851-9be7-e647fdc57517"
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

