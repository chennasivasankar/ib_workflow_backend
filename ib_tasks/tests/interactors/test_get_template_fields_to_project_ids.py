from typing import List

import pytest

from ib_tasks.tests.factories.adapter_dtos import UserProjectStatusDTOFactory
from ib_tasks.tests.factories.storage_dtos import ProjectTemplateDTOFactory, \
    TaskTemplateGofsDTOFactory, \
    FieldNameDTOFactory
from ib_tasks.tests.interactors.super_storage_mock_class import \
    StorageMockClass


class TestGetProjectsTemplatesFieldsInteractor(StorageMockClass):

    @staticmethod
    @pytest.fixture()
    def interactor(task_template_storage, gof_storage, field_storage):
        from ib_tasks.interactors.get_templates_fields_to_project_ids \
            import GetProjectsTemplatesFieldsInteractor
        interactor = GetProjectsTemplatesFieldsInteractor(
            task_template_storage=task_template_storage,
            gof_storage=gof_storage, field_storage=field_storage
        )
        return interactor

    @staticmethod
    @pytest.fixture()
    def projects_mock(mocker):
        path = "ib_tasks.adapters.auth_service.AuthService.validate_project_ids"
        return mocker.patch(path)

    @pytest.fixture()
    def user_in_projects_mock(self, mocker):
        path = "ib_tasks.adapters.auth_service.AuthService.validate_if_user_is_in_projects"
        return mocker.patch(path)

    @pytest.fixture()
    def user_roles_mock(self, mocker):
        path = "ib_tasks.adapters.roles_service.RolesService.get_user_role_ids"
        return mocker.patch(path)

    @classmethod
    def setup(cls):
        UserProjectStatusDTOFactory.reset_sequence(1)
        ProjectTemplateDTOFactory.reset_sequence(1)
        TaskTemplateGofsDTOFactory.reset_sequence(1)
        FieldNameDTOFactory.reset_sequence(1)

    @pytest.fixture()
    def expected_response(self):
        self.setup()
        from ib_tasks.tests.factories.presenter_dtos import ProjectTemplateFieldsDTOFactory
        return ProjectTemplateFieldsDTOFactory(
            fields_dto=FieldNameDTOFactory.create_batch(2)
        )

    @staticmethod
    def set_up_storage(
            projects_mock, project_ids: List[str], user_in_projects_mock,
            user_roles_mock, role_ids, task_template_storage, template_projects,
            gof_storage, template_gofs, field_storage, field_dtos
    ):
        projects_mock.return_value = project_ids
        user_project_dtos = UserProjectStatusDTOFactory.create_batch(1)
        user_in_projects_mock.return_value = user_project_dtos
        user_roles_mock.return_value = role_ids
        task_template_storage.get_task_templates_to_project_ids.return_value = \
            template_projects
        gof_storage.get_user_permitted_template_gof_dtos.return_value = \
            template_gofs
        field_storage.get_user_permitted_gof_field_dtos.return_value = \
            field_dtos


    def test_given_valid_details_returns_details(
            self, projects_mock, interactor, user_in_projects_mock,
            user_roles_mock, task_template_storage, gof_storage, field_storage,
            expected_response
    ):
        # Arrange
        project_ids = ["project_1"]
        template_ids = ["template_1"]
        gof_ids = ["gof_1", "gof_2"]
        user_id = "user_1"
        role_ids = ["role_1", "role_2"]
        project_templates = ProjectTemplateDTOFactory.create_batch(1)
        template_gofs = TaskTemplateGofsDTOFactory.create_batch(1)
        field_dtos = FieldNameDTOFactory.create_batch(2)
        self.set_up_storage(
            projects_mock=projects_mock, project_ids=project_ids,
            user_in_projects_mock=user_in_projects_mock,
            user_roles_mock=user_roles_mock, role_ids=role_ids,
            task_template_storage=task_template_storage,
            template_projects=project_templates,
            gof_storage=gof_storage, template_gofs=template_gofs,
            field_storage=field_storage, field_dtos=field_dtos
        )

        # Act
        response = interactor.get_task_templates(
            user_id=user_id, project_ids=project_ids
        )

        # Assert
        assert response == expected_response
        task_template_storage.get_task_templates_to_project_ids\
            .assert_called_once_with(project_ids=project_ids)
        gof_storage.get_user_permitted_template_gof_dtos\
            .assert_called_once_with(
                user_roles=role_ids, template_ids=template_ids
            )
        field_storage.get_user_permitted_gof_field_dtos \
            .assert_called_once_with(
                user_roles=role_ids, gof_ids=gof_ids
            )