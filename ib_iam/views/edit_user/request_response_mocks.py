

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "12d9ee37-1083-4161-b6a2-6e70d96a32a7",
    "team_ids": [
        "bb21269e-5bf5-4194-8c28-eb0d88aa6a3c"
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

