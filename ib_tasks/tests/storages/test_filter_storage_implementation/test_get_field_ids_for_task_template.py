import pytest

from ib_tasks.tests.factories.models import FieldFactory, \
    GoFToTaskTemplateFactory


@pytest.mark.django_db
class TestGetFieldIdsForTaskTemplate:

    def test_get_field_ids_for_task_template_return_valid_field_ids(
            self, storage):
        # Arrange
        fields = FieldFactory.create_batch(3)
        gof_ids = [field.gof_id for field in fields]
        template_id = 'template_12'
        GoFToTaskTemplateFactory(
            task_template__template_id=template_id, gof_id=gof_ids[0])
        expected_field_ids = [field.field_id for field in fields]

        # Act
        actual_field_ids = storage.get_field_ids_for_task_template(
            field_ids=expected_field_ids[:2], template_id=template_id)

        # Assert
        assert actual_field_ids == expected_field_ids[:1]
