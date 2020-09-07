from typing import List, Dict, Any

from ib_boards.interactors.add_project_for_boards import \
    AddProjectForBoardsInteractor
from ib_boards.interactors.dtos import ProjectBoardDTO
from ib_boards.storages.storage_implementation import StorageImplementation


def populate_project_for_boards(list_of_project_boards_dict: List[Dict]):
    validation_for_list_of_project_boards_dict(list_of_project_boards_dict)
    project_boards_dtos = [append_project_board_dto(project_dict)
                           for project_dict in list_of_project_boards_dict]
    storage = StorageImplementation()
    interactor = AddProjectForBoardsInteractor(
        storage=storage
    )
    interactor.add_project_for_boards(project_boards_dtos)


def append_project_board_dto(project_dict: Dict[str, Any]):
    project_board_dto = ProjectBoardDTO(
        project_id=project_dict['project_id'],
        board_id=project_dict['board_id']
    )
    return project_board_dto


def validation_for_list_of_project_boards_dict(
        list_of_project_boards: List[Dict]):
    from schema import Schema, SchemaError, And

    schema = Schema(
        [{
            "project_id": And(str, len),
            "board_id": And(str, len)
        }],
        ignore_extra_keys=True
    )

    try:
        schema.validate(list_of_project_boards)
    except SchemaError:
        raise_exception_for_invalid_format()


def raise_exception_for_invalid_format():
    valid_format = {
        "project_id": "project_id_2",
        "board_id": "board_id_2"
    }

    import json
    json_valid_format = json.dumps(valid_format)

    from ib_boards.exceptions.custom_exceptions import InvalidFormatException
    raise InvalidFormatException(valid_format=json_valid_format)
