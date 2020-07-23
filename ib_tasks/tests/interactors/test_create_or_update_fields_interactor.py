import pytest

from ib_tasks.constants.enum import PermissionTypes, FieldTypes

from ib_tasks.interactors.create_or_update_fields_interactor \
    import CreateOrUpdateFieldsInteractor
from ib_tasks.tests.factories.storage_dtos import \
    FieldDTOFactory, FieldRolesDTOFactory, FieldRoleDTOFactory

from ib_tasks.tests.common_fixtures.adapters.roles_service \
        import get_valid_role_ids_in_given_role_ids


class TestCreateOrUpdateFieldsInteractor:

    @pytest.fixture
    def storage_mock(self):
        from ib_tasks.interactors.storage_interfaces.task_storage_interface \
            import TaskStorageInterface
        from unittest.mock import create_autospec
        storage = create_autospec(TaskStorageInterface)
        return storage

    @pytest.fixture
    def reset_sequence(self):
        FieldDTOFactory.reset_sequence(1)
        FieldRolesDTOFactory.reset_sequence(1)

    def test_given_new_field_ids_populate_fields(
            self, storage_mock, mocker, reset_sequence
    ):
        # Arrange

        field_roles_dtos = [
            FieldRolesDTOFactory(
                read_permission_roles=["FIN_PAYMENT_REQUESTER", "FIN_PAYMENT_POC"],
                write_permission_roles=["FIN_PAYMENT_REQUESTER", "FIN_PAYMENT_POC"]
            )
        ]
        field_role_dtos = [
            FieldRoleDTOFactory(
                field_id="field1",
                role="FIN_PAYMENT_REQUESTER",
                permission_type=PermissionTypes.READ.value
            ),
            FieldRoleDTOFactory(
                field_id="field1",
                role="FIN_PAYMENT_POC",
                permission_type=PermissionTypes.READ.value
            ),
            FieldRoleDTOFactory(
                field_id="field1",
                role="FIN_PAYMENT_REQUESTER",
                permission_type=PermissionTypes.WRITE.value
            ),
            FieldRoleDTOFactory(
                field_id="field1",
                role="FIN_PAYMENT_POC",
                permission_type=PermissionTypes.WRITE.value
            ),
        ]
        get_valid_role_ids_mock_method = get_valid_role_ids_in_given_role_ids(mocker)

        FieldDTOFactory.reset_sequence(1)
        field_dtos = [
            FieldDTOFactory()
        ]
        existing_field_ids = []
        interactor = CreateOrUpdateFieldsInteractor(storage=storage_mock)
        storage_mock.get_existing_field_ids.return_value = existing_field_ids
        existing_gof_ids = ["FIN_VENDOR_BASIC_DETAILS"]
        storage_mock.get_existing_gof_ids.return_value = existing_gof_ids

        # Act
        interactor.create_or_update_fields(
            field_dtos=field_dtos, field_roles_dtos=field_roles_dtos
        )

        # Assert
        storage_mock.create_fields.assert_called_once_with(field_dtos)
        storage_mock.create_fields_roles.assert_called_once_with(field_role_dtos)
        get_valid_role_ids_mock_method.assert_called_once()

    def test_given_field_ids_already_exist_in_database_then_update_fields(
            self, storage_mock, mocker, reset_sequence
    ):
        # Arrange
        field_roles_dtos = [
            FieldRolesDTOFactory(field_id="FIN_FIRST NAME"),
        ]
        field_dtos = [
            FieldDTOFactory(field_id="FIN_FIRST NAME")
        ]
        get_valid_role_ids_mock_method = get_valid_role_ids_in_given_role_ids(mocker)

        existing_field_ids = ["FIN_FIRST NAME"]
        interactor = CreateOrUpdateFieldsInteractor(storage=storage_mock)
        storage_mock.get_existing_field_ids.return_value = existing_field_ids
        existing_gof_ids = ["FIN_VENDOR_BASIC_DETAILS"]
        storage_mock.get_existing_gof_ids.return_value = existing_gof_ids


        # Act
        interactor.create_or_update_fields(
            field_dtos=field_dtos, field_roles_dtos=field_roles_dtos
        )

        # Assert
        storage_mock.update_fields.assert_called_once_with(field_dtos)
        storage_mock.delete_field_roles.assert_called_once_with(existing_field_ids)
        get_valid_role_ids_mock_method.assert_called_once()

    def test_new_and_already_existing_field_ids_in_database_are_given_then_create_and_update_fields(
            self, storage_mock, mocker, reset_sequence
    ):
        # Arrange
        field_dtos = [
            FieldDTOFactory(field_id="field1"),
            FieldDTOFactory(field_id="FIN_SALUATION")
        ]
        field_roles_dtos = [
            FieldRolesDTOFactory(field_id="field1"),
            FieldRolesDTOFactory(field_id="FIN_SALUATION")
        ]
        existing_field_ids = ["field1"]
        new_field_dtos = [
            FieldDTOFactory(
                field_id="FIN_SALUATION",
                field_values='["Mr", "Mrs", "Ms"]'
            )
        ]
        existing_field_dtos = [
            FieldDTOFactory(
                field_id="field1",
                field_values='["Mr", "Mrs", "Ms"]'
            )
        ]

        field_role_dtos = [
            FieldRoleDTOFactory(
                field_id="field1",
                role="FIN_PAYMENT_REQUESTER",
                permission_type=PermissionTypes.READ.value
            ),
            FieldRoleDTOFactory(
                field_id="field1",
                role="FIN_PAYMENT_POC",
                permission_type=PermissionTypes.READ.value
            ),
            FieldRoleDTOFactory(
                field_id="field1",
                role="FIN_PAYMENT_REQUESTER",
                permission_type=PermissionTypes.WRITE.value
            ),
            FieldRoleDTOFactory(
                field_id="field1",
                role="FIN_PAYMENT_POC",
                permission_type=PermissionTypes.WRITE.value
            ),
            FieldRoleDTOFactory(
                field_id="FIN_SALUATION",
                role="FIN_PAYMENT_REQUESTER",
                permission_type=PermissionTypes.READ.value
            ),
            FieldRoleDTOFactory(
                field_id="FIN_SALUATION",
                role="FIN_PAYMENT_POC",
                permission_type=PermissionTypes.READ.value
            ),
            FieldRoleDTOFactory(
                field_id="FIN_SALUATION",
                role="FIN_PAYMENT_REQUESTER",
                permission_type=PermissionTypes.WRITE.value
            ),
            FieldRoleDTOFactory(
                field_id="FIN_SALUATION",
                role="FIN_PAYMENT_POC",
                permission_type=PermissionTypes.WRITE.value
            )
        ]

        get_valid_role_ids_mock_method = get_valid_role_ids_in_given_role_ids(mocker)

        storage_mock.get_existing_field_ids.return_value = existing_field_ids
        interactor = CreateOrUpdateFieldsInteractor(storage=storage_mock)
        existing_gof_ids = ["FIN_VENDOR_BASIC_DETAILS"]
        storage_mock.get_existing_gof_ids.return_value = existing_gof_ids

        # Act
        interactor.create_or_update_fields(
            field_dtos=field_dtos, field_roles_dtos=field_roles_dtos
        )

        # Assert
        get_valid_role_ids_mock_method.assert_called_once()
        storage_mock.create_fields.assert_called_once_with(new_field_dtos)
        storage_mock.delete_field_roles.assert_called_once_with(existing_field_ids)
        storage_mock.update_fields.assert_called_once_with(existing_field_dtos)
        storage_mock.create_fields_roles.assert_called_once_with(field_role_dtos)
