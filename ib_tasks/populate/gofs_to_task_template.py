from typing import List
from ib_tasks.interactors.dtos import GoFWithOrderAndAddAnotherDTO, \
    GoFsWithTemplateIdDTO
from ib_tasks.utils.get_google_sheet import get_google_sheet


class PopulateGoFsToTaskTemplate:

    def populate_gofs_to_task_template(self):
        sheet = get_google_sheet()
        gofs_with_template_ids_dicts = \
            sheet.worksheet("Task Templates").get_all_records()

        import collections
        group_by_template_id_dict = collections.defaultdict(list)
        for item in gofs_with_template_ids_dicts:
            group_by_template_id_dict[item['Template ID']].append(
                [item['GOF ID*'], item['Order'], item['Enable add another']]
            )

        group_by_template_id_dict = collections.OrderedDict(
            sorted(dict.items(group_by_template_id_dict))
        )

        for template_id, group in group_by_template_id_dict.items():
            gofs_with_template_id_dto = \
                self._get_gofs_with_template_id_dto(
                    template_id=template_id, gofs_list=group
                )
            self._populate_gofs_to_template_in_db(
                gofs_with_template_id_dto=gofs_with_template_id_dto
            )

    def _get_gofs_with_template_id_dto(
            self, template_id: str, gofs_list: List[str]):

        from ib_tasks.interactors.dtos import GoFsWithTemplateIdDTO
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

    def _get_gof_with_order_and_add_another_dtos(
            self, gofs_list: List[any]) -> List[GoFWithOrderAndAddAnotherDTO]:

        gof_with_order_and_add_another_dtos = []
        for gof in gofs_list:
            gof_id = gof[0]
            from ib_tasks.exceptions.custom_exceptions import \
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

    @staticmethod
    def _populate_gofs_to_template_in_db(
            gofs_with_template_id_dto: GoFsWithTemplateIdDTO):
        from ib_tasks.storages.tasks_storage_implementation import \
            TasksStorageImplementation
        task_storage = TasksStorageImplementation()

        from ib_tasks.interactors.add_gofs_to_task_template_interactor \
            import AddGoFsToTaskTemplateInteractor
        interactor = \
            AddGoFsToTaskTemplateInteractor(task_storage=task_storage)
        interactor.add_gofs_to_task_template_wrapper(
            gofs_with_template_id_dto=gofs_with_template_id_dto
        )
