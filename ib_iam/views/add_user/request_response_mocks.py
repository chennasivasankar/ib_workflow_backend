

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "21579483-3d41-47bb-99f5-109d1d328a71",
    "team_ids": [
        "55f1c394-64fc-4351-b798-deb8fdb8c8b7"
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

