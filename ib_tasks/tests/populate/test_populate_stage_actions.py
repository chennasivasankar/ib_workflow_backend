from unittest import mock


class TestCasePopulateStageActions:

    @staticmethod
    def test_given_invalid_key_raises_exception():

        # Arrange

        valid_format = {
            "stage_id": "stage_1",
            "action_logic": "logic_1",
            "action_name": "action_name_1",
            "roles": "ROLE_1, ROLE_2",
            "button_text": "button_text_1",
            "button_color": "button_color_1"
        }
        import json
        import pytest
        json_valid_format = json.dumps(valid_format)
        actions = [
            {
                "stage": "stage_1",
                "stage_display_logic": "logic_1",
                "action_name": "action_name_1",
                "roles": "ROLE_1",
                "button_text": "button_text_1",
                "button_color": "button_color_1"
            }
        ]
        from ib_tasks.populate.populate_stage_actions \
            import populate_stage_actions
        from ib_tasks.exceptions.stage_custom_exceptions import InvalidFormatException

        # Act
        with pytest.raises(InvalidFormatException) as err:
            populate_stage_actions(action_dicts=actions)

        # Assert
        assert err.value.valid_format == json_valid_format

    @staticmethod
    def test_given_invalid_python_code_raises_exception():

        # Arrange
        actions = [
            {
                "stage_id": "stage_1",
                "action_logic": "if a> b c=8",
                "action_name": "action_name_1",
                "roles": "ROLE_1",
                "button_text": "button_text_1",
                "button_color": "button_color_1"
            }
        ]
        import pytest
        from ib_tasks.populate.populate_stage_actions \
            import populate_stage_actions
        from ib_tasks.exceptions.stage_custom_exceptions import InvalidPythonCodeException

        # Act
        with pytest.raises(InvalidPythonCodeException):
            populate_stage_actions(action_dicts=actions)

    @staticmethod
    @mock.patch('builtins.open', new_callable=mock.mock_open)
    def test_given_valid_key_creates_dtos(os_system):
        # Arrange
        actions = [
            {
                "stage_id": "stage_1",
                "action_logic": "logic_1",
                "action_name": "action_name_1",
                "roles": "ROLE_1",
                "button_text": "button_text_1",
                "button_color": "button_color_1"
            }
        ]
        from ib_tasks.interactors.stages_dtos import StageActionDTO
        expected_action_dto = [StageActionDTO(
            stage_id="stage_1",
            action_name="action_name_1",
            logic="logic_1",
            roles=["ROLE_1"],
            function_path='ib_tasks.populate.stage_actions_logic.stage_1_action_name_1',
            button_text="button_text_1",
            button_color="button_color_1"
        )]
        from ib_tasks.populate.populate_stage_actions \
            import populate_stage_actions

        # Act
        response = populate_stage_actions(action_dicts=actions)

        # Assert
        assert response == expected_action_dto
        os_system.assert_called_with(
            'ib_tasks/populate/stage_actions_logic.py', 'a')
