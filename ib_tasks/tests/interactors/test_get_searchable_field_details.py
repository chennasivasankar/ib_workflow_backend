import json
from unittest.mock import patch

import factory
import pytest

from ib_tasks.adapters.searchable_details_service import \
    SearchableDetailsService
from ib_tasks.constants.enum import Searchable
from ib_tasks.interactors.get_searchable_field_details import \
    GetSearchableFieldDetails
from ib_tasks.tests.factories.adapter_dtos import SearchableDetailsDTOFactory
from ib_tasks.tests.factories.storage_dtos import FieldSearchableDTOFactory


class TestGetSearchableFieldDetails:

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        FieldSearchableDTOFactory.reset_sequence()

    @pytest.fixture
    def searchable_dtos_with_city_type(self, reset_sequence):
        city_ids = [1, 2, 5]
        city_searchable_dtos = FieldSearchableDTOFactory.create_batch(
            size=3, field_value=Searchable.CITY.value,
            field_response=factory.Iterator(city_ids)
        )
        return city_searchable_dtos

    @pytest.fixture
    def searchable_dtos_with_state_type(self, reset_sequence):
        state_ids = [1, 2, 5]
        state_searchable_dtos = FieldSearchableDTOFactory.create_batch(
            size=3, field_value=Searchable.STATE.value,
            field_response=factory.Iterator(state_ids)
        )
        return state_searchable_dtos

    @pytest.fixture
    def searchable_dtos_with_country_type(self, reset_sequence):
        country_ids = [1, 2, 5]
        country_searchable_dtos = FieldSearchableDTOFactory.create_batch(
            size=3, field_value=Searchable.COUNTRY.value,
            field_response=factory.Iterator(country_ids)
        )
        return country_searchable_dtos

    @pytest.fixture
    def searchable_dtos_with_user_type(self, reset_sequence):
        user_ids = [
            "123e4567-e89b-12d3-a456-426614174000",
            "123e4567-e89b-12d3-a456-426614174001",
            "123e4567-e89b-12d3-a456-426614174002"
        ]
        user_searchable_dtos = FieldSearchableDTOFactory.create_batch(
            size=3, field_value=Searchable.USER.value,
            field_response=factory.Iterator(user_ids)
        )
        return user_searchable_dtos

    @pytest.fixture
    def searchable_dtos(self, reset_sequence):
        field_response = [
            "123e4567-e89b-12d3-a456-426614174000",
            1, 2, 3
        ]
        field_value = [
            Searchable.USER.value,
            Searchable.CITY.value,
            Searchable.STATE.value,
            Searchable.COUNTRY.value
        ]
        searchable_dtos = FieldSearchableDTOFactory.create_batch(
            size=4,
            field_value=factory.Iterator(field_value),
            field_response=factory.Iterator(field_response)
        )
        return searchable_dtos

    @patch.object(SearchableDetailsService, "get_searchable_details_dtos")
    def test_given_field_city_searchable_dtos_returns_field_searchable_dtos_with_updated_field_response(
            self, searchable_details_dtos_mock, searchable_dtos_with_city_type
    ):
        # Arrange
        city_ids = [1, 2, 5]
        values = ["Hyderabad", "Delhi", "Mumbai"]
        searchable_details_dtos = SearchableDetailsDTOFactory.create_batch(
            size=3,
            search_type=Searchable.CITY.value,
            id=factory.Iterator(city_ids),
            value=factory.Iterator(values)
        )
        field_response = [
            json.dumps({"id": city_ids[0], "value": values[0]}),
            json.dumps({"id": city_ids[1], "value": values[1]}),
            json.dumps({"id": city_ids[2], "value": values[2]})
        ]
        FieldSearchableDTOFactory.reset_sequence()
        expected_field_searchable_details_dtos = \
            FieldSearchableDTOFactory.create_batch(
                size=3, field_value=Searchable.CITY.value,
                field_response=factory.Iterator(field_response)
            )
        searchable_details_dtos_mock.return_value = searchable_details_dtos
        interactor = GetSearchableFieldDetails()

        # Act
        actual_field_searchable_details_dtos = \
            interactor.get_searchable_fields_details(
                searchable_dtos_with_city_type)

        # Assert
        assert actual_field_searchable_details_dtos == \
               expected_field_searchable_details_dtos

    @patch.object(SearchableDetailsService, "get_searchable_details_dtos")
    def test_given_field_state_searchable_dtos_returns_field_searchable_dtos_with_updated_field_response(
            self, searchable_details_dtos_mock, searchable_dtos_with_state_type
    ):
        # Arrange
        state_ids = [1, 2, 5]
        values = ["Andhra Pradesh", "Karnataka", "TamilNadu"]
        searchable_details_dtos = SearchableDetailsDTOFactory.create_batch(
            size=3,
            search_type=Searchable.STATE.value,
            id=factory.Iterator(state_ids),
            value=factory.Iterator(values)
        )
        field_response = [
            json.dumps({"id": state_ids[0], "value": values[0]}),
            json.dumps({"id": state_ids[1], "value": values[1]}),
            json.dumps({"id": state_ids[2], "value": values[2]})
        ]
        FieldSearchableDTOFactory.reset_sequence()
        expected_field_searchable_details_dtos = \
            FieldSearchableDTOFactory.create_batch(
                size=3, field_value=Searchable.STATE.value,
                field_response=factory.Iterator(field_response)
            )
        searchable_details_dtos_mock.return_value = searchable_details_dtos
        interactor = GetSearchableFieldDetails()

        # Act
        actual_field_searchable_details_dtos = \
            interactor.get_searchable_fields_details(
                searchable_dtos_with_state_type)

        # Assert
        assert actual_field_searchable_details_dtos == \
               expected_field_searchable_details_dtos

    @patch.object(SearchableDetailsService, "get_searchable_details_dtos")
    def test_given_field_country_searchable_dtos_returns_field_searchable_dtos_with_updated_field_response(
            self, searchable_details_dtos_mock,
            searchable_dtos_with_country_type
    ):
        # Arrange
        country_ids = [1, 2, 5]
        values = ["India", "America", "Spain"]
        searchable_details_dtos = SearchableDetailsDTOFactory.create_batch(
            size=3,
            search_type=Searchable.COUNTRY.value,
            id=factory.Iterator(country_ids),
            value=factory.Iterator(values)
        )
        field_response = [
            json.dumps({"id": country_ids[0], "value": values[0]}),
            json.dumps({"id": country_ids[1], "value": values[1]}),
            json.dumps({"id": country_ids[2], "value": values[2]})
        ]
        FieldSearchableDTOFactory.reset_sequence()
        expected_field_searchable_details_dtos = \
            FieldSearchableDTOFactory.create_batch(
                size=3, field_value=Searchable.COUNTRY.value,
                field_response=factory.Iterator(field_response)
            )
        searchable_details_dtos_mock.return_value = searchable_details_dtos
        interactor = GetSearchableFieldDetails()

        # Act
        actual_field_searchable_details_dtos = \
            interactor.get_searchable_fields_details(
                searchable_dtos_with_country_type)

        # Assert
        assert actual_field_searchable_details_dtos == \
               expected_field_searchable_details_dtos

    @patch.object(SearchableDetailsService, "get_searchable_details_dtos")
    def test_given_field_user_searchable_dtos_returns_field_searchable_dtos_with_updated_field_response(
            self, searchable_details_dtos_mock,
            searchable_dtos_with_user_type
    ):
        # Arrange
        user_ids = [
            "123e4567-e89b-12d3-a456-426614174000",
            "123e4567-e89b-12d3-a456-426614174001",
            "123e4567-e89b-12d3-a456-426614174002"
        ]
        values = [
            json.dumps({"name": "user1", "profile_pic_url": None}),
            json.dumps(
                {"name": "user2", "profile_pic_url": "https:ibhubs.co/image"}),
            json.dumps({"name": "user3", "profile_pic_url": None}),
        ]
        searchable_details_dtos = SearchableDetailsDTOFactory.create_batch(
            size=3,
            search_type=Searchable.USER.value,
            id=factory.Iterator(user_ids),
            value=factory.Iterator(values)
        )
        field_response = [
            json.dumps({"id": user_ids[0], "value": values[0]}),
            json.dumps({"id": user_ids[1], "value": values[1]}),
            json.dumps({"id": user_ids[2], "value": values[2]})
        ]
        FieldSearchableDTOFactory.reset_sequence()
        expected_field_searchable_details_dtos = \
            FieldSearchableDTOFactory.create_batch(
                size=3, field_value=Searchable.USER.value,
                field_response=factory.Iterator(field_response)
            )
        searchable_details_dtos_mock.return_value = searchable_details_dtos
        interactor = GetSearchableFieldDetails()

        # Act
        actual_field_searchable_details_dtos = \
            interactor.get_searchable_fields_details(
                searchable_dtos_with_user_type)

        # Assert
        assert actual_field_searchable_details_dtos == \
               expected_field_searchable_details_dtos

    @patch.object(SearchableDetailsService, "get_searchable_details_dtos")
    def test_given_field_user_searchable_dtos_returns_field_searchable_dtos_with_updated_field_response(
            self, searchable_details_dtos_mock,
            searchable_dtos
    ):
        # Arrange
        ids = [
            "123e4567-e89b-12d3-a456-426614174000",
            1, 2, 3
        ]
        values = [
            json.dumps({"name": "user1", "profile_pic_url": None}),
            "Hyderabad", "Telangana", "India"
        ]
        search_type = [
            Searchable.USER.value, Searchable.CITY.value,
            Searchable.STATE.value, Searchable.COUNTRY.value
        ]
        searchable_details_dtos = SearchableDetailsDTOFactory.create_batch(
            size=4,
            search_type=factory.Iterator(search_type),
            id=factory.Iterator(ids),
            value=factory.Iterator(values)
        )
        field_response = [
            json.dumps({"id": ids[0], "value": values[0]}),
            json.dumps({"id": ids[1], "value": values[1]}),
            json.dumps({"id": ids[2], "value": values[2]}),
            json.dumps({"id": ids[3], "value": values[3]})
        ]
        FieldSearchableDTOFactory.reset_sequence()
        expected_field_searchable_details_dtos = \
            FieldSearchableDTOFactory.create_batch(
                size=4, field_value=factory.Iterator(search_type),
                field_response=factory.Iterator(field_response)
            )
        searchable_details_dtos_mock.return_value = searchable_details_dtos
        interactor = GetSearchableFieldDetails()

        # Act
        actual_field_searchable_details_dtos = \
            interactor.get_searchable_fields_details(
                searchable_dtos)

        # Assert
        assert actual_field_searchable_details_dtos == \
               expected_field_searchable_details_dtos

    @patch.object(SearchableDetailsService, "get_searchable_details_dtos")
    def test_given_invalid_city_ids_in_field_response_raise_exception(
            self, exception_mock,
            searchable_dtos
    ):
        # Arrange
        from ib_tasks.adapters.searchable_details_service import \
            InvalidCityIdsException
        city_ids = [1]
        exception_object = InvalidCityIdsException(city_ids)
        exception_mock.side_effect = exception_object
        interactor = GetSearchableFieldDetails()

        # Act
        with pytest.raises(InvalidCityIdsException) as err:
            interactor.get_searchable_fields_details(searchable_dtos)

        # Assert

        assert city_ids == err.value.city_ids

    @patch.object(SearchableDetailsService, "get_searchable_details_dtos")
    def test_given_invalid_state_ids_in_field_response_raise_exception(
            self, exception_mock,
            searchable_dtos
    ):
        # Arrange
        from ib_tasks.adapters.searchable_details_service import \
            InvalidStateIdsException
        state_ids = [2]
        exception_object = InvalidStateIdsException(state_ids)
        exception_mock.side_effect = exception_object
        interactor = GetSearchableFieldDetails()

        # Act
        with pytest.raises(InvalidStateIdsException) as err:
            interactor.get_searchable_fields_details(searchable_dtos)

        # Assert

        assert state_ids == err.value.state_ids

    @patch.object(SearchableDetailsService, "get_searchable_details_dtos")
    def test_given_invalid_country_ids_in_field_response_raise_exception(
            self, exception_mock,
            searchable_dtos
    ):
        # Arrange
        from ib_tasks.adapters.searchable_details_service import \
            InvalidCountryIdsException
        country_ids = [2]
        exception_object = InvalidCountryIdsException(country_ids)
        exception_mock.side_effect = exception_object
        interactor = GetSearchableFieldDetails()

        # Act
        with pytest.raises(InvalidCountryIdsException) as err:
            interactor.get_searchable_fields_details(searchable_dtos)

        # Assert

        assert country_ids == err.value.country_ids

    @patch.object(SearchableDetailsService, "get_searchable_details_dtos")
    def test_given_invalid_user_ids_in_field_response_raise_exception(
            self, exception_mock,
            searchable_dtos
    ):
        # Arrange
        from ib_tasks.adapters.searchable_details_service import \
            InvalidUserIdsException
        user_ids = ["123e4567-e89b-12d3-a456-426614174000"]
        exception_object = InvalidUserIdsException(user_ids)
        exception_mock.side_effect = exception_object
        interactor = GetSearchableFieldDetails()

        # Act
        with pytest.raises(InvalidUserIdsException) as err:
            interactor.get_searchable_fields_details(searchable_dtos)

        # Assert

        assert user_ids == err.value.user_ids
