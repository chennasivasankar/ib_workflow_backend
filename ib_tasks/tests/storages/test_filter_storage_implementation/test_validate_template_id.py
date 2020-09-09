import pytest

from ib_tasks.tests.factories.models import TaskTemplateFactory


@pytest.mark.django_db
class TestValidateTemplateId:

    def test_validate_template_id_with_invalid_template_id(self, storage):
        # Arrange
        template_id = 'template_id'

        # Act
        from ib_tasks.exceptions.filter_exceptions import InvalidTemplateID
        with pytest.raises(InvalidTemplateID):
            storage.validate_template_id(
                template_id=template_id)

    def test_validate_template_id_with_valid_template_id(self, storage):
        # Arrange
        template_id = 'template_1'
        TaskTemplateFactory.reset_sequence()
        TaskTemplateFactory()

        # Act
        storage.validate_template_id(template_id=template_id)
