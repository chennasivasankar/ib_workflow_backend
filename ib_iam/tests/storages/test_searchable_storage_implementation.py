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
        CountryFactory.reset_sequence()

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

    def test_given_user_ids_returns_valid_user_ids(self, storage, snapshot):
        # Arrange
        UserDetailsFactory.reset_sequence(0)
        user_objs = UserDetailsFactory.create_batch(size=10)
        valid_user_ids = [
            user_obj.user_id
            for user_obj in user_objs
        ]
        invalid_user_ids = ["user100", "user200", "user400", "user500"]
        user_ids = valid_user_ids + invalid_user_ids

        # Act
        valid_user_ids = storage.get_valid_user_ids(ids=user_ids)

        # Assert
        snapshot.assert_match(name="valid_user_ids", value=valid_user_ids)

    def test_given_city_ids_returns_valid_city_ids(self, storage, snapshot):
        # Arrange
        city_objs = CityFactory.create_batch(size=5)
        valid_city_ids = [
            city_obj.id
            for city_obj in city_objs
        ]
        invalid_city_ids = [1000, 2000, 4000]
        city_ids = valid_city_ids + invalid_city_ids

        # Act
        actual_valid_city_ids = storage.get_valid_city_ids(city_ids=city_ids)

        # Assert
        snapshot.assert_match(
            name="valid_city_ids",
            value=actual_valid_city_ids
        )

    def test_given_state_id_returns_valid_state_ids(self, storage, snapshot):
        # Arrange
        state_objs = StateFactory.create_batch(size=6)
        valid_state_ids = [
            state_obj.id
            for state_obj in state_objs
        ]
        invalid_state_ids = [3000, 4567, 8902]
        state_ids = valid_state_ids + invalid_state_ids

        # Act
        actual_valid_state_ids = storage.get_valid_state_ids(state_ids)

        # Assert
        snapshot.assert_match(
            name="valid_state_ids",
            value=actual_valid_state_ids
        )

    def test_given_country_ids_return_valid_country_ids(
            self, storage, snapshot
    ):
        # Arrange
        country_objs = CountryFactory.create_batch(size=7)
        valid_country_ids = [
            country_obj.id
            for country_obj in country_objs
        ]
        invalid_country_ids = [-2, -6, 4567]
        country_ids = valid_country_ids + invalid_country_ids

        # Act
        actual_valid_country_ids = storage.get_valid_country_ids(country_ids)

        # Assert
        snapshot.assert_match(
            name="valid_country_ids",
            value=actual_valid_country_ids
        )
