from typing import List

from ib_iam.constants.enums import Searchable
from ib_iam.interactors.storage_interfaces.dtos import SearchableDetailsDTO
from ib_iam.interactors.storage_interfaces.searchable_storage_interface \
    import \
    SearchableStorageInterface


class SearchableStorageImplementation(SearchableStorageInterface):

    def get_searchable_type_city_details_dtos(
            self, ids: List[int]
    ) -> List[SearchableDetailsDTO]:
        from ib_iam.models import City
        city_details_set = City.objects.filter(
            id__in=ids
        ).values_list('id', 'name')
        searchable_type_city_details_dtos = [
            SearchableDetailsDTO(
                search_type=Searchable.City.value,
                id=city_details[0],
                value=city_details[1]
            )
            for city_details in city_details_set
        ]
        return searchable_type_city_details_dtos

    def get_searchable_type_state_details_dtos(
            self, ids: List[int]
    ) -> List[SearchableDetailsDTO]:
        pass

    def get_searchable_type_country_details_dtos(
            self, ids: List[int]
    ) -> List[SearchableDetailsDTO]:
        pass

    def get_searchable_type_user_details_dtos(
            self, ids: List[int]
    ) -> List[SearchableDetailsDTO]:
        pass
