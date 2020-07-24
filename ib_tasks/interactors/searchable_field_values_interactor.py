from typing import List
from ib_tasks.adapters.dtos import UserDTO
from ib_tasks.interactors.field_dtos import SearchableFieldTypeDTO, \
    SearchableFieldDetailDTO
from ib_tasks.interactors.presenter_interfaces. \
    searchable_field_values_presenter_interface import \
    SearchableFieldValuesPresenterInterface


class SearchableFieldValuesInteractor:
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

        return presenter.get_searchable_field_values_response(
            searchable_value_detail_dtos)

    def searchable_field_values_based_on_query(
            self, searchable_field_type_dto: SearchableFieldTypeDTO) -> \
            List[SearchableFieldDetailDTO]:
        limit = searchable_field_type_dto.limit
        offset = searchable_field_type_dto.offset
        search_query = searchable_field_type_dto.search_query
        if offset is None:
            from ib_tasks.constants.constants import OFFSET_VALUE
            offset = OFFSET_VALUE
        if limit is None:
            from ib_tasks.constants.constants import LIMIT_VALUE
            limit = LIMIT_VALUE
        self._validations_of_limit_and_offset(limit=limit, offset=offset)
        limit = offset + limit

        searchable_value_detail_dtos = self._get_user_dtos(offset=offset,
                                                           limit=limit,
                                                           search_query=search_query)

        return searchable_value_detail_dtos

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
