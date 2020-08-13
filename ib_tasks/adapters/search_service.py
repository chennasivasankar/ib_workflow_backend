from ib_tasks.interactors.field_dtos import SearchableFieldDetailDTO


class SearchService:

    @property
    def interface(self):
        from ib_iam.app_interfaces.service_interface \
            import ServiceInterface
        return ServiceInterface()

    def get_search_user_ids(self, offset: int, limit: int, search_query: str):

        user_ids = self.interface.get_search_users(
            offset=offset, limit=limit, search_query=search_query
        )
        return user_ids

    def get_search_countries(self, offset: int, limit: int, search_query: str):
        country_dtos = self.interface.get_search_countries(
            offset=offset, limit=limit, search_query=search_query
        )
        return [
            SearchableFieldDetailDTO(
                id=str(country_dto.country_id),
                name=country_dto.country_name
            ) for country_dto in country_dtos
        ]

    def get_search_states(self, offset: int, limit: int, search_query: str):
        state_dtos = self.interface.get_search_states(
            offset=offset, limit=limit, search_query=search_query
        )
        return [
            SearchableFieldDetailDTO(
                id=str(state_dto.state_id),
                name=state_dto.state_name
            ) for state_dto in state_dtos
        ]

    def get_search_cities(self, offset: int, limit: int, search_query: str):
        city_dtos = self.interface.get_search_cities(
            offset=offset, limit=limit, search_query=search_query
        )
        return [
            SearchableFieldDetailDTO(
                id=str(city_dto.city_id),
                name=city_dto.city_name
            ) for city_dto in city_dtos
        ]
