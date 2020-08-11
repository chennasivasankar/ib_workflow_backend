

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "0bb346bf-75eb-4784-a63d-88ac60f6c23d",
    "team_ids": [
        "f4a8267c-cb02-4ea1-b86c-9bcba0c20876"
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

