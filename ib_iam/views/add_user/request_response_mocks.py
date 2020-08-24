

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "e503a3e6-c0c5-4ca5-905f-018a1ad6e6d5",
    "team_ids": [
        "e6798433-fb8e-4451-b468-fea5ed0dfade"
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

