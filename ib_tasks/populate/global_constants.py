from typing import List, Dict
from ib_tasks.interactors.dtos import GlobalConstantsDTO, \
    GlobalConstantsWithTemplateIdDTO
from ib_tasks.utils.get_google_sheet import get_google_sheet


class PopulateGlobalConstantsToTemplate:

    def poulate_global_contants_to_template(self):
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
        from ib_tasks.models.global_constant import GlobalConstant
        print(GlobalConstant.objects.all().values())

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
    def _get_data_from_global_constants_csv_file(
            file_path: str) -> List[Dict]:
        import csv
        with open(file_path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            col_headers = csv_reader.__next__()
            result = []

            from itertools import zip_longest
            from collections import defaultdict
            for row in csv_reader:
                row_dict = defaultdict()
                for col_header, col_val in zip_longest(col_headers, row):
                    row_dict[col_header] = col_val
                result.append(row_dict)
            return result

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
