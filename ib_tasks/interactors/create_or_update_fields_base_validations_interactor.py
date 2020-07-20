from typing import List, Optional

import collections

from ib_tasks.interactors.storage_interfaces.dtos import FieldDTO

from ib_tasks.interactors.storage_interfaces.task_storage_interface \
    import TaskStorageInterface

from ib_tasks.exceptions.custom_exceptions import (
    InvalidGOFIds,
    FieldIdEmptyValueException,
    DuplicationOfFieldIdsExist,
    InvalidValueForFieldDisplayName,
    InvalidValueForFieldType,

)


class CreateOrUpdateFieldsBaseVaidationInteractor:

    def __init__(self, storage: TaskStorageInterface):
        self.storage = storage

    def fields_base_validations(self, field_dtos: List[FieldDTO]):
        self._validate_field_ids(field_dtos)
        self._check_for_duplication_of_filed_ids(field_dtos)
        self._validate_field_display_name(field_dtos)
        self._validate_field_type(field_dtos)
        self._validate_gof_ids(field_dtos)

    def _validate_gof_ids(
            self, field_dtos: List[FieldDTO]
    ) -> Optional[InvalidGOFIds]:

        from ib_tasks.constants.exception_messages \
            import INVALID_GOF_IDS_EXCEPTION_MESSAGE

        gof_ids = [field_dto.gof_id for field_dto in field_dtos]
        existing_gof_ids = self.storage.get_existing_gof_ids(gof_ids)
        invalid_gof_ids = []
        for gof_id in gof_ids:
            if gof_id not in existing_gof_ids:
                invalid_gof_ids.append(gof_id)

        if invalid_gof_ids:
            raise InvalidGOFIds(
                INVALID_GOF_IDS_EXCEPTION_MESSAGE.format(invalid_gof_ids)
            )
        return

    @staticmethod
    def _validate_field_ids(
            field_dtos: List[FieldDTO]
    ) -> Optional[FieldIdEmptyValueException]:

        from ib_tasks.constants.exception_messages \
            import EMPTY_VALUE_FOR_FIELD_ID
        for field_dto in field_dtos:
            field_id = field_dto.field_id.strip()
            is_field_id_empty = not field_id
            if is_field_id_empty:
                raise FieldIdEmptyValueException(EMPTY_VALUE_FOR_FIELD_ID)
        return

    @staticmethod
    def _check_for_duplication_of_filed_ids(
            field_dtos
    ) -> Optional[DuplicationOfFieldIdsExist]:

        from ib_tasks.constants.exception_messages \
            import DUPLICATION_OF_FIELD_IDS
        field_ids = []
        for field_dto in field_dtos:
            field_id = field_dto.field_id
            field_ids.append(field_id)

        duplication_of_field_ids = [
            field_id
            for field_id, count in collections.Counter(field_ids).items()
            if count > 1
        ]
        if duplication_of_field_ids:
            raise DuplicationOfFieldIdsExist(
                DUPLICATION_OF_FIELD_IDS.format(duplication_of_field_ids)
            )
        return

    @staticmethod
    def _validate_field_display_name(
            field_dtos: List[FieldDTO]
    ) -> Optional[InvalidValueForFieldDisplayName]:

        from ib_tasks.constants.exception_messages \
            import INVALID_FIELDS_DISPLAY_NAMES
        invalid_field_display_names = []

        for field_dto in field_dtos:
            field_display_name = field_dto.field_display_name.strip()
            is_field_display_name_empty = not field_display_name
            if is_field_display_name_empty:
                invalid_field_display_name_dict = {
                    "field_id": field_dto.field_id,
                    "display_name": field_dto.field_display_name
                }
                invalid_field_display_names.append(invalid_field_display_name_dict)

        if invalid_field_display_names:
            raise InvalidValueForFieldDisplayName(
                INVALID_FIELDS_DISPLAY_NAMES.format(invalid_field_display_names)
            )
        return

    @staticmethod
    def _validate_field_type(
            field_dtos: List[FieldDTO]
    ) -> Optional[InvalidValueForFieldType]:

        from ib_tasks.constants.exception_messages \
            import INVALID_VALUES_FOR_FIELD_TYPES
        from ib_tasks.constants.constants import FIELD_TYPES_LIST

        for field_dto in field_dtos:
            field_type = field_dto.field_type
            if field_type not in FIELD_TYPES_LIST:
                raise InvalidValueForFieldType(
                    INVALID_VALUES_FOR_FIELD_TYPES.format(FIELD_TYPES_LIST)
                )
        return

    @staticmethod
    def _validate_field_type(
            field_dtos: List[FieldDTO]
    ) -> Optional[InvalidValueForFieldType]:

        from ib_tasks.constants.exception_messages \
            import INVALID_VALUES_FOR_FIELD_TYPES
        field_ids = []
        from ib_tasks.constants.constants import FIELD_TYPES_LIST

        for field_dto in field_dtos:
            field_type = field_dto.field_type
            if field_type not in FIELD_TYPES_LIST:
                field_ids.append(field_dto.field_id)

        if field_ids:
            raise InvalidValueForFieldType(
                INVALID_VALUES_FOR_FIELD_TYPES.format(FIELD_TYPES_LIST, field_ids)
            )
        return
