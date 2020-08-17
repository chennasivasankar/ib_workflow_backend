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
                search_type=Searchable.CITY.value,
                id=city_details[0],
                value=city_details[1]
            )
            for city_details in city_details_set
        ]
        return searchable_type_city_details_dtos

    def get_searchable_type_state_details_dtos(
            self, ids: List[int]
    ) -> List[SearchableDetailsDTO]:
        from ib_iam.models import State
        state_details_set = State.objects.filter(
            id__in=ids
        ).values_list('id', 'name')
        searchable_type_state_details_dtos = [
            SearchableDetailsDTO(
                search_type=Searchable.STATE.value,
                id=state_details[0],
                value=state_details[1]
            )
            for state_details in state_details_set
        ]
        return searchable_type_state_details_dtos

    def get_searchable_type_country_details_dtos(
            self, ids: List[int]
    ) -> List[SearchableDetailsDTO]:
        from ib_iam.models import Country
        country_details_set = Country.objects.filter(
            id__in=ids
        ).values_list('id', 'name')
        searchable_type_country_details_dtos = [
            SearchableDetailsDTO(
                search_type=Searchable.COUNTRY.value,
                id=country_details[0],
                value=country_details[1]
            )
            for country_details in country_details_set
        ]
        return searchable_type_country_details_dtos
