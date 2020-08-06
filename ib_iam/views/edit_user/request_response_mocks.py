

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "70f9b21e-0a94-444c-ac72-42bb1de0ff4d",
    "team_ids": [
        "c7453c2b-2380-4633-8597-dd92897c8199"
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

