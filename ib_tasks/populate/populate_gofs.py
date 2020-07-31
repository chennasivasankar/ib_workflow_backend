from ib_tasks.interactors.storage_interfaces.gof_dtos import GoFDTO, \
    GoFRolesDTO, CompleteGoFDetailsDTO
from typing import List, Dict

from ib_tasks.utils.get_google_sheet import get_google_sheet


class PopulateGoFs:
    def create_or_update_gofs(self):
        from ib_tasks.constants.constants import (
            GOOGLE_SHEET_NAME, GOF_SUB_SHEET_TITLE
        )
        from ib_tasks.interactors.create_or_update_gofs import \
            CreateOrUpdateGoFsInteractor
        from ib_tasks.storages.tasks_storage_implementation import \
            TasksStorageImplementation

        sheet = get_google_sheet(sheet_name=GOOGLE_SHEET_NAME)
        gof_sheet = sheet.worksheet(GOF_SUB_SHEET_TITLE)
        gof_records = gof_sheet.get_all_records()
        complete_gof_details_dtos = self.prepare_complete_gof_details_dtos(
            gof_records)

        storage = TasksStorageImplementation()
        interactor = CreateOrUpdateGoFsInteractor(storage=storage)
        interactor.create_or_update_gofs(complete_gof_details_dtos)

    def prepare_complete_gof_details_dtos(
            self, gof_records: List[Dict]
    ) -> List[CompleteGoFDetailsDTO]:
        complete_gof_details_dtos = [
            CompleteGoFDetailsDTO(
                gof_dto=self.get_gof_dto_for_a_gof_record(gof_record),
                gof_roles_dto=self.get_gof_roles_dto_for_a_gof_record(
                    gof_record)
            )
            for gof_record in gof_records
        ]
        return complete_gof_details_dtos

    @staticmethod
    def get_gof_dto_for_a_gof_record(gof_record: Dict) -> GoFDTO:
        max_columns = gof_record['MAX_COLUMNS']
        max_columns_is_not_integer = not isinstance(max_columns, int)
        if max_columns_is_not_integer:
            from ib_tasks.constants.exception_messages import \
                MAX_COLUMNS_VALUE_MUST_BE_INTEGER
            from ib_tasks.exceptions.columns_custom_exceptions import \
                MaxColumnsMustBeANumber
            MAX_COLUMNS_VALUE_MUST_BE_INTEGER += ", got {}".format(max_columns)
            raise MaxColumnsMustBeANumber(MAX_COLUMNS_VALUE_MUST_BE_INTEGER)

        gof_dto = GoFDTO(
            gof_id=gof_record['GOF ID*'].strip(),
            gof_display_name=gof_record['GOF Display Name*'].strip(),
            max_columns=max_columns
        )
        return gof_dto

    @staticmethod
    def get_gof_roles_dto_for_a_gof_record(gof_record: Dict) -> \
            GoFRolesDTO:
        read_permissions_is_empty = \
            not gof_record['Read permission Roles*'].strip()
        write_permissions_is_empty = \
            not gof_record['Write permission Roles*'].strip()
        read_permission_roles_is_not_empty = not read_permissions_is_empty
        write_permissions_is_not_empty = not write_permissions_is_empty
        read_permission_roles, write_permission_roles = [], []
        if read_permission_roles_is_not_empty:
            read_permission_roles = \
                gof_record['Read permission Roles*'].split('\n')
        if write_permissions_is_not_empty:
            write_permission_roles = \
                gof_record['Write permission Roles*'].split('\n')
        gof_roles_dto = GoFRolesDTO(
            gof_id=gof_record['GOF ID*'],
            read_permission_roles=read_permission_roles,
            write_permission_roles=write_permission_roles
        )
        return gof_roles_dto
