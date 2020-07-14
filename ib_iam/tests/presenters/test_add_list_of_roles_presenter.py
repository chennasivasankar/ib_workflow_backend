import json
from ib_iam.presenters.presenter_implementation import PresenterImplementation


class TestAddListOfRolesPresenter:

    def test_raise_role_id_should_not_be_empty(self):

        # Arrange
        presenter = PresenterImplementation()

        from ib_iam.constants.exception_messages \
            import ROLE_ID_SHOULD_NOT_BE_EMPTY

        expected_response = ROLE_ID_SHOULD_NOT_BE_EMPTY[0]
        response_status_code = ROLE_ID_SHOULD_NOT_BE_EMPTY[1]


        # Act
        response_object = presenter.raise_role_id_should_not_be_empty_exception()

        # Assert
        response = json.loads(response_object.content)
        assert response['http_status_code'] == 400
        assert response['res_status'] == response_status_code
        assert response['response'] == expected_response

    def test_raise_role_id_should_not_be_in_valid_format(self):

        # Arrange
        presenter = PresenterImplementation()

        from ib_iam.constants.exception_messages \
            import ROLE_ID_SHOULD_NOT_BE_IN_VALID_FORMAT

        expected_response = ROLE_ID_SHOULD_NOT_BE_IN_VALID_FORMAT[0]
        response_status_code = ROLE_ID_SHOULD_NOT_BE_IN_VALID_FORMAT[1]


        # Act
        response_object = presenter.raise_role_id_format_is_invalid_exception()

        # Assert
        response = json.loads(response_object.content)
        assert response['http_status_code'] == 400
        assert response['res_status'] == response_status_code
        assert response['response'] == expected_response

    def test_raise_role_id_duplicate(self):

        # Arrange
        presenter = PresenterImplementation()

        from ib_iam.constants.exception_messages \
            import DUPLICATE_ROLE_IDS

        expected_response = DUPLICATE_ROLE_IDS[0]
        response_status_code = DUPLICATE_ROLE_IDS[1]


        # Act
        response_object = presenter.raise_duplicate_role_ids_exception()

        # Assert
        response = json.loads(response_object.content)
        assert response['http_status_code'] == 400
        assert response['res_status'] == response_status_code
        assert response['response'] == expected_response

    def test_raise_role_name_should_not_be_empty(self):

        # Arrange
        presenter = PresenterImplementation()

        from ib_iam.constants.exception_messages \
            import ROLE_NAME_SHOULD_NOT_BE_EMPTY

        expected_response = ROLE_NAME_SHOULD_NOT_BE_EMPTY[0]
        response_status_code = ROLE_NAME_SHOULD_NOT_BE_EMPTY[1]


        # Act
        response_object = presenter.raise_role_name_should_not_be_empty_exception()

        # Assert
        response = json.loads(response_object.content)
        assert response['http_status_code'] == 400
        assert response['res_status'] == response_status_code
        assert response['response'] == expected_response


    def test_raise_role_description_should_not_be_empty(self):

        # Arrange
        presenter = PresenterImplementation()

        from ib_iam.constants.exception_messages \
            import ROLE_DESCRIPTION_SHOULD_NOT_BE_EMPTY

        expected_response = ROLE_DESCRIPTION_SHOULD_NOT_BE_EMPTY[0]
        response_status_code = ROLE_DESCRIPTION_SHOULD_NOT_BE_EMPTY[1]


        # Act
        response_object = presenter.raise_role_description_should_not_be_empty_exception()

        # Assert
        response = json.loads(response_object.content)
        assert response['http_status_code'] == 400
        assert response['res_status'] == response_status_code
        assert response['response'] == expected_response
