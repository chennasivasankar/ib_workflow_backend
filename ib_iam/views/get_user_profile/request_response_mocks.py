


RESPONSE_200_JSON = """
{
    "user_id": "285b8740-62b7-499d-b208-c8146de0180c",
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

