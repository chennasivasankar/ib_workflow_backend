

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "af495711-458a-4b29-afe1-a58fb0541850",
    "team_ids": [
        "cec9505a-ef5e-409e-87e7-ee306d36aa27"
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

