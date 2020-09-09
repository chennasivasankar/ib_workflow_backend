import factory
import pytest

from ib_tasks.tests.factories.models import ProjectTaskTemplateFactory, \
    TaskTemplateFactory


@pytest.mark.django_db
class TestGetProjectIdWithTaskTemplateIdDTOS:

    def test_get_project_id_with_task_template_id_dtos(self, storage):
        # Arrange
        template_ids = ["template_1", "template_2"]
        task_templates = TaskTemplateFactory.create_batch(
            size=2, template_id=factory.Iterator(template_ids))
        ProjectTaskTemplateFactory.create_batch(
            size=2, task_template=factory.Iterator(task_templates))

        from ib_tasks.interactors.storage_interfaces.task_templates_dtos \
            import \
            ProjectIdWithTaskTemplateIdDTO
        expected_project_id_with_task_template_id_dtos = \
            [
                ProjectIdWithTaskTemplateIdDTO(
                    project_id="project_1",
                    task_template_id=template_ids[0]
                ),
                ProjectIdWithTaskTemplateIdDTO(
                    project_id="project_2",
                    task_template_id=template_ids[1]
                )
            ]
        # Act
        result = storage.get_project_id_with_task_template_id_dtos()

        # Assert
        assert result == expected_project_id_with_task_template_id_dtos
