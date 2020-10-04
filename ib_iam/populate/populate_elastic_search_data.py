from ib_iam.documents.elastic_docs import (
    ElasticCountryDTO, ElasticStateDTO, ElasticCityDTO,
    USER_INDEX_NAME, COUNTRY_INDEX_NAME, STATE_INDEX_NAME,
    CITY_INDEX_NAME, ElasticDistrictDTO
)
from ib_iam.models import (
    UserDetails, Country, State, City, ElasticUserIntermediary
)
from ib_iam.storages.elastic_storage_implementation \
    import ElasticStorageImplementation


def populate_data():
    populate_elastic_search_country_data()
    populate_elastic_search_state_data()
    populate_elastic_search_city_data()
    populate_elastic_search_district_data()


def populate_existing_users_to_elastic_search_database():
    storage = ElasticStorageImplementation()
    user_ids = list(
        UserDetails.objects.all().values_list('user_id', flat=True)
    )
    from ib_iam.adapters.user_service import UserService
    user_service = UserService()
    user_dtos = user_service.get_user_profile_bulk(
        user_ids=user_ids
    )
    ElasticUserIntermediary.objects.all().delete()
    for user_dto in user_dtos:
        elastic_id = storage.create_elastic_user(
            user_id=user_dto.user_id, name=user_dto.name,
            email=user_dto.email
        )
        storage.create_elastic_user_intermediary(
            elastic_user_id=elastic_id,
            user_id=user_dto.user_id
        )


def populate_elastic_search_country_data():
    country_dtos = [
        ElasticCountryDTO(
            country_id=1,
            country_name="India"
        ),
        ElasticCountryDTO(
            country_id=2,
            country_name="America"
        ),
        ElasticCountryDTO(
            country_id=3,
            country_name="Australia"
        ),
        ElasticCountryDTO(
            country_id=4,
            country_name="Singapore"
        ),
        ElasticCountryDTO(
            country_id=5,
            country_name="Bangladesh"
        ),
        ElasticCountryDTO(
            country_id=1,
            country_name="Pakistan"
        ),
        ElasticCountryDTO(
            country_id=1,
            country_name="United States of America"
        ),
        ElasticCountryDTO(
            country_id=1,
            country_name="Saint Vincent Grenadines Country"
        )
    ]
    Country.objects.all().delete()
    countries = [
        Country(name=country_dto.country_name)
        for country_dto in country_dtos
    ]
    Country.objects.bulk_create(countries)
    copy_countries_to_es()


def copy_countries_to_es():
    country_objs = Country.objects.all()

    country_dtos = [
        ElasticCountryDTO(
            country_id=country_obj.id,
            country_name=country_obj.name
        )
        for country_obj in country_objs
    ]
    storage = ElasticStorageImplementation()
    for country_dto in country_dtos:
        storage.create_elastic_country(country_dto=country_dto)


def populate_elastic_search_state_data():
    state_dtos = [
        ElasticStateDTO(
            state_id=1,
            state_name="Andhra Pradhesh"
        ),
        ElasticStateDTO(
            state_id=2,
            state_name="Uttar Pradhesh"
        ),
        ElasticStateDTO(
            state_id=1,
            state_name="Telangana"
        ),
        ElasticStateDTO(
            state_id=1,
            state_name="Tamilnadu"
        ),
        ElasticStateDTO(
            state_id=1,
            state_name="Karnataka"
        ),
        ElasticStateDTO(
            state_id=1,
            state_name="Kerala"
        ),
        ElasticStateDTO(
            state_id=1,
            state_name="Orissa"
        )
    ]
    State.objects.all().delete()
    countries = [
        State(name=country_dto.state_name)
        for country_dto in state_dtos
    ]
    State.objects.bulk_create(countries)
    copy_states_to_es()


def copy_states_to_es():
    country_objs = State.objects.all()
    state_dtos = [
        ElasticStateDTO(
            state_id=state_obj.id,
            state_name=state_obj.name
        )
        for state_obj in country_objs
    ]
    storage = ElasticStorageImplementation()
    for state_dto in state_dtos:
        storage.create_elastic_state(state_dto=state_dto)


def populate_elastic_search_city_data():
    city_dtos = [
        ElasticCityDTO(
            city_id=1,
            city_name="Hyderabad"
        ),
        ElasticCityDTO(
            city_id=2,
            city_name="Vijayawada"
        ),
        ElasticCityDTO(
            city_id=3,
            city_name="Mumbai"
        ),
        ElasticCityDTO(
            city_id=4,
            city_name="Chennai"
        ),
        ElasticCityDTO(
            city_id=5,
            city_name="Punjab"
        ),
        ElasticCityDTO(
            city_id=6,
            city_name="Visakapatnam"
        ),
        ElasticCityDTO(
            city_id=6,
            city_name="Sri Potti Sriramula Nellore"
        )
    ]
    City.objects.all().delete()
    countries = [
        City(name=country_dto.city_name)
        for country_dto in city_dtos
    ]
    City.objects.bulk_create(countries)
    copy_cities_to_es()


def copy_cities_to_es():
    city_objs = City.objects.all()
    city_dtos = [
        ElasticCityDTO(
            city_id=city_obj.id,
            city_name=city_obj.name
        )
        for city_obj in city_objs
    ]
    storage = ElasticStorageImplementation()
    for state_dto in city_dtos:
        storage.create_elastic_city(city_dto=state_dto)


def populate_elastic_search_district_data():
    district_dtos = [
        ElasticDistrictDTO(
            district_id=1,
            district_name="Sri Potti Sriramula Nellore"
        ),
        ElasticDistrictDTO(
            district_id=2,
            district_name="Kadapa"
        ),
        ElasticDistrictDTO(
            district_id=3,
            district_name="Chittor"
        ),
        ElasticDistrictDTO(
            district_id=4,
            district_name="Ananthapur"
        ),
        ElasticDistrictDTO(
            district_id=5,
            district_name="Kurnool"
        ),
        ElasticDistrictDTO(
            district_id=6,
            district_name="Visakapatnam"
        ),
        ElasticDistrictDTO(
            district_id=6,
            district_name="West Godavari"
        )
    ]
    from ib_iam.models import District
    District.objects.all().delete()
    countries = [
        District(name=country_dto.district_name)
        for country_dto in district_dtos
    ]
    District.objects.bulk_create(countries)
    copy_districts_to_es()


def copy_districts_to_es():
    from ib_iam.models import District
    district_objs = District.objects.all()
    district_dtos = [
        ElasticDistrictDTO(
            district_id=district_obj.id,
            district_name=district_obj.name
        )
        for district_obj in district_objs
    ]
    storage = ElasticStorageImplementation()
    for state_dto in district_dtos:
        storage.create_elastic_district(district_dto=state_dto)


def delete_elastic_search_data():
    from elasticsearch_dsl import connections
    from django.conf import settings
    connections.create_connection(
        hosts=[settings.ELASTICSEARCH_ENDPOINT], timeout=20
    )
    from elasticsearch import Elasticsearch
    es = Elasticsearch(hosts=[settings.ELASTICSEARCH_ENDPOINT])
    indices = [
        USER_INDEX_NAME,
        COUNTRY_INDEX_NAME,
        STATE_INDEX_NAME,
        CITY_INDEX_NAME
    ]
    es.delete_by_query(index=indices, body={"query": {"match_all": {}}})


def delete_elastic_search_data_for_user_index():
    from elasticsearch_dsl import connections
    from django.conf import settings
    connections.create_connection(
        hosts=[settings.ELASTICSEARCH_ENDPOINT], timeout=20
    )
    from elasticsearch import Elasticsearch
    es = Elasticsearch(hosts=[settings.ELASTICSEARCH_ENDPOINT])
    indices = [
        USER_INDEX_NAME
    ]
    es.delete_by_query(index=indices, body={"query": {"match_all": {}}})
