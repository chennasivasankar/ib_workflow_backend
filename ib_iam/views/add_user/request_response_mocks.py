

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "2749343c-fe51-40ca-8dc3-26a2cdc48d6c",
    "team_ids": [
        "662fab9f-2e71-438f-910e-7d9961fbed90"
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

