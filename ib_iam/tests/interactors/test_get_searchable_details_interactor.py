import pytest
from mock import create_autospec

from ib_iam.constants.enums import Searchable
from ib_iam.interactors.get_searchable_details_interactor import \
    GetSearchableDetailsInteractor
from ib_iam.tests.factories.storage_dtos import SearchableDetailsDTOFactory


class TestGetSearchableDetailsInteractor:

    @pytest.fixture
    def storage_mock(self):
        from ib_iam.interactors.storage_interfaces \
            .searchable_storage_interface import \
            SearchableStorageInterface
        return create_autospec(SearchableStorageInterface)

    @pytest.fixture
    def searchable_dtos(self):
        from ib_iam.tests.factories.adapter_dtos import SearchableDTOFactory
        searchable_dtos = [
            SearchableDTOFactory(
                search_type=Searchable.CITY.value,
                id=1
            ),
            SearchableDTOFactory(
                search_type=Searchable.STATE.value,
                id=2
            ),
            SearchableDTOFactory(
                search_type=Searchable.COUNTRY.value,
                id=6
            ),
            SearchableDTOFactory(
                search_type=Searchable.USER.value,
                id="123e4567-e89b-12d3-a456-426614174000"
            ),
            SearchableDTOFactory(
                search_type=Searchable.STATE.value,
                id=5
            ),
            SearchableDTOFactory(
                search_type=Searchable.COUNTRY.value,
                id=4
            ),
            SearchableDTOFactory(
                search_type=Searchable.CITY.value,
                id=6
            ),
            SearchableDTOFactory(
                search_type=Searchable.USER.value,
                id="123e4567-e89b-12d3-a456-426614174001"
            )
        ]
        return searchable_dtos

    @pytest.fixture
    def searchable_type_city_details_dtos(self):
        searchable_type_city_details_dtos = [
            SearchableDetailsDTOFactory(
                search_type=Searchable.CITY.value,
                id=1,
                value="Hyderabad"
            ),
            SearchableDetailsDTOFactory(
                search_type=Searchable.CITY.value,
                id=6,
                value="Delhi"
            )
        ]
        return searchable_type_city_details_dtos

    @pytest.fixture
    def searchable_type_state_details_dtos(self):
        searchable_type_state_details_dtos = [
            SearchableDetailsDTOFactory(
                search_type=Searchable.STATE.value,
                id=2,
                value="Andhra Pradesh"
            ),
            SearchableDetailsDTOFactory(
                search_type=Searchable.STATE.value,
                id=5,
                value="Kerala"
            )
        ]
        return searchable_type_state_details_dtos

    @pytest.fixture
    def searchable_type_country_details_dtos(self):
        searchable_type_country_details_dtos = [
            SearchableDetailsDTOFactory(
                search_type=Searchable.COUNTRY.value,
                id=4,
                value="India"
            ),
            SearchableDetailsDTOFactory(
                search_type=Searchable.COUNTRY.value,
                id=6,
                value="America"
            )
        ]
        return searchable_type_country_details_dtos

    @pytest.fixture
    def searchable_type_user_details_dtos(self):
        searchable_type_user_details_dtos = [
            SearchableDetailsDTOFactory(
                search_type=Searchable.USER.value,
                id="123e4567-e89b-12d3-a456-426614174001",
                value="User1"
            ),
            SearchableDetailsDTOFactory(
                search_type=Searchable.USER.value,
                id="123e4567-e89b-12d3-a456-426614174000",
                value="User2"
            )
        ]
        return searchable_type_user_details_dtos

    @pytest.fixture
    def searchable_details_dtos(
            self, searchable_type_city_details_dtos,
            searchable_type_state_details_dtos,
            searchable_type_country_details_dtos,
            searchable_type_user_details_dtos
    ):
        searchable_details_dtos = (
                searchable_type_city_details_dtos +
                searchable_type_state_details_dtos +
                searchable_type_country_details_dtos +
                searchable_type_user_details_dtos
        )
        return searchable_details_dtos

    def test_given_searchable_dtos_returns_searchable_details_dtos(
            self, searchable_dtos, searchable_type_city_details_dtos,
            searchable_type_state_details_dtos,
            searchable_type_country_details_dtos, searchable_details_dtos,
            searchable_type_user_details_dtos, storage_mock
    ):
        # Arrange
        city_ids = [1, 6]
        state_ids = [2, 5]
        country_ids = [6, 4]
        user_ids = ["123e4567-e89b-12d3-a456-426614174000",
                    "123e4567-e89b-12d3-a456-426614174001"]
        interactor = GetSearchableDetailsInteractor(storage=storage_mock)
        storage_mock.get_searchable_type_user_details_dtos.return_value = \
            searchable_type_user_details_dtos
        storage_mock.get_searchable_type_country_details_dtos.return_value = \
            searchable_type_country_details_dtos
        storage_mock.get_searchable_type_state_details_dtos.return_value = \
            searchable_type_state_details_dtos
        storage_mock.get_searchable_type_city_details_dtos.return_value = \
            searchable_type_city_details_dtos

        # Act
        actual_searchable_details_dtos = \
            interactor.get_searchable_details_dtos(
                searchable_dtos=searchable_dtos
            )

        # Assert
        assert actual_searchable_details_dtos == searchable_details_dtos
        storage_mock.get_searchable_type_user_details_dtos\
            .assert_called_once_with(
                user_ids)
        storage_mock.get_searchable_type_country_details_dtos \
            .assert_called_once_with(country_ids)
        storage_mock.get_searchable_type_state_details_dtos \
            .assert_called_once_with(state_ids)
        storage_mock.get_searchable_type_city_details_dtos\
            .assert_called_once_with(
                city_ids)
