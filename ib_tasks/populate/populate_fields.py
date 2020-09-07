from typing import List, Dict, Union

from ib_tasks.constants.constants import MULTI_VALUES_INPUT_FIELDS, UPLOADERS
from ib_tasks.interactors.storage_interfaces.fields_dtos import FieldDTO, \
    FieldRolesDTO


class PopulateFields:
    def create_or_update_fields(self, spread_sheet_name: str):
        from ib_tasks.constants.constants import FIELD_SUB_SHEET_TITLE

        from ib_tasks.interactors.create_or_update_fields_interactor \
            import CreateOrUpdateFieldsInteractor
        from ib_tasks.utils.get_google_sheet import get_google_sheet
        sheet = get_google_sheet(sheet_name=spread_sheet_name)

        fields_config_sheet = sheet.worksheet(FIELD_SUB_SHEET_TITLE)
        field_records = fields_config_sheet.get_all_records()
        field_dtos = self.prepare_field_dtos(field_records)
        field_roles_dtos = self.prepare_field_roles_dtos(field_records)
        from ib_tasks.storages.field_config_storage_implementation import \
            FieldConfigStorageImplementation
        storage = FieldConfigStorageImplementation()
        from ib_tasks.storages.gof_storage_implementation import \
            GoFStorageImplementation
        gof_storage = GoFStorageImplementation()
        interactor = CreateOrUpdateFieldsInteractor(storage=storage,
                                                    gof_storage=gof_storage)
        interactor.create_or_update_fields(field_dtos, field_roles_dtos)

    def prepare_field_dtos(self, field_records: List[Dict]) -> List[FieldDTO]:
        field_dtos = []
        for field_record in field_records:
            field_type = field_record["Field Type*"].strip()
            field_values = field_record["Field Values"].strip()
            required = field_record["Required*"].strip()
            help_text = field_record["Help Text"].strip()
            tooltip = field_record["Tool Tip"].strip()
            placeholder_text = field_record["Place Holder Text"].strip()
            error_message = field_record["Error Message"].strip()
            allowed_formats = field_record["Allowed Formats"].strip()
            validation_regex = field_record["Validation - RegEx"].strip()
            order = field_record["Order"]

            required = self.get_required_bool_value_based_on_given_input(
                required)
            field_values = self.get_field_values(field_type, field_values)
            allowed_formats = self.get_allowed_formats(field_type,
                                                       allowed_formats)

            if help_text == "":
                help_text = None
            if tooltip == "":
                tooltip = None
            if placeholder_text == "":
                placeholder_text = None
            if error_message == "":
                error_message = None
            if validation_regex == "":
                validation_regex = None

            field_dto = FieldDTO(
                gof_id=field_record["GOF ID*"].strip(),
                field_id=field_record["Field ID*"].strip(),
                field_display_name=field_record["Field Display Name*"].strip(),
                field_type=field_type,
                field_values=field_values,
                required=required,
                help_text=help_text,
                tooltip=tooltip,
                placeholder_text=placeholder_text,
                error_message=error_message,
                allowed_formats=allowed_formats,
                validation_regex=validation_regex,
                order=int(order)
            )
            field_dtos.append(field_dto)
        return field_dtos

    @staticmethod
    def get_allowed_formats(field_type,
                            allowed_formats) -> Union[None, str, List[str]]:
        if allowed_formats == "":
            allowed_formats = None
        if field_type in UPLOADERS and allowed_formats is not None:
            allowed_formats = allowed_formats.split("\r\n")
            allowed_formats = allowed_formats[0].split("\n")
        if field_type in UPLOADERS and allowed_formats is None:
            allowed_formats = []
        return allowed_formats

    @staticmethod
    def get_field_values(field_type,
                         field_values) -> Union[None, str, List[str]]:
        if field_values == "":
            field_values = None
        if field_type in MULTI_VALUES_INPUT_FIELDS and field_values is not \
                None:
            field_values = field_values.split("\n")
            field_values_without_space = []
            for field_value in field_values:
                field_value = field_value.strip()
                field_values_without_space.append(field_value)
            field_values = field_values_without_space
        if field_type in MULTI_VALUES_INPUT_FIELDS and field_values is None:
            field_values = []
        return field_values

    @staticmethod
    def get_required_bool_value_based_on_given_input(required) -> bool:
        if required == "Yes":
            required = True
        else:
            required = False
        return required

    def prepare_field_roles_dtos(
            self, field_records: List[Dict]) -> List[FieldRolesDTO]:
        field_roles_dtos = []
        for field_record in field_records:
            field_roles_dto = self.get_field_roles_dto(field_record)
            field_roles_dtos.append(field_roles_dto)
        return field_roles_dtos

    @staticmethod
    def get_field_roles_dto(field_record: Dict) -> FieldRolesDTO:
        read_permissions_is_empty = not field_record[
            "Write Permission to roles"].strip()
        write_permissions_is_empty = not field_record[
            'Read Permission to roles'].strip()
        write_permission_roles = field_record[
            "Write Permission to roles"].split("\n")
        read_permission_roles = field_record["Read Permission to roles"].split(
            "\n")
        if read_permissions_is_empty:
            read_permission_roles = []
        if write_permissions_is_empty:
            write_permission_roles = []

        read_permission_roles = [
            role.strip() for role in read_permission_roles
        ]
        write_permission_roles = [
            role.strip() for role in write_permission_roles
        ]

        field_roles_dto = FieldRolesDTO(
            field_id=field_record["Field ID*"].strip(),
            write_permission_roles=read_permission_roles,
            read_permission_roles=write_permission_roles)
        return field_roles_dto
