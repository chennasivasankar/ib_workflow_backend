import pytest

from ib_tasks.tests.factories.models import TaskTemplateFactory


@pytest.mark.django_db
class TestUpdateTemplate:

    def test_update_template(self, storage):
        # Arrange
        template_id = "FIN_VENDOR"
        template_name = "iB Template"
        is_transition_template = True
        TaskTemplateFactory(template_id=template_id, name=template_name)

        # Act
        storage.update_template(
            template_id=template_id, template_name=template_name,
            is_transition_template=is_transition_template
        )

        # Assert
        from ib_tasks.models.task_template import TaskTemplate
        template = TaskTemplate.objects.get(template_id=template_id)

        assert template.template_id == template_id
        assert template.name == template_name
        assert template.is_transition_template == is_transition_template
