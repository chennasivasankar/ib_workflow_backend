import pytest
from ib_tasks.tests.factories.storage_dtos \
    import FieldRolesDTOFactory
from ib_tasks.interactors.fields_roles_validations_interactor \
    import FieldsRolesValidationsInteractor


class TestFieldsRolesValidationsInteractor:

    def test_given_empty_values_for_read_permissions_roles_raise_exception(
            self
    ):
        # Arrange
        from ib_tasks.constants.exception_messages \
            import EMPTY_VALUE_FOR_READ_PERMISSIONS
        from ib_tasks.exceptions.fields_custom_exceptions \
            import EmptyValueForPermissions

        field_ids_with_read_permissions_empty = ["field1", "field2"]

        exception_message = EMPTY_VALUE_FOR_READ_PERMISSIONS.format(
            field_ids_with_read_permissions_empty
        )

        field_roles_dtos = [
            FieldRolesDTOFactory(
                field_id="field1",
                read_permission_roles=[]
            ),
            FieldRolesDTOFactory(
                field_id="field2",
                read_permission_roles=[]
            ),
            FieldRolesDTOFactory(field_id="field3")
        ]

        interactor = FieldsRolesValidationsInteractor()

        # Act
        with pytest.raises(EmptyValueForPermissions) as err:
            interactor.fields_roles_validations(
                field_roles_dtos=field_roles_dtos
            )

        # Assert
        assert str(err.value) == exception_message

    def test_given_empty_values_for_write_permissions_roles_raise_exception(
            self
    ):
        # Arrange
        from ib_tasks.constants.exception_messages \
            import EMPTY_VALUE_FOR_WRITE_PERMISSIONS
        from ib_tasks.exceptions.fields_custom_exceptions \
            import EmptyValueForPermissions

        field_ids_with_write_permissions_empty = ["field1", "field2"]

        exception_message = EMPTY_VALUE_FOR_WRITE_PERMISSIONS.format(
            field_ids_with_write_permissions_empty
        )

        field_roles_dtos = [
            FieldRolesDTOFactory(
                field_id="field1",
                write_permission_roles=[]
            ),
            FieldRolesDTOFactory(
                field_id="field2",
                write_permission_roles=[]
            ),
            FieldRolesDTOFactory(field_id="filed3")
        ]

        interactor = FieldsRolesValidationsInteractor()

        # Act
        with pytest.raises(EmptyValueForPermissions) as err:
            interactor.fields_roles_validations(
                field_roles_dtos=field_roles_dtos
            )

        # Assert
        assert str(err.value) == exception_message

    def test_given_duplication_of_values_for_read_permissions_roles_raise_exception(
            self
    ):
        # Arrange
        from ib_tasks.constants.exception_messages \
            import DUPLICATED_VALUES_FOR_READ_PERMISSIONS
        from ib_tasks.exceptions.fields_custom_exceptions \
            import DuplicationOfPermissionRoles

        duplication_of_read_permission_roles = [
            {
                "field_id": "field1",
                "duplication_values_for_read_permissions": ["User"]
            },
            {
                "field_id": "field2",
                "duplication_values_for_read_permissions": ["Admin"]
            }
        ]

        field_roles_dtos = [
            FieldRolesDTOFactory(
                field_id="field1",
                read_permission_roles=["User", "Admin", "User"]
            ),
            FieldRolesDTOFactory(
                field_id="field2",
                read_permission_roles=["Admin", "User", "Admin"]
            ),
            FieldRolesDTOFactory(field_id="field3")
        ]
        exception_message = DUPLICATED_VALUES_FOR_READ_PERMISSIONS.format(
            duplication_of_read_permission_roles
        )

        interactor = FieldsRolesValidationsInteractor()

        # Act
        with pytest.raises(DuplicationOfPermissionRoles) as err:
            interactor.fields_roles_validations(
                field_roles_dtos=field_roles_dtos
            )

        # Assert
        assert str(err.value) == exception_message

    def test_given_duplication_of_values_for_write_permissions_roles_raise_exception(
            self
    ):
        # Arrange
        from ib_tasks.constants.exception_messages \
            import DUPLICATED_VALUES_FOR_WRITE_PERMISSIONS
        from ib_tasks.exceptions.fields_custom_exceptions \
            import DuplicationOfPermissionRoles

        duplication_of_write_permission_roles = [
            {
                "field_id": "field1",
                "duplication_values_for_write_permissions": ["User"]
            },
            {
                "field_id": "field2",
                "duplication_values_for_write_permissions": ["Admin"]
            }
        ]

        field_roles_dtos = [
            FieldRolesDTOFactory(
                field_id="field1",
                write_permission_roles=["User", "Admin", "User"]
            ),
            FieldRolesDTOFactory(
                field_id="field2",
                write_permission_roles=["Admin", "User", "Admin"]
            ),
            FieldRolesDTOFactory(field_id="field3")
        ]
        exception_message = DUPLICATED_VALUES_FOR_WRITE_PERMISSIONS.format(
            duplication_of_write_permission_roles
        )

        interactor = FieldsRolesValidationsInteractor()

        # Act
        with pytest.raises(DuplicationOfPermissionRoles) as err:
            interactor.fields_roles_validations(
                field_roles_dtos=field_roles_dtos
            )

        # Assert
        assert str(err.value) == exception_message

    def test_given_invalid_roles_for_read_permissions_raise_exception(
            self, mocker
    ):
        # Arrange
        from ib_tasks.exceptions.fields_custom_exceptions \
            import InvalidFieldRolesException
        from ib_tasks.tests.common_fixtures.adapters.roles_service import \
            get_valid_role_ids_in_given_role_ids
        get_valid_role_ids_mock_method = \
            get_valid_role_ids_in_given_role_ids(mocker)

        FieldRolesDTOFactory.reset_sequence(1)
        field_roles_dtos = [
            FieldRolesDTOFactory(
                read_permission_roles=[
                    "FIN_PAYMENT_POC", "User", "Vendor", "FIN_PAYMENT_REQUESTER"
                ]
            ),
            FieldRolesDTOFactory(
                read_permission_roles=[
                    "FIN_PAYMENT_REQUESTER",
                    "admin",
                ]
            )
        ]
        fields_invalid_roles_for_read_permission = [
            {
                "field_id": "field1",
                "invalid_roles": ["User", "Vendor"],
                "permissions": "read_permissions",
            },
            {
                "field_id": "field2",
                "permissions": "read_permissions",
                "invalid_roles": ["admin"]
            }
        ]

        interactor = FieldsRolesValidationsInteractor()

        # Act
        with pytest.raises(InvalidFieldRolesException) as err:
            interactor.fields_roles_validations(field_roles_dtos=field_roles_dtos)

        # Assert
        exception_object = err.value
        assert exception_object.roles == fields_invalid_roles_for_read_permission
        get_valid_role_ids_mock_method.assert_called_once()

    def test_given_invalid_roles_for_write_permissions_raise_exception(
            self, mocker
    ):
        # Arrange
        FieldRolesDTOFactory.reset_sequence(1)
        from ib_tasks.exceptions.fields_custom_exceptions \
            import InvalidFieldRolesException
        from ib_tasks.tests.common_fixtures.adapters.roles_service \
            import get_valid_role_ids_in_given_role_ids
        get_valid_role_ids_mock_method = get_valid_role_ids_in_given_role_ids(mocker)

        field_roles_dtos = [
            FieldRolesDTOFactory(
                read_permission_roles=[
                    "FIN_PAYMENT_POC", "FIN_PAYMENT_REQUESTER"
                ],
                write_permission_roles=[
                    "FIN_PAYMENT_POC", "User", "Vendor", "FIN_PAYMENTS_LEVEL1_VERIFIER"
                ]
            ),
            FieldRolesDTOFactory(
                read_permission_roles=[
                    "FIN_PAYMENT_POC"
                ],
                write_permission_roles=[
                    "FIN_PAYMENT_POC",
                    "admin",
                ]
            )
        ]
        fields_invalid_roles_for_write_permission = [
            {
                "field_id": "field1",
                "invalid_roles": ["User", "Vendor", "FIN_PAYMENTS_LEVEL1_VERIFIER"],
                "permissions": "write_permissions",
            },
            {
                "field_id": "field2",
                "permissions": "write_permissions",
                "invalid_roles": ["admin"]
            }
        ]
        interactor = FieldsRolesValidationsInteractor()

        # Act
        with pytest.raises(InvalidFieldRolesException) as err:
            interactor.fields_roles_validations(field_roles_dtos=field_roles_dtos)

        # Assert
        exception_object = err.value
        assert exception_object.roles == fields_invalid_roles_for_write_permission
        get_valid_role_ids_mock_method.assert_called_once()
