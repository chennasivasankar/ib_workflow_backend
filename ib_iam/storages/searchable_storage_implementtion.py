from typing import List

from ib_iam.constants.enums import Searchable
from ib_iam.interactors.storage_interfaces.dtos import SearchableDetailsDTO
from ib_iam.interactors.storage_interfaces.searchable_storage_interface \
    import \
    SearchableStorageInterface


class SearchableStorageImplementation(SearchableStorageInterface):

    def get_valid_city_ids(self, city_ids: List[int]) -> List[int]:
        from ib_iam.models import City
        valid_city_ids = list(
            City.objects.filter(
                id__in=city_ids
            ).values_list('id', flat=True)
        )
        return valid_city_ids

    def get_valid_state_ids(self, state_ids: List[int]) -> List[int]:
        from ib_iam.models import State
        valid_state_ids = list(
            State.objects.filter(
                id__in=state_ids
            ).values_list('id', flat=True)
        )
        return valid_state_ids

    def get_valid_country_ids(self, country_ids: List[int]) -> List[int]:
        from ib_iam.models import Country
        valid_country_ids = list(
            Country.objects.filter(
                id__in=country_ids
            ).values_list('id', flat=True)
        )
        return valid_country_ids

    def get_valid_user_ids(self, ids: List[str]) -> List[str]:
        from ib_iam.models import UserDetails
        valid_user_ids = list(
            UserDetails.objects.filter(
                user_id__in=ids
            ).values_list('user_id', flat=True)
        )
        return valid_user_ids

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
