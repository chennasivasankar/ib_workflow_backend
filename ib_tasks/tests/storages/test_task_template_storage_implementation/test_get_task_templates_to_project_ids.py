import pytest


@pytest.mark.django_db
class TestGetTaskTemplatesToProjectIds:

    def setup_storage(self):
        from ib_tasks.tests.factories.models \
            import TaskTemplateFactory, ProjectTaskTemplateFactory
        TaskTemplateFactory.reset_sequence()
        ProjectTaskTemplateFactory.reset_sequence(1)
        template = TaskTemplateFactory()
        ProjectTaskTemplateFactory(task_template=template)

    def expected_response(self):
        from ib_tasks.tests.factories.storage_dtos import ProjectTemplateDTOFactory
        ProjectTemplateDTOFactory.reset_sequence(1)
        response = ProjectTemplateDTOFactory.create_batch(1, template_name="Template 1")
        return response

    def test_get_task_templates_dtos_to_project_ids(self, storage):
        # Arrange
        project_ids = ["project_1"]
        self.setup_storage()
        expected = self.expected_response()

        # Act
        result = storage.get_task_templates_to_project_ids(project_ids=project_ids)

        # Assert
        assert result == expected
