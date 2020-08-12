

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "38068f28-6bc3-4b55-9c3f-3368243142fc",
    "team_ids": [
        "eacf2d98-768c-4ef8-a38f-6fb603bedc2c"
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

