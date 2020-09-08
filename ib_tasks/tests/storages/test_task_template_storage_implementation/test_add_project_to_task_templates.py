import pytest


@pytest.mark.django_db
class TestAddProjectToTaskTemplates:

    def test_add_project_to_task_templates(self, storage, snapshot):
        # Arrange
        task_template_ids = ["template_1", "template_2"]
        from ib_tasks.tests.factories.models import TaskTemplateFactory
        import factory
        TaskTemplateFactory.create_batch(
            size=2, template_id=factory.Iterator(task_template_ids))

        project_id = "project_1"

        # Act
        storage.add_project_to_task_templates(
            task_template_ids=task_template_ids, project_id=project_id)

        # Assert
        from ib_tasks.models.project_task_template import ProjectTaskTemplate
        project_task_templates = ProjectTaskTemplate.objects.all()

        counter = 1
        for project_task_template in project_task_templates:
            snapshot.assert_match(
                project_task_template.project_id,
                'project_id_of_project_task_template_{}'.format(counter))
            snapshot.assert_match(
                project_task_template.task_template_id,
                'task_template_id_of_project_task_template_{}'.format(counter))
            counter = counter + 1
