


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "d3f9a413-7670-4f38-ae0a-a66080541a61",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "bdbf7a45-70ea-427d-b29f-1353610f2ad9",
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
                "company_id": "3adfd9d6-d698-4df9-a93a-f8a6299ef10a",
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

