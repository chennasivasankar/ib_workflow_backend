import pytest

from ib_tasks.tests.factories.models import TaskTemplateFactory


@pytest.mark.django_db
class TestCheckIsTransitionTemplateExists:

    def test_check_is_transition_template_exists_with_invalid_transition_template_id_returns_false(
            self, storage):
        # Arrange
        transition_template_id = "template_1"

        # Act
        is_transition_template_exists = \
            storage.check_is_transition_template_exists(
                transition_template_id=transition_template_id)

        # Assert
        assert is_transition_template_exists is False

    def test_check_is_transition_template_exists_with_valid_transition_template_id_returns_true(
            self, storage):
        # Arrange
        transition_template = TaskTemplateFactory(is_transition_template=True)
        transition_template_id = transition_template.template_id

        # Act
        is_transition_template_exists = \
            storage.check_is_transition_template_exists(
                transition_template_id=transition_template_id)

        # Assert
        assert is_transition_template_exists is True
