

REQUEST_BODY_JSON = """
{
    "name": "string",
    "template_id": "string",
    "conditions": [
        {
            "field_id": "string",
            "operator": "EQ",
            "value": "string"
        }
    ]
}
"""


RESPONSE_201_JSON = """
{
    "name": "string",
    "template_id": "string",
    "conditions": [
        {
            "field_id": "string",
            "operator": "EQ",
            "value": "string"
        }
    ],
    "filter_id": 1,
    "is_selected": true
}
"""

RESPONSE_404_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "TASK_TEMPLATES_DOES_NOT_EXISTS"
}
"""

RESPONSE_417_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "VALUE_SHOULD_NOT_BE_EMPTY"
}
"""

RESPONSE_403_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "FIELDS_NOT_BELONGS_TASK_TEMPLATE"
}
"""

