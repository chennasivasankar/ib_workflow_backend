from dataclasses import dataclass
from typing import Optional

from django.conf import settings
from elasticsearch_dsl import Document, Text, Integer, SearchAsYouType

USER_INDEX_NAME = 'user-{}'.format(settings.STAGE)
COUNTRY_INDEX_NAME = 'country-{}'.format(settings.STAGE)
STATE_INDEX_NAME = 'state-{}'.format(settings.STAGE)
CITY_INDEX_NAME = 'city-{}'.format(settings.STAGE)


@dataclass()
class ElasticUserDTO:
    user_id: str
    name: Optional[str]
    elastic_user_id: Optional[str]
    email: str = None


class ElasticUser(Document):
    user_id = Text()
    name = SearchAsYouType()
    email = Text()

    class Index:
        name = USER_INDEX_NAME


@dataclass()
class ElasticCountryDTO:
    country_id: int
    country_name: Optional[str]


class Country(Document):
    country_id = Integer()
    country_name = SearchAsYouType()

    class Index:
        name = COUNTRY_INDEX_NAME


@dataclass()
class ElasticStateDTO:
    state_id: int
    state_name: Optional[str]


class State(Document):
    state_id = Integer()
    state_name = SearchAsYouType()

    class Index:
        name = STATE_INDEX_NAME


@dataclass()
class ElasticCityDTO:
    city_id: int
    city_name: Optional[str]


class City(Document):
    city_id = Integer()
    city_name = SearchAsYouType()

    class Index:
        name = CITY_INDEX_NAME
