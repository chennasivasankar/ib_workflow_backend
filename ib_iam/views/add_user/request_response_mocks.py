

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "a231fcc9-2085-42c8-838c-fbdcb9e13ea5",
    "team_ids": [
        "b345baca-2993-4887-8b8d-57baed6b80f8"
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

