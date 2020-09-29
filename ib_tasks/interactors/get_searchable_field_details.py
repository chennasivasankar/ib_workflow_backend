from typing import List

from ib_tasks.adapters.dtos import SearchableDetailsDTO
from ib_tasks.interactors.storage_interfaces.get_task_dtos import \
    FieldSearchableDTO
from ib_tasks.interactors.task_dtos import SearchableDTO


class GetSearchableFieldDetails:

    def get_searchable_fields_details(
            self, field_searchable_dtos: List[FieldSearchableDTO]
    ) -> List[FieldSearchableDTO]:
        field_searchable_dtos = \
            self._get_field_searchable_dtos_with_searchable_field_response(
                field_searchable_dtos)
        return field_searchable_dtos

    def _get_field_searchable_dtos_with_searchable_field_response(
            self, field_searchable_dtos: List[FieldSearchableDTO]
    ) -> List[FieldSearchableDTO]:
        field_searchable_dtos = \
            self._convert_field_response_based_on_field_value(
                field_searchable_dtos)
        searchable_dtos = self._get_searchable_dtos(field_searchable_dtos)
        searchable_details_dtos = self._get_searchable_details_dtos(
            searchable_dtos
        )
        field_searchable_dtos = \
            self._get_searchable_field_response_for_field_searchable_dtos(
                field_searchable_dtos, searchable_details_dtos
            )

        return field_searchable_dtos

    @staticmethod
    def _convert_field_response_based_on_field_value(
            field_searchable_dtos: List[FieldSearchableDTO]
    ) -> List[FieldSearchableDTO]:
        from ib_tasks.constants.constants import \
            SEARCHABLE_TYPES_WITH_RESPONSE_ID_AS_STRING

        for field_searchable_dto in field_searchable_dtos:
            if field_searchable_dto.field_value in \
                    SEARCHABLE_TYPES_WITH_RESPONSE_ID_AS_STRING:
                continue
            field_searchable_dto.field_response = int(
                field_searchable_dto.field_response)
        return field_searchable_dtos

    @staticmethod
    def _get_searchable_dtos(
            field_searchable_dtos: List[FieldSearchableDTO]
    ) -> List[SearchableDTO]:
        searchable_dtos = [
            SearchableDTO(
                search_type=field_searchable_dto.field_value,
                id=field_searchable_dto.field_response
            )
            for field_searchable_dto in field_searchable_dtos
        ]
        return searchable_dtos

    @staticmethod
    def _get_searchable_details_dtos(
            searchable_dtos: List[SearchableDTO]
    ) -> List[SearchableDetailsDTO]:
        from ib_tasks.adapters.service_adapter import get_service_adapter
        service_adapter = get_service_adapter()
        searchable_details_service = service_adapter.searchable_details_service
        searchable_details_dtos = \
            searchable_details_service.get_searchable_details_dtos(
                searchable_dtos
            )
        return searchable_details_dtos

    def _get_searchable_field_response_for_field_searchable_dtos(
            self, field_searchable_dtos: List[FieldSearchableDTO],
            searchable_details_dtos: List[SearchableDetailsDTO]
    ) -> List[FieldSearchableDTO]:
        for field_searchable_dto in field_searchable_dtos:
            field_response = self._get_updated_field_response(
                field_searchable_dto, searchable_details_dtos
            )
            field_searchable_dto.field_response = field_response
        return field_searchable_dtos

    @staticmethod
    def _get_updated_field_response(
            field_searchable_dto: FieldSearchableDTO,
            searchable_details_dtos: List[SearchableDetailsDTO]
    ) -> str:
        import json
        field_value = field_searchable_dto.field_value
        field_response = field_searchable_dto.field_response
        for searchable_details_dto in searchable_details_dtos:
            search_type = searchable_details_dto.search_type
            response_id = searchable_details_dto.id
            if field_value == search_type and field_response == response_id:
                field_response = {
                    "id": response_id,
                    "value": searchable_details_dto.value
                }
                return json.dumps(field_response)
