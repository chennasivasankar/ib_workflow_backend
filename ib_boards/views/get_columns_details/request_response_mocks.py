

REQUEST_BODY_JSON = """
{
    "view_type": "LIST"
}
"""


RESPONSE_403_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "USER_DONOT_HAVE_ACCESS"
}
"""

RESPONSE_404_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "INVALID_BOARD_ID"
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
    "total_columns_count": 1,
    "columns": [
        {
            "column_id": "string",
            "name": "string",
            "total_tasks_count": 1,
            "tasks": [
                {
                    "task_id": "string",
                    "fields": [
                        {
                            "field_type": "string",
                            "key": "string",
                            "value": "string"
                        }
                    ],
                    "actions": [
                        {
                            "action_id": "string",
                            "name": "string",
                            "button_text": "string",
                            "button_color": "string"
                        }
                    ]
                }
            ]
        }
    ]
}
"""

