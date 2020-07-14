import json
from ib_iam.presenters.presenter_implementation import PresenterImplementation


class TestAddListOfRolesPresenter:

    def test_raise_role_id_should_not_be_empty(self, snapshot):

        # Arrange
        presenter = PresenterImplementation()

        from ib_iam.constants.exception_messages \
            import ROLE_ID_SHOULD_NOT_BE_EMPTY

        expected_response = ROLE_ID_SHOULD_NOT_BE_EMPTY[0]
        response_status_code = ROLE_ID_SHOULD_NOT_BE_EMPTY[1]


        # Act
        response_object = presenter.raise_role_id_should_not_be_empty()

        # Assert
        response = json.loads(response_object.content)
        # snapshot.assert_match(response, 'role_id_exception')
        assert response['http_status_code'] == 400
        assert response['res_status'] == response_status_code
        assert response['response'] == expected_response


    def test_raise_role_name_should_not_be_empty(self, snapshot):

        # Arrange
        presenter = PresenterImplementation()

        from ib_iam.constants.exception_messages \
            import ROLE_NAME_SHOULD_NOT_BE_EMPTY

        expected_response = ROLE_NAME_SHOULD_NOT_BE_EMPTY[0]
        response_status_code = ROLE_NAME_SHOULD_NOT_BE_EMPTY[1]


        # Act
        response_object = presenter.raise_role_name_should_not_be_empty()

        # Assert
        response = json.loads(response_object.content)
        # snapshot.assert_match(response, 'role_id_exception')
        assert response['http_status_code'] == 400
        assert response['res_status'] == response_status_code
        assert response['response'] == expected_response


    def test_raise_role_description_should_not_be_empty(self, snapshot):

        # Arrange
        presenter = PresenterImplementation()

        from ib_iam.constants.exception_messages \
            import ROLE_DESCRIPTION_SHOULD_NOT_BE_EMPTY

        expected_response = ROLE_DESCRIPTION_SHOULD_NOT_BE_EMPTY[0]
        response_status_code = ROLE_DESCRIPTION_SHOULD_NOT_BE_EMPTY[1]


        # Act
        response_object = presenter.raise_role_description_should_not_be_empty()

        # Assert
        response = json.loads(response_object.content)
        # snapshot.assert_match(response, 'role_id_exception')
        assert response['http_status_code'] == 400
        assert response['res_status'] == response_status_code
        assert response['response'] == expected_response