from ib_tasks.interactors.task_template_dtos import \
    CreateTemplateDTO
from ib_tasks.populate.populate_template import PopulateTemplate


class PopulateTaskTemplates(PopulateTemplate):

    def populate_task_templates(self):
        from ib_tasks.utils.get_google_sheet import get_google_sheet
        from ib_tasks.constants.constants import GOOGLE_SHEET_NAME
        sheet = get_google_sheet(sheet_name=GOOGLE_SHEET_NAME)

        from ib_tasks.constants.constants import TASK_TEMPLATE_SUB_SHEET_TITLE
        task_templates_dicts = \
            sheet.worksheet(TASK_TEMPLATE_SUB_SHEET_TITLE).get_all_records()

        for task_templates_dict in task_templates_dicts:
            create_template_dto = CreateTemplateDTO(
                template_id=task_templates_dict['Template ID'].strip(),
                template_name=task_templates_dict['Template Name'].strip(),
                is_transition_template=False
            )
            self._populate_template_in_db(
                create_template_dto=create_template_dto
            )
