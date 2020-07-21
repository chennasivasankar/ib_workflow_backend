from ib_tasks.interactors.storage_interfaces.dtos import CompleteGoFDetailsDTO, \
    GoFDTO, GoFRolesDTO
from ib_tasks.utils.read_google_sheet import read_google_sheet
from typing import List, Dict


def create_or_update_gofs():
    from ib_tasks.constants.constants import (
        GOOGLE_SHEET_NAME, GOF_SUB_SHEET_TITLE
    )
    from ib_tasks.interactors.create_or_update_gofs import \
        CreateOrUpdateGoFsInteractor
    from ib_tasks.storages.tasks_storage_implementation import \
        TasksStorageImplementation

    sheet = read_google_sheet(sheet_name=GOOGLE_SHEET_NAME)
    gof_sheet = sheet.worksheet(GOF_SUB_SHEET_TITLE)
    gof_records = gof_sheet.get_all_records()
    complete_gof_details_dtos = prepare_complete_gof_details_dtos(gof_records)

    storage = TasksStorageImplementation()
    interactor = CreateOrUpdateGoFsInteractor(storage=storage)
    interactor.create_or_update_gofs(complete_gof_details_dtos)


def prepare_complete_gof_details_dtos(
        gof_records: List[Dict]
) -> List[CompleteGoFDetailsDTO]:
    complete_gof_details_dtos = [
        CompleteGoFDetailsDTO(
            gof_dto=get_gof_dto_for_a_gof_record(gof_record),
            gof_roles_dto=get_gof_roles_dto_for_a_gof_record(gof_record)
        )
        for gof_record in gof_records
    ]
    return complete_gof_details_dtos


def get_gof_dto_for_a_gof_record(gof_record: Dict) -> GoFDTO:
    max_columns = gof_record['MAX_COLUMNS*']
    max_columns_is_not_integer = not isinstance(max_columns, int)
    if max_columns_is_not_integer:
        from ib_tasks.constants.exception_messages import \
            MAX_COLUMNS_VALUE_MUST_BE_INTEGER
        from ib_tasks.exceptions.custom_exceptions import \
            MaxColumnsMustBeANumber
        MAX_COLUMNS_VALUE_MUST_BE_INTEGER += ", got {}".format(max_columns)
        raise MaxColumnsMustBeANumber(MAX_COLUMNS_VALUE_MUST_BE_INTEGER)

    gof_dto = GoFDTO(
        gof_id=gof_record['GOF ID*'],
        gof_display_name=gof_record['GOF Display Name*'],
        max_columns=gof_record['MAX_COLUMNS*']
    )
    return gof_dto


def get_gof_roles_dto_for_a_gof_record(gof_record: Dict) -> GoFRolesDTO:
    import json
    read_permissions_is_empty = \
        not gof_record['Read Permission Roles*'].strip()
    write_permissions_is_empty = \
        not gof_record['Read Permission Roles*'].strip()
    read_permission_roles_is_not_empty = not read_permissions_is_empty
    write_permissions_is_not_empty = not write_permissions_is_empty
    read_permission_roles, write_permission_roles = [], []
    if read_permission_roles_is_not_empty:
        read_permission_roles = \
            gof_record['Read Permission Roles*'].split('\n')
    if write_permissions_is_not_empty:
        write_permission_roles = \
            gof_record['Write Permission Roles*'].split('\n')
    gof_roles_dto = GoFRolesDTO(
        gof_id=gof_record['GOF ID*'],
        read_permission_roles=read_permission_roles,
        write_permission_roles=write_permission_roles
    )
    return gof_roles_dto
