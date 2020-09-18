import pytest


@pytest.mark.django_db
class TestGetTaskTemplatesToProjectIds:

    def setup_storage(self):
        from ib_tasks.tests.factories.models import (
            TaskTemplateFactory, GoFToTaskTemplateFactory,
            GoFRoleFactory, GoFFactory
        )
        GoFFactory.reset_sequence()
        GoFRoleFactory.reset_sequence(1)
        TaskTemplateFactory.reset_sequence()
        template = TaskTemplateFactory()
        gofs = GoFFactory.create_batch(3)
        GoFToTaskTemplateFactory(task_template=template, gof=gofs[0])
        GoFToTaskTemplateFactory(task_template=template, gof=gofs[1])
        GoFToTaskTemplateFactory(task_template=template, gof=gofs[2])
        GoFRoleFactory(gof=gofs[0])
        GoFRoleFactory(gof=gofs[1])
        GoFRoleFactory(gof=gofs[2])

    def expected_response(self):
        from ib_tasks.tests.factories.storage_dtos import TaskTemplateGofsDTOFactory
        TaskTemplateGofsDTOFactory.reset_sequence(1)
        response = TaskTemplateGofsDTOFactory.create_batch(1)
        return response

    def test_get_user_permitted_gofs_to_template_ids(self, storage):
        # Arrange
        template_ids = ["template_1"]
        user_roles = ["ROLE-1", "ROLE-2"]
        self.setup_storage()
        expected = self.expected_response()

        # Act
        result = storage.get_user_permitted_template_gof_dtos(
            template_ids=template_ids, user_roles=user_roles
        )

        # Assert
        assert result == expected

    def test_get_user_permitted_empty_gofs_to_template_ids(self, storage):
        # Arrange
        template_ids = ["template_1"]
        user_roles = ["ROLE-4", "ROLE-5"]
        self.setup_storage()

        # Act
        result = storage.get_user_permitted_template_gof_dtos(
            template_ids=template_ids, user_roles=user_roles
        )

        # Assert
        assert result == []
