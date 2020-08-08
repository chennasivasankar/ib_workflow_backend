


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "4f71a11b-02c3-4f40-b2bc-eb58fb56ce87",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "318f9b5e-879f-4b3b-8293-543f7d453558",
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

