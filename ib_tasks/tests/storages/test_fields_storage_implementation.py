import factory
import pytest

from ib_tasks.constants.constants import ALL_ROLES_ID
from ib_tasks.constants.enum import PermissionTypes
from ib_tasks.interactors.storage_interfaces.task_dtos import TaskProjectRolesDTO
from ib_tasks.tests.factories.models import FieldFactory, FieldRoleFactory, TaskGoFFieldFactory
from ib_tasks.tests.factories.storage_dtos import \
    FieldCompleteDetailsDTOFactory


@pytest.mark.django_db
class TestFieldsStorageImplementation:

    @pytest.fixture
    def storage(self):
        from ib_tasks.storages.fields_storage_implementation import \
            FieldsStorageImplementation
        return FieldsStorageImplementation()

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        from ib_tasks.tests.factories.models import GoFFactory, FieldFactory
        GoFFactory.reset_sequence()
        FieldFactory.reset_sequence(1)

    def test_get_fields_of_gofs_in_dtos(self, storage):
        from ib_tasks.tests.factories.models import GoFFactory, FieldFactory
        from ib_tasks.interactors.storage_interfaces.fields_dtos \
            import FieldDTO
        from ib_tasks.constants.enum import FieldTypes
        expected_gof_ids = ['gof_1', 'gof_2']
        expected_field_dtos = [FieldDTO(gof_id='gof_1', field_id='FIELD_ID-1',
                                        field_display_name='DISPLAY_NAME-1',
                                        field_type=FieldTypes.PLAIN_TEXT.value,
                                        field_values=None, required=True,
                                        help_text=None, tooltip=None,
                                        placeholder_text=None,
                                        error_message=None,
                                        allowed_formats=None,
                                        validation_regex=None,
                                        order=1),
                               FieldDTO(gof_id='gof_2', field_id='FIELD_ID-2',
                                        field_display_name='DISPLAY_NAME-2',
                                        field_type=FieldTypes.PLAIN_TEXT.value,
                                        field_values=None, required=True,
                                        help_text=None, tooltip=None,
                                        placeholder_text=None,
                                        error_message=None,
                                        allowed_formats=None,
                                        validation_regex=None,
                                        order=2)]

        import factory
        gof_objs = GoFFactory.create_batch(
            size=2, gof_id=factory.Iterator(expected_gof_ids)
        )
        FieldFactory.create_batch(size=2,
                                  gof=factory.Iterator(gof_objs))

        # Act
        result = storage.get_fields_of_gofs_in_dtos(gof_ids=expected_gof_ids)

        # Assert
        assert result == expected_field_dtos

    def test_get_user_field_permission_dtos(self, storage):
        from ib_tasks.tests.factories.models import FieldFactory, \
            FieldRoleFactory
        from ib_tasks.interactors.storage_interfaces.fields_dtos \
            import UserFieldPermissionDTO
        from ib_tasks.constants.enum import PermissionTypes
        expected_field_ids = ['field_1', 'field_2']
        expected_user_field_permission_dtos = [
            UserFieldPermissionDTO(field_id='field_1',
                                   permission_type=PermissionTypes.READ.value)]

        import factory
        field_objs = FieldFactory.create_batch(size=2,
                                               field_id=factory.Iterator(
                                                   expected_field_ids))
        FieldRoleFactory.create_batch(size=2,
                                      field=factory.Iterator(field_objs))

        # Act
        result = storage.get_user_field_permission_dtos(
            field_ids=expected_field_ids, roles=['FIN_PAYMENT_REQUESTER'])

        # Assert
        assert result == expected_user_field_permission_dtos

    def test_get_field_details_for_given_field_ids(self, storage):
        # Arrange
        field_objects = FieldFactory.create_batch(size=2)
        field_ids_list = [field_object.field_id for field_object in
                          field_objects]
        field_types_list = [
            field_object.field_type for field_object in field_objects
        ]
        field_required_list = [
            field_object.required for field_object in field_objects
        ]
        field_values_list = [
            field_object.field_values for field_object in field_objects
        ]
        allowed_formats_list = [
            field_object.allowed_formats for field_object in field_objects
        ]
        validation_regex_list = [
            field_object.validation_regex for field_object in field_objects
        ]
        expected_field_type_dtos = FieldCompleteDetailsDTOFactory.create_batch(
            size=2, field_id=factory.Iterator(field_ids_list),
            field_type=factory.Iterator(field_types_list),
            required=factory.Iterator(field_required_list),
            field_values=factory.Iterator(field_values_list),
            allowed_formats=factory.Iterator(allowed_formats_list),
            validation_regex=factory.Iterator(validation_regex_list)
        )

        # Act
        actual_field_type_dtos = storage.get_field_details_for_given_field_ids(
            field_ids=field_ids_list
        )

        # Assert
        assert expected_field_type_dtos == actual_field_type_dtos

    def test_get_field_ids_having_read_permission_for_user(self, storage):
        # Arrange
        user_roles = ["FIN_MAN"]
        fields = FieldFactory.create_batch(size=2)
        FieldRoleFactory.create_batch(
            size=2, permission_type=PermissionTypes.READ.value,
            role=factory.Iterator(user_roles),
            field=factory.Iterator(fields)
        )
        field_ids = [field.field_id for field in fields]

        # Act
        field_ids_having_read_permission_for_user = \
            storage.get_field_ids_having_read_permission_for_user(
                field_ids=field_ids, user_roles=user_roles)

        # Assert
        assert field_ids_having_read_permission_for_user == field_ids

    def test_get_field_ids_having_permission_for_user_projects(self, storage):
        # Arrange
        user_roles = [TaskProjectRolesDTO(
            task_id=1,
            project_id="project_id_1",
            roles=["FIN_MAN"]),
            TaskProjectRolesDTO(
                task_id=1,
                project_id="project_id_1",
                roles=["FIN_MAN"])]
        fields = FieldFactory.create_batch(size=2)
        FieldRoleFactory.create_batch(
            size=2, permission_type=PermissionTypes.READ.value,
            role=factory.Iterator(user_roles),
            field=factory.Iterator(fields)
        )
        TaskGoFFieldFactory.create_batch()

        field_ids = [field.field_id for field in fields]

        # Act
        field_ids_having_read_permission_for_user = \
            storage.get_field_ids_permissions_for_user_in_projects(
                field_ids=field_ids, task_project_roles=user_roles)

        # Assert
        assert field_ids_having_read_permission_for_user == field_ids

    def test_get_field_ids_having_read_permission_for_user_when_fields_has_all_roles(
            self, storage):
        # Arrange
        user_roles = ["FIN_MAN"]
        fields = FieldFactory.create_batch(size=2)
        FieldRoleFactory.create_batch(
            size=2, permission_type=factory.Iterator(
                [PermissionTypes.WRITE.value, PermissionTypes.READ.value]),
            role=factory.Iterator([ALL_ROLES_ID]),
            field=factory.Iterator(fields)
        )
        field_ids = [field.field_id for field in fields]

        # Act
        field_ids_having_read_permission_for_user = \
            storage.get_field_ids_having_read_permission_for_user(
                field_ids=field_ids, user_roles=user_roles)

        # Assert
        assert field_ids_having_read_permission_for_user == field_ids

    def test_get_field_ids_having_write_permission_for_user(self, storage):
        # Arrange
        user_roles = ["FIN_MAN"]
        fields = FieldFactory.create_batch(size=2)
        FieldRoleFactory.create_batch(
            size=2, permission_type=PermissionTypes.WRITE.value,
            role=factory.Iterator(user_roles),
            field=factory.Iterator(fields)
        )
        field_ids = [field.field_id for field in fields]

        # Act
        field_ids_having_write_permission_for_user = \
            storage.get_field_ids_having_write_permission_for_user(
                field_ids=field_ids, user_roles=user_roles)

        # Assert
        assert field_ids_having_write_permission_for_user == field_ids

    def test_get_field_ids_having_write_permission_for_user_when_field_has_all_roles(
            self, storage):
        # Arrange
        user_roles = ["FIN_MAN"]
        fields = FieldFactory.create_batch(size=2)
        FieldRoleFactory.create_batch(
            size=2, permission_type=PermissionTypes.WRITE.value,
            role=factory.Iterator([ALL_ROLES_ID]),
            field=factory.Iterator(fields)
        )
        field_ids = [field.field_id for field in fields]

        # Act
        field_ids_having_write_permission_for_user = \
            storage.get_field_ids_having_write_permission_for_user(
                field_ids=field_ids, user_roles=user_roles)

        # Assert
        assert field_ids_having_write_permission_for_user == field_ids

    def test_check_is_user_has_write_permission_for_field_with_invalid_role_returns_false(
            self, storage):
        # Arrange
        user_roles = ["FIN_MAN"]
        field = FieldFactory.create()
        FieldRoleFactory.create(
            permission_type=PermissionTypes.WRITE.value,
            role=factory.Iterator(["RP_VALIDATIONS"]), field=field
        )
        field_id = field.field_id

        # Act
        is_user_has_read_permission_for_field = \
            storage.check_is_user_has_write_permission_for_field(
                field_id=field_id, user_roles=user_roles)

        # Assert
        assert is_user_has_read_permission_for_field is False

    def test_check_is_user_has_write_permission_for_field_with_valid_role_returns_true(
            self, storage):
        # Arrange
        user_roles = ["FIN_MAN"]
        field = FieldFactory.create()
        FieldRoleFactory.create(
            permission_type=PermissionTypes.WRITE.value,
            role=factory.Iterator(user_roles), field=field
        )
        field_id = field.field_id

        # Act
        is_user_has_read_permission_for_field = \
            storage.check_is_user_has_write_permission_for_field(
                field_id=field_id, user_roles=user_roles)

        # Assert
        assert is_user_has_read_permission_for_field is True

    def test_check_is_user_has_write_permission_for_field_with_all_roles_returns_true(
            self, storage):
        # Arrange
        user_roles = ["FIN_MAN"]
        field = FieldFactory.create()
        FieldRoleFactory.create(
            permission_type=PermissionTypes.WRITE.value,
            role=factory.Iterator([ALL_ROLES_ID]), field=field
        )
        field_id = field.field_id

        # Act
        is_user_has_read_permission_for_field = \
            storage.check_is_user_has_write_permission_for_field(
                field_id=field_id, user_roles=user_roles)

        # Assert
        assert is_user_has_read_permission_for_field is True

    def test_get_field_ids_for_given_gofs_when_exists_return_field_ids(
            self, storage):
        # Arrange
        fields = FieldFactory.create_batch(size=2)
        expected_field_ids = [field.field_id for field in fields]
        gof_ids = [field.gof_id for field in fields]

        # Act
        field_ids = storage.get_field_ids_for_given_gofs(gof_ids=gof_ids)

        # Assert
        assert field_ids == expected_field_ids

    def test_get_field_ids_for_given_gofs_when_not_exists_return_empty_list(
            self, storage):
        # Arrange
        expected_field_ids = []
        gof_ids = ["gof_1"]

        # Act
        field_ids = storage.get_field_ids_for_given_gofs(gof_ids=gof_ids)

        # Assert
        assert field_ids == expected_field_ids

    def test_get_field_dtos_when_exists_returns_field_dtos(self, storage):
        # Arrange
        from ib_tasks.interactors.storage_interfaces.fields_dtos import \
            FieldDTO
        from ib_tasks.constants.enum import FieldTypes
        fields = FieldFactory.create_batch(size=2)
        field_ids = [field.field_id for field in fields]
        expected_field_dtos = [
            FieldDTO(
                gof_id='gof_1', field_id='FIELD_ID-1',
                field_display_name='DISPLAY_NAME-1',
                field_type=FieldTypes.PLAIN_TEXT.value,
                field_values=None, required=True,
                help_text=None, tooltip=None, placeholder_text=None,
                error_message=None, allowed_formats=None,
                validation_regex=None, order=1
            ),
            FieldDTO(
                gof_id='gof_2', field_id='FIELD_ID-2',
                field_display_name='DISPLAY_NAME-2',
                field_type=FieldTypes.PLAIN_TEXT.value,
                field_values=None, required=True, help_text=None, tooltip=None,
                placeholder_text=None, error_message=None,
                allowed_formats=None, validation_regex=None, order=2
            )]

        # Act
        field_dtos = storage.get_field_dtos(field_ids=field_ids)

        # Assert
        assert field_dtos == expected_field_dtos

    def test_get_field_dtos_when_not_exists_returns_empty_list(self, storage):
        # Arrange
        field_ids = ["field_1"]
        expected_field_dtos = []

        # Act
        field_dtos = storage.get_field_dtos(field_ids=field_ids)

        # Assert
        assert field_dtos == expected_field_dtos
