from typing import Optional, List

from ib_tasks.interactors.storage_interfaces.fields_dtos import \
    FieldWithGoFDisplayNameDTO
from ib_tasks.interactors.storage_interfaces.gof_dtos import \
    GoFIdWithGoFDisplayNameDTO


class GetGoFsFieldsDisplayNameMixin:

    @staticmethod
    def get_gof_display_name(
            gof_id: str,
            gof_id_with_gof_display_name_dtos: List[GoFIdWithGoFDisplayNameDTO]
    ) -> Optional[str]:
        for gof_dto in gof_id_with_gof_display_name_dtos:
            gof_id_matched = gof_id == gof_dto.gof_id
            if gof_id_matched:
                return gof_dto.gof_display_name
        return

    @staticmethod
    def get_field_display_name(
            field_id: str,
            field_id_with_field_display_name_dtos: List[
                FieldWithGoFDisplayNameDTO]
    ) -> Optional[str]:
        for field_dto in field_id_with_field_display_name_dtos:
            field_id_matched = field_id == field_dto.field_id
            if field_id_matched:
                return field_dto.field_display_name
        return

    @staticmethod
    def get_gof_display_names(
            gof_ids: List[str],
            gof_id_with_gof_display_name_dtos: List[GoFIdWithGoFDisplayNameDTO]
    ) -> List[str]:
        gof_display_names = []
        for gof_dto in gof_id_with_gof_display_name_dtos:
            gof_id_matched = gof_dto.gof_id in gof_ids
            if gof_id_matched:
                gof_display_names.append(gof_dto.gof_display_name)
        return gof_display_names

    @staticmethod
    def get_field_display_names(
            field_ids: List[str],
            field_id_with_field_display_name_dtos: List[
                FieldWithGoFDisplayNameDTO]
    ) -> List[str]:
        field_display_names = []
        for field_dto in field_id_with_field_display_name_dtos:
            field_id_matched = field_dto.field_id in field_ids
            if field_id_matched:
                field_display_names.append(field_dto.field_display_name)
        return sorted(list(set(field_display_names)))
