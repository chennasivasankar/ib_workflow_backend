# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestGetResponseForGetListOfTeams.test_given_valid_team_with_members_details_dto_returns_http_response response'] = {
    'companies': [
        {
            'company_id': 'f2c02d98-f311-4ab2-8673-3daa00757003',
            'description': 'comapny_description1',
            'logo_url': 'logo_url1',
            'name': 'company1',
            'no_of_employees': 3
        },
        {
            'company_id': 'aa66c40f-6d93-484a-b418-984716514c7c',
            'description': 'comapny_description2',
            'logo_url': 'logo_url2',
            'name': 'company1',
            'no_of_employees': 5
        }
    ]
}
