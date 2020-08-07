import json

import pytest

from ib_tasks.models import Stage
from ib_tasks.tests.factories.models import TaskStatusVariableFactory, GoFFactory, TaskTemplateFactory, \
    GoFToTaskTemplateFactory, FieldFactory, StageModelFactory


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
            "stage_color": "blue",
            "roles": "ALL_ROLES\nFIN_PAYMENT_REQUESTER",
            "stage_display_name": "stage_name",
            "stage_display_logic": "status_1==stage_id_1"
        }

        json_valid_format = json.dumps(valid_format)
        return json_valid_format

    @pytest.fixture()
    def expected_stages_dto(self):
        from ib_tasks.tests.factories.storage_dtos import StageDTOFactory
        StageDTOFactory.reset_sequence()
        return StageDTOFactory.create_batch(size=2)

    @pytest.fixture()
    def create_data(self):
        StageModelFactory.reset_sequence(1)
        StageModelFactory()
        TaskStatusVariableFactory.reset_sequence()
        TaskStatusVariableFactory.create_batch(size=15)
        GoFFactory.reset_sequence()
        gof_obj = GoFFactory()
        TaskTemplateFactory.reset_sequence()
        task_obj1 = TaskTemplateFactory(template_id="task_template_id_1")
        task_obj2 = TaskTemplateFactory(template_id="task_template_id_2")
        GoFToTaskTemplateFactory.reset_sequence()
        GoFToTaskTemplateFactory(gof=gof_obj, task_template=task_obj1)
        GoFToTaskTemplateFactory(gof=gof_obj, task_template=task_obj2)
        FieldFactory.reset_sequence()
        FieldFactory(field_id="field_id_1", gof=gof_obj)
        FieldFactory(field_id="field_id_2", gof=gof_obj)

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
                "stage_color": "blue",
                "roles": "ALL_ROLES\nFIN_PAYMENT_REQUESTER",
                "stage_display_name": "stage_name",
                "stage_display_logic": "status_1==stage_id_1"
            },
            {
                "task_template_id": "task_template_id_2",
                "stage_id": "stage_id_2",
                "values": -1,
                "card_info_kanban": json.dumps(["field_id_1", "field_id_2"]),
                "card_info_list": json.dumps(["field_id_1", "field_id_2"]),
                "stage_color": "blue",
                "roles": "ALL_ROLES\nFIN_PAYMENT_REQUESTER",
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
                                                        mocker,
                                                        snapshot,
                                                        create_data):
        # Arrange
        stage_ids = ["stage_id_2", "stage_id_3"]
        expected_stages_dto = expected_stages_dto
        list_of_stages_dict = [
            {
                "task_template_id": "task_template_id_1",
                "stage_id": "stage_id_2",
                "value": 1,
                "card_info_kanban": json.dumps(["field_id_1", "field_id_2"]),
                "card_info_list": json.dumps(["field_id_1", "field_id_2"]),
                "stage_color": "blue",
                "roles": "role_id_0\nrole_id_1",
                "stage_display_name": "name_1",
                "stage_display_logic": "status_id_1==stage_id"
            },
            {
                "task_template_id": "task_template_id_2",
                "stage_id": "stage_id_3",
                "value": 2,
                "card_info_kanban": json.dumps(["field_id_1", "field_id_2"]),
                "card_info_list": json.dumps(["field_id_1", "field_id_2"]),
                "stage_color": "blue",
                "roles": "role_id_0\nrole_id_1",
                "stage_display_name": "name_2",
                "stage_display_logic": "status_id_2==stage_id"
            }
        ]
        from ib_tasks.tests.common_fixtures.adapters.roles_service \
            import get_valid_role_ids_in_given_role_ids
        mocker_obj = get_valid_role_ids_in_given_role_ids(mocker)
        mocker_obj.return_value = ["role_id_1", "role_id_2", "role_id_0"]
        from ib_tasks.tests.common_fixtures.storages import mock_storage
        mock_storage(mocker, ['task_template_id_1', 'task_template_id_2'])

        from ib_tasks.populate.create_or_update_stages import \
            populate_stages_values

        # Act
        response = populate_stages_values(
            list_of_stages_dict=list_of_stages_dict)

        # Assert
        stages = list(Stage.objects.filter(stage_id__in=stage_ids).values())
        snapshot.assert_match(stages, "populated_stages")
