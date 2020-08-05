

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "0cb35ba4-9042-453d-856d-c21836b69079",
    "team_ids": [
        "f3320917-9f25-4057-80af-c02a6981e39f"
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

