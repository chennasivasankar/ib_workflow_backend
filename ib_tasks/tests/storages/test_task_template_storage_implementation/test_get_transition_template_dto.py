import pytest

from ib_tasks.tests.factories.models import TaskTemplateFactory


@pytest.mark.django_db
class TestGetTransitionTemplateDTO:

    def test_get_transition_template_dto(self, storage):
        # Arrange
        transition_template = TaskTemplateFactory()

        # Act
        transition_template_dto = storage.get_transition_template_dto(
            transition_template_id=transition_template.template_id)

        # Assert
        assert transition_template_dto.template_id == \
               transition_template.template_id
        assert transition_template_dto.template_name == \
               transition_template.name
