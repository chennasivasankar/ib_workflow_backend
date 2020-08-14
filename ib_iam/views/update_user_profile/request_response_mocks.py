

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "profile_pic_url": "string",
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

RESPONSE_404_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "INVALID_ROLE_IDS"
}
"""

