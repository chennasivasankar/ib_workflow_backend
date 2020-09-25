import json

import pytest


class TestGetAdhocTaskTemplateFieldsAndGroupByPresenterImplementation:

    @pytest.fixture
    def presenter(self):
        from ib_adhoc_tasks.presenters \
            .get_adhoc_task_template_fields_and_group_by_presenter_implementation \
            import GetAdhocTaskTemplateFieldsAndGroupByPresenterImplementation
        return GetAdhocTaskTemplateFieldsAndGroupByPresenterImplementation()

    @pytest.fixture
    def group_by_fields_dtos(self):
        from ib_adhoc_tasks.tests.factories.storage_dtos import \
            GroupByResponseDTOFactory
        GroupByResponseDTOFactory.reset_sequence(0)
        GroupByResponseDTOFactory.order.reset()
        GroupByResponseDTOFactory.group_by_key.reset()
        GroupByResponseDTOFactory.display_name.reset()
        return GroupByResponseDTOFactory.create_batch(size=2)

    def test_given_valid_data_returns_success_response(
            self, presenter, snapshot, group_by_fields_dtos
    ):
        # Arrange
        from ib_adhoc_tasks.tests.factories.adapter_dtos import \
            FieldIdAndNameDTOFactory
        FieldIdAndNameDTOFactory.reset_sequence(0)
        field_dtos = FieldIdAndNameDTOFactory.create_batch(size=2)
        from ib_adhoc_tasks.interactors.dtos.dtos import \
            TemplateFieldsAndGroupByFieldsDTO
        template_fields_and_group_by_fields_dto = \
            TemplateFieldsAndGroupByFieldsDTO(
                group_by_fields_dtos=group_by_fields_dtos,
                field_dtos=field_dtos
            )

        # Act
        http_response = presenter.get_response_for_get_template_and_group_by_fields(
            template_fields_and_group_by_fields_dto=
            template_fields_and_group_by_fields_dto
        )

        # Assert
        response = json.loads(http_response.content)
        snapshot.assert_match(response, "response_dict")

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
