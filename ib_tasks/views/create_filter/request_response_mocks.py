

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
    "filter_id": 1,
    "name": "string",
    "template_id": "string",
    "template_name": "string",
    "status": "ENABLED",
    "conditions": [
        {
            "field_id": "string",
            "operator": "EQ",
            "value": "string",
            "field_name": "string"
        }
    ]
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

