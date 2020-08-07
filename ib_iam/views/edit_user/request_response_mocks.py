

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "37455b8c-02a6-4f19-b438-a6687ff87ea1",
    "team_ids": [
        "991628ca-b639-4769-a088-75fb64dd8f0f"
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

