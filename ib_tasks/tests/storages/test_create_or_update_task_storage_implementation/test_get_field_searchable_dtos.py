import factory
import pytest

from ib_tasks.tests.factories.models import TaskGoFFieldFactory, \
    TaskGoFFactory, FieldFactory


@pytest.mark.django_db
class TestGetFieldSearchableDTOS:

    def test_given_field_ids_returns_field_searchable_dtos(
            self, storage, snapshot
    ):
        # Arrange
        from ib_tasks.constants.enum import Searchable
        field_values = [
            Searchable.CITY.value,
            Searchable.USER.value,
            Searchable.COUNTRY.value,
            Searchable.CITY.value
        ]
        from ib_tasks.constants.enum import FieldTypes
        field_objects = FieldFactory.create_batch(
            size=4, field_values=factory.Iterator(field_values),
            field_type=FieldTypes.SEARCHABLE.value
        )
        field_response = [
            "1", "123e4567-e89b-12d3-a456-426614174000",
            "India", "5"
        ]
        FieldFactory()
        task_gof_objects = TaskGoFFactory.create_batch(size=2)
        TaskGoFFieldFactory.create_batch(
            size=4, field=factory.Iterator(field_objects),
            task_gof=factory.Iterator(task_gof_objects),
            field_response=factory.Iterator(field_response)
        )
        TaskGoFFieldFactory()
        field_ids = [
            field_obj.field_id
            for field_obj in field_objects
        ]
        task_gof_ids = [
            task_gof_obj.id
            for task_gof_obj in task_gof_objects
        ]

        # Act
        field_searchable_dtos = storage.get_field_searchable_dtos(
            field_ids, task_gof_ids
        )

        # Assert
        snapshot.assert_match(
            name="field_searchable_dtos", value=field_searchable_dtos
        )
