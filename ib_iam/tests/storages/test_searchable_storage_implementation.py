import factory
import pytest

from ib_iam.tests.factories.models import CityFactory, StateFactory, \
    CountryFactory, UserDetailsFactory


@pytest.mark.django_db
class TestSearchableStorageImplementation:

    @pytest.fixture
    def storage(self):
        from ib_iam.storages.searchable_storage_implementtion import \
            SearchableStorageImplementation
        storage = SearchableStorageImplementation()
        return storage

    @pytest.fixture
    def reset_sequence(self):
        CityFactory.reset_sequence()
        StateFactory.reset_sequence()

    def test_given_city_ids_returns_searchable_type_city_details_dtos(
            self, storage, snapshot
    ):
        # Arrange
        CityFactory.create_batch(size=5)
        ids = [1, 2, 3, 4]

        # Act
        searchable_type_city_details_dtos = \
            storage.get_searchable_type_city_details_dtos(ids)

        # Assert
        snapshot.assert_match(
            name="searchable_type_city_details_dtos",
            value=searchable_type_city_details_dtos
        )

    def test_given_state_ids_returns_searchable_type_state_details_dtos(
            self, storage, snapshot
    ):
        # Arrange
        StateFactory.create_batch(size=10)
        ids = [3, 5, 6, 1, 7]

        # Act
        searchable_type_state_details_dtos = \
            storage.get_searchable_type_state_details_dtos(ids)

        # Assert
        snapshot.assert_match(
            name="searchable_type_state_details_dtos",
            value=searchable_type_state_details_dtos
        )

    def test_given_country_ids_returns_searchable_type_country_details_dtos(
            self, storage, snapshot
    ):
        # Arrange
        CountryFactory.create_batch(size=20)
        ids = [13, 4, 18, 5, 16]

        # Act
        searchable_type_country_details_dtos = \
            storage.get_searchable_type_country_details_dtos(ids)

        # Assert
        snapshot.assert_match(
            name="searchable_type_country_details_dtos",
            value=searchable_type_country_details_dtos
        )

    def test_given_user_ids_returns_get_searchable_type_user_details_dtos(
            self, storage, snapshot
    ):
        # Arrange
        user_ids = [
            "123e4567-e89b-12d3-a456-426614174000",
            "123e4567-e89b-12d3-a456-426614174001",
            "123e4567-e89b-12d3-a456-426614174002",
            "123e4567-e89b-12d3-a456-426614174003"
        ]
        names = ["name1", "name2", "name3", "name4"]
        UserDetailsFactory.create_batch(
            size=4,
            user_id=factory.Iterator(user_ids),
            name=factory.Iterator(names)
        )

        # Act
        searchable_type_user_details_dtos = \
            storage.get_searchable_type_user_details_dtos(ids=user_ids)

        # Assert
        snapshot.assert_match(
            name="searchable_type_user_details_dtos",
            value=searchable_type_user_details_dtos
        )
