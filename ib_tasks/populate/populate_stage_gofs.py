from typing import List


class PopulateStageGoFs:

    def populate_stage_gofs(self, spread_sheet_name: str):
        from ib_tasks.utils.get_google_sheet import get_google_sheet
        sheet = get_google_sheet(sheet_name=spread_sheet_name)

        from ib_tasks.constants.constants import STAGE_ID_AND_VALUES_SUB_SHEET
        stage_id_with_gof_ids_dicts = \
            sheet.worksheet(STAGE_ID_AND_VALUES_SUB_SHEET).get_all_records()

        import re
        from ib_tasks.interactors.stage_dtos import StageIdWithGoFIdsDTO
        stage_id_with_gof_ids_dtos = []
        for item in stage_id_with_gof_ids_dicts:
            stage_id = item['Stage ID*'].strip()
            gof_ids = re.split('[\r\n]', item['GOFs to be Displayed'])
            gof_ids_after_strip = \
                self._get_gof_ids_after_strip(gof_ids=gof_ids)
            stage_id_with_gof_ids_dtos.append(
                StageIdWithGoFIdsDTO(stage_id=stage_id,
                                     gof_ids=gof_ids_after_strip)
            )

        from ib_tasks.interactors.create_stage_gofs_interactor import \
            CreateStageGoFsInteractor
        from ib_tasks.storages.storage_implementation import \
            StagesStorageImplementation
        from ib_tasks.storages.gof_storage_implementation import \
            GoFStorageImplementation
        stage_storage = StagesStorageImplementation()
        gof_storage = GoFStorageImplementation()
        create_stage_gofs_interactor = CreateStageGoFsInteractor(
            gof_storage=gof_storage, stage_storage=stage_storage
        )
        create_stage_gofs_interactor.create_stage_gofs(
            stage_id_with_gof_ids_dtos=stage_id_with_gof_ids_dtos)

    @staticmethod
    def _get_gof_ids_after_strip(gof_ids: List[str]) -> List[str]:
        gof_ids_after_strip = []
        for gof_id in gof_ids:
            gof_id_after_strip = gof_id.strip()
            if gof_id_after_strip:
                gof_ids_after_strip.append(gof_id_after_strip)
        return gof_ids_after_strip
