


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "4ad92ed3-7b12-41d6-9845-f8fa9feaa25d",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "50715475-f9ed-4110-a80c-9a74c9064936",
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
                "company_id": "6a8e780b-94a3-4d4d-980d-5dc0d1651177",
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

