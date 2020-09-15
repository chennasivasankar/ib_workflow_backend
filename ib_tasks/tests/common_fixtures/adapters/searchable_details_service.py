def searchable_details_dtos_mock(mocker):
    path = "ib_tasks.adapters.searchable_details_service" \
           ".SearchableDetailsService.get_searchable_details_dtos"
    mock = mocker.patch(path)
    from ib_tasks.adapters.dtos import SearchableDetailsDTO
    from ib_tasks.constants.enum import Searchable
    import json
    value = {
            "name": "User1",
            "profile_pic_url": "https://ib-workflows-web-alpha.apigateway.in"
                               "/boards?board=FINB_AV4_VENDOR_VERIFICATION"
    }
    value = json.dumps(value)
    searchable_details_dtos = [
            SearchableDetailsDTO(
                    search_type=Searchable.CITY.value,
                    id=1, value="Hyderabad",
            ),
            SearchableDetailsDTO(
                    search_type=Searchable.USER.value,
                    id="123e4567-e89b-12d3-a456-426614174000",
                    value=value
            )
    ]
    mock.return_value = searchable_details_dtos
    return mock


def searchable_details_dtos_invalid_city_ids_mock(mocker):
    path = "ib_tasks.adapters.searchable_details_service" \
           ".SearchableDetailsService.get_searchable_details_dtos"
    mock = mocker.patch(path)
    from ib_tasks.adapters.searchable_details_service import \
        InvalidCityIdsException
    invalid_city_ids = [100, 110]
    exception_object = InvalidCityIdsException(invalid_city_ids)
    mock.side_effect = exception_object
    return mock


def user_searchable_details_dtos_mock(mocker):
    path = "ib_tasks.adapters.searchable_details_service" \
           ".SearchableDetailsService.get_searchable_details_dtos"
    mock = mocker.patch(path)
    from ib_tasks.adapters.dtos import SearchableDetailsDTO
    from ib_tasks.constants.enum import Searchable
    import json
    value = {
            "name": "User1",
            "profile_pic_url": "https://ib-workflows-web-alpha.apigateway.in"
                               "/boards?board=FINB_AV4_VENDOR_VERIFICATION"
    }
    value = json.dumps(value)
    searchable_details_dtos = [
            SearchableDetailsDTO(
                    search_type=Searchable.USER.value,
                    id="123e4567-e89b-12d3-a456-426614174001",
                    value=json.dumps({
                            "name": "User2",
                            "profile_pic_url":
                                "https://ib-workflows-web-alpha.apigateway.in"
                                "/boards?board=FINB_AV4_VENDOR_VERIFICATION"
                    }),
            ),
            SearchableDetailsDTO(
                    search_type=Searchable.USER.value,
                    id="123e4567-e89b-12d3-a456-426614174000",
                    value=value
            )
    ]
    mock.return_value = searchable_details_dtos
    return mock
