# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCreateOrUpdateFields.test_given_field_ids_empty_raise_exception exception_message = '] = "Field ids shouldn't be empty"

snapshots['TestCreateOrUpdateFields.test_given_duplication_of_filed_ids_raise_exception exception_message = '] = "These are duplicated field ids ['FIN_SALUATION']"

snapshots['TestCreateOrUpdateFields.test_given_field_display_name_as_empty_raise_exception exception_message = '] = "Invalid fields display names for these field ids ['field2', 'field3']"

snapshots['TestCreateOrUpdateFields.test_given_invalid_field_type_raise_ecxception exception_message = '] = "Field Types should be one of these ['PLAIN_TEXT', 'PHONE_NUMBER', 'EMAIL', 'URL', 'PASSWORD', 'NUMBER', 'FLOAT', 'LONG_TEXT', 'DROPDOWN', 'GOF_SELECTOR', 'RADIO_GROUP', 'CHECKBOX_GROUP', 'MULTI_SELECT_FIELD', 'MULTI_SELECT_LABELS', 'DATE', 'TIME', 'DATE_TIME', 'IMAGE_UPLOADER', 'FILE_UPLOADER', 'SEARCHABLE'] for these field_ids ['field1', 'field2']"

snapshots['TestCreateOrUpdateFields.test_given_gof_ids_not_in_database_raise_exception exception_message = '] = "Invalid values for gof_ids ['FIN_VENDOR_BASIC_DETAILS', 'Hello', '']"

snapshots['TestCreateOrUpdateFields.test_given_empty_values_for_read_permissions_roles_raise_exception exception_message = '] = "Read Permission roles shouldn't be empty for these fields ids ['field1', 'field2']"

snapshots['TestCreateOrUpdateFields.test_given_empty_values_for_write_permissions_roles_raise_exception exception_message = '] = "Write Permission roles shouldn't be empty for these fields ids ['field1', 'field2']"

snapshots['TestCreateOrUpdateFields.test_given_duplication_of_values_for_read_permissions_roles_raise_exception exception_message = '] = "Repeated roles for read permissions for these fields [{'field_id': 'field1', 'duplication_values_for_read_permissions': ['User']}, {'field_id': 'field2', 'duplication_values_for_read_permissions': ['Admin']}]"

snapshots['TestCreateOrUpdateFields.test_given_duplication_of_values_for_write_permissions_roles_raise_exception exception_message = '] = "Repeated roles for write permissions for these fields [{'field_id': 'field1', 'duplication_values_for_write_permissions': ['User']}, {'field_id': 'field2', 'duplication_values_for_write_permissions': ['Admin']}]"

snapshots['TestCreateOrUpdateFields.test_given_invalid_roles_for_read_permissions_raise_exception exception_message = '] = [
    {
        'field_id': 'field1',
        'invalid_roles': [
            'User',
            'Vendor'
        ],
        'permissions': 'read_permissions'
    },
    {
        'field_id': 'field2',
        'invalid_roles': [
            'admin'
        ],
        'permissions': 'read_permissions'
    }
]

snapshots['TestCreateOrUpdateFields.test_given_invalid_roles_for_write_permissions_raise_exception exception_message = '] = [
    {
        'field_id': 'field1',
        'invalid_roles': [
            'User',
            'Vendor',
            'FIN_PAYMENTS_LEVEL1_VERIFIER'
        ],
        'permissions': 'write_permissions'
    },
    {
        'field_id': 'field2',
        'invalid_roles': [
            'admin'
        ],
        'permissions': 'write_permissions'
    }
]

snapshots['TestCreateOrUpdateFields.test_given_empty_values_in_field_values_raise_exceptions exception_message = '] = "Field values shouldn't be empty for these field id field1"

snapshots['TestCreateOrUpdateFields.test_given_field_values_is_empty_raise_exceptions exception_message = '] = "Field values shouldn't be empty for these field id field1"

snapshots['TestCreateOrUpdateFields.test_given_duplication_of_field_values_raise_exception exception_message = '] = "Duplication of Field values for these field {'field_id': 'field1', 'field_type': 'DROPDOWN', 'duplication_of_values': ['Mrs']}"

snapshots['TestCreateOrUpdateFields.test_given_field_type_gof_selector_and_field_values_as_invalid_json_raise_exception exception_message = '] = 'Field values contains invalid json for these field_id = field1'

snapshots['TestCreateOrUpdateFields.test_given_gof_names_as_empty_for_field_values_raise_exception exception_message = '] = "GoF names for field values shouldn't be empty for these field id = field1"

snapshots['TestCreateOrUpdateFields.test_given_duplication_of_gof_names_for_field_values_raise_exception exception_message = '] = 'Duplication of gof names for field values of these field = '

snapshots['TestCreateOrUpdateFields.test_given_invalid_gof_ids_for_field_values_raise_exception exception_message = '] = "Invalid values for gof_ids {'field_id': 'field1', 'invalid_gof_ids': ['CUSTOMER_DETAILS', 'GST_DETAILS']}"

snapshots['TestCreateOrUpdateFields.test_given_empty_values_for_allowed_format_raise_exception[IMAGE_UPLOADER] exception_message = '] = "Allowed formats for these field id shouldn't be empty = field1"

snapshots['TestCreateOrUpdateFields.test_given_empty_values_for_allowed_format_raise_exception[FILE_UPLOADER] exception_message = '] = "Allowed formats for these field id shouldn't be empty = field1"

snapshots['TestCreateOrUpdateFields.test_given_duplication_of_allowed_formats_for_field_type_image_uploder_raise_exception exception_message = '] = "Duplication of values for allowed formats = {'field_id': 'field1', 'field_type': 'IMAGE_UPLOADER', 'duplication_of_values': ['.jpg']}"

snapshots['TestCreateOrUpdateFields.test_given_duplication_of_allowed_formats_for_field_type_file_uploader_raise_exception exception_message = '] = "Duplication of values for allowed formats = {'field_id': 'field1', 'field_type': 'FILE_UPLOADER', 'duplication_of_values': ['.pdf']}"

snapshots['TestCreateOrUpdateFields.test_given_empty_values_for_allowed_formats_raise_exception[IMAGE_UPLOADER] exception_message = '] = "Allowed formats shouldn't contain empty values for these filed_id = field1"

snapshots['TestCreateOrUpdateFields.test_given_empty_values_for_allowed_formats_raise_exception[FILE_UPLOADER] exception_message = '] = "Allowed formats shouldn't contain empty values for these filed_id = field1"

snapshots['TestCreateOrUpdateFields.test_given_empty_values_for_field_values_for_field_type_searchable_raise_exception exception_message = '] = "Searchable value should be one of these  ['CITY', 'STATE', 'COUNTRY', 'VENDOR', 'USER', 'COMPANY', 'TEAM'] for this field_id field1"

snapshots['TestCreateOrUpdateFields.test_given_invalid_field_values_for_field_type_searchable_raise_exception exception_message = '] = "Searchable value should be one of these  ['CITY', 'STATE', 'COUNTRY', 'VENDOR', 'USER', 'COMPANY', 'TEAM'] for this field_id field1"

snapshots['TestCreateOrUpdateFields.test_create_fields_and_fields_roles_given_field_dtos_and_field_role_dtos field_id1'] = 'field1'

snapshots['TestCreateOrUpdateFields.test_create_fields_and_fields_roles_given_field_dtos_and_field_role_dtos gof_id1'] = 'gof1'

snapshots['TestCreateOrUpdateFields.test_create_fields_and_fields_roles_given_field_dtos_and_field_role_dtos display_name1'] = 'field name'

snapshots['TestCreateOrUpdateFields.test_create_fields_and_fields_roles_given_field_dtos_and_field_role_dtos field_type1'] = 'PLAIN_TEXT'

snapshots['TestCreateOrUpdateFields.test_create_fields_and_fields_roles_given_field_dtos_and_field_role_dtos field_values1'] = None

snapshots['TestCreateOrUpdateFields.test_create_fields_and_fields_roles_given_field_dtos_and_field_role_dtos allowed_formats1'] = None

snapshots['TestCreateOrUpdateFields.test_create_fields_and_fields_roles_given_field_dtos_and_field_role_dtos help_text1'] = None

snapshots['TestCreateOrUpdateFields.test_create_fields_and_fields_roles_given_field_dtos_and_field_role_dtos tooltip1'] = None

snapshots['TestCreateOrUpdateFields.test_create_fields_and_fields_roles_given_field_dtos_and_field_role_dtos placeholder_text1'] = None

snapshots['TestCreateOrUpdateFields.test_create_fields_and_fields_roles_given_field_dtos_and_field_role_dtos error_messages1'] = None

snapshots['TestCreateOrUpdateFields.test_create_fields_and_fields_roles_given_field_dtos_and_field_role_dtos validation_regex1'] = None

snapshots['TestCreateOrUpdateFields.test_create_fields_and_fields_roles_given_field_dtos_and_field_role_dtos field_id2'] = 'field2'

snapshots['TestCreateOrUpdateFields.test_create_fields_and_fields_roles_given_field_dtos_and_field_role_dtos gof_id2'] = 'gof2'

snapshots['TestCreateOrUpdateFields.test_create_fields_and_fields_roles_given_field_dtos_and_field_role_dtos display_name2'] = 'field name'

snapshots['TestCreateOrUpdateFields.test_create_fields_and_fields_roles_given_field_dtos_and_field_role_dtos field_type2'] = 'DROPDOWN'

snapshots['TestCreateOrUpdateFields.test_create_fields_and_fields_roles_given_field_dtos_and_field_role_dtos field_values2'] = '["Mr", "Mrs", "Ms"]'

snapshots['TestCreateOrUpdateFields.test_create_fields_and_fields_roles_given_field_dtos_and_field_role_dtos allowed_formats2'] = None

snapshots['TestCreateOrUpdateFields.test_create_fields_and_fields_roles_given_field_dtos_and_field_role_dtos help_text2'] = None

snapshots['TestCreateOrUpdateFields.test_create_fields_and_fields_roles_given_field_dtos_and_field_role_dtos tooltip2'] = None

snapshots['TestCreateOrUpdateFields.test_create_fields_and_fields_roles_given_field_dtos_and_field_role_dtos placeholder_text2'] = None

snapshots['TestCreateOrUpdateFields.test_create_fields_and_fields_roles_given_field_dtos_and_field_role_dtos error_messages2'] = None

snapshots['TestCreateOrUpdateFields.test_create_fields_and_fields_roles_given_field_dtos_and_field_role_dtos validation_regex2'] = None

snapshots['TestCreateOrUpdateFields.test_create_fields_and_fields_roles_given_field_dtos_and_field_role_dtos field_id3'] = 'field3'

snapshots['TestCreateOrUpdateFields.test_create_fields_and_fields_roles_given_field_dtos_and_field_role_dtos gof_id3'] = 'gof2'

snapshots['TestCreateOrUpdateFields.test_create_fields_and_fields_roles_given_field_dtos_and_field_role_dtos display_name3'] = 'field name'

snapshots['TestCreateOrUpdateFields.test_create_fields_and_fields_roles_given_field_dtos_and_field_role_dtos field_type3'] = 'GOF_SELECTOR'

snapshots['TestCreateOrUpdateFields.test_create_fields_and_fields_roles_given_field_dtos_and_field_role_dtos field_values3'] = '[{"name": "Individual", "gof_ids": ["gof1", "gof2"]}, {"name": "Company", "gof_ids": ["gof1", "gof2"]}]'

snapshots['TestCreateOrUpdateFields.test_create_fields_and_fields_roles_given_field_dtos_and_field_role_dtos allowed_formats3'] = None

snapshots['TestCreateOrUpdateFields.test_create_fields_and_fields_roles_given_field_dtos_and_field_role_dtos help_text3'] = None

snapshots['TestCreateOrUpdateFields.test_create_fields_and_fields_roles_given_field_dtos_and_field_role_dtos tooltip3'] = None

snapshots['TestCreateOrUpdateFields.test_create_fields_and_fields_roles_given_field_dtos_and_field_role_dtos placeholder_text3'] = None

snapshots['TestCreateOrUpdateFields.test_create_fields_and_fields_roles_given_field_dtos_and_field_role_dtos error_messages3'] = None

snapshots['TestCreateOrUpdateFields.test_create_fields_and_fields_roles_given_field_dtos_and_field_role_dtos validation_regex3'] = None

snapshots['TestCreateOrUpdateFields.test_create_fields_and_fields_roles_given_field_dtos_and_field_role_dtos field_id4'] = 'field1'

snapshots['TestCreateOrUpdateFields.test_create_fields_and_fields_roles_given_field_dtos_and_field_role_dtos role4'] = 'FIN_PAYMENTS_RP'

snapshots['TestCreateOrUpdateFields.test_create_fields_and_fields_roles_given_field_dtos_and_field_role_dtos permission_type4'] = 'READ'

snapshots['TestCreateOrUpdateFields.test_create_fields_and_fields_roles_given_field_dtos_and_field_role_dtos field_id5'] = 'field1'

snapshots['TestCreateOrUpdateFields.test_create_fields_and_fields_roles_given_field_dtos_and_field_role_dtos role5'] = 'FIN_FINANCE_RP'

snapshots['TestCreateOrUpdateFields.test_create_fields_and_fields_roles_given_field_dtos_and_field_role_dtos permission_type5'] = 'WRITE'

snapshots['TestCreateOrUpdateFields.test_create_fields_and_fields_roles_given_field_dtos_and_field_role_dtos field_id6'] = 'field2'

snapshots['TestCreateOrUpdateFields.test_create_fields_and_fields_roles_given_field_dtos_and_field_role_dtos role6'] = 'FIN_PAYMENTS_RP'

snapshots['TestCreateOrUpdateFields.test_create_fields_and_fields_roles_given_field_dtos_and_field_role_dtos permission_type6'] = 'READ'

snapshots['TestCreateOrUpdateFields.test_create_fields_and_fields_roles_given_field_dtos_and_field_role_dtos field_id7'] = 'field2'

snapshots['TestCreateOrUpdateFields.test_create_fields_and_fields_roles_given_field_dtos_and_field_role_dtos role7'] = 'FIN_FINANCE_RP'

snapshots['TestCreateOrUpdateFields.test_create_fields_and_fields_roles_given_field_dtos_and_field_role_dtos permission_type7'] = 'WRITE'

snapshots['TestCreateOrUpdateFields.test_create_fields_and_fields_roles_given_field_dtos_and_field_role_dtos field_id8'] = 'field3'

snapshots['TestCreateOrUpdateFields.test_create_fields_and_fields_roles_given_field_dtos_and_field_role_dtos role8'] = 'FIN_FINANCE_RP'

snapshots['TestCreateOrUpdateFields.test_create_fields_and_fields_roles_given_field_dtos_and_field_role_dtos permission_type8'] = 'READ'

snapshots['TestCreateOrUpdateFields.test_create_fields_and_fields_roles_given_field_dtos_and_field_role_dtos field_id9'] = 'field3'

snapshots['TestCreateOrUpdateFields.test_create_fields_and_fields_roles_given_field_dtos_and_field_role_dtos role9'] = 'FIN_PAYMENTS_RP'

snapshots['TestCreateOrUpdateFields.test_create_fields_and_fields_roles_given_field_dtos_and_field_role_dtos permission_type9'] = 'WRITE'

snapshots['TestCreateOrUpdateFields.test_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos field_id1'] = 'field3'

snapshots['TestCreateOrUpdateFields.test_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos gof_id1'] = 'gof1'

snapshots['TestCreateOrUpdateFields.test_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos display_name1'] = 'field name'

snapshots['TestCreateOrUpdateFields.test_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos field_type1'] = 'GOF_SELECTOR'

snapshots['TestCreateOrUpdateFields.test_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos field_values1'] = '[{"name": "Individual", "gof_ids": ["gof0", "gof1"]}, {"name": "Company", "gof_ids": ["gof0", "gof1"]}]'

snapshots['TestCreateOrUpdateFields.test_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos allowed_formats1'] = None

snapshots['TestCreateOrUpdateFields.test_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos help_text1'] = None

snapshots['TestCreateOrUpdateFields.test_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos tooltip1'] = None

snapshots['TestCreateOrUpdateFields.test_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos placeholder_text1'] = None

snapshots['TestCreateOrUpdateFields.test_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos error_messages1'] = None

snapshots['TestCreateOrUpdateFields.test_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos validation_regex1'] = None

snapshots['TestCreateOrUpdateFields.test_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos field_id2'] = 'field4'

snapshots['TestCreateOrUpdateFields.test_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos gof_id2'] = 'gof0'

snapshots['TestCreateOrUpdateFields.test_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos display_name2'] = 'field name'

snapshots['TestCreateOrUpdateFields.test_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos field_type2'] = 'DROPDOWN'

snapshots['TestCreateOrUpdateFields.test_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos field_values2'] = '["Mr", "Mrs", "Ms"]'

snapshots['TestCreateOrUpdateFields.test_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos allowed_formats2'] = None

snapshots['TestCreateOrUpdateFields.test_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos help_text2'] = None

snapshots['TestCreateOrUpdateFields.test_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos tooltip2'] = None

snapshots['TestCreateOrUpdateFields.test_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos placeholder_text2'] = None

snapshots['TestCreateOrUpdateFields.test_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos error_messages2'] = None

snapshots['TestCreateOrUpdateFields.test_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos validation_regex2'] = None

snapshots['TestCreateOrUpdateFields.test_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos field_id3'] = 'field3'

snapshots['TestCreateOrUpdateFields.test_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos role3'] = 'FIN_PAYMENTS_RP'

snapshots['TestCreateOrUpdateFields.test_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos permission_type3'] = 'READ'

snapshots['TestCreateOrUpdateFields.test_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos field_id4'] = 'field3'

snapshots['TestCreateOrUpdateFields.test_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos role4'] = 'FIN_FINANCE_RP'

snapshots['TestCreateOrUpdateFields.test_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos permission_type4'] = 'WRITE'

snapshots['TestCreateOrUpdateFields.test_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos field_id5'] = 'field4'

snapshots['TestCreateOrUpdateFields.test_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos role5'] = 'FIN_PAYMENTS_RP'

snapshots['TestCreateOrUpdateFields.test_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos permission_type5'] = 'READ'

snapshots['TestCreateOrUpdateFields.test_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos field_id6'] = 'field4'

snapshots['TestCreateOrUpdateFields.test_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos role6'] = 'FIN_FINANCE_RP'

snapshots['TestCreateOrUpdateFields.test_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos permission_type6'] = 'WRITE'

snapshots['TestCreateOrUpdateFields.test_create_or_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos field_id1'] = 'field1'

snapshots['TestCreateOrUpdateFields.test_create_or_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos gof_id1'] = 'gof1'

snapshots['TestCreateOrUpdateFields.test_create_or_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos display_name1'] = 'field name'

snapshots['TestCreateOrUpdateFields.test_create_or_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos field_type1'] = 'PLAIN_TEXT'

snapshots['TestCreateOrUpdateFields.test_create_or_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos field_values1'] = None

snapshots['TestCreateOrUpdateFields.test_create_or_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos allowed_formats1'] = None

snapshots['TestCreateOrUpdateFields.test_create_or_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos help_text1'] = None

snapshots['TestCreateOrUpdateFields.test_create_or_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos tooltip1'] = None

snapshots['TestCreateOrUpdateFields.test_create_or_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos placeholder_text1'] = None

snapshots['TestCreateOrUpdateFields.test_create_or_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos error_messages1'] = None

snapshots['TestCreateOrUpdateFields.test_create_or_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos validation_regex1'] = None

snapshots['TestCreateOrUpdateFields.test_create_or_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos field_id2'] = 'field2'

snapshots['TestCreateOrUpdateFields.test_create_or_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos gof_id2'] = 'gof2'

snapshots['TestCreateOrUpdateFields.test_create_or_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos display_name2'] = 'field name'

snapshots['TestCreateOrUpdateFields.test_create_or_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos field_type2'] = 'DROPDOWN'

snapshots['TestCreateOrUpdateFields.test_create_or_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos field_values2'] = '["Mr", "Mrs", "Ms"]'

snapshots['TestCreateOrUpdateFields.test_create_or_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos allowed_formats2'] = None

snapshots['TestCreateOrUpdateFields.test_create_or_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos help_text2'] = None

snapshots['TestCreateOrUpdateFields.test_create_or_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos tooltip2'] = None

snapshots['TestCreateOrUpdateFields.test_create_or_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos placeholder_text2'] = None

snapshots['TestCreateOrUpdateFields.test_create_or_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos error_messages2'] = None

snapshots['TestCreateOrUpdateFields.test_create_or_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos validation_regex2'] = None

snapshots['TestCreateOrUpdateFields.test_create_or_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos field_id3'] = 'field3'

snapshots['TestCreateOrUpdateFields.test_create_or_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos gof_id3'] = 'gof2'

snapshots['TestCreateOrUpdateFields.test_create_or_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos display_name3'] = 'field name'

snapshots['TestCreateOrUpdateFields.test_create_or_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos field_type3'] = 'GOF_SELECTOR'

snapshots['TestCreateOrUpdateFields.test_create_or_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos field_values3'] = '[{"name": "Individual", "gof_ids": ["gof1", "gof2"]}, {"name": "Company", "gof_ids": ["gof1", "gof2"]}]'

snapshots['TestCreateOrUpdateFields.test_create_or_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos allowed_formats3'] = None

snapshots['TestCreateOrUpdateFields.test_create_or_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos help_text3'] = None

snapshots['TestCreateOrUpdateFields.test_create_or_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos tooltip3'] = None

snapshots['TestCreateOrUpdateFields.test_create_or_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos placeholder_text3'] = None

snapshots['TestCreateOrUpdateFields.test_create_or_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos error_messages3'] = None

snapshots['TestCreateOrUpdateFields.test_create_or_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos validation_regex3'] = None

snapshots['TestCreateOrUpdateFields.test_create_or_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos field_id4'] = 'field1'

snapshots['TestCreateOrUpdateFields.test_create_or_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos role4'] = 'FIN_PAYMENTS_RP'

snapshots['TestCreateOrUpdateFields.test_create_or_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos permission_type4'] = 'READ'

snapshots['TestCreateOrUpdateFields.test_create_or_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos field_id5'] = 'field1'

snapshots['TestCreateOrUpdateFields.test_create_or_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos role5'] = 'FIN_FINANCE_RP'

snapshots['TestCreateOrUpdateFields.test_create_or_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos permission_type5'] = 'WRITE'

snapshots['TestCreateOrUpdateFields.test_create_or_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos field_id6'] = 'field2'

snapshots['TestCreateOrUpdateFields.test_create_or_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos role6'] = 'FIN_PAYMENTS_RP'

snapshots['TestCreateOrUpdateFields.test_create_or_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos permission_type6'] = 'READ'

snapshots['TestCreateOrUpdateFields.test_create_or_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos field_id7'] = 'field2'

snapshots['TestCreateOrUpdateFields.test_create_or_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos role7'] = 'FIN_FINANCE_RP'

snapshots['TestCreateOrUpdateFields.test_create_or_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos permission_type7'] = 'WRITE'

snapshots['TestCreateOrUpdateFields.test_create_or_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos field_id8'] = 'field3'

snapshots['TestCreateOrUpdateFields.test_create_or_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos role8'] = 'FIN_FINANCE_RP'

snapshots['TestCreateOrUpdateFields.test_create_or_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos permission_type8'] = 'READ'

snapshots['TestCreateOrUpdateFields.test_create_or_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos field_id9'] = 'field3'

snapshots['TestCreateOrUpdateFields.test_create_or_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos role9'] = 'FIN_PAYMENTS_RP'

snapshots['TestCreateOrUpdateFields.test_create_or_update_fields_and_fields_roles_given_field_dtos_and_field_role_dtos permission_type9'] = 'WRITE'
