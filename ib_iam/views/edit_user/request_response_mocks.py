

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "9469bd8e-0863-4fd9-98ba-0adc6dfef650",
    "team_ids": [
        "d03ad005-a991-41db-a4c7-c5dda6b0d0ec"
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

