import pytest


class TestPopulateStatusVariables:

    @pytest.fixture()
    def valid_format(self):
        valid_format = {
            "task_template_id": "task_template_id_1",
            "status_variable_id": "status_id_1"
        }

        import json
        json_valid_format = json.dumps(valid_format)
        return json_valid_format

    @pytest.fixture()
    def expected_status_dto(self):
        from ib_tasks.tests.factories.storage_dtos import TaskTemplateStatusDTOFactory
        TaskTemplateStatusDTOFactory.reset_sequence(1)
        return TaskTemplateStatusDTOFactory.create_batch(size=2)

    @pytest.mark.django_db
    def test_with_invalid_keys_raises_exception(self, valid_format):
        # Arrange
        valid_json_format = valid_format
        list_of_status_dict = [
            {
                "invalid_field_name": "task_template_id_1",
                "status_variable_id": "status_id_1"
            },
            {
                "task_template_id": "task_template_id_2",
                "status_variable_id": "status_id_2"
            }
        ]

        from ib_tasks.populate.create_task_status_variables import \
            populate_status_variables

        # Act

        from ib_tasks.exceptions.custom_exceptions import \
            InvalidFormatException
        with pytest.raises(InvalidFormatException) as err:
            populate_status_variables(list_of_status_dict=list_of_status_dict)

        # Assert
        assert err.value.valid_format == valid_json_format

    @pytest.mark.django_db
    def test_with_valid_keys_returns_list_of_status_dtos(
            self, expected_status_dto, mocker):
        # Arrange
        expected_status_dto = expected_status_dto
        list_of_status_dict = [
            {
                "task_template_id": "task_template_id_1",
                "status_variable_id": "status_id_1"
            },
            {
                "task_template_id": "task_template_id_2",
                "status_variable_id": "status_id_2"
            }
        ]
        from ib_tasks.tests.common_fixtures.storages import mock_storage
        mock_storage(mocker, ['task_template_id_1', 'task_template_id_2'])

        from ib_tasks.populate.create_task_status_variables import \
            populate_status_variables

        # Act
        populate_status_variables(list_of_status_dict=list_of_status_dict)
