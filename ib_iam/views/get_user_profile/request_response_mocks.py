


RESPONSE_200_JSON = """
{
    "user_id": "9afc3e6f-05a9-4e30-8a9c-45e20d64f40e",
    "name": "string",
    "email": "string",
    "profile_pic_url": "string",
    "cover_page_url": "string",
    "is_admin": true,
    "roles": [
        {
            "role_id": "string",
            "role_name": "string"
        }
    ],
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

