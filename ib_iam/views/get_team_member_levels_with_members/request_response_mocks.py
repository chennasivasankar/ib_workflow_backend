


RESPONSE_200_JSON = """
{
    "team_member_levels_with_members": [
        {
            "level_details": {
                "team_member_level_id": "7b475eb5-85c0-4a19-8063-0fcb8d7329d7",
                "team_member_level_name": "string",
                "level_hierarchy": 1
            },
            "level_members": [
                {
                    "member_id": "string",
                    "name": "string",
                    "profile_pic_url": "string",
                    "immediate_superior_team_user_id": "string",
                    "immediate_subordinate_team_members": [
                        {
                            "member_id": "string",
                            "name": "string",
                            "profile_pic_url": "string"
                        }
                    ]
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
    "res_status": "INVALID_TEAM_ID"
}
"""

RESPONSE_403_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "USER_DOES_NOT_HAVE_ACCESS"
}
"""

