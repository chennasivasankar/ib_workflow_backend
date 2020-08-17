# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot, GenericRepr


snapshots = Snapshot()

snapshots['TestSearchableStorageImplementation.test_given_city_ids_returns_searchable_type_city_details_dtos searchable_type_city_details_dtos'] = [
    GenericRepr("SearchableDetailsDTO(search_type='CITY', id=1, value='city_name0')"),
    GenericRepr("SearchableDetailsDTO(search_type='CITY', id=2, value='city_name1')"),
    GenericRepr("SearchableDetailsDTO(search_type='CITY', id=3, value='city_name2')"),
    GenericRepr("SearchableDetailsDTO(search_type='CITY', id=4, value='city_name3')")
]

snapshots['TestSearchableStorageImplementation.test_given_state_ids_returns_searchable_type_state_details_dtos searchable_type_state_details_dtos'] = [
    GenericRepr("SearchableDetailsDTO(search_type='STATE', id=1, value='state_name0')"),
    GenericRepr("SearchableDetailsDTO(search_type='STATE', id=3, value='state_name2')"),
    GenericRepr("SearchableDetailsDTO(search_type='STATE', id=5, value='state_name4')"),
    GenericRepr("SearchableDetailsDTO(search_type='STATE', id=6, value='state_name5')"),
    GenericRepr("SearchableDetailsDTO(search_type='STATE', id=7, value='state_name6')")
]

snapshots['TestSearchableStorageImplementation.test_given_country_ids_returns_searchable_type_country_details_dtos searchable_type_country_details_dtos'] = [
    GenericRepr("SearchableDetailsDTO(search_type='COUNTRY', id=4, value='country_name3')"),
    GenericRepr("SearchableDetailsDTO(search_type='COUNTRY', id=5, value='country_name4')"),
    GenericRepr("SearchableDetailsDTO(search_type='COUNTRY', id=13, value='country_name12')"),
    GenericRepr("SearchableDetailsDTO(search_type='COUNTRY', id=16, value='country_name15')"),
    GenericRepr("SearchableDetailsDTO(search_type='COUNTRY', id=18, value='country_name17')")
]

snapshots['TestSearchableStorageImplementation.test_given_user_ids_returns_get_searchable_type_user_details_dtos searchable_type_user_details_dtos'] = [
    GenericRepr("SearchableDetailsDTO(search_type='USER', id='123e4567-e89b-12d3-a456-426614174000', value='name1')"),
    GenericRepr("SearchableDetailsDTO(search_type='USER', id='123e4567-e89b-12d3-a456-426614174001', value='name2')"),
    GenericRepr("SearchableDetailsDTO(search_type='USER', id='123e4567-e89b-12d3-a456-426614174002', value='name3')"),
    GenericRepr("SearchableDetailsDTO(search_type='USER', id='123e4567-e89b-12d3-a456-426614174003', value='name4')")
]
