def searchable_details_dtos_mock(mocker):
    path = "ib_tasks.adapters.searchable_details_service" \
           ".SearchableDetailsService.get_searchable_details_dtos"
    mock = mocker.patch(path)
    from ib_tasks.adapters.dtos import SearchableDetailsDTO
    from ib_tasks.constants.enum import Searchable
    searchable_details_dtos = [
        SearchableDetailsDTO(
            search_type=Searchable.CITY.value,
            id=1, value="Hyderabad",
        ),
        SearchableDetailsDTO(
            search_type=Searchable.USER.value,
            id="123e4567-e89b-12d3-a456-426614174000",
            value="User1"
        )
    ]
    mock.return_value = searchable_details_dtos
    return mock
