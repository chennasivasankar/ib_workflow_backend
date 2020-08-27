from typing import List, Optional

import collections

from ib_tasks.interactors.storage_interfaces.fields_dtos import FieldDTO
from ib_tasks.interactors.storage_interfaces.gof_storage_interface import \
    GoFStorageInterface

from ib_tasks.exceptions.fields_custom_exceptions import (
    FieldIdEmptyValueException,
    InvalidGOFIds,
    DuplicationOfFieldIdsExist,
    InvalidValueForFieldDisplayName,
    InvalidValueForFieldType,
)


class CreateOrUpdateFieldsBaseValidationInteractor:

    def __init__(self, gof_storage: GoFStorageInterface):
        self.gof_storage = gof_storage

    def fields_base_validations(self, field_dtos: List[FieldDTO]):
        self._validate_field_orders(field_dtos=field_dtos)
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
        existing_gof_ids = self.gof_storage.get_existing_gof_ids(gof_ids)
        invalid_gof_ids = []
        for gof_id in gof_ids:
            if gof_id not in existing_gof_ids:
                invalid_gof_ids.append(gof_id)

        if invalid_gof_ids:
            raise InvalidGOFIds(
                INVALID_GOF_IDS_EXCEPTION_MESSAGE.format(invalid_gof_ids)
            )
        return

    def _validate_field_orders(self, field_dtos: List[FieldDTO]):
        negative_ordered_fields = []
        for field_dto in field_dtos:
            is_negative_order = field_dto.order < 0
            if is_negative_order:
                negative_ordered_fields.append(field_dto.field_id)
        if negative_ordered_fields:
            from ib_tasks.exceptions.fields_custom_exceptions import \
                OrderForFieldShouldNotBeNegativeException
            from ib_tasks.constants.exception_messages import \
                ORDER_FOR_FIELD_SHOULD_NOT_BE_NEGATIVE
            raise OrderForFieldShouldNotBeNegativeException(
                ORDER_FOR_FIELD_SHOULD_NOT_BE_NEGATIVE.format(
                    negative_ordered_fields))

        field_dtos_group_by_gof_id_dict = collections.defaultdict(list)
        for field_dto in field_dtos:
            field_dtos_group_by_gof_id_dict[field_dto.gof_id].append(field_dto)

        for gof_id, field_dtos_of_gof in \
                field_dtos_group_by_gof_id_dict.items():
            self._validate_duplicate_orders_for_fields_of_same_gof(
                gof_id=gof_id, field_dtos=field_dtos_of_gof)

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
        field_ids = []

        for field_dto in field_dtos:
            field_display_name = field_dto.field_display_name.strip()
            is_field_display_name_empty = not field_display_name
            if is_field_display_name_empty:
                field_ids.append(field_dto.field_id)

        if field_ids:
            raise InvalidValueForFieldDisplayName(
                INVALID_FIELDS_DISPLAY_NAMES.format(field_ids)
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
                INVALID_VALUES_FOR_FIELD_TYPES.format(
                    FIELD_TYPES_LIST, field_ids
                )
            )
        return

    @staticmethod
    def _validate_duplicate_orders_for_fields_of_same_gof(
            gof_id: str, field_dtos: List[FieldDTO]):
        field_orders_of_gof = [
            field_dto.order
            for field_dto in field_dtos
        ]
        counter = collections.Counter(field_orders_of_gof)
        duplicate_orders = []
        for order, count in counter.items():
            is_duplicate_order = count >= 2
            if is_duplicate_order:
                duplicate_orders.append(order)
        if duplicate_orders:
            from ib_tasks.exceptions.fields_custom_exceptions import \
                DuplicateOrdersForFieldsOfGoFException
            from ib_tasks.constants.exception_messages import \
                DUPLICATE_ORDER_FOR_FIELDS_OF_SAME_GOF
            raise DuplicateOrdersForFieldsOfGoFException(
                DUPLICATE_ORDER_FOR_FIELDS_OF_SAME_GOF.format(
                    duplicate_orders, gof_id)
            )
