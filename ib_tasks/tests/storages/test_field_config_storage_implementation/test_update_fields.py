from typing import List

import pytest

from ib_tasks.constants.enum import FieldTypes
from ib_tasks.models import Field
from ib_tasks.tests.factories.models import FieldFactory, GoFFactory
from ib_tasks.tests.factories.storage_dtos import FieldDTOFactory


@pytest.mark.django_db
class TestUpdateFields:

    def test_update_fields_given_field_dtos(self, storage):
        
        # Arrange
        FieldFactory(field_id="field1")
        FieldFactory(field_id="field2")

        GoFFactory(gof_id="gof10")
        GoFFactory(gof_id="gof11")

        field_dtos = [
            FieldDTOFactory(
                gof_id="gof11", field_id="field1",
                field_type=FieldTypes.PASSWORD.value,
                field_values=None
            ),
            FieldDTOFactory(
                gof_id="gof10", field_id="field2",
                field_type=FieldTypes.DROPDOWN.value,
                field_values="['User', 'admin']"
            )
        ]

        # Act
        storage.update_fields(field_dtos)

        # Assert
        self._assert_fields(field_dtos)

    @staticmethod
    def _assert_fields(field_dtos: List[FieldDTOFactory]):
        for field_dto in field_dtos:
            field_obj = Field.objects.get(pk=field_dto.field_id)
            assert field_obj.gof_id == field_dto.gof_id
            assert field_obj.display_name == field_dto.field_display_name
            assert field_obj.field_type == field_dto.field_type
            assert field_obj.field_values == field_dto.field_values
            assert field_obj.required == field_dto.required
            assert field_obj.help_text == field_dto.help_text
            assert field_obj.tooltip == field_dto.tooltip
            assert field_obj.placeholder_text == field_dto.placeholder_text
            assert field_obj.error_messages == field_dto.error_message
            assert field_obj.validation_regex == field_dto.validation_regex
