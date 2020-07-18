from ib_tasks.interactors.storage_interfaces.dtos import CompleteGoFDetailsDTO, \
    GoFDTO, GoFRolesDTO
from ib_tasks.utils.read_google_sheet import read_google_sheet
from typing import List, Dict


def populate_required_task_templates(task_template_records: List[Dict]):
    from ib_tasks.models.task_template import TaskTemplate
    task_template_model_objects = [
        TaskTemplate(
            template_id=task_template_record['Template ID'],
            template_name=task_template_record['Template Name']
        )
        for task_template_record in task_template_records
    ]
    TaskTemplate.objects.bulk_create(task_template_model_objects)


def create_gofs():
    from ib_tasks.constants.constants import (
        GOOGLE_SHEET_NAME, TASK_TEMPLATE_SUB_SHEET_TITLE, GOF_SUB_SHEET_TITLE
    )
    from ib_tasks.interactors.create_or_update_gofs import \
        CreateOrUpdateGoFsInteractor
    from ib_tasks.storages.tasks_storage_implementation import \
        TasksStorageImplementation
    sheet = read_google_sheet(sheet_name=GOOGLE_SHEET_NAME)
    task_template_sheet = sheet.worksheet(TASK_TEMPLATE_SUB_SHEET_TITLE)
    gof_sheet = sheet.worksheet(GOF_SUB_SHEET_TITLE)
    task_template_records = task_template_sheet.get_all_records()
    gof_records = gof_sheet.get_all_records()
    print_in_json_format(gof_records)


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

    gof_dto = GoFDTO(
        gof_id=gof_record['GOF ID*'],
        gof_display_name=gof_record['GOF Display Name*'],
        task_template_id=gof_record['Task Template ID*'],
        order=gof_record['Order*'],
        max_columns=gof_record['MAX_COLUMNS'],

    )
    return gof_dto

def get_gof_roles_dto_for_a_gof_record(gof_record: Dict) -> GoFRolesDTO:
    pass

def print_in_json_format(value):
    import json
    print(json.dumps(value, indent=4))


create_gofs()
