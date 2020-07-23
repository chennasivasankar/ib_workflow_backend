from typing import Dict, Any, List

from ib_tasks.interactors.storage_interfaces.dtos import TaskStatusDTO


def populate_status_variables(list_of_status_dict: List[Dict]):
    validation_for_list_of_status_dict(list_of_status_dict)
    status_dtos = [append_status_dto(status_dict)
                   for status_dict in list_of_status_dict]

    return status_dtos


def append_status_dto(status_dict: Dict[str, Any]):
    status_dto = TaskStatusDTO(
        task_template_id=status_dict['task_template_id'],
        status_variable_id=status_dict['status_variable_id']
    )
    return status_dto


def validation_for_list_of_status_dict(status_dict: List[Dict]):
    from schema import Schema, SchemaError

    schema = Schema(
        [{
            "task_template_id": str,
            "status_variable_id": str
        }]

    )

    try:
        schema.validate(status_dict)
    except SchemaError:
        raise_exception_for_invalid_format()


def raise_exception_for_invalid_format():
    valid_format = {
        "task_template_id": "task_template_id_1",
        "status_variable_id": "status_id_1"
    }

    import json
    json_valid_format = json.dumps(valid_format)

    from ib_tasks.exceptions.stage_custom_exceptions import InvalidFormatException
    raise InvalidFormatException(valid_format=json_valid_format)
