


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "9d743ba6-110b-4cba-b2f2-df98dc3043e4",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "785a5f45-0b48-4ab8-bad3-8b02b1f8857c",
                    "team_name": "string"
                }
            ],
            "roles": [
                {
                    "role_id": "string",
                    "role_name": "string"
                }
            ],
            "company": {
                "company_id": "string",
                "company_name": "string"
            }
        }
    ],
    "total": 1
}
"""

RESPONSE_403_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "USER_DOES_NOT_HAVE_PERMISSION"
}
"""

RESPONSE_400_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "INVALID_LIMIT"
}
"""

