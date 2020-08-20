import pytest
from mock import create_autospec

from ib_iam.constants.enums import Searchable
from ib_iam.interactors.get_searchable_details_interactor import \
    GetSearchableDetailsInteractor
from ib_iam.tests.factories.adapter_dtos import SearchableDTOFactory
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
    def searchable_dtos_for_invalid_city_ids(self):
        searchable_dtos = [
            SearchableDTOFactory(
                search_type=Searchable.CITY.value,
                id=1
            ),
            SearchableDTOFactory(
                search_type=Searchable.CITY.value,
                id=6
            ),
            SearchableDTOFactory(
                search_type=Searchable.CITY.value,
                id=4
            ),
            SearchableDTOFactory(
                search_type=Searchable.CITY.value,
                id=5
            )
        ]
        return searchable_dtos

    @pytest.fixture
    def searchable_dtos_for_invalid_state_ids(self):
        searchable_dtos = [
            SearchableDTOFactory(
                search_type=Searchable.STATE.value,
                id=2
            ),
            SearchableDTOFactory(
                search_type=Searchable.STATE.value,
                id=5
            ),
            SearchableDTOFactory(
                search_type=Searchable.STATE.value,
                id=4
            ),
            SearchableDTOFactory(
                search_type=Searchable.STATE.value,
                id=7
            )
        ]
        return searchable_dtos

    @pytest.fixture
    def searchable_dtos_for_invalid_country_ids(self):
        searchable_dtos = [
            SearchableDTOFactory(
                search_type=Searchable.COUNTRY.value,
                id=6
            ),
            SearchableDTOFactory(
                search_type=Searchable.COUNTRY.value,
                id=4
            ),
            SearchableDTOFactory(
                search_type=Searchable.COUNTRY.value,
                id=16
            ),
            SearchableDTOFactory(
                search_type=Searchable.COUNTRY.value,
                id=17
            )
        ]
        return searchable_dtos

    @pytest.fixture
    def searchable_dtos_for_invalid_user_ids(self):
        searchable_dtos = [
            SearchableDTOFactory(
                search_type=Searchable.USER.value,
                id="123e4567-e89b-12d3-a456-426614174000"
            ),
            SearchableDTOFactory(
                search_type=Searchable.USER.value,
                id="123e4567-e89b-12d3-a456-426614174001"
            ),
            SearchableDTOFactory(
                search_type=Searchable.USER.value,
                id="123e4567-e89b-12d3-a456-426614174002"
            ),
            SearchableDTOFactory(
                search_type=Searchable.USER.value,
                id="123e4567-e89b-12d3-a456-426614174003"
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
                id="123e4567-e89b-12d3-a456-426614174000",
                value='{"name": "name0", "profile_pic_url": "url0"}'
            ),
            SearchableDetailsDTOFactory(
                search_type=Searchable.USER.value,
                id="123e4567-e89b-12d3-a456-426614174001",
                value='{"name": "name1", "profile_pic_url": "url1"}'
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
            searchable_type_user_details_dtos, storage_mock, mocker
    ):
        # Arrange
        city_ids = [1, 6]
        state_ids = [2, 5]
        country_ids = [6, 4]
        from ib_iam.tests.common_fixtures.adapters.user_base_details import \
            get_basic_user_dtos_mock
        get_basic_user_dtos_mock_method = get_basic_user_dtos_mock(mocker)
        interactor = GetSearchableDetailsInteractor(storage=storage_mock)
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
        storage_mock.get_searchable_type_country_details_dtos \
            .assert_called_once_with(country_ids)
        storage_mock.get_searchable_type_state_details_dtos \
            .assert_called_once_with(state_ids)
        storage_mock.get_searchable_type_city_details_dtos \
            .assert_called_once_with(
                city_ids)
        get_basic_user_dtos_mock_method.assert_called_once()

    def test_given_searchable_dtos_with_invalid_city_ids_raise_exception(
            self, searchable_dtos_for_invalid_city_ids,
            searchable_type_city_details_dtos, storage_mock
    ):
        # Arrange
        from ib_iam.exceptions.custom_exceptions import InvalidCityIds
        city_ids = [1, 6, 4, 5]
        invalid_city_ids = [4, 5]
        interactor = GetSearchableDetailsInteractor(storage=storage_mock)
        storage_mock.get_searchable_type_city_details_dtos.return_value = \
            searchable_type_city_details_dtos

        # Act
        with pytest.raises(InvalidCityIds) as err:
            interactor.get_searchable_details_dtos(
                searchable_dtos=searchable_dtos_for_invalid_city_ids
            )

        # Assert
        exception_object = err.value
        assert exception_object.city_ids == invalid_city_ids
        storage_mock.get_searchable_type_city_details_dtos\
            .assert_called_once_with(
                city_ids)

    def test_given_searchable_dtos_with_invalid_state_ids_raise_exception(
            self, searchable_dtos_for_invalid_state_ids,
            searchable_type_state_details_dtos, storage_mock
    ):
        # Arrange
        from ib_iam.exceptions.custom_exceptions import InvalidStateIds
        state_ids = [2, 5, 4, 7]
        invalid_state_ids = [4, 7]
        interactor = GetSearchableDetailsInteractor(storage=storage_mock)
        storage_mock.get_searchable_type_city_details_dtos.return_value = []
        storage_mock.get_searchable_type_state_details_dtos.return_value = \
            searchable_type_state_details_dtos

        # Act
        with pytest.raises(InvalidStateIds) as err:
            interactor.get_searchable_details_dtos(
                searchable_dtos=searchable_dtos_for_invalid_state_ids
            )

        # Assert
        exception_object = err.value
        assert exception_object.state_ids == invalid_state_ids
        storage_mock.get_searchable_type_state_details_dtos\
            .assert_called_once_with(
                state_ids)

    def test_given_searchable_dtos_with_invalid_country_ids_raise_exception(
            self, searchable_dtos_for_invalid_country_ids,
            searchable_type_country_details_dtos, storage_mock
    ):
        # Arrange
        from ib_iam.exceptions.custom_exceptions import InvalidCountryIds
        country_ids = [6, 4, 16, 17]
        invalid_country_ids = [16, 17]
        interactor = GetSearchableDetailsInteractor(storage=storage_mock)
        storage_mock.get_searchable_type_city_details_dtos.return_value = []
        storage_mock.get_searchable_type_state_details_dtos.return_value = []
        storage_mock.get_searchable_type_country_details_dtos.return_value = \
            searchable_type_country_details_dtos

        # Act
        with pytest.raises(InvalidCountryIds) as err:
            interactor.get_searchable_details_dtos(
                searchable_dtos=searchable_dtos_for_invalid_country_ids
            )

        # Assert
        exception_object = err.value
        assert exception_object.country_ids == invalid_country_ids
        storage_mock.get_searchable_type_country_details_dtos\
            .assert_called_once_with(
                country_ids)

    def test_given_searchable_dtos_with_invalid_user_ids_raise_exception(
            self, searchable_dtos_for_invalid_user_ids,
            storage_mock, mocker
    ):
        # Arrange
        from ib_iam.tests.common_fixtures.adapters.user_base_details import \
            get_basic_user_dtos_mock
        get_basic_user_dtos_mock(mocker)
        invalid_user_ids = [
            "123e4567-e89b-12d3-a456-426614174002",
            "123e4567-e89b-12d3-a456-426614174003"
        ]
        from ib_iam.exceptions.custom_exceptions import InvalidUserIds
        interactor = GetSearchableDetailsInteractor(storage=storage_mock)
        storage_mock.get_searchable_type_city_details_dtos.return_value = []
        storage_mock.get_searchable_type_state_details_dtos.return_value = []
        storage_mock.get_searchable_type_country_details_dtos.return_value = []

        # Act
        with pytest.raises(InvalidUserIds) as err:
            interactor.get_searchable_details_dtos(
                searchable_dtos=searchable_dtos_for_invalid_user_ids
            )

        # Assert
        exception_object = err.value
        assert exception_object.user_ids == invalid_user_ids
