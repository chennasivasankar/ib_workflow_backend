import pytest


@pytest.mark.django_db
class TestGetTaskTemplatesDTOS:

    def test_get_task_templates_dtos(self, storage):
        # Arrange
        from ib_tasks.tests.factories.models import TaskTemplateFactory
        from ib_tasks.interactors.storage_interfaces.task_templates_dtos \
            import TemplateDTO
        expected_output = [
            TemplateDTO(
                template_id='template_1', template_name='Template 1'
            ),
            TemplateDTO(
                template_id='template_2', template_name='Template 2'
            )
        ]

        TaskTemplateFactory.create_batch(size=2)

        # Act
        result = storage.get_task_templates_dtos()

        # Assert
        assert result == expected_output
