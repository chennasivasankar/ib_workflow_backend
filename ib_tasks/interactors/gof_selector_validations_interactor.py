import json
from typing import List, Dict, Union, Optional
from json.decoder import JSONDecodeError
import collections

from ib_tasks.exceptions.custom_exceptions import (
    InvalidJsonForFieldValue,
    EmptyValuesForGoFNames,
    DuplicationOfGoFNamesForFieldValues,
    InvalidGOFIds
)

from ib_tasks.interactors.storage_interfaces.task_storage_interface \
    import TaskStorageInterface
from ib_tasks.interactors.storage_interfaces.dtos import FieldDTO


class GoFSelectorValidationsInteractor:
    def __init__(self, storage: TaskStorageInterface):
        self.storage = storage

    def gof_selector_validations(self, field_dto: FieldDTO):
        field_values = self._check_for_valid_json(field_dto)
        gof_names = self._get_gof_names(field_values)
        field_id = field_dto.field_id
        self._check_empty_values_for_gof_names(gof_names, field_id)
        self._check_for_duplication_of_gof_names(gof_names, field_id)
        gof_ids = self._get_gof_ids(field_values)
        self._validate_gof_ids(gof_ids, field_id)
        field_values = self._eliminate_duplication_of_gof_ids(field_values)
        field_dto.field_values = json.dumps(field_values)

    @staticmethod
    def _eliminate_duplication_of_gof_ids(
            field_values: List[Dict]
    ) -> List[Dict]:

        for field_value_dict in field_values:
            gof_ids = field_value_dict["gof_ids"]
            field_value_dict["gof_ids"] = sorted(list(set(gof_ids)))
        return field_values

    @staticmethod
    def _check_for_valid_json(
            field_dto: FieldDTO
    ) -> Union[InvalidJsonForFieldValue, List[Dict]]:

        from ib_tasks.constants.exception_messages import INVALID_JSON

        try:
            field_values = json.loads(field_dto.field_values)
        except JSONDecodeError:
            raise InvalidJsonForFieldValue(
                INVALID_JSON.format(field_dto.field_id)
            )
        return field_values

    @staticmethod
    def _get_gof_names(field_values) -> List[str]:
        gof_names = []
        for field_value in field_values:
            name = field_value['name']
            gof_names.append(name)
        return gof_names

    @staticmethod
    def _check_empty_values_for_gof_names(
            gof_names: List[str], field_id: str
    ) -> Optional[EmptyValuesForGoFNames]:

        from ib_tasks.constants.exception_messages \
            import EMPTY_VALUE_FOR_GOF_NAMES

        for gof_name in gof_names:
            is_gof_name_empty = not gof_name.strip()
            if is_gof_name_empty:
                raise EmptyValuesForGoFNames(
                    EMPTY_VALUE_FOR_GOF_NAMES.format(field_id)
                )
        return

    @staticmethod
    def _check_for_duplication_of_gof_names(
            gof_names: List[str], field_id: str
    ) -> Optional[DuplicationOfGoFNamesForFieldValues]:

        from ib_tasks.constants.exception_messages \
            import DUPLICATED_OF_GOF_NAMES_FOR_FIELD_VALUES

        duplication_of_gof_names = [
            gof_name
            for gof_name, count in collections.Counter(gof_names).items()
            if count > 1
        ]
        if duplication_of_gof_names:
            exception_message = {
                "field_id": field_id,
                "duplication_of_gof_names": duplication_of_gof_names
            }
            raise DuplicationOfGoFNamesForFieldValues(
                DUPLICATED_OF_GOF_NAMES_FOR_FIELD_VALUES.format(
                    exception_message
                )
            )
        return

    @staticmethod
    def _get_gof_ids(field_values):
        all_gof_ids = []
        for field_value in field_values:
            gof_ids = field_value['gof_ids']
            all_gof_ids += gof_ids
        return all_gof_ids

    def _validate_gof_ids(
            self, gof_ids: List[str], field_id: str
    ) -> Optional[InvalidGOFIds]:

        from ib_tasks.constants.exception_messages \
            import INVALID_GOF_IDS_EXCEPTION_MESSAGE
        existing_gof_ids = self.storage.get_existing_gof_ids(gof_ids)
        invalid_gof_ids = []

        for gof_id in gof_ids:
            if gof_id not in existing_gof_ids:
                invalid_gof_ids.append(gof_id)

        if invalid_gof_ids:
            gof_ids = sorted(list(set(invalid_gof_ids)))
            exception_message = {
                "field_id": field_id,
                "invalid_gof_ids": gof_ids
            }
            raise InvalidGOFIds(
                INVALID_GOF_IDS_EXCEPTION_MESSAGE.format(exception_message)
            )
        return
