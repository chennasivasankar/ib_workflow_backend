

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "147a1ec9-02c8-4aa6-8587-7b79b617d8c8",
    "team_ids": [
        "f5ca5228-795f-4a61-95d9-cde8e0fa9c3d"
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

