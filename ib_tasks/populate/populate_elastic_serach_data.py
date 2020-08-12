from ib_tasks.documents.elastic_task import ElasticUserDTO, ElasticCountryDTO, ElasticStateDTO, ElasticCityDTO
from ib_tasks.storages.elasticsearch_storage_implementation import ElasticSearchStorageImplementation


def populate_data():
    from elasticsearch_dsl import connections
    from django.conf import settings
    connections.create_connection(hosts=[settings.ELASTICSEARCH_ENDPOINT],
                                  timeout=20)
    push_user_details_to_elasticsearch()
    populate_elastic_search_user_data()
    populate_elastic_search_country_data()
    populate_elastic_search_state_data()
    populate_elastic_search_city_data()


def populate_elastic_search_user_data():
    user_dtos = [
        ElasticUserDTO(
            user_id="1",
            username="Ravi teja",
            elastic_user_id=None
        ),
        ElasticUserDTO(
            user_id="2",
            username="Pavankumar",
            elastic_user_id=None
        ),
        ElasticUserDTO(
            user_id="3",
            username="Vedavidh Budimuri",
            elastic_user_id=None
        ),
        ElasticUserDTO(
            user_id="4",
            username="Harshini Ravula",
            elastic_user_id=None
        ),
        ElasticUserDTO(
            user_id="5",
            username="Geetha Kogara",
            elastic_user_id=None
        ),
        ElasticUserDTO(
            user_id="6",
            username="Santhosh",
            elastic_user_id=None
        )
    ]

    storage = ElasticSearchStorageImplementation()
    for user_dto in user_dtos:
        storage.create_elastic_user(user_dto=user_dto)


def push_user_details_to_elasticsearch():
    from ib_iam.models import UserDetails
    user_objects = UserDetails.objects.all()

    for user_object in user_objects:
        from ib_tasks.documents.elastic_task import User
        user = User(user_id=user_object.user_id, name=user_object.name)
        user.save()


def populate_elastic_search_country_data():
    country_dtos = [
        ElasticCountryDTO(
            country_id=1,
            country_name="India",
            elastic_country_id=None
        ),
        ElasticCountryDTO(
            country_id=2,
            country_name="America",
            elastic_country_id=None
        ),
        ElasticCountryDTO(
            country_id=3,
            country_name="Australia",
            elastic_country_id=None
        ),
        ElasticCountryDTO(
            country_id=4,
            country_name="Singapore",
            elastic_country_id=None
        ),
        ElasticCountryDTO(
            country_id=5,
            country_name="Bangladesh",
            elastic_country_id=None
        ),
        ElasticCountryDTO(
            country_id=1,
            country_name="Pakistan",
            elastic_country_id=None
        )
    ]
    storage = ElasticSearchStorageImplementation()
    for country_dto in country_dtos:
        storage.create_elastic_country(country_dto=country_dto)


def populate_elastic_search_state_data():
    state_dtos = [
        ElasticStateDTO(
            state_id=1,
            state_name="Andhra Pradhesh",
            elastic_state_name=None
        ),
        ElasticStateDTO(
            state_id=2,
            state_name="Uttar Pradhesh",
            elastic_state_name=None
        ),
        ElasticStateDTO(
            state_id=1,
            state_name="Telangana",
            elastic_state_name=None
        ),
        ElasticStateDTO(
            state_id=1,
            state_name="Tamilnadu",
            elastic_state_name=None
        ),
        ElasticStateDTO(
            state_id=1,
            state_name="Karnataka",
            elastic_state_name=None
        ),
        ElasticStateDTO(
            state_id=1,
            state_name="Kerala",
            elastic_state_name=None
        ),
        ElasticStateDTO(
            state_id=1,
            state_name="Orissa",
            elastic_state_name=None
        )
    ]
    storage = ElasticSearchStorageImplementation()
    for state_dto in state_dtos:
        storage.create_elastic_state(state_dto=state_dto)


def populate_elastic_search_city_data():
    state_dtos = [
        ElasticCityDTO(
            city_id=1,
            city_name="Hyderabad",
            elastic_city_name=None
        ),
        ElasticCityDTO(
            city_id=2,
            city_name="Vijayawada",
            elastic_city_name=None
        ),
        ElasticCityDTO(
            city_id=3,
            city_name="Mumbai",
            elastic_city_name=None
        ),
        ElasticCityDTO(
            city_id=4,
            city_name="Chennai",
            elastic_city_name=None
        ),
        ElasticCityDTO(
            city_id=5,
            city_name="Punjab",
            elastic_city_name=None
        ),
        ElasticCityDTO(
            city_id=6,
            city_name="Visakapatnam",
            elastic_city_name=None
        )
    ]
    storage = ElasticSearchStorageImplementation()
    for state_dto in state_dtos:
        storage.create_elastic_city(city_dto=state_dto)

