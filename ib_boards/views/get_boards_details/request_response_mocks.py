


RESPONSE_403_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "USER_DONOT_HAVE_ACCESS"
}
"""

RESPONSE_400_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "INVALID_OFFSET_VALUE"
}
"""

RESPONSE_200_JSON = """
{
    "total_boards": 1,
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

