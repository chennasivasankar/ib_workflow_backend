

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "ee866cec-739f-4ee5-8c15-772c17cff907",
    "team_ids": [
        "d0164f78-671d-44f1-9581-70b36d4ccc03"
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

