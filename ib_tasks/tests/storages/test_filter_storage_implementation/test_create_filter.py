import factory
import pytest

from ib_tasks.tests.factories.models import TaskTemplateFactory, FieldFactory


@pytest.mark.django_db
class TestCreateFilter:

    def test_create_filter_with_valid_details(
            self, storage, filter_dto, condition_dtos, snapshot):
        # Arrange
        template_id = 'template_0'
        TaskTemplateFactory(template_id=template_id)
        FieldFactory.create_batch(
            3, field_id=factory.Iterator(
                ['field_0', 'field_1', 'field_2']
            )
        )
        # Act
        filter_dto, condition_dtos = storage.create_filter(
            filter_dto=filter_dto,
            condition_dtos=condition_dtos
        )

        # Assert
        snapshot.assert_match(filter_dto, 'filter_dto')
        snapshot.assert_match(condition_dtos, 'condition_dtos')
