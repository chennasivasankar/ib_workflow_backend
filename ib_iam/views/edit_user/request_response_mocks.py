

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "d65a4669-826b-4d34-9742-e1628cbce03b",
    "team_ids": [
        "d5e7b11f-18ce-4747-bb44-e9a7fcbeb6fa"
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

