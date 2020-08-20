

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "090b5526-1385-45d3-ab71-308323079d1a",
    "team_ids": [
        "e54b8db9-200e-40bf-a5b0-c28cc2d86458"
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

