from typing import List
from ib_tasks.interactors.field_dtos import SearchableFieldTypeDTO, \
    SearchableFieldDetailDTO
from ib_tasks.interactors.presenter_interfaces. \
    searchable_field_values_presenter_interface import \
    SearchableFieldValuesPresenterInterface
from ib_tasks.interactors.storage_interfaces.elastic_storage_interface \
    import ElasticSearchStorageInterface


class SearchableFieldValuesInteractor:

    def __init__(self, elastic_storage: ElasticSearchStorageInterface):
        self.elastic_storage = elastic_storage

    def searchable_field_values_wrapper(
            self, searchable_field_type_dto: SearchableFieldTypeDTO,
            presenter: SearchableFieldValuesPresenterInterface):
        from ib_tasks.exceptions.fields_custom_exceptions import \
            LimitShouldBeGreaterThanZeroException, \
            OffsetShouldBeGreaterThanOrEqualToMinusOneException
        try:

            searchable_value_detail_dtos = self.searchable_field_values_based_on_query(
                searchable_field_type_dto)
        except LimitShouldBeGreaterThanZeroException:
            return presenter.raise_limit_should_be_greater_than_zero_exception(
            )
        except OffsetShouldBeGreaterThanOrEqualToMinusOneException:
            return presenter. \
                raise_offset_should_be_greater_than_or_equal_to_minus_one_exception(
            )
        print("searchable_value_detail_dtos", searchable_value_detail_dtos)

        return presenter.get_searchable_field_values_response(
            searchable_value_detail_dtos)

    def searchable_field_values_based_on_query(
            self, searchable_field_type_dto: SearchableFieldTypeDTO) -> \
            List[SearchableFieldDetailDTO]:
        limit = searchable_field_type_dto.limit
        offset = searchable_field_type_dto.offset
        search_query = searchable_field_type_dto.search_query
        self._validations_of_limit_and_offset(limit=limit, offset=offset)

        search_type = searchable_field_type_dto.searchable_type
        from ib_tasks.constants.enum import Searchable
        if search_type == Searchable.USER.value:
            user_dtos = self.elastic_storage.query_users(
                offset=offset, limit=limit, search_query=search_query
            )
            return [
                SearchableFieldDetailDTO(
                    id=user_dto.user_id,
                    name=user_dto.username
                ) for user_dto in user_dtos
            ]
        elif search_type == Searchable.COUNTRY.value:
            country_dtos = self.elastic_storage.query_countries(
                offset=offset, limit=limit, search_query=search_query
            )
            return [
                SearchableFieldDetailDTO(
                    id=str(country_dto.country_id),
                    name=country_dto.country_name
                ) for country_dto in country_dtos
            ]
        elif search_type == Searchable.STATE.value:
            state_dtos = self.elastic_storage.query_states(
                offset=offset, limit=limit, search_query=search_query
            )
            return [
                SearchableFieldDetailDTO(
                    id=str(state_dto.state_id),
                    name=state_dto.state_name
                ) for state_dto in state_dtos
            ]
        elif search_type == Searchable.CITY.value:
            city_dtos = self.elastic_storage.query_cities(
                offset=offset, limit=limit, search_query=search_query
            )
            return [
                SearchableFieldDetailDTO(
                    id=str(city_dto.city_id),
                    name=city_dto.city_name
                ) for city_dto in city_dtos
            ]

    @staticmethod
    def _get_user_dtos(offset: int, limit: int, search_query: str) -> \
            List[SearchableFieldDetailDTO]:
        from ib_tasks.adapters.service_adapter import get_service_adapter
        service_adapter = get_service_adapter()
        if offset == -1:
            user_dtos = service_adapter.auth_service. \
                get_all_user_dtos_based_on_query(
                search_query=search_query)
            return user_dtos

        user_dtos = service_adapter.auth_service. \
            get_user_dtos_based_on_limit_and_offset(
            limit=limit, offset=offset, search_query=search_query)
        return user_dtos

    @staticmethod
    def _validations_of_limit_and_offset(offset: int, limit: int):
        if limit < 1:
            from ib_tasks.exceptions.fields_custom_exceptions import \
                LimitShouldBeGreaterThanZeroException
            raise LimitShouldBeGreaterThanZeroException

        if offset < -1:
            from ib_tasks.exceptions.fields_custom_exceptions import \
                OffsetShouldBeGreaterThanOrEqualToMinusOneException
            raise OffsetShouldBeGreaterThanOrEqualToMinusOneException
