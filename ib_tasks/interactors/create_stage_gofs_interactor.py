from typing import List, Dict

from ib_tasks.interactors.stage_dtos import StageIdWithGoFIdsDTO, \
    DBStageIdWithStageIdDTO, DBStageIdWithGoFIdsDTO
from ib_tasks.interactors.storage_interfaces.gof_storage_interface import \
    GoFStorageInterface
from ib_tasks.interactors.storage_interfaces.stages_storage_interface \
    import StageStorageInterface


class CreateStageGoFsInteractor:
    def __init__(
            self, stage_storage: StageStorageInterface,
            gof_storage: GoFStorageInterface
    ):
        self.gof_storage = gof_storage
        self.stage_storage = stage_storage

    def create_stage_gofs(
            self, stage_id_with_gof_ids_dtos: List[StageIdWithGoFIdsDTO]):
        self._make_validations(
            stage_id_with_gof_ids_dtos=stage_id_with_gof_ids_dtos)

        stage_ids = self._get_stage_ids(
            stage_id_with_gof_ids_dtos=stage_id_with_gof_ids_dtos)
        db_stage_id_with_stage_id_dtos = self.stage_storage.\
            get_db_stage_ids_with_stage_ids_dtos(stage_ids=stage_ids)
        db_stage_id_with_stage_id_dtos_dict = \
            self._make_db_stage_id_with_stage_id_dtos_dict(
                db_stage_id_with_stage_id_dtos=db_stage_id_with_stage_id_dtos)

        stage_id_with_gof_ids_dtos_to_create = \
            self._get_stage_id_with_gof_ids_dtos_to_create(
                stage_id_with_gof_ids_dtos=stage_id_with_gof_ids_dtos,
                db_stage_id_with_stage_id_dtos_dict=
                db_stage_id_with_stage_id_dtos_dict
            )
        self.stage_storage.create_stage_gofs(
            stage_id_with_gof_ids_dtos=stage_id_with_gof_ids_dtos_to_create
        )

    def _get_stage_id_with_gof_ids_dtos_to_create(
            self, stage_id_with_gof_ids_dtos: List[StageIdWithGoFIdsDTO],
            db_stage_id_with_stage_id_dtos_dict: Dict
    ) -> List[DBStageIdWithGoFIdsDTO]:

        stage_id_with_gof_ids_dtos_to_create = []
        for stage_id_with_gof_ids_dto in stage_id_with_gof_ids_dtos:
            db_stage_id = db_stage_id_with_stage_id_dtos_dict[
                stage_id_with_gof_ids_dto.stage_id]
            existing_gof_ids_of_stage = self.stage_storage.\
                get_existing_gof_ids_of_stage(stage_id=db_stage_id)
            gof_ids_to_create = self._get_gof_ids_to_create(
                gof_ids=stage_id_with_gof_ids_dto.gof_ids,
                existing_gof_ids_of_stage=existing_gof_ids_of_stage
            )
            if gof_ids_to_create:
                stage_id_with_gof_ids_dtos_to_create.append(
                    DBStageIdWithGoFIdsDTO(
                        db_stage_id=db_stage_id,
                        gof_ids=gof_ids_to_create
                    )
                )
        return stage_id_with_gof_ids_dtos_to_create

    def _make_validations(
            self, stage_id_with_gof_ids_dtos: List[StageIdWithGoFIdsDTO]):
        stage_ids = self._get_stage_ids(
            stage_id_with_gof_ids_dtos=stage_id_with_gof_ids_dtos)
        gof_ids = self._get_gof_ids_of_all_stages(
            stage_id_with_gof_ids_dtos=stage_id_with_gof_ids_dtos)

        self._validate_uniqueness_in_stage_ids(stage_ids=stage_ids)
        self._validate_uniqueness_of_gof_ids_in_each_stage(
            stage_id_with_gof_ids_dtos=stage_id_with_gof_ids_dtos)
        self._make_database_validations(gof_ids=gof_ids, stage_ids=stage_ids)

    def _validate_uniqueness_of_gof_ids_in_each_stage(
            self, stage_id_with_gof_ids_dtos: List[StageIdWithGoFIdsDTO]):
        for stage_id_with_gof_ids_dto in stage_id_with_gof_ids_dtos:
            self._validate_uniqueness_in_gof_ids(
                gof_ids=stage_id_with_gof_ids_dto.gof_ids)

    def _make_database_validations(
            self, gof_ids: List[str], stage_ids: List[str]):
        valid_stage_ids = \
            self.stage_storage.get_valid_stage_ids_in_given_stage_ids(
                stage_ids=stage_ids)
        invalid_stage_ids = [
            stage_id for stage_id in stage_ids
            if stage_id not in valid_stage_ids]
        if invalid_stage_ids:
            from ib_tasks.exceptions.stage_custom_exceptions import \
                InvalidStageIdsListException
            raise InvalidStageIdsListException(invalid_stage_ids)

        valid_gof_ids = \
            self.gof_storage.get_valid_gof_ids_in_given_gof_ids(
                gof_ids=gof_ids
            )
        invalid_gof_ids = [
            gof_id for gof_id in gof_ids if gof_id not in valid_gof_ids
        ]
        if invalid_gof_ids:
            from ib_tasks.exceptions.gofs_custom_exceptions import \
                InvalidGoFIds
            raise InvalidGoFIds(invalid_gof_ids)

    @staticmethod
    def _get_gof_ids_to_create(
            gof_ids: List[str], existing_gof_ids_of_stage: List[str]
    ) -> List[str]:
        gof_ids_to_create = [
            gof_id
            for gof_id in gof_ids if gof_id not in existing_gof_ids_of_stage
        ]
        return gof_ids_to_create

    @staticmethod
    def _get_stage_ids(
            stage_id_with_gof_ids_dtos: List[StageIdWithGoFIdsDTO]
    ) -> List[str]:
        stage_ids = [
            stage_id_with_gof_ids_dtos.stage_id
            for stage_id_with_gof_ids_dtos in stage_id_with_gof_ids_dtos
        ]
        return stage_ids

    @staticmethod
    def _get_gof_ids_of_all_stages(
            stage_id_with_gof_ids_dtos: List[StageIdWithGoFIdsDTO]
    ) -> List[str]:
        gof_ids_of_all_stages = []
        for stage_id_with_gof_ids_dto in stage_id_with_gof_ids_dtos:
            gof_ids_of_stage = stage_id_with_gof_ids_dto.gof_ids
            gof_ids_of_all_stages += gof_ids_of_stage
        return gof_ids_of_all_stages

    @staticmethod
    def _validate_uniqueness_in_gof_ids(gof_ids: List[str]):
        from collections import Counter
        gof_ids_counter = Counter(gof_ids)

        duplicate_gof_ids = []
        for gof_id, count in gof_ids_counter.items():
            is_duplicate_gof_id = count > 1
            if is_duplicate_gof_id:
                duplicate_gof_ids.append(gof_id)

        from ib_tasks.exceptions.gofs_custom_exceptions import DuplicateGoFIds
        if duplicate_gof_ids:
            raise DuplicateGoFIds(duplicate_gof_ids)

    @staticmethod
    def _validate_uniqueness_in_stage_ids(stage_ids: List[str]):
        from collections import Counter
        stage_ids_counter = Counter(stage_ids)

        duplicate_stage_ids = []
        for stage_id, count in stage_ids_counter.items():
            is_duplicate_stage_id = count > 1
            if is_duplicate_stage_id:
                duplicate_stage_ids.append(stage_id)

        from ib_tasks.exceptions.stage_custom_exceptions import \
            DuplicateStageIds
        if duplicate_stage_ids:
            raise DuplicateStageIds(duplicate_stage_ids)

    @staticmethod
    def _make_db_stage_id_with_stage_id_dtos_dict(
            db_stage_id_with_stage_id_dtos: List[DBStageIdWithStageIdDTO]
    ) -> Dict:
        db_stage_id_with_stage_id_dtos_dict = {
            db_stage_id_with_stage_id_dto.stage_id:
                db_stage_id_with_stage_id_dto.db_stage_id
            for db_stage_id_with_stage_id_dto in db_stage_id_with_stage_id_dtos
        }
        return db_stage_id_with_stage_id_dtos_dict
