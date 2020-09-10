


RESPONSE_403_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "USER_IS_NOT_IN_PROJECT"
}
"""

RESPONSE_400_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "INVALID_OFFSET_VALUE"
}
"""

RESPONSE_404_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "INVALID_PROJECT_ID"
}
"""

RESPONSE_200_JSON = """
{
    "total_boards_count": 1,
    "starred_boards": [
        {
            "board_id": "string",
            "name": "string"
        }
    ],
    "all_boards": [
        {
            "board_id": "string",
            "name": "string"
        }
    ]
}
"""

