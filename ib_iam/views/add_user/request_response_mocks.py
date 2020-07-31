

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "c815ac88-ac12-44b1-9e54-324ee9fdeba5",
    "team_ids": [
        "07285641-5e37-4f02-9496-ec2c3b7064c8"
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

