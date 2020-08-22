import json


class TestGetProjectsPresenterImplementation:
    def test_get_response_for_get_projects_returns_projects(self, snapshot):
        from ib_iam.presenters.get_projects_presenter_implementation import \
            GetProjectsPresenterImplementation
        json_presenter = GetProjectsPresenterImplementation()
        from ib_iam.tests.factories.storage_dtos import ProjectDTOFactory
        project_ids = ["641bfcc5-e1ea-4231-b482-f7f34fb5c7c4",
                       "641bfcc5-e1ea-4231-b482-f7f34fb5c7c5"]
        ProjectDTOFactory.reset_sequence(1)
        project_dtos = [ProjectDTOFactory(project_id=project_id)
                        for project_id in project_ids]

        http_response = json_presenter.get_response_for_get_projects(
            project_dtos=project_dtos)

        response = json.loads(http_response.content)

        snapshot.assert_match(response, "projects")
