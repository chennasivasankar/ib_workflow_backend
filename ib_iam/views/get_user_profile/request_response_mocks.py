


RESPONSE_200_JSON = """
{
    "user_id": "932ab285-4bcc-4b2c-95a1-77397856aac3",
    "name": "string",
    "email": "string",
    "profile_pic_url": "string",
    "cover_page_url": "string",
    "is_admin": true,
    "company": {
        "company_id": "string",
        "name": "string",
        "description": "string",
        "logo_url": "string",
        "employees": [
            {
                "employee_id": "string",
                "name": "string",
                "profile_pic_url": "string"
            }
        ],
        "roles": {
            "roles": [
                {
                    "role_id": "string",
                    "role_name": "string"
                }
            ]
        }
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

