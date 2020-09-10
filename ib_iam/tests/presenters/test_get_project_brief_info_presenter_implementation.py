import json

import pytest

from ib_iam.constants.enums import StatusCode


class TestGetProjectBriefInfoPresenterImplementation:

    @pytest.fixture()
    def presenter(self):
        from ib_iam.presenters.get_project_brief_info_presenter_implementation \
            import GetProjectBriefInfoPresenterImplementation
        presenter = GetProjectBriefInfoPresenterImplementation()
        return presenter

    @pytest.fixture()
    def project_dtos(self):
        from ib_iam.tests.factories.storage_dtos import \
            ProjectWithDisplayIdDTOFactory
        ProjectWithDisplayIdDTOFactory.reset_sequence(1)

        project_ids = ["project_1", "project_2"]
        project_dtos = [
            ProjectWithDisplayIdDTOFactory(project_id=project_id)
            for project_id in project_ids
        ]
        return project_dtos

    def test_raise_exception_for_invalid_user_id(self, presenter):
        # Arrange
        from ib_iam.presenters.get_project_brief_info_presenter_implementation import \
            USER_DOES_NOT_EXIST
        expected_response = USER_DOES_NOT_EXIST[0]
        expected_http_status_code = StatusCode.BAD_REQUEST.value
        expected_res_status = USER_DOES_NOT_EXIST[1]

        # Act
        response_obj \
            = presenter.response_for_user_does_not_exist()

        # Assert
        response_data = json.loads(response_obj.content)

        assert response_data["response"] == expected_response
        assert response_data["http_status_code"] == expected_http_status_code
        assert response_data["res_status"] == expected_res_status

    def test_success_response_for_get_project_brief_info_return_response(
            self, presenter, project_dtos, snapshot
    ):
        # Act
        response_obj = presenter.success_response_for_get_project_brief_info(
            project_dtos=project_dtos
        )

        # Assert
        response_data = json.loads(response_obj.content)

        snapshot.assert_match(response_data, "get_project_brief_info")
