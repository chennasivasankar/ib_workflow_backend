import json

import pytest
from freezegun import freeze_time

from ib_discussions.constants.enum import StatusCode


class TestCreateDiscussionPresenterImplementation:
    @pytest.fixture()
    def presenter(self):
        from ib_discussions.presenters.create_discussion_presenter_implementation import \
            CreateDiscussionPresenterImplementation
        presenter = CreateDiscussionPresenterImplementation()
        return presenter

    def test_raise_exception_for_entity_id_not_found(self, presenter):
        # Arrange
        from ib_discussions.presenters.create_discussion_presenter_implementation import \
            ENTITY_ID_NOT_FOUND
        expected_response = ENTITY_ID_NOT_FOUND[0]
        expected_http_status_code = StatusCode.NOT_FOUND.value
        expected_res_status = ENTITY_ID_NOT_FOUND[1]

        # Act
        response_obj = presenter.raise_exception_for_entity_id_not_found()

        # Assert
        response_data = json.loads(response_obj.content)

        assert response_data["response"] == expected_response
        assert response_data["http_status_code"] == expected_http_status_code
        assert response_data["res_status"] == expected_res_status

    def test_raise_exception_for_invalid_entity_type_for_entity_id(self,
                                                                   presenter):
        # Arrange
        from ib_discussions.presenters.create_discussion_presenter_implementation import \
            INVALID_ENTITY_TYPE_FOR_ENTITY_ID
        expected_response = INVALID_ENTITY_TYPE_FOR_ENTITY_ID[0]
        expected_http_status_code = StatusCode.BAD_REQUEST.value
        expected_res_status = INVALID_ENTITY_TYPE_FOR_ENTITY_ID[1]

        # Act
        response_obj \
            = presenter.raise_exception_for_invalid_entity_type_for_entity_id()

        # Assert
        response_data = json.loads(response_obj.content)

        assert response_data["response"] == expected_response
        assert response_data["http_status_code"] == expected_http_status_code
        assert response_data["res_status"] == expected_res_status

    def test_prepare_success_response_for_create_discussion(self, presenter):
        # Act
        response_obj \
            = presenter.prepare_success_response_for_create_discussion()

        # Assert
        assert response_obj.status_code == StatusCode.CREATED.value
