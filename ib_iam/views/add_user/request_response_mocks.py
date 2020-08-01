

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "15558092-b36d-4351-9fc9-bbd5973b0ac1",
    "team_ids": [
        "3d0947f4-3a58-43b5-b5d5-f444ab98cd45"
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

