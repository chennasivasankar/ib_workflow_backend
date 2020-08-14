from typing import List

from ib_tasks.adapters.dtos import SearchableDetailsDTO
from ib_tasks.interactors.task_dtos import SearchableDTO


class SearchableDetailsService:

    @property
    def interface(self):
        pass

    def get_searchable_details_dtos(
            self, searchable_details_dtos: List[SearchableDTO]
    ) -> List[SearchableDetailsDTO]:
        searchable_details_dtos = []
        return searchable_details_dtos
