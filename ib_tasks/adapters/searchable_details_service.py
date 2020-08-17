from typing import List

from ib_tasks.adapters.dtos import SearchableDetailsDTO
from ib_tasks.interactors.task_dtos import SearchableDTO


class SearchableDetailsService:

    @property
    def interface(self):
        from ib_iam.app_interfaces.service_interface import ServiceInterface
        return ServiceInterface()

    def get_searchable_details_dtos(
            self, searchable_dtos: List[SearchableDTO]
    ) -> List[SearchableDetailsDTO]:
        searchable_dtos = self.interface.get_searchable_details_dtos(
            searchable_dtos
        )
        searchable_details_dtos = [
            SearchableDetailsDTO(
                search_type=searchable_dto.search_type,
                id=searchable_dto.id,
                value=searchable_dto.value
            )
            for searchable_dto in searchable_dtos
        ]
        return searchable_details_dtos
