import pytest

from ib_iam.populate.add_roles_details import RollsDetails
from ib_tasks.constants.constants import GOOGLE_SHEET_NAME, ROLES_SUB_SHEET
from ib_tasks.populate.get_sheet_data_for_creating_or_updating_stages import GetSheetDataForStages
from ib_tasks.populate.get_sheet_data_for_stage_actions import GetSheetDataForStageActions
from ib_tasks.populate.get_sheet_data_for_task_creation_config import GetSheetDataForTaskCreationConfig
from ib_tasks.populate.get_sheet_data_for_task_status_variables import GetSheetDataForStatusVariables
from ib_tasks.populate.gofs_to_task_template import PopulateGoFsToTaskTemplate
from ib_tasks.populate.populate_fields import create_fields
from ib_tasks.populate.populate_gofs import create_or_update_gofs
from ib_tasks.populate.task_templates import PopulateTaskTemplates


class PopulationUtils:

    # def populate_dependencies(self):
    #     task_template = PopulateTaskTemplates()
    #     task_template.populate_task_templates()
    #     # roles = RollsDetails()
    #     # roles.add_roles_details_to_database()
    #     create_or_update_gofs()
    #     template_gofs = PopulateGoFsToTaskTemplate()
    #     template_gofs.populate_gofs_to_task_template()
    #     create_fields()

    def populate_data(self):
        task_template = PopulateTaskTemplates()
        task_template.populate_task_templates()
        roles = RollsDetails()
        roles.add_roles_details_to_database(
            GOOGLE_SHEET_NAME, ROLES_SUB_SHEET)
        create_or_update_gofs()
        template_gofs = PopulateGoFsToTaskTemplate()
        template_gofs.populate_gofs_to_task_template()
        create_fields()

        status_variables = GetSheetDataForStatusVariables()
        status_variables.get_data_from_status_variables_sub_sheet()

        stage_values = GetSheetDataForStages()
        stage_values.get_data_from_stage_id_and_values_sub_sheet()

        stage_actions = GetSheetDataForStageActions()
        stage_actions.get_data_from_stages_and_actions_sub_sheet()

        task_creation_config = GetSheetDataForTaskCreationConfig()
        task_creation_config.get_data_from_task_creation_config_sub_sheet()
