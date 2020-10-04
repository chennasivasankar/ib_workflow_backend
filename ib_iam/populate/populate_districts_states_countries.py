"""
Created on: 04/10/20
Author: Pavankumar Pamuru

"""


def populate_data(spread_sheet_name: str, sub_sheet_name: str):
    populate_elastic_search_state_data(
        spread_sheet_name=spread_sheet_name,
        sub_sheet_name=sub_sheet_name
    )
    populate_elastic_search_district_data(
        spread_sheet_name=spread_sheet_name,
        sub_sheet_name=sub_sheet_name
    )
    from ib_iam.populate.populate_elastic_search_data import \
        copy_districts_to_es, copy_states_to_es
    copy_districts_to_es()
    copy_states_to_es()


def get_spread_sheet_data(spread_sheet_name: str, sub_sheet_name: str):
    from ib_iam.populate.spreedsheet_utils import SpreadSheetUtil
    spreadsheet_utils = SpreadSheetUtil()
    sheet_dict_objects = spreadsheet_utils \
        .read_spread_sheet_data_and_get_row_wise_dicts(
            spread_sheet_name=spread_sheet_name,
            sub_sheet_name=sub_sheet_name
        )
    return sheet_dict_objects


def populate_elastic_search_country_data(spread_sheet_name: str, sub_sheet_name: str):

    countries = get_spread_sheet_data(
        spread_sheet_name=spread_sheet_name,
        sub_sheet_name=sub_sheet_name
    )
    country_names = [
        country['countries']
        for country in countries
    ]
    from ib_iam.models import Country
    Country.objects.all().delete()
    country_objects = [
        Country(name=country_name)
        for country_name in country_names
    ]
    Country.objects.bulk_create(country_objects)


def populate_elastic_search_state_data(spread_sheet_name: str, sub_sheet_name: str):
    states = get_spread_sheet_data(
        spread_sheet_name=spread_sheet_name,
        sub_sheet_name=sub_sheet_name
    )
    state_names = [
        state['states']
        for state in states
    ]
    from ib_iam.models import State
    State.objects.all().delete()
    state_objects = [
        State(name=state_name)
        for state_name in state_names
    ]
    State.objects.bulk_create(state_objects)


def populate_elastic_search_city_data(spread_sheet_name: str, sub_sheet_name: str):
    cities = get_spread_sheet_data(
        spread_sheet_name=spread_sheet_name,
        sub_sheet_name=sub_sheet_name
    )
    city_names = [
        city['cities']
        for city in cities
    ]
    from ib_iam.models import City
    City.objects.all().delete()
    countries = [
        City(name=city_name)
        for city_name in city_names
    ]
    City.objects.bulk_create(countries)


def populate_elastic_search_district_data(spread_sheet_name: str, sub_sheet_name: str):
    districts = get_spread_sheet_data(
        spread_sheet_name=spread_sheet_name,
        sub_sheet_name=sub_sheet_name
    )
    district_names = [
        district['districts']
        for district in districts
    ]
    from ib_iam.models import District
    District.objects.all().delete()
    countries = [
        District(name=district_name)
        for district_name in district_names
    ]
    District.objects.bulk_create(countries)
