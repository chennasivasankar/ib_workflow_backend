"""
All exceptions
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase02GetProjectDiscussionsAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read']}}

    def _get_or_create_user(self):
        user_id = "e597ab2f-a10c-4164-930e-23af375741cb"
        from ib_users.models import UserAccount
        user = UserAccount.objects.create(user_id=user_id)
        return user

    @pytest.mark.django_db
    def test_invalid_offset_raise_exception(self, snapshot):
        from ib_discussions.constants.enum import EntityType
        from ib_discussions.constants.enum import SortByEnum
        from ib_discussions.constants.enum import FilterByEnum

        entity_id = '31be920b-7b4c-49e7-8adb-41a0c18da848'
        entity_type = EntityType.TASK.value
        offset = -1
        limit = 2
        filter_by = FilterByEnum.CLARIFIED.value
        sort_by = SortByEnum.LATEST.value

        body = {
            'entity_id': entity_id,
            'entity_type': entity_type,
            'filter_by': filter_by,
            'sort_by': sort_by,
            'project_id': 'FIN_MAN'
        }
        path_params = {}
        query_params = {'offset': offset, 'limit': limit}
        headers = {}
        self.make_api_call(body=body,
                           path_params=path_params,
                           query_params=query_params,
                           headers=headers,
                           snapshot=snapshot)

    @pytest.mark.django_db
    def test_invalid_project_id_return_response(self, snapshot, mocker):
        from ib_discussions.constants.enum import EntityType
        from ib_discussions.constants.enum import SortByEnum
        from ib_discussions.constants.enum import FilterByEnum
        from ib_discussions.adapters.iam_service import InvalidProjectId

        from ib_discussions.tests.common_fixtures.adapters import \
            validate_user_id_for_given_project
        validate_user_id_for_given_project(mocker, side_effect=InvalidProjectId)

        entity_id = '31be920b-7b4c-49e7-8adb-41a0c18da848'
        entity_type = EntityType.TASK.value
        offset = 1
        limit = 2
        filter_by = FilterByEnum.CLARIFIED.value
        sort_by = SortByEnum.LATEST.value

        body = {
            'entity_id': entity_id,
            'entity_type': entity_type,
            'filter_by': filter_by,
            'sort_by': sort_by,
            'project_id': 'FIN_MAN'
        }
        path_params = {}
        query_params = {'offset': offset, 'limit': limit}
        headers = {}
        self.make_api_call(body=body,
                           path_params=path_params,
                           query_params=query_params,
                           headers=headers,
                           snapshot=snapshot)

    @pytest.mark.django_db
    def test_invalid_user_for_project_return_response(self, snapshot, mocker):
        from ib_discussions.constants.enum import EntityType
        from ib_discussions.constants.enum import SortByEnum
        from ib_discussions.constants.enum import FilterByEnum
        from ib_discussions.adapters.iam_service import InvalidUserForProject

        from ib_discussions.tests.common_fixtures.adapters import \
            validate_user_id_for_given_project
        validate_user_id_for_given_project(
            mocker, side_effect=InvalidUserForProject)

        entity_id = '31be920b-7b4c-49e7-8adb-41a0c18da848'
        entity_type = EntityType.TASK.value
        offset = 1
        limit = 2
        filter_by = FilterByEnum.CLARIFIED.value
        sort_by = SortByEnum.LATEST.value

        body = {
            'entity_id': entity_id,
            'entity_type': entity_type,
            'filter_by': filter_by,
            'sort_by': sort_by,
            'project_id': 'FIN_MAN'
        }
        path_params = {}
        query_params = {'offset': offset, 'limit': limit}
        headers = {}
        self.make_api_call(body=body,
                           path_params=path_params,
                           query_params=query_params,
                           headers=headers,
                           snapshot=snapshot)

    @pytest.mark.django_db
    def test_invalid_limit_raise_exception(self, snapshot):
        from ib_discussions.constants.enum import EntityType
        from ib_discussions.constants.enum import SortByEnum
        from ib_discussions.constants.enum import FilterByEnum

        entity_id = '31be920b-7b4c-49e7-8adb-41a0c18da848'
        entity_type = EntityType.TASK.value
        offset = 1
        limit = -1
        filter_by = FilterByEnum.CLARIFIED.value
        sort_by = SortByEnum.LATEST.value
        body = {
            'entity_id': entity_id,
            'entity_type': entity_type,
            'filter_by': filter_by,
            'sort_by': sort_by,
            'project_id': 'FIN_MAN'
        }
        path_params = {}
        query_params = {'offset': offset, 'limit': limit}
        headers = {}
        self.make_api_call(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )

    @pytest.mark.django_db
    def test_user_profile_does_not_exist_raise_exception(
            self, snapshot, prepare_discussion_setup, mocker):
        from ib_discussions.constants.enum import EntityType
        from ib_discussions.constants.enum import SortByEnum
        from ib_discussions.constants.enum import FilterByEnum
        from ib_discussions.tests.common_fixtures.adapters import \
            validate_user_id_for_given_project

        validate_user_id_for_given_project(mocker)
        user_ids = ["user_id_1", "user_id_2"]
        from ib_discussions.tests.common_fixtures.adapters import \
            get_subordinate_user_ids_mock
        get_subordinate_user_ids_mock = get_subordinate_user_ids_mock(mocker)
        get_subordinate_user_ids_mock.return_value = user_ids

        from ib_discussions.tests.common_fixtures.adapters import \
            prepare_get_user_profile_dtos_mock
        get_user_profile_dtos_mock = prepare_get_user_profile_dtos_mock(mocker)
        from ib_discussions.exceptions.custom_exceptions import InvalidUserId
        get_user_profile_dtos_mock.side_effect = InvalidUserId

        entity_id = '31be920b-7b4c-49e7-8adb-41a0c18da848'
        entity_type = EntityType.TASK.value
        offset = 1
        limit = 2
        filter_by = FilterByEnum.CLARIFIED.value
        sort_by = SortByEnum.LATEST.value
        body = {
            'entity_id': entity_id,
            'entity_type': entity_type,
            'filter_by': filter_by,
            'sort_by': sort_by,
            'project_id': 'PROJECT_ID'
        }
        path_params = {}
        query_params = {'offset': offset, 'limit': limit}
        headers = {}
        self.make_api_call(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )
