import json

from ib_iam.constants.enums import StatusCode
from ib_iam.presenters.add_roles_presenter_implementation import AddRolesPresenterImplementation


class TestAddListOfRolesPresenter:
    def test_raise_role_id_should_not_be_in_valid_format_exception(self):
        # Arrange
        presenter = AddRolesPresenterImplementation()

        from ib_iam.constants.exception_messages \
            import ROLE_ID_SHOULD_NOT_BE_IN_VALID_FORMAT
        expected_response = ROLE_ID_SHOULD_NOT_BE_IN_VALID_FORMAT[0]
        response_status_code = ROLE_ID_SHOULD_NOT_BE_IN_VALID_FORMAT[1]

        # Act
        response_object = presenter.response_for_role_id_format_is_invalid_exception()

        # Assert
        response = json.loads(response_object.content)
        assert response['http_status_code'] == StatusCode.BAD_REQUEST.value
        assert response['res_status'] == response_status_code
        assert response['response'] == expected_response

    def test_raise_role_id_duplicate_exception(self):
        # Arrange
        presenter = AddRolesPresenterImplementation()
        duplicate_role_ids = ["PAYMENT_POC"]
        from ib_iam.constants.exception_messages \
            import DUPLICATE_ROLE_IDS
        expected_response = DUPLICATE_ROLE_IDS[0].format(
            duplicate_role_ids=duplicate_role_ids
        )
        response_status_code = DUPLICATE_ROLE_IDS[1]
        from ib_iam.exceptions.custom_exceptions import DuplicateRoleIds
        duplicate_ids_err_object = DuplicateRoleIds(
            role_ids=duplicate_role_ids
        )

        # Act
        response_object = presenter.response_for_duplicate_role_ids_exception(
            err=duplicate_ids_err_object
        )

        # Assert
        response = json.loads(response_object.content)
        assert response['http_status_code'] == StatusCode.BAD_REQUEST.value
        assert response['res_status'] == response_status_code
        assert response['response'] == expected_response

    def test_raise_role_name_should_not_be_empty_exception(self):
        # Arrange
        presenter = AddRolesPresenterImplementation()
        from ib_iam.constants.exception_messages \
            import ROLE_NAME_SHOULD_NOT_BE_EMPTY
        expected_response = ROLE_NAME_SHOULD_NOT_BE_EMPTY[0]
        response_status_code = ROLE_NAME_SHOULD_NOT_BE_EMPTY[1]

        # Act
        response_object = presenter. \
            response_for_role_name_should_not_be_empty_exception()

        # Assert
        response = json.loads(response_object.content)
        assert response['http_status_code'] == StatusCode.BAD_REQUEST.value
        assert response['res_status'] == response_status_code
        assert response['response'] == expected_response

    def test_raise_role_description_should_not_be_empty_exception(self):
        # Arrange
        presenter = AddRolesPresenterImplementation()
        from ib_iam.constants.exception_messages \
            import ROLE_DESCRIPTION_SHOULD_NOT_BE_EMPTY
        expected_response = ROLE_DESCRIPTION_SHOULD_NOT_BE_EMPTY[0]
        response_status_code = ROLE_DESCRIPTION_SHOULD_NOT_BE_EMPTY[1]

        # Act
        response_object = presenter.response_for_role_description_should_not_be_empty_exception()

        # Assert
        response = json.loads(response_object.content)
        assert response['http_status_code'] == StatusCode.BAD_REQUEST.value
        assert response['res_status'] == response_status_code
        assert response['response'] == expected_response