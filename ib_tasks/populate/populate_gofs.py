from ib_tasks.utils.csv_reader import read_csv_file
import json


def populate_required_fields(file_path: str):
    from ib_tasks.models.field import Field
    field_dicts = read_csv_file(file_path=file_path)
    field_model_objects = [
        Field(
            field_id=field_dict['Feild ID'],
            display_name=field_dict['Field Display Name'],
            field_type=field_dict['Field Type'],
            field_values=field_dict['Field Values'],
            allowed_formats=field_dict['Allowed Formats'],
            help_text=field_dict['Help Text'],
            tooltip=field_dict['Tool Tip'],
            placeholder_text=field_dict['Place Holder Text'],
            error_message=field_dict['Error Message'],
            validation_regex=field_dict['Validation - RegEx']
        )
        for field_dict in field_dicts
    ]
    Field.objects.bulk_create(field_model_objects)


def populate_required_task_templates(file_path: str):
    from ib_tasks.models.task_template import TaskTemplate
    task_template_dicts = read_csv_file(file_path=file_path)
    task_template_model_objects = [
        TaskTemplate(
            template_id=task_template_dict['Template ID'],
            template_name=task_template_dict['Template Name']
        )
        for task_template_dict in task_template_dicts
    ]
    TaskTemplate.objects.bulk_create(task_template_model_objects)


def prepare_complete_gof_details_dtos():
    from ib_tasks.constants.constants import GOFS_CSV_FILE_PATH
    gof_dicts = read_csv_file(file_path=GOFS_CSV_FILE_PATH)
    from ib_tasks.interactors.storage_interfaces.dtos import (
        CompleteGoFDetailsDTO, GoFRolesDTO, GoFFieldsDTO
    )
    return


def create_gofs():
    from ib_tasks.constants.constants import (
        FIELDS_CSV_FILE_PATH, TASK_TEMPLATES_CSV_FILE_PATH
    )
    # populate_required_fields(file_path=FIELDS_CSV_FILE_PATH)
    # populate_required_task_templates(file_path=TASK_TEMPLATES_CSV_FILE_PATH)
    complete_gof_details_dtos = prepare_complete_gof_details_dtos()


create_gofs()
