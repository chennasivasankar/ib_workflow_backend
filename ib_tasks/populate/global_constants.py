from typing import List
from ib_tasks.interactors.dtos import GlobalConstantsDTO, \
    GlobalConstantsWithTemplateIdDTO
from ib_tasks.utils.get_google_sheet import get_google_sheet


class PopulateGlobalConstantsToTemplate:

    def populate_global_constants_to_template(self):
        sheet = get_google_sheet()
        global_constants_with_template_ids_dicts = \
            sheet.worksheet("Global Constants").get_all_records()

        import collections
        group_by_template_id_dict = collections.defaultdict(list)
        for item in global_constants_with_template_ids_dicts:
            group_by_template_id_dict[item['Template ID']].\
                append([item['Constant name'], item['Value']])

        group_by_template_id_dict = collections.OrderedDict(
            sorted(dict.items(group_by_template_id_dict))
        )

        for template_id, group in group_by_template_id_dict.items():
            global_constants_with_template_id_dto = \
                self._get_global_constants_with_template_id_dto(
                    template_id=template_id,
                    global_constants_list=group
                )
            self._populate_global_constants_to_template_in_db(
                global_constants_with_template_id_dto=global_constants_with_template_id_dto
            )

    def _get_global_constants_with_template_id_dto(
            self, template_id: str,
            global_constants_list: List[str]):

        from ib_tasks.interactors.dtos import GlobalConstantsWithTemplateIdDTO
        global_constants_dtos = self._get_global_constant_dtos(
            global_constants_list=global_constants_list
        )

        global_constants_with_template_id_dto = \
            GlobalConstantsWithTemplateIdDTO(
                template_id=template_id,
                global_constants_dtos = global_constants_dtos
            )
        return global_constants_with_template_id_dto

    def _get_global_constant_dtos(
            self, global_constants_list: List[str]
    ) -> List[GlobalConstantsDTO]:
        global_constants_dtos = []
        for global_constant in global_constants_list:
            constant_name = global_constant[0]
            value = int(global_constant[1])
            global_constants_dto = GlobalConstantsDTO(
                constant_name=constant_name, value=value
            )
            global_constants_dtos.append(global_constants_dto)
        return  global_constants_dtos

    @staticmethod
    def _populate_global_constants_to_template_in_db(
            global_constants_with_template_id_dto: GlobalConstantsWithTemplateIdDTO
        ):
        from ib_tasks.storages.tasks_storage_implementation import \
            TasksStorageImplementation
        task_storage = TasksStorageImplementation()

        from ib_tasks.interactors.global_constants_interactor import \
            GlobalConstantsInteractor
        interactor = GlobalConstantsInteractor(task_storage=task_storage)
        interactor.create_global_constants_to_template_wrapper(
            global_constants_with_template_id_dto=global_constants_with_template_id_dto
        )
