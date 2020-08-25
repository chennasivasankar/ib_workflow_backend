


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "cd5d1ff6-ab16-40d6-ab51-0b72e633c6a6",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "566f1dc7-1e29-400c-8513-3d668938dc3a",
                    "team_name": "string"
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

