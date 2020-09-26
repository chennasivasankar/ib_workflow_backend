import json

import pytest


class TestAddOrEditGroupByPresenterImplementation:

    @pytest.fixture
    def presenter(self):
        from ib_adhoc_tasks.presenters.add_or_edit_group_by_presenter_implementation import \
            AddOrEditGroupByPresenterImplementation
        return AddOrEditGroupByPresenterImplementation()

    # def test_get_response_for_add_or_edit_group_by_gives_response_dict(
    #         self, presenter
    # ):
    #     # Arrange
    #     from ib_adhoc_tasks.tests.factories.storage_dtos import \
    #         GroupByResponseDTOFactory
    #     GroupByResponseDTOFactory.reset_sequence(0)
    #     GroupByResponseDTOFactory.display_name.reset()
    #     GroupByResponseDTOFactory.group_by_key.reset()
    #     group_by_response_dto = GroupByResponseDTOFactory()
    #     expected_response_dict = {
    #         'display_name': 'ASSIGNEE',
    #         'group_by_key': 'ASSIGNEE',
    #         'group_by_id': 0,
    #         'order': 1
    #     }
    #
    #     # Act
    #     http_response = presenter.get_response_for_add_or_edit_group_by(
    #         group_by_response_dto=group_by_response_dto
    #     )
    #
    #     # Assert
    #     actual_response_dict = json.loads(http_response.content)
    #     assert actual_response_dict == expected_response_dict

    def test_whether_it_returns_user_not_allowed_to_create_more_than_one_group_by_in_list_view_http_response(
            self, presenter
    ):
        # Arrange
        from ib_adhoc_tasks.constants.exception_messages import \
            USER_NOT_ALLOWED_TO_CREATE_MORE_THAN_ONE_GROUP_BY_IN_LIST_VIEW
        expected_response = \
            USER_NOT_ALLOWED_TO_CREATE_MORE_THAN_ONE_GROUP_BY_IN_LIST_VIEW[0]
        expected_res_status = \
            USER_NOT_ALLOWED_TO_CREATE_MORE_THAN_ONE_GROUP_BY_IN_LIST_VIEW[1]
        from ib_iam.constants.enums import StatusCode
        expected_http_status_code = StatusCode.BAD_REQUEST.value

        # Act
        result = presenter.get_response_for_user_not_allowed_to_create_more_than_one_group_by_in_list_view()

        # Assert
        response_dict = json.loads(result.content)
        actual_response = response_dict["response"]
        actual_res_status = response_dict["res_status"]
        actual_http_status_code = response_dict["http_status_code"]
        assert actual_response == expected_response
        assert actual_res_status == expected_res_status
        assert expected_http_status_code == actual_http_status_code

    def test_whether_it_returns_user_not_allowed_to_create_more_than_two_group_by_in_kanban_view_http_response(
            self, presenter
    ):
        # Arrange
        from ib_adhoc_tasks.constants.exception_messages import \
            USER_NOT_ALLOWED_TO_CREATE_MORE_THAN_TWO_GROUP_BY_IN_KANBAN_VIEW
        expected_response = \
            USER_NOT_ALLOWED_TO_CREATE_MORE_THAN_TWO_GROUP_BY_IN_KANBAN_VIEW[0]
        expected_res_status = \
            USER_NOT_ALLOWED_TO_CREATE_MORE_THAN_TWO_GROUP_BY_IN_KANBAN_VIEW[1]
        from ib_iam.constants.enums import StatusCode
        expected_http_status_code = StatusCode.BAD_REQUEST.value

        # Act
        result = presenter.get_response_for_user_not_allowed_to_create_more_than_two_group_by_in_kanban_view()

        # Assert
        response_dict = json.loads(result.content)
        actual_response = response_dict["response"]
        actual_res_status = response_dict["res_status"]
        actual_http_status_code = response_dict["http_status_code"]
        assert actual_response == expected_response
        assert actual_res_status == expected_res_status
        assert expected_http_status_code == actual_http_status_code
