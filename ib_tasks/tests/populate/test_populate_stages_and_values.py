import json

import pytest


class TestPopulateStagesAndValues:

    @pytest.fixture()
    def valid_format(self):
        import json
        valid_format = {
            "task_template_id": "task_template_id_1",
            "stage_id": "stage_id_1",
            "value": 1,
            "card_info_kanban": json.dumps(["field_id_1", "field_id_2"]),
            "card_info_list": json.dumps(["field_id_1", "field_id_2"]),
            "stage_display_name": "stage_name",
            "stage_display_logic": "status_1==stage_id_1"
        }

        json_valid_format = json.dumps(valid_format)
        return json_valid_format

    @pytest.fixture()
    def expected_stages_dto(self):
        from ib_tasks.tests.factories.storage_dtos import StageDTOFactory
        StageDTOFactory.reset_sequence(1)
        return StageDTOFactory.create_batch(size=2)

    @pytest.mark.django_db
    def test_with_invalid_keys_raises_exception(self, valid_format):
        # Arrange
        valid_json_format = valid_format
        list_of_stages_dict = [
            {
                "task_template_id": "task_template_id_1",
                "stage_id": "stage_id_1",
                "invalid_field_name": 1,
                "card_info_kanban": json.dumps(["field_id_1", "field_id_2"]),
                "card_info_list": json.dumps(["field_id_1", "field_id_2"]),
                "stage_display_name": "stage_name",
                "stage_display_logic": "status_1==stage_id_1"
            },
            {
                "task_template_id": "task_template_id_2",
                "stage_id": "stage_id_2",
                "values": -1,
                "card_info_kanban": json.dumps(["field_id_1", "field_id_2"]),
                "card_info_list": json.dumps(["field_id_1", "field_id_2"]),
                "stage_display_name": "stage_name",
                "stage_display_logic": "status_2==stage_id_2"
            }
        ]

        from ib_tasks.populate.create_or_update_stages import \
            populate_stages_values

        # Act

        from ib_tasks.exceptions.custom_exceptions import \
            InvalidFormatException
        with pytest.raises(InvalidFormatException) as err:
            populate_stages_values(list_of_stages_dict=list_of_stages_dict)

        # Assert
        assert err.value.valid_format == valid_json_format

    @pytest.mark.django_db
    def test_with_valid_keys_returns_list_of_stage_dtos(self,
                                                        expected_stages_dto,
                                                        mocker):
        # Arrange
        expected_stages_dto = expected_stages_dto
        list_of_stages_dict = [
            {
                "task_template_id": "task_template_id_1",
                "stage_id": "stage_id_1",
                "value": 1,
                "card_info_kanban": json.dumps(["field_id_1", "field_id_2"]),
                "card_info_list": json.dumps(["field_id_1", "field_id_2"]),
                "stage_display_name": "name_1",
                "stage_display_logic": "status_id_1==stage_id"
            },
            {
                "task_template_id": "task_template_id_2",
                "stage_id": "stage_id_2",
                "value": 2,
                "card_info_kanban": json.dumps(["field_id_1", "field_id_2"]),
                "card_info_list": json.dumps(["field_id_1", "field_id_2"]),
                "stage_display_name": "name_2",
                "stage_display_logic": "status_id_2==stage_id"
            }
        ]
        from ib_tasks.tests.common_fixtures.storages import mock_storage
        mock_storage(mocker, ['task_template_id_1', 'task_template_id_2'])

        from ib_tasks.populate.create_or_update_stages import \
            populate_stages_values

        # Act
        response = populate_stages_values(
            list_of_stages_dict=list_of_stages_dict)

        # Assert
        assert response == expected_stages_dto
