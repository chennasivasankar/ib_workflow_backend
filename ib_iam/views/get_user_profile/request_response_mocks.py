


RESPONSE_200_JSON = """
{
    "user_id": "46fe2d18-756b-4e4b-9f0f-9b1caa9a90ff",
    "name": "string",
    "email": "string",
    "profile_pic_url": "string",
    "is_admin": true,
    "company": {
        "name": "string",
        "description": "string",
        "logo_url": "string",
        "company_id": "string",
        "employees": [
            {
                "employee_id": "string",
                "name": "string",
                "profile_pic_url": "string"
            }
        ]
    },
    "teams": [
        {
            "name": "string",
            "description": "string",
            "team_id": "string",
            "members": [
                {
                    "member_id": "string",
                    "name": "string",
                    "profile_pic_url": "string"
                }
            ]
        }
    ]
}
"""

RESPONSE_400_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "INVALID_USER_ID"
}
"""

RESPONSE_404_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "USER_ACCOUNT_DOES_NOT_EXIST"
}
"""

