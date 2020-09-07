import pytest

from ib_tasks.tests.factories.models import TaskTemplateFactory


@pytest.mark.django_db
class TestCheckIsTemplateExists:

    def test_check_is_template_exists_with_invalid_template_id_returns_false(
            self, storage):
        # Arrange
        template_id = "FIN_VENDOR"

        # Act
        is_template_exists = \
            storage.check_is_template_exists(template_id=template_id)

        # Assert
        assert is_template_exists is False

    def test_check_is_template_exists_with_valid_template_id_returns_true(
            self, storage):
        # Arrange
        task_template = TaskTemplateFactory()
        template_id = task_template.template_id

        # Act
        is_template_exists = \
            storage.check_is_template_exists(template_id=template_id)

        # Assert
        assert is_template_exists is True
