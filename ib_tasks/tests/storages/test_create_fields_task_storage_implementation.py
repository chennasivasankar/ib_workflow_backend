import pytest
from typing import List
from ib_tasks.tests.factories.models import \
    FieldFactory, GoFFactory
from ib_tasks.constants.enum import FieldTypes
from ib_tasks.tests.factories.storage_dtos import (
    FieldDTOFactory
)
from ib_tasks.models.field import Field


class TestTaskStorageImplementation:

    @pytest.fixture
    def storage(self):
        from ib_tasks.storages.task_storage_implementation \
            import TaskStorageImplementation
        storage = TaskStorageImplementation()
        return storage

    @pytest.fixture
    def reset_factories(self):
        FieldFactory.reset_sequence(0)
        GoFFactory.reset_sequence(0)

    @pytest.mark.django_db
    def test_get_existing_field_ids_in_given_field_ids(
            self, storage, reset_factories
    ):
        # Arrange
        field_ids = ["field0", "field1", "field2"]
        FieldFactory.create_batch(size=2)
        expected_existing_field_ids = ["field0", "field1"]

        # Act
        actual_existing_field_ids = storage.get_existing_field_ids(field_ids)
        print("actual_existing_field_ids = ", actual_existing_field_ids)
        # Assert

        assert expected_existing_field_ids == actual_existing_field_ids

    @pytest.mark.django_db
    def test_create_fields_given_field_dtos(
            self, storage, reset_factories
    ):
        # Arrange

        GoFFactory(gof_id="gof1")
        GoFFactory(gof_id="gof2")

        field_dtos = [
            FieldDTOFactory(
                gof_id="gof1", field_id="field1",
                field_type=FieldTypes.PLAIN_TEXT.value
            ),
            FieldDTOFactory(
                gof_id="gof2", field_id="field2",
                field_type=FieldTypes.DROPDOWN.value
            )
        ]

        # Act
        storage.create_fields(field_dtos)

        # Assert
        self._assert_fileds(field_dtos)

    @pytest.mark.django_db
    def test_update_fields_given_field_dtos(
            self, storage, reset_factories
    ):
        # Arrange
        FieldFactory(field_id="field1")
        FieldFactory(field_id="field2")

        GoFFactory(gof_id="gof10")
        GoFFactory(gof_id="gof11")

        field_dtos = [
            FieldDTOFactory(
                gof_id="gof11", field_id="field1",
                field_type=FieldTypes.PLAIN_TEXT.value
            ),
            FieldDTOFactory(
                gof_id="gof10", field_id="field2",
                field_type=FieldTypes.DROPDOWN.value
            )
        ]

        # Act
        storage.update_fields(field_dtos)

        # Assert
        self._assert_fileds(field_dtos)

    def _assert_fileds(self, field_dtos: List[FieldDTOFactory]):
        for field_dto in field_dtos:
            field_obj = Field.objects.get(pk=field_dto.field_id)
            assert field_obj.gof_id == field_dto.gof_id
            assert field_obj.display_name == field_dto.field_display_name
            assert field_obj.field_type == field_dto.field_type
            assert field_obj.field_values == field_dto.field_values
            assert field_obj.required == field_dto.required
            assert field_obj.help_text == field_dto.help_text
            assert field_obj.tooltip == field_dto.tool_tip
            assert field_obj.placeholder_text == field_dto.placeholder_text
            assert field_obj.error_messages == field_dto.error_message
            assert field_obj.validation_regex == field_dto.validation_regex
