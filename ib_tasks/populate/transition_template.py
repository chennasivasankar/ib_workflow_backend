from ib_tasks.interactors.task_template_dtos import \
    CreateTemplateDTO
from ib_tasks.populate.populate_template import PopulateTemplate


class PopulateTransitionTemplates(PopulateTemplate):

    def populate_transition_templates(self, spread_sheet_name: str):
        from ib_tasks.utils.get_google_sheet import get_google_sheet
        sheet = get_google_sheet(sheet_name=spread_sheet_name)

        from ib_tasks.constants.constants import TRANSITION_TEMPLATES_SUB_SHEET
        task_templates_dicts = \
            sheet.worksheet(TRANSITION_TEMPLATES_SUB_SHEET).get_all_records()

        for task_templates_dict in task_templates_dicts:
            create_template_dto = CreateTemplateDTO(
                template_id=task_templates_dict['Template ID'].strip(),
                template_name=task_templates_dict['Template Name'].strip(),
                is_transition_template=True
            )
            self._populate_template_in_db(
                create_template_dto=create_template_dto
            )
