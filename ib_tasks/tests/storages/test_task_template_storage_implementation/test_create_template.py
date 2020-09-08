import pytest


@pytest.mark.django_db
class TestCreateTemplate:

    def test_create_template(self, storage):
        # Arrange
        template_id = "FIN_VENDOR"
        template_name = "Task Template 1"
        is_transition_template = True

        # Act
        storage.create_template(
            template_id=template_id, template_name=template_name,
            is_transition_template=is_transition_template
        )

        # Assert
        from ib_tasks.models.task_template import TaskTemplate
        template = TaskTemplate.objects.get(template_id=template_id)

        assert template.template_id == template_id
        assert template.name == template_name
        assert template.is_transition_template == is_transition_template
