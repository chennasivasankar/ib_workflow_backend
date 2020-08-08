import pytest

from ib_tasks.interactors.presenter_interfaces.dtos import \
    AllTasksOverviewDetailsDTO
from ib_tasks.presenters.get_all_tasks_overview_for_user_presenter_impl import \
    GetAllTasksOverviewForUserPresenterImpl
from ib_tasks.tests.factories.presenter_dtos import \
    TaskIdWithStageDetailsDTOFactory, GetTaskStageCompleteDetailsDTOFactory, \
    TaskWithCompleteStageDetailsDTOFactory
from ib_tasks.tests.factories.storage_dtos import FieldDetailsDTOFactory, \
    StageActionDetailsDTOFactory


class TestGetAllTasksOverviewForUserPresenterImpl:
    def test_raise_exception_for_limit_less_than_zero(self):
        # Arrange
        from ib_tasks.constants.exception_messages import \
            LIMIT_SHOULD_BE_GREATER_THAN_ZERO
        expected_response = LIMIT_SHOULD_BE_GREATER_THAN_ZERO[0]
        response_status_code = LIMIT_SHOULD_BE_GREATER_THAN_ZERO[1]

        presenter = GetAllTasksOverviewForUserPresenterImpl()
        # Act
        response_object = presenter. \
            raise_limit_should_be_greater_than_zero_exception()
        # Assert
        import json
        response = json.loads(response_object.content)
        assert response['http_status_code'] == 400
        assert response['res_status'] == response_status_code
        assert response['response'] == expected_response

    def test_raise_exception_for_offset_less_than_zero(self):
        # Arrange
        from ib_tasks.constants.exception_messages import \
            OFFSET_SHOULD_BE_GREATER_THAN_ZERO
        expected_response = \
            OFFSET_SHOULD_BE_GREATER_THAN_ZERO[0]
        response_status_code = \
            OFFSET_SHOULD_BE_GREATER_THAN_ZERO[1]

        presenter = GetAllTasksOverviewForUserPresenterImpl()
        # Act
        response_object = presenter. \
            raise_offset_should_be_greater_than_zero_exception()
        # Assert
        import json
        response = json.loads(response_object.content)
        assert response['http_status_code'] == 400
        assert response['res_status'] == response_status_code
        assert response['response'] == expected_response

    def test_raise_exception_when_given_empty_stage_ids_list(self):
        # Arrange
        from ib_tasks.constants.exception_messages import \
            EMPTY_STAGE_IDS_ARE_INVALID
        expected_response = \
            EMPTY_STAGE_IDS_ARE_INVALID[0]
        response_status_code = \
            EMPTY_STAGE_IDS_ARE_INVALID[1]

        presenter = GetAllTasksOverviewForUserPresenterImpl()
        # Act
        response_object = presenter. \
            raise_stage_ids_empty_exception()
        # Assert
        import json
        response = json.loads(response_object.content)
        assert response['http_status_code'] == 400
        assert response['res_status'] == response_status_code
        assert response['response'] == expected_response

    @pytest.fixture
    def all_tasks_overview_details_response_dict(self):
        all_tasks_overview_details_response_dict = {
            "tasks": [{
                "task_id":
                    "task_1",
                "task_overview_fields": [{
                    "field_type": "Drop down",
                    "field_display_name": "key",
                    "field_response": "value"
                }],
                "stage_with_actions": {
                    "stage_id": 1,
                    "stage_display_name":
                        "stage_display_1",
                    "stage_color": "color_1",
                    "actions": [{
                        "action_id": 1,
                        "button_text": "button_text_1",
                        'action_type': 'action_type_1',
                        'transition_template_id': 'template_id_1',
                        "button_color": None
                    }, {
                        "action_id": 2,
                        "button_text": "button_text_2",
                        'action_type': 'action_type_2',
                        'transition_template_id': 'template_id_2',
                        "button_color": None
                    }]
                }
            }, {
                "task_id":
                    "task_2",
                "task_overview_fields": [{
                    "field_type": "Drop down",
                    "field_display_name": "key",
                    "field_response": "value"
                }],
                "stage_with_actions": {
                    "stage_id": 2,
                    "stage_display_name":
                        "stage_display_2",
                    "stage_color": "color_2",
                    "actions": [{
                        "action_id": 1,
                        'action_type': 'action_type_1',
                        'transition_template_id': 'template_id_1',
                        "button_text": "button_text_1",
                        "button_color": None
                    }, {
                        "action_id": 2,
                        'action_type': 'action_type_2',
                        'transition_template_id': 'template_id_2',
                        "button_text": "button_text_2",
                        "button_color": None
                    }]
                }
            }],
            "total_tasks":
                2
        }
        return all_tasks_overview_details_response_dict

    def test_given_valid_details_get_all_tasks_overview_details_response(
            self, all_tasks_overview_details_response_dict):
        #Arrange
        TaskIdWithStageDetailsDTOFactory.reset_sequence()
        GetTaskStageCompleteDetailsDTOFactory.reset_sequence()
        FieldDetailsDTOFactory.reset_sequence()
        StageActionDetailsDTOFactory.reset_sequence()
        TaskWithCompleteStageDetailsDTOFactory.reset_sequence()
        task_with_complete_stage_details_dtos = \
            TaskWithCompleteStageDetailsDTOFactory.create_batch(2)

        task_fields_and_action_details_dtos = \
            GetTaskStageCompleteDetailsDTOFactory. \
                create_batch(2, field_dtos=[FieldDetailsDTOFactory()],
                             action_dtos=StageActionDetailsDTOFactory.create_batch(
                                 2))

        all_tasks_overview_details_dto = AllTasksOverviewDetailsDTO(
            task_with_complete_stage_details_dtos=
                task_with_complete_stage_details_dtos,
            task_fields_and_action_details_dtos=
            task_fields_and_action_details_dtos)

        presenter = GetAllTasksOverviewForUserPresenterImpl()
        # Act
        response_object = presenter.all_tasks_overview_details_response(
            all_tasks_overview_details_dto)

        # Assert
        import json
        response = json.loads(response_object.content)
        assert response == all_tasks_overview_details_response_dict
