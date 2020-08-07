from typing import List

from ib_tasks.interactors.gofs_dtos import GoFWithOrderAndAddAnotherDTO, \
    GoFsWithTemplateIdDTO


class PopulateGoFsToTransitionTemplate:

    def populate_gofs_to_transition_templates(self):
        from ib_tasks.utils.get_google_sheet import get_google_sheet
        from ib_tasks.constants.constants import GOOGLE_SHEET_NAME
        sheet = get_google_sheet(sheet_name=GOOGLE_SHEET_NAME)

        from ib_tasks.constants.constants import TRANSITION_TEMPLATES_SUB_SHEET
        gofs_with_template_ids_dicts = \
            sheet.worksheet(TRANSITION_TEMPLATES_SUB_SHEET).get_all_records()

        import collections
        group_by_template_id_dict = collections.defaultdict(list)
        for item in gofs_with_template_ids_dicts:
            group_by_template_id_dict[item['Template ID'].strip()].append(
                [item['GOF ID*'].strip(), item['Order'],
                 item['Enable add another'].strip()]
            )

        from ib_tasks.populate.populate_gofs_to_template import \
            PopulateGoFsToTemplate
        populate_gofs_to_template = PopulateGoFsToTemplate()
        for template_id, group in group_by_template_id_dict.items():
            gofs_with_template_id_dto = \
                self._get_gofs_with_template_id_dto(
                    template_id=template_id, gofs_list=group
                )
            populate_gofs_to_template.populate_gofs_to_template(
                gofs_with_template_id_dto=gofs_with_template_id_dto
            )

    def _get_gofs_with_template_id_dto(
            self, template_id: str, gofs_list: List[str]):

        gof_with_order_and_add_another_dtos = \
            self._get_gof_with_order_and_add_another_dtos(
                gofs_list=gofs_list
            )

        gofs_with_template_id_dto = \
            GoFsWithTemplateIdDTO(
                template_id=template_id,
                gof_dtos=gof_with_order_and_add_another_dtos
            )
        return gofs_with_template_id_dto

    @staticmethod
    def _get_gof_with_order_and_add_another_dtos(
            gofs_list: List[any]) -> List[GoFWithOrderAndAddAnotherDTO]:

        gof_with_order_and_add_another_dtos = []
        for gof in gofs_list:
            gof_id = gof[0]
            from ib_tasks.exceptions.constants_custom_exceptions import \
                InvalidTypeForOrder
            from ib_tasks.constants.exception_messages import \
                INVALID_TYPE_FOR_ORDER

            order = gof[1]
            is_order_is_int = isinstance(order, int)
            is_order_is_not_int = not is_order_is_int
            if is_order_is_not_int:
                message = INVALID_TYPE_FOR_ORDER.format(order)
                raise InvalidTypeForOrder(message)

            is_enable_add_another_gof_is_yes = gof[2] == "Yes"
            if is_enable_add_another_gof_is_yes:
                enable_add_another_gof = True
            else:
                enable_add_another_gof = False

            gof_with_order_and_add_another_dto = GoFWithOrderAndAddAnotherDTO(
                gof_id=gof_id, order=order,
                enable_add_another_gof=enable_add_another_gof
            )
            gof_with_order_and_add_another_dtos.append(
                gof_with_order_and_add_another_dto
            )
        return gof_with_order_and_add_another_dtos
