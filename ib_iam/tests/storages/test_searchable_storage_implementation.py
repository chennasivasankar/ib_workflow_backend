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

    def test_given_user_ids_returns_valid_user_ids(self, storage, snapshot):
        # Arrange
        user_objs = UserDetailsFactory.create_batch(size=10)
        user_ids = [
            user_objs[0], user_objs[1],
            user_objs[2], "user100", "user200",
            "user400", "user500"
        ]

        # Act
        valid_user_ids = storage.get_valid_user_ids(ids=user_ids)

        # Assert
        snapshot.assert_match(name=valid_user_ids, value=valid_user_ids)
