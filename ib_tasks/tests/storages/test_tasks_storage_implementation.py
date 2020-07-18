import factory
import pytest
from typing import List

from ib_tasks.models.gof_role import GoFRole
from ib_tasks.tests.factories.models import (
    GoFFactory, TaskTemplateFactory,
    FieldFactory, FieldRoleFactory
)
from ib_tasks.tests.factories.storage_dtos \
    import GoFRoleDTOFactory, FieldDTOFactory
from ib_tasks.constants.enum import FieldTypes
from ib_tasks.models.field import Field


@pytest.mark.django_db
class TestTasksStorageImplementation:

    @pytest.fixture
    def storage(self):
        from ib_tasks.storages.tasks_storage_implementation import \
            TasksStorageImplementation
        return TasksStorageImplementation()

    @pytest.fixture
    def reset_factories(self):
        FieldFactory.reset_sequence(0)
        GoFFactory.reset_sequence(0)

    def test_get_existing_gof_ids_in_given_gof_ids(self, storage, reset_factories):
        # Arrange
        GoFFactory.create_batch(size=2)

        gof_ids = ["gof0", "gof1"]
        expected_existing_gof_ids = ["gof0", "gof1"]

        # Act
        actual_existing_gof_ids = \
            storage.get_existing_gof_ids_in_given_gof_ids(
                gof_ids=gof_ids
            )

        # Assert
        assert expected_existing_gof_ids == actual_existing_gof_ids

    def test_create_gofs(self, storage):
        # Arrange
        from ib_tasks.models.gof import GoF
        from ib_tasks.tests.factories.storage_dtos import GoFDTOFactory
        task_templates = TaskTemplateFactory.create_batch(size=2)

        gof_dtos = [
            GoFDTOFactory(task_template_id=task_templates[0].pk),
            GoFDTOFactory(task_template_id=task_templates[0].pk)
        ]

        # Act
        storage.create_gofs(gof_dtos=gof_dtos)

        # Assert
        for gof_dto in gof_dtos:
            gof = GoF.objects.get(pk=gof_dto.gof_id)
            assert gof.display_name == gof_dto.gof_display_name
            assert gof.order == gof_dto.order
            assert gof.max_columns == gof_dto.max_columns
            assert gof.task_template_id == gof_dto.task_template_id

    def test_create_gof_roles(self, storage):

        # Arrange
        gof_role_dtos = [
            GoFRoleDTOFactory(), GoFRoleDTOFactory()
        ]
        gof_ids = [
            gof_role_dto.gof_id
            for gof_role_dto in gof_role_dtos
        ]
        GoFFactory.create_batch(size=2, gof_id=factory.Iterator(gof_ids))

        # Act
        storage.create_gof_roles(gof_role_dtos=gof_role_dtos)

        # Assert
        for gof_role_dto in gof_role_dtos:
            gof_role = GoFRole.objects.get(
                gof_id=gof_role_dto.gof_id, role=gof_role_dto.role
            )
            assert gof_role_dto.permission_type == gof_role.permission_type


    def test_update_gofs(self, storage):

        # Arrange
        from ib_tasks.models.gof import GoF
        from ib_tasks.tests.factories.storage_dtos import GoFDTOFactory
        from ib_tasks.tests.factories.models import GoFFactory

        pr_task_template = TaskTemplateFactory.create(
            template_id="FIN_PR", name="Payment Request"
        )
        vendor_task_template = TaskTemplateFactory.create(
            template_id="FIN_VENDOR", name="Vendor"
        )
        gofs = [
            GoFFactory(
                display_name="Request Details",
                task_template=vendor_task_template,
                order=1,
                max_columns=3
            ),
            GoFFactory(
                display_name="Vendor Type",
                task_template=pr_task_template,
                order=2,
                max_columns=4
            )
        ]

        gof_dtos = [
            GoFDTOFactory(
                gof_id=gofs[0].gof_id,
                gof_display_name="details of request",
                task_template_id=pr_task_template.template_id,
                order=10,
                max_columns=12
            ),
            GoFDTOFactory(
                gof_id=gofs[1].gof_id,
                gof_display_name="details of vendor",
                task_template_id=vendor_task_template.template_id,
                order=10,
                max_columns=12
            )
        ]

        # Act
        storage.update_gofs(gof_dtos=gof_dtos)

        # Assert
        for gof_dto in gof_dtos:
            gof = GoF.objects.get(pk=gof_dto.gof_id)
            assert gof.display_name == gof_dto.gof_display_name
            assert gof.order == gof_dto.order
            assert gof.max_columns == gof_dto.max_columns
            assert gof.task_template_id == gof_dto.task_template_id

    def test_get_existing_field_ids_in_given_field_ids(
            self, storage, reset_factories
    ):
        # Arrange
        field_ids = ["field0", "field1", "field2"]
        FieldFactory(field_id="field0")
        FieldFactory(field_id="field1")
        expected_existing_field_ids = ["field0", "field1"]

        # Act
        actual_existing_field_ids = storage.get_existing_field_ids(field_ids)
        # Assert

        assert expected_existing_field_ids == actual_existing_field_ids


    def test_create_fields_given_field_dtos(
            self, storage, reset_factories
    ):
        # Arrange

        GoFFactory(gof_id="gof1")
        GoFFactory(gof_id="gof2")

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
            )
        ]

        # Act
        storage.create_fields(field_dtos)

        # Assert
        self._assert_fileds(field_dtos)

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
            assert field_obj.tooltip == field_dto.tool_tip
            assert field_obj.placeholder_text == field_dto.placeholder_text
            assert field_obj.error_messages == field_dto.error_message
            assert field_obj.validation_regex == field_dto.validation_regex

    def test_create_field_roles_given_field_roles_dtos(self, storage, reset_factories):
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

    def test_get_existing_gof_ids_given_gof_ids(self, storage):
        # Arrange
        gof_ids = ["gof0", "gof1", "gof2"]
        GoFFactory(gof_id="gof0")
        GoFFactory(gof_id="gof1")
        expected_existing_gof_ids = ["gof0", "gof1"]

        # Act
        actual_existing_gof_ids = storage.get_existing_gof_ids(gof_ids)

        # Assert

        assert expected_existing_gof_ids == actual_existing_gof_ids

    def test_update_field_roles_given_field_roles_dtos(self, storage, reset_factories):
        # Arrange
        from ib_tasks.tests.factories.storage_dtos import FieldRoleDTOFactory
        from ib_tasks.constants.enum import PermissionTypes

        FieldFactory(field_id="field10")
        FieldFactory(field_id="field20")
        FieldRoleFactory(field_id="field10", role="FIN_PAYMENT_REQUESTER")
        FieldRoleFactory(field_id="field20", role="FIN_PAYMENT_APPROVER")
        field_role_dtos = [
            FieldRoleDTOFactory(field_id="field10", role="FIN_PAYMENT_REQUESTER"),
            FieldRoleDTOFactory(
                field_id="field20",
                role="FIN_PAYMENT_APPROVER",
                permission_type=PermissionTypes.WRITE.value
            )
        ]

        # Act
        storage.update_fields_roles(field_role_dtos)

        # Assert
        from ib_tasks.models.field_role import FieldRole
        for field_role_dto in field_role_dtos:
            field_role_obj = FieldRole.objects.get(
                field_id=field_role_dto.field_id,
                role=field_role_dto.role
            )
            assert field_role_dto.permission_type == field_role_obj.permission_type

    def test_get_fields_role_dtos_given_field_ids(self, storage, reset_factories):
        # Arrange
        from ib_tasks.tests.factories.storage_dtos import FieldRoleDTOFactory
        from ib_tasks.constants.enum import PermissionTypes
        FieldFactory(field_id="field100")
        FieldFactory(field_id="field200")
        field_ids = ["field100", "field200", "field100"]
        FieldRoleFactory(
            field_id="field100",
            role="FIN_PAYMENT_REQUESTER",
            permission_type=PermissionTypes.READ.value
        )
        FieldRoleFactory(
            field_id="field100",
            role="FIN_PAYMENT_APPROVER",
            permission_type=PermissionTypes.READ.value
        )
        expected_field_role_dtos = [
            FieldRoleDTOFactory(
                field_id="field100",
                role="FIN_PAYMENT_REQUESTER",
                permission_type=PermissionTypes.READ.value
            ),
            FieldRoleDTOFactory(
                field_id="field100",
                role="FIN_PAYMENT_APPROVER",
                permission_type=PermissionTypes.READ.value
            )
        ]

        # Act
        actual_field_role_dtos = storage.get_fields_role_dtos(field_ids)

        # Assert

        assert actual_field_role_dtos == expected_field_role_dtos