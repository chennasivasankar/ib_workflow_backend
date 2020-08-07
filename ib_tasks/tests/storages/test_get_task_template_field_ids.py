import pytest

from ib_tasks.storages.tasks_storage_implementation import TasksStorageImplementation
from ib_tasks.tests.factories.models import GoFToTaskTemplateFactory, GoFFactory, TaskTemplateFactory, FieldFactory


@pytest.mark.django_db
class TestGetTaskTemplateFieldIds:

    @pytest.fixture()
    def create_task_fields(self):
        GoFFactory.reset_sequence()
        gof_obj = GoFFactory()
        TaskTemplateFactory.reset_sequence()
        task_objs = TaskTemplateFactory.create_batch(size=2)
        GoFToTaskTemplateFactory.reset_sequence()
        GoFToTaskTemplateFactory(gof=gof_obj, task_template=task_objs[0])
        GoFToTaskTemplateFactory(gof=gof_obj, task_template=task_objs[1])
        FieldFactory.reset_sequence()
        FieldFactory.create_batch(size=4, gof=gof_obj)

    def test_given_template_ids_get_their_related_field_ids(self,
                                                            snapshot,
                                                            create_task_fields):
        # Arrange
        task_template_ids = ["template_1", "template_2"]
        storage = TasksStorageImplementation()

        # Act
        result = storage.get_field_ids_for_given_task_template_ids(
            task_template_ids=task_template_ids)

        # Assert
        snapshot.assert_match(result, "task_fields")
