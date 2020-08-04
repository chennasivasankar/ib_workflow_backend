


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "11ddba60-c483-4af7-9342-322a49940bfa",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "93ed1fdf-f4d8-4487-8b9f-b94742531ee7",
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
                "company_id": "3a897c6e-f133-46ad-91f1-33d585424578",
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

