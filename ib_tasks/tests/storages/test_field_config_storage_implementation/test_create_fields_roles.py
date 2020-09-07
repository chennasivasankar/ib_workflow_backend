import pytest

from ib_tasks.constants.enum import PermissionTypes
from ib_tasks.tests.factories.models import FieldFactory
from ib_tasks.tests.factories.storage_dtos import FieldRoleDTOFactory


@pytest.mark.django_db
class TestCreateFieldRoles:

    def test_create_field_roles_given_field_roles_dtos(
            self, storage
    ):
        # Arrange

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
            assert field_role_dto.permission_type == \
                   field_role_obj.permission_type
