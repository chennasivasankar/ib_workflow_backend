import mock
import pytest

from ib_iam.exceptions.custom_exceptions import InvalidProjectId
from ib_iam.interactors.project_interactor import ProjectInteractor
from ib_iam.storages.project_storage_implementation import \
    ProjectStorageImplementation
from ib_iam.tests.factories.adapter_dtos import ProjectTeamUserDTOFactory


class TestGetTeamDetailsForGivenProjectTeamUserDetailsDto:

    def test_given_invalid_project_raises_invalid_project_exception(self):
        project_storage = mock.create_autospec(ProjectStorageImplementation)
        interactor = ProjectInteractor(project_storage=project_storage)
        project_id = "1"
        project_team_user_dto = ProjectTeamUserDTOFactory(
            project_id=project_id)
        project_storage \
            .get_valid_project_ids_from_given_project_ids \
            .return_value = []

        with pytest.raises(InvalidProjectId):
            interactor \
                .get_team_details_for_given_project_team_user_details_dto(
                project_team_user_dto=project_team_user_dto)

        project_storage.get_valid_project_ids_from_given_project_ids \
            .assert_called_once_with(project_ids=[project_id])
