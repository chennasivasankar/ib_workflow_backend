from typing import List
import pytest

from ib_tasks.constants.enum import FieldTypes
from ib_tasks.models import FieldRole
from ib_tasks.models.field import Field
from ib_tasks.tests.factories.models import GoFFactory, TaskTemplateWithTransitionFactory, \
    GoFRoleFactory, FieldFactory, FieldRoleFactory
from ib_tasks.tests.factories.storage_dtos import (
    GoFDTOFactory,
    GoFRolesDTOFactory,
    CompleteGoFDetailsDTOFactory,
    FieldCompleteDetailsDTOFactory
)
from ib_tasks.tests.factories.storage_dtos \
    import GoFRoleDTOFactory, FieldDTOFactory


@pytest.mark.django_db
class TestFieldConfigStorageImplementation:

    @pytest.fixture
    def storage(self):
        from ib_tasks.storages.field_config_storage_implementation import \
            FieldConfigStorageImplementation
        return FieldConfigStorageImplementation()

    @pytest.fixture
    def gof_storage(self):
        from ib_tasks.storages.gof_storage_implementation import \
            GoFStorageImplementation
        return GoFStorageImplementation()

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        GoFFactory.reset_sequence(1)
        TaskTemplateWithTransitionFactory.reset_sequence(1)
        FieldFactory.reset_sequence(1)
        GoFRoleFactory.reset_sequence(1)
        GoFDTOFactory.reset_sequence(1)
        GoFRolesDTOFactory.reset_sequence(1)
        CompleteGoFDetailsDTOFactory.reset_sequence(1)
        GoFRoleDTOFactory.reset_sequence(1)
        FieldCompleteDetailsDTOFactory.reset_sequence(1)

    def test_get_existing_field_ids_in_given_field_ids(
            self, storage
    ):
        # Arrange
        field_ids = ["field0", "field1", "field2"]
        FieldFactory.create(field_id="field0")
        FieldFactory.create(field_id="field1")
        expected_existing_field_ids = ["field0", "field1"]

        # Act
        actual_existing_field_ids = storage.get_existing_field_ids(field_ids)
        # Assert

        assert expected_existing_field_ids == actual_existing_field_ids

    def test_create_fields_given_field_dtos(
            self, storage
    ):
        # Arrange

        GoFFactory(gof_id="gof1")
        GoFFactory(gof_id="gof2")
        import json

        field_values = [
            {
                "name": "Individual",
                "gof_ids": ["gof2", "gof1"]
            },
            {
                "name": "Company",
                "gof_ids": ["gof1", "gof2"]
            }
        ]
        field_values = json.dumps(field_values)

        field_dtos = [
            FieldDTOFactory(
                gof_id="gof1", field_id="field1",
                field_type=FieldTypes.PLAIN_TEXT.value,
                field_values=None
            ),
            FieldDTOFactory(
                gof_id="gof2", field_id="field2",
                field_type=FieldTypes.DROPDOWN.value,
                field_values="['Mr', 'Mrs', 'Ms']"
            ),
            FieldDTOFactory(
                gof_id="gof2", field_id="field3",
                field_type=FieldTypes.GOF_SELECTOR.value,
                field_values=field_values
            )

        ]

        # Act
        storage.create_fields(field_dtos)

        # Assert
        self._assert_fileds(field_dtos)

    def test_update_fields_given_field_dtos(
            self, storage
    ):
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
            assert field_obj.tooltip == field_dto.tooltip
            assert field_obj.placeholder_text == field_dto.placeholder_text
            assert field_obj.error_messages == field_dto.error_message
            assert field_obj.validation_regex == field_dto.validation_regex

    def test_create_field_roles_given_field_roles_dtos(
            self, storage
    ):
        # Arrange
        from ib_tasks.tests.factories.storage_dtos import FieldRoleDTOFactory
        from ib_tasks.constants.enum import PermissionTypes

        FieldFactory(field_id="field1")
        FieldFactory(field_id="field2")
        field_role_dtos = [
            FieldRoleDTOFactory(field_id="field1"),
            FieldRoleDTOFactory(
                field_id="field2",
                permission_type=PermissionTypes.WRITE.value
            )
        ]

        # Act
        storage.create_fields_roles(field_role_dtos)

        # Assert
        from ib_tasks.models.field_role import FieldRole
        for field_role_dto in field_role_dtos:
            field_role_obj = FieldRole.objects.get(
                field_id=field_role_dto.field_id,
                role=field_role_dto.role
            )
            assert field_role_dto.permission_type == field_role_obj.permission_type

    def test_get_existing_gof_ids_given_gof_ids(self, gof_storage):
        # Arrange
        gof_ids = ["gof0", "gof1", "gof2"]
        GoFFactory(gof_id="gof0")
        GoFFactory(gof_id="gof1")
        expected_existing_gof_ids = ["gof0", "gof1"]

        # Act
        actual_existing_gof_ids = gof_storage.get_existing_gof_ids(gof_ids)

        # Assert

        assert expected_existing_gof_ids == actual_existing_gof_ids

    def test_delete_field_roles_given_field_ids(self, storage):
        # Arrange
        field_roles = FieldRoleFactory.create_batch(size=2)
        field_ids = [field_role.field_id for field_role in field_roles]

        # Act
        storage.delete_field_roles(field_ids)

        # Assert
        field_roles = list(FieldRole.objects.filter(field_id__in=field_ids))
        assert field_roles == []
