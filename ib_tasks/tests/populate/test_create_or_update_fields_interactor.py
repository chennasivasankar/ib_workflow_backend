import pytest
import json

from ib_tasks.tests.factories.models import (
    GoFFactory,
    FieldFactory
)
from ib_tasks.tests.factories.storage_dtos \
    import FieldDTOFactory, FieldRolesDTOFactory, FieldRoleDTOFactory
from ib_tasks.interactors.create_or_update_fields_interactor \
    import CreateOrUpdateFieldsInteractor

from ib_tasks.constants.enum import FieldTypes, PermissionTypes
from ib_tasks.models.field import Field
from ib_tasks.models.field_role import FieldRole



@pytest.mark.django_db
class TestCreateOrUpdateFields:

    @pytest.fixture
    def reset_factories(self):
        FieldFactory.reset_sequence(0)
        GoFFactory.reset_sequence(0)

    @pytest.fixture
    def storage(self):
        from ib_tasks.storages.tasks_storage_implementation \
            import TasksStorageImplementation
        storage = TasksStorageImplementation()
        return storage

    @pytest.fixture
    def reset_field_dto(self):
        FieldDTOFactory.reset_sequence(1)

    @pytest.fixture
    def field_roles_dtos(self):
        field_roles_dtos = [
            FieldRolesDTOFactory(
                field_id="field1",
                read_permission_roles=["User"],
                write_permission_roles=["FIN_FINANCE_RP"]
            ),
            FieldRolesDTOFactory(
                field_id="field2",
                read_permission_roles=["FIN_PAYMENTS_RP"],
                write_permission_roles=["FIN_FINANCE_RP"]
            ),
        ]
        return field_roles_dtos

    @pytest.fixture
    def field_dtos(self):
        GoFFactory(gof_id="gof1")
        field_dtos = [
            FieldDTOFactory(gof_id="gof1", field_id="field1"),
            FieldDTOFactory(gof_id="gof1", field_id="field2")
        ]
        return field_dtos

    @pytest.fixture
    def valid_field_roles_dtos(self):
        field_roles_dtos = [
            FieldRolesDTOFactory(
                field_id="field1",
                read_permission_roles=["FIN_PAYMENTS_RP"],
                write_permission_roles=["FIN_FINANCE_RP"]
            ),
            FieldRolesDTOFactory(
                field_id="field2",
                read_permission_roles=["FIN_PAYMENTS_RP"],
                write_permission_roles=["FIN_FINANCE_RP"]
            ),
        ]
        return field_roles_dtos

    @pytest.fixture
    def populate_gofs(self):
        GoFFactory(gof_id="FIN_VENDOR_BASIC_DETAILS")


    def test_given_field_ids_empty_raise_exception(
            self, storage, field_roles_dtos, snapshot
    ):
        # Arrange
        field_dtos = [FieldDTOFactory(), FieldDTOFactory(field_id=" ")]
        from ib_tasks.exceptions.fields_custom_exceptions import FieldIdEmptyValueException
        interactor = CreateOrUpdateFieldsInteractor(storage=storage)

        # Act
        with pytest.raises(FieldIdEmptyValueException) as err:
            interactor.create_or_update_fields(
                field_dtos=field_dtos, field_roles_dtos=field_roles_dtos
            )

        # Arrange
        snapshot.assert_match(name="exception_message = ", value=str(err.value))

    def test_given_duplication_of_filed_ids_raise_exception(
            self, storage, field_roles_dtos, snapshot
    ):
        # Arrange
        from ib_tasks.exceptions.fields_custom_exceptions \
            import DuplicationOfFieldIdsExist

        field_dtos = [
            FieldDTOFactory(), FieldDTOFactory(),
            FieldDTOFactory(field_id="FIN_SALUATION"),
            FieldDTOFactory(field_id="FIN_SALUATION")
        ]

        duplication_of_field_ids = ["FIN_SALUATION"]
        interactor = CreateOrUpdateFieldsInteractor(storage=storage)

        # Act
        with pytest.raises(DuplicationOfFieldIdsExist) as err:
            interactor.create_or_update_fields(
                field_dtos=field_dtos, field_roles_dtos=field_roles_dtos
            )

        # Assert
        snapshot.assert_match(name="exception_message = ", value=str(err.value))

    def test_given_field_display_name_as_empty_raise_exception(
            self, storage, field_roles_dtos, snapshot
    ):
        # Arrange
        from ib_tasks.exceptions.fields_custom_exceptions \
            import InvalidValueForFieldDisplayName

        field_dtos = [
            FieldDTOFactory(field_id="field1"),
            FieldDTOFactory(field_id="field2", field_display_name=""),
            FieldDTOFactory(field_id="field3", field_display_name=" "),
            FieldDTOFactory(field_id="field4")
        ]
        interactor = CreateOrUpdateFieldsInteractor(storage=storage)

        # Act
        with pytest.raises(InvalidValueForFieldDisplayName) as err:
            interactor.create_or_update_fields(
                field_dtos=field_dtos, field_roles_dtos=field_roles_dtos
            )

        # Assert
        snapshot.assert_match(name="exception_message = ", value=str(err.value))

    def test_given_invalid_field_type_raise_ecxception(
            self, storage, field_roles_dtos, snapshot
    ):
        # Arrange
        from ib_tasks.exceptions.fields_custom_exceptions \
            import InvalidValueForFieldType
        from ib_tasks.constants.enum import FieldTypes

        field_dtos = [
            FieldDTOFactory(field_id="field1", field_type=""),
            FieldDTOFactory(field_id="field2", field_type="Hello"),
            FieldDTOFactory(field_id="field3", field_type=FieldTypes.PLAIN_TEXT.value)
        ]

        interactor = CreateOrUpdateFieldsInteractor(storage=storage)

        # Act
        with pytest.raises(InvalidValueForFieldType) as err:
            interactor.create_or_update_fields(
                field_dtos=field_dtos, field_roles_dtos=field_roles_dtos
            )

        # Arrange
        snapshot.assert_match(name="exception_message = ", value=str(err.value))
        
    def test_given_gof_ids_not_in_database_raise_exception(
            self, storage, field_roles_dtos, snapshot
    ):
        # Arrange
        from ib_tasks.exceptions.fields_custom_exceptions import InvalidGOFIds
        field_dtos = [
            FieldDTOFactory(),
            FieldDTOFactory(gof_id="Hello"),
            FieldDTOFactory(gof_id="")
        ]
        interactor = CreateOrUpdateFieldsInteractor(storage=storage)

        # Act
        with pytest.raises(InvalidGOFIds) as err:
            interactor.create_or_update_fields(
                field_dtos=field_dtos,
                field_roles_dtos=field_roles_dtos
            )

        # Arrange
        snapshot.assert_match(name="exception_message = ", value=str(err.value))

    def test_given_empty_values_for_read_permissions_roles_raise_exception(
            self, storage, field_dtos, snapshot
    ):
        # Arrange
        from ib_tasks.exceptions.fields_custom_exceptions import EmptyValueForPermissions

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

        interactor = CreateOrUpdateFieldsInteractor(storage=storage)

        # Act
        with pytest.raises(EmptyValueForPermissions) as err:
            interactor.create_or_update_fields(
                field_dtos=field_dtos,
                field_roles_dtos=field_roles_dtos
            )

        # Assert
        snapshot.assert_match(name="exception_message = ", value=str(err.value))

    def test_given_empty_values_for_write_permissions_roles_raise_exception(
            self, storage, field_dtos, snapshot
    ):
        # Arrange
        from ib_tasks.exceptions.fields_custom_exceptions import EmptyValueForPermissions

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

        interactor = CreateOrUpdateFieldsInteractor(storage=storage)

        # Act
        with pytest.raises(EmptyValueForPermissions) as err:
            interactor.create_or_update_fields(
                field_dtos=field_dtos,
                field_roles_dtos=field_roles_dtos
            )
        # Assert
        snapshot.assert_match(name="exception_message = ", value=str(err.value))

    def test_given_duplication_of_values_for_read_permissions_roles_raise_exception(
            self, storage, field_dtos, snapshot
    ):
        from ib_tasks.exceptions.fields_custom_exceptions import DuplicationOfPermissionRoles

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
        interactor = CreateOrUpdateFieldsInteractor(storage=storage)

        # Act
        with pytest.raises(DuplicationOfPermissionRoles) as err:
            interactor.create_or_update_fields(
                field_dtos=field_dtos,
                field_roles_dtos=field_roles_dtos
            )
        # Assert
        snapshot.assert_match(name="exception_message = ", value=str(err.value))

    def test_given_duplication_of_values_for_write_permissions_roles_raise_exception(
            self, storage, field_dtos, snapshot
    ):
        # Arrange
        from ib_tasks.exceptions.fields_custom_exceptions\
            import DuplicationOfPermissionRoles

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

        interactor = CreateOrUpdateFieldsInteractor(storage=storage)

        # Act
        with pytest.raises(DuplicationOfPermissionRoles) as err:
            interactor.create_or_update_fields(
                field_dtos=field_dtos,
                field_roles_dtos=field_roles_dtos
            )
        # Assert
        snapshot.assert_match(name="exception_message = ", value=str(err.value))

    def test_given_invalid_roles_for_read_permissions_raise_exception(
            self, mocker, storage, field_dtos, snapshot
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

        interactor = CreateOrUpdateFieldsInteractor(storage=storage)

        # Act
        with pytest.raises(InvalidFieldRolesException) as err:
            interactor.create_or_update_fields(
                field_dtos=field_dtos,
                field_roles_dtos=field_roles_dtos
            )

        # Assert
        exception_object = err.value
        get_valid_role_ids_mock_method.assert_called_once()
        snapshot.assert_match(name="exception_message = ", value=exception_object.roles)

    def test_given_invalid_roles_for_write_permissions_raise_exception(
            self, mocker, storage, field_dtos, snapshot
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
        interactor = CreateOrUpdateFieldsInteractor(storage=storage)

        # Act
        with pytest.raises(InvalidFieldRolesException) as err:
            interactor.create_or_update_fields(
                field_dtos=field_dtos,
                field_roles_dtos=field_roles_dtos
            )

        # Assert
        exception_object = err.value
        get_valid_role_ids_mock_method.assert_called_once()
        snapshot.assert_match(name="exception_message = ", value=exception_object.roles)

    def test_given_empty_values_in_field_values_raise_exceptions(
            self, storage, valid_field_roles_dtos,
            populate_gofs, snapshot
    ):
        # Arrange
        from ib_tasks.exceptions.fields_custom_exceptions import EmptyValuesForFieldValues

        field_dtos = [
            FieldDTOFactory(
                field_id="field1", field_values=["Mr", "  ", "Mrs"]
            )
        ]
        field_id = "field1"
        interactor = CreateOrUpdateFieldsInteractor(storage=storage)

        # Act
        with pytest.raises(EmptyValuesForFieldValues) as err:
            interactor.create_or_update_fields(
                field_dtos=field_dtos,
                field_roles_dtos=valid_field_roles_dtos
            )

        # Assert
        snapshot.assert_match(name="exception_message = ", value=str(err.value))

    def test_given_field_values_is_empty_raise_exceptions(
            self, storage, valid_field_roles_dtos,
            populate_gofs, snapshot
    ):
        # Arrange
        from ib_tasks.exceptions.fields_custom_exceptions import EmptyValuesForFieldValues

        field_dtos = [
            FieldDTOFactory(
                field_id="field1", field_values=[]
            )
        ]
        field_id = "field1"
        interactor = CreateOrUpdateFieldsInteractor(storage=storage)

        # Act
        with pytest.raises(EmptyValuesForFieldValues) as err:
            interactor.create_or_update_fields(
                field_dtos=field_dtos,
                field_roles_dtos=valid_field_roles_dtos
            )

        # Assert
        snapshot.assert_match(name="exception_message = ", value=str(err.value))

    def test_given_duplication_of_field_values_raise_exception(
            self, storage, valid_field_roles_dtos,
            populate_gofs, snapshot
    ):
        # Arrange
        from ib_tasks.exceptions.fields_custom_exceptions \
            import DuplicationOfFieldValuesForFieldTypeMultiValues

        field_dtos = [
            FieldDTOFactory(
                field_id="field1", field_values=["Mr", "Mrs", "Mrs"]
            )
        ]
        duplication_of_field_values = ["Mrs"]
        field_dict = {
            "field_id": "field1",
            "field_type": FieldTypes.DROPDOWN.value,
            "duplication_of_values": duplication_of_field_values
        }
        interactor = CreateOrUpdateFieldsInteractor(storage=storage)

        # Act
        with pytest.raises(DuplicationOfFieldValuesForFieldTypeMultiValues) as err:
            interactor.create_or_update_fields(
                field_dtos=field_dtos,
                field_roles_dtos=valid_field_roles_dtos
            )

        # Assert
        snapshot.assert_match(name="exception_message = ", value=str(err.value))

    def test_given_field_type_gof_selector_and_field_values_as_invalid_json_raise_exception(
            self, storage, reset_field_dto, snapshot,
            valid_field_roles_dtos, populate_gofs
    ):
        # Arrange
        from ib_tasks.exceptions.fields_custom_exceptions import InvalidJsonForFieldValue
        field_values = [
            {
                "name": "Individual",
                "gof_ids": ['GST_DETAILS', "CUSTOMER_DETAILS"]
            },
            {
                "name": "Company",
                "gof_ids": ["GST_DETAILS", "CUSTOMER_DETAILS"]
            }
        ]
        field_dtos = [
            FieldDTOFactory(
                field_id="field1",
                field_type=FieldTypes.GOF_SELECTOR.value,
                field_values=str(field_values)
            )
        ]

        interactor = CreateOrUpdateFieldsInteractor(storage=storage)

        # Act
        with pytest.raises(InvalidJsonForFieldValue) as err:
            interactor.create_or_update_fields(
                field_dtos=field_dtos,
                field_roles_dtos=valid_field_roles_dtos
            )

        # Assert
        snapshot.assert_match(name="exception_message = ", value=str(err.value))
    
    def test_given_gof_names_as_empty_for_field_values_raise_exception(
            self, storage, reset_field_dto, snapshot,
            valid_field_roles_dtos, populate_gofs
    ):
        # Arrange
        from ib_tasks.exceptions.fields_custom_exceptions \
            import EmptyValuesForGoFNames
        field_values = [
            {
                "name": "Individual",
                "gof_ids": ["GST_DETAILS", "CUSTOMER_DETAILS"]
            },
            {
                "name": " ",
                "gof_ids": ["GST_DETAILS", "CUSTOMER_DETAILS"]
            }
        ]
        field_values = json.dumps(field_values)
        field_dtos = [
            FieldDTOFactory(
                field_id="field1",
                field_type=FieldTypes.GOF_SELECTOR.value,
                field_values=field_values
            )
        ]
        field_id = "field1"
        interactor = CreateOrUpdateFieldsInteractor(storage=storage)

        # Act
        with pytest.raises(EmptyValuesForGoFNames) as err:
            interactor.create_or_update_fields(
                field_dtos=field_dtos,
                field_roles_dtos=valid_field_roles_dtos
            )

        # Assert
        snapshot.assert_match(name="exception_message = ", value=str(err.value))

    def test_given_duplication_of_gof_names_for_field_values_raise_exception(
            self, storage, reset_field_dto, snapshot,
            valid_field_roles_dtos, populate_gofs
    ):
        # Arrange
        from ib_tasks.exceptions.fields_custom_exceptions \
            import DuplicationOfGoFNamesForFieldValues
        field_values = [
            {
                "name": "Individual",
                "gof_ids": ["GST_DETAILS", "CUSTOMER_DETAILS"]
            },
            {
                "name": "Company",
                "gof_ids": ["GST_DETAILS", "CUSTOMER_DETAILS"]
            },
            {
                "name": "Individual",
                "gof_ids": ["GST_DETAILS", "CUSTOMER_DETAILS"]
            }
        ]
        field_values = json.dumps(field_values)
        field_dtos = [
            FieldDTOFactory(
                field_id="field1",
                field_type=FieldTypes.GOF_SELECTOR.value,
                field_values=field_values
            )
        ]
        interactor = CreateOrUpdateFieldsInteractor(storage=storage)

        # Act
        with pytest.raises(DuplicationOfGoFNamesForFieldValues) as err:
            interactor.create_or_update_fields(
                field_dtos=field_dtos,
                field_roles_dtos=valid_field_roles_dtos
            )
        print("str(err.value) = ", str(err.value))

        # Assert
        snapshot.assert_match(name="exception_message = ", value=str(err.value))

    def test_given_invalid_gof_ids_for_field_values_raise_exception(
            self, storage, reset_field_dto, snapshot,
            valid_field_roles_dtos, populate_gofs
    ):
        # Arrange
        from ib_tasks.exceptions.fields_custom_exceptions import InvalidGOFIds
        from ib_tasks.constants.exception_messages \
            import INVALID_GOF_IDS_EXCEPTION_MESSAGE
        field_values = [
            {
                "name": "Individual",
                "gof_ids": ["GST_DETAILS", "CUSTOMER_DETAILS"]
            },
            {
                "name": "Company",
                "gof_ids": ["GST_DETAILS", "FIN_VENDOR_BASIC_DETAILS"]
            }
        ]
        field_values = json.dumps(field_values)
        field_dtos = [
            FieldDTOFactory(
                field_id="field1",
                field_type=FieldTypes.GOF_SELECTOR.value,
                field_values=field_values
            )
        ]
        invalid_gof_ids = ["CUSTOMER_DETAILS", "GST_DETAILS"]
        exception_message = {
            "field_id": "field1",
            "invalid_gof_ids": invalid_gof_ids
        }
        error_message = INVALID_GOF_IDS_EXCEPTION_MESSAGE.format(exception_message)
        interactor = CreateOrUpdateFieldsInteractor(storage=storage)

        # Act
        with pytest.raises(InvalidGOFIds) as err:
            interactor.create_or_update_fields(
                field_dtos=field_dtos,
                field_roles_dtos=valid_field_roles_dtos
            )

        # Assert
        snapshot.assert_match(name="exception_message = ", value=str(err.value))

    @pytest.mark.parametrize("field_type", [FieldTypes.IMAGE_UPLOADER.value, FieldTypes.FILE_UPLOADER.value])
    def test_given_empty_values_for_allowed_format_raise_exception(
            self, field_type, storage, reset_field_dto,
            valid_field_roles_dtos, populate_gofs, snapshot
    ):
        # Arrange
        from ib_tasks.exceptions.fields_custom_exceptions \
            import AllowedFormatsEmptyValueException

        field_dtos = [
            FieldDTOFactory(
                field_id="field1",
                field_type=field_type,
                allowed_formats=[]
            )
        ]
        field_id = "field1"
        interactor = CreateOrUpdateFieldsInteractor(storage=storage)

        # Act
        with pytest.raises(AllowedFormatsEmptyValueException) as err:
            interactor.create_or_update_fields(
                field_dtos=field_dtos,
                field_roles_dtos=valid_field_roles_dtos
            )

        # Assert
        snapshot.assert_match(name="exception_message = ", value=str(err.value))

    def test_given_duplication_of_allowed_formats_for_field_type_image_uploder_raise_exception(
            self, storage, reset_field_dto, snapshot,
            valid_field_roles_dtos, populate_gofs
    ):
        # Arrange
        from ib_tasks.exceptions.fields_custom_exceptions \
            import FieldsDuplicationOfAllowedFormatsValues

        field_dtos = [
            FieldDTOFactory(
                field_id="field1",
                field_type=FieldTypes.IMAGE_UPLOADER.value,
                allowed_formats=[".jpg", ".jpg", ".mpeg"]
            )
        ]
        interactor = CreateOrUpdateFieldsInteractor(storage=storage)

        # Act
        with pytest.raises(FieldsDuplicationOfAllowedFormatsValues) as err:
            interactor.create_or_update_fields(
                field_dtos=field_dtos,
                field_roles_dtos=valid_field_roles_dtos
            )

        # Assert
        snapshot.assert_match(name="exception_message = ", value=str(err.value))

    def test_given_duplication_of_allowed_formats_for_field_type_file_uploader_raise_exception(
            self, storage, reset_field_dto, snapshot,
            valid_field_roles_dtos, populate_gofs
    ):
        # Arrange
        from ib_tasks.exceptions.fields_custom_exceptions \
            import FieldsDuplicationOfAllowedFormatsValues

        field_dtos = [
            FieldDTOFactory(
                field_id="field1",
                field_type=FieldTypes.FILE_UPLOADER.value,
                allowed_formats=[".pdf", ".pdf"]
            )
        ]

        interactor = CreateOrUpdateFieldsInteractor(storage=storage)

        # Act
        with pytest.raises(FieldsDuplicationOfAllowedFormatsValues) as err:
            interactor.create_or_update_fields(
                field_dtos=field_dtos,
                field_roles_dtos=valid_field_roles_dtos
            )

        # Assert
        snapshot.assert_match(name="exception_message = ", value=str(err.value))

    @pytest.mark.parametrize("field_type", [FieldTypes.IMAGE_UPLOADER.value, FieldTypes.FILE_UPLOADER.value])
    def test_given_empty_values_for_allowed_formats_raise_exception(
            self, field_type, storage, reset_field_dto,
            valid_field_roles_dtos, populate_gofs, snapshot
    ):
        # Arrange
        from ib_tasks.exceptions.fields_custom_exceptions \
            import EmptyValuesForAllowedFormats

        field_dtos = [
            FieldDTOFactory(
                field_id="field1",
                field_type=field_type,
                allowed_formats=[".pdf", "  "]
            )
        ]
        field_id = "field1"
        interactor = CreateOrUpdateFieldsInteractor(storage=storage)

        # Act
        with pytest.raises(EmptyValuesForAllowedFormats) as err:
            interactor.create_or_update_fields(
                field_dtos=field_dtos,
                field_roles_dtos=valid_field_roles_dtos
            )

        # Assert
        snapshot.assert_match(name="exception_message = ", value=str(err.value))

    def test_given_empty_values_for_field_values_for_field_type_searchable_raise_exception(
            self, storage, reset_field_dto, snapshot,
            valid_field_roles_dtos, populate_gofs
    ):
        # Arrange

        from ib_tasks.exceptions.fields_custom_exceptions \
            import InvalidValueForSearchable
        field_dtos = [
            FieldDTOFactory(
                field_id="field1",
                field_type=FieldTypes.SEARCHABLE.value,
                field_values=" "
            )
        ]
        interactor = CreateOrUpdateFieldsInteractor(storage=storage)

        # Act
        with pytest.raises(InvalidValueForSearchable) as err:
            interactor.create_or_update_fields(
                field_dtos=field_dtos,
                field_roles_dtos=valid_field_roles_dtos
            )

        # Assert
        snapshot.assert_match(name="exception_message = ", value=str(err.value))

    def test_given_invalid_field_values_for_field_type_searchable_raise_exception(
            self, storage, reset_field_dto, snapshot,
            valid_field_roles_dtos, populate_gofs
    ):
        # Arrange

        from ib_tasks.exceptions.fields_custom_exceptions \
            import InvalidValueForSearchable
        field_dtos = [
            FieldDTOFactory(
                field_id="field1",
                field_type=FieldTypes.SEARCHABLE.value,
                field_values="Hello"
            )
        ]

        interactor = CreateOrUpdateFieldsInteractor(storage=storage)

        # Act
        with pytest.raises(InvalidValueForSearchable) as err:
            interactor.create_or_update_fields(
                field_dtos=field_dtos,
                field_roles_dtos=valid_field_roles_dtos
            )

        # Assert
        snapshot.assert_match(name="exception_message = ", value=str(err.value))

    def test_create_fields_and_fields_roles_given_field_dtos_and_field_role_dtos(
            self, storage, reset_factories, snapshot, mocker
    ):
        # Arrange
        import json
        GoFFactory(gof_id="gof1")
        GoFFactory(gof_id="gof2")

        field_values = [
            {
                "name": "Individual",
                "gof_ids": ["gof1", "gof2"]
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
                field_values=["Mr", "Mrs", "Ms"]
            ),
            FieldDTOFactory(
                gof_id="gof2", field_id="field3",
                field_type=FieldTypes.GOF_SELECTOR.value,
                field_values=field_values
            )
        ]

        field_roles_dtos = [
            FieldRolesDTOFactory(
                field_id="field1",
                read_permission_roles=["FIN_PAYMENTS_RP"],
                write_permission_roles=["FIN_FINANCE_RP"]
            ),
            FieldRolesDTOFactory(
                field_id="field2",
                read_permission_roles=["FIN_PAYMENTS_RP"],
                write_permission_roles=["FIN_FINANCE_RP"]
            ),
            FieldRolesDTOFactory(
                field_id="field3",
                read_permission_roles=["FIN_FINANCE_RP"],
                write_permission_roles=["FIN_PAYMENTS_RP"]
            )
        ]

        field_role_dtos = [
            FieldRoleDTOFactory(
                field_id="field1",
                role="FIN_PAYMENTS_RP",
                permission_type=PermissionTypes.READ.value
            ),
            FieldRoleDTOFactory(
                field_id="field1",
                role="FIN_FINANCE_RP",
                permission_type=PermissionTypes.WRITE.value
            ),
            FieldRoleDTOFactory(
                field_id="field2",
                role="FIN_PAYMENTS_RP",
                permission_type=PermissionTypes.READ.value
            ),
            FieldRoleDTOFactory(
                field_id="field2",
                role="FIN_FINANCE_RP",
                permission_type=PermissionTypes.WRITE.value
            ),
            FieldRoleDTOFactory(
                field_id="field3",
                role="FIN_FINANCE_RP",
                permission_type=PermissionTypes.READ.value
            ),
            FieldRoleDTOFactory(
                field_id="field3",
                role="FIN_PAYMENTS_RP",
                permission_type=PermissionTypes.WRITE.value
            )
        ]
        from ib_tasks.tests.common_fixtures.adapters.roles_service import \
            get_valid_role_ids_in_given_role_ids
        get_valid_role_ids_mock_method = \
            get_valid_role_ids_in_given_role_ids(mocker)
        interactor = CreateOrUpdateFieldsInteractor(storage=storage)


        # Act
        interactor.create_or_update_fields(field_dtos, field_roles_dtos)

        # Assert
        counter = 1
        get_valid_role_ids_mock_method.assert_called_once()
        for field_dto in field_dtos:
            field_obj = Field.objects.get(field_id=field_dto.field_id)
            self._assert_field_dto_and_field_obj(counter, field_obj, snapshot)
            counter += 1

        for field_role_dto in field_role_dtos:
            field_role_obj = FieldRole.objects.get(
                field_id=field_role_dto.field_id,
                role=field_role_dto.role
            )
            self._assert_field_role_dto_and_field_role_obj(counter, field_role_obj, snapshot)
            counter += 1

    def _assert_field_dto_and_field_obj(
            self, counter: int, field_obj: Field, snapshot
    ):
        snapshot.assert_match(name="field_id{}".format(counter), value=field_obj.field_id)
        snapshot.assert_match(name="gof_id{}".format(counter), value=field_obj.gof_id)
        snapshot.assert_match(name="display_name{}".format(counter), value=field_obj.display_name)
        snapshot.assert_match(name="field_type{}".format(counter), value=field_obj.field_type)
        snapshot.assert_match(name="field_values{}".format(counter), value=field_obj.field_values)
        snapshot.assert_match(name="allowed_formats{}".format(counter), value=field_obj.allowed_formats)
        snapshot.assert_match(name="help_text{}".format(counter), value=field_obj.help_text)
        snapshot.assert_match(name="tooltip{}".format(counter), value=field_obj.tooltip)
        snapshot.assert_match(name="placeholder_text{}".format(counter), value=field_obj.placeholder_text)
        snapshot.assert_match(name="error_messages{}".format(counter), value=field_obj.error_messages)
        snapshot.assert_match(name="validation_regex{}".format(counter), value=field_obj.validation_regex)

    def _assert_field_role_dto_and_field_role_obj(
            self, counter: int, field_role_obj: FieldRole, snapshot
    ):
        snapshot.assert_match(name="field_id{}".format(counter), value=field_role_obj.field_id)
        snapshot.assert_match(name="role{}".format(counter), value=field_role_obj.role)
        snapshot.assert_match(name="permission_type{}".format(counter), value=field_role_obj.permission_type)

    def test_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos(
            self, storage, reset_factories, snapshot, mocker
    ):
        # Arrange
        GoFFactory(gof_id="gof0")
        GoFFactory(gof_id="gof1")
        FieldFactory(field_id="field3")
        FieldFactory(field_id="field4")

        field_values = [
            {
                "name": "Individual",
                "gof_ids": ["gof0", "gof1"]
            },
            {
                "name": "Company",
                "gof_ids": ["gof0", "gof1"]
            }
        ]
        field_values = json.dumps(field_values)

        field_dtos = [
            FieldDTOFactory(
                gof_id="gof1", field_id="field3",
                field_type=FieldTypes.GOF_SELECTOR.value,
                field_values=field_values
            ),
            FieldDTOFactory(
                gof_id="gof0", field_id="field4",
                field_type=FieldTypes.DROPDOWN.value,
                field_values=["Mr", "Mrs", "Ms"]
            )
        ]

        field_roles_dtos = [
            FieldRolesDTOFactory(
                field_id="field3",
                read_permission_roles=["FIN_PAYMENTS_RP"],
                write_permission_roles=["FIN_FINANCE_RP"]
            ),
            FieldRolesDTOFactory(
                field_id="field4",
                read_permission_roles=["FIN_PAYMENTS_RP"],
                write_permission_roles=["FIN_FINANCE_RP"]
            )
        ]

        field_role_dtos = [
            FieldRoleDTOFactory(
                field_id="field3",
                role="FIN_PAYMENTS_RP",
                permission_type=PermissionTypes.READ.value
            ),
            FieldRoleDTOFactory(
                field_id="field3",
                role="FIN_FINANCE_RP",
                permission_type=PermissionTypes.WRITE.value
            ),
            FieldRoleDTOFactory(
                field_id="field4",
                role="FIN_PAYMENTS_RP",
                permission_type=PermissionTypes.READ.value
            ),
            FieldRoleDTOFactory(
                field_id="field4",
                role="FIN_FINANCE_RP",
                permission_type=PermissionTypes.WRITE.value
            )
        ]
        from ib_tasks.tests.common_fixtures.adapters.roles_service import \
            get_valid_role_ids_in_given_role_ids
        get_valid_role_ids_mock_method = \
            get_valid_role_ids_in_given_role_ids(mocker)

        interactor = CreateOrUpdateFieldsInteractor(storage=storage)

        # Act
        interactor.create_or_update_fields(field_dtos, field_roles_dtos)

        # Assert
        get_valid_role_ids_mock_method.assert_called_once()
        counter = 1
        for field_dto in field_dtos:
            field_obj = Field.objects.get(field_id=field_dto.field_id)
            self._assert_field_dto_and_field_obj(counter, field_obj, snapshot)
            counter += 1

        for field_role_dto in field_role_dtos:
            field_role_obj = FieldRole.objects.get(
                field_id=field_role_dto.field_id,
                role=field_role_dto.role
            )
            self._assert_field_role_dto_and_field_role_obj(counter, field_role_obj, snapshot)
            counter += 1

    def test_create_or_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos(
            self, storage, reset_factories, snapshot, mocker
    ):
        # Arrange
        GoFFactory(gof_id="gof1")
        GoFFactory(gof_id="gof2")
        FieldFactory(field_id="field1")
        FieldFactory(field_id="field2")

        field_values = [
            {
                "name": "Individual",
                "gof_ids": ["gof1", "gof2"]
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
                field_values=["Mr", "Mrs", "Ms"]
            ),
            FieldDTOFactory(
                gof_id="gof2", field_id="field3",
                field_type=FieldTypes.GOF_SELECTOR.value,
                field_values=field_values
            )
        ]

        field_roles_dtos = [
            FieldRolesDTOFactory(
                field_id="field1",
                read_permission_roles=["FIN_PAYMENTS_RP"],
                write_permission_roles=["FIN_FINANCE_RP"]
            ),
            FieldRolesDTOFactory(
                field_id="field2",
                read_permission_roles=["FIN_PAYMENTS_RP"],
                write_permission_roles=["FIN_FINANCE_RP"]
            ),
            FieldRolesDTOFactory(
                field_id="field3",
                read_permission_roles=["FIN_FINANCE_RP"],
                write_permission_roles=["FIN_PAYMENTS_RP"]
            )
        ]

        field_role_dtos = [
            FieldRoleDTOFactory(
                field_id="field1",
                role="FIN_PAYMENTS_RP",
                permission_type=PermissionTypes.READ.value
            ),
            FieldRoleDTOFactory(
                field_id="field1",
                role="FIN_FINANCE_RP",
                permission_type=PermissionTypes.WRITE.value
            ),
            FieldRoleDTOFactory(
                field_id="field2",
                role="FIN_PAYMENTS_RP",
                permission_type=PermissionTypes.READ.value
            ),
            FieldRoleDTOFactory(
                field_id="field2",
                role="FIN_FINANCE_RP",
                permission_type=PermissionTypes.WRITE.value
            ),
            FieldRoleDTOFactory(
                field_id="field3",
                role="FIN_FINANCE_RP",
                permission_type=PermissionTypes.READ.value
            ),
            FieldRoleDTOFactory(
                field_id="field3",
                role="FIN_PAYMENTS_RP",
                permission_type=PermissionTypes.WRITE.value
            )
        ]
        from ib_tasks.tests.common_fixtures.adapters.roles_service import \
            get_valid_role_ids_in_given_role_ids
        get_valid_role_ids_mock_method = \
            get_valid_role_ids_in_given_role_ids(mocker)

        interactor = CreateOrUpdateFieldsInteractor(storage=storage)

        # Act
        interactor.create_or_update_fields(field_dtos, field_roles_dtos)

        # Assert
        get_valid_role_ids_mock_method.assert_called_once()
        counter = 1
        for field_dto in field_dtos:
            field_obj = Field.objects.get(field_id=field_dto.field_id)
            self._assert_field_dto_and_field_obj(counter, field_obj, snapshot)
            counter += 1

        for field_role_dto in field_role_dtos:
            field_role_obj = FieldRole.objects.get(
                field_id=field_role_dto.field_id,
                role=field_role_dto.role
            )
            self._assert_field_role_dto_and_field_role_obj(counter, field_role_obj, snapshot)
            counter += 1
