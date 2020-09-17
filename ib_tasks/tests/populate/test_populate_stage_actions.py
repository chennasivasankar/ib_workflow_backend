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
            "button_color": "button_color_1",
            "action_type": "NO VALIDATIONS",
            "transition_template_id": "transition_id"
        }
        import json
        import pytest
        json_valid_format = json.dumps(valid_format)
        actions = [
            {
                "stage_id": "stage_1",
                "action_logic": "logic_1",
                "invalid_key": "action_name_1",
                "roles": "ROLE_1, ROLE_2",
                "button_text": "button_text_1",
                "button_color": "button_color_1",
                "action_type": "NO VALIDATIONS",
                "transition_template_id": "transition_id"
            }
        ]
        from ib_tasks.populate.populate_stage_actions \
            import populate_stage_actions
        from ib_tasks.exceptions.custom_exceptions import \
            InvalidFormatException

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
                "roles": "ROLE_1, ROLE_2",
                "button_text": "button_text_1",
                "button_color": "button_color_1",
                "action_type": "NO VALIDATIONS",
                "transition_template_id": "transition_id"
            }
        ]
        import pytest
        from ib_tasks.populate.populate_stage_actions \
            import populate_stage_actions
        from ib_tasks.exceptions.custom_exceptions \
            import InvalidPythonCodeException

        # Act
        with pytest.raises(InvalidPythonCodeException):
            populate_stage_actions(action_dicts=actions)

    @staticmethod
    def test_given_valid_key_creates_dtos(mocker):
        # Arrange
        
        actions = [
            {
                "stage_id": "stage_1",
                "action_logic": "logic_1",
                "action_name": "action_name_1",
                "roles": "ROLE_1\nROLE_2",
                "button_text": "button_text_1",
                "button_color": "button_color_1",
                "action_type": "NO VALIDATIONS",
                "transition_template_id": "transition_id"
            }
        ]
        from ib_tasks.interactors.stages_dtos import StageActionDTO
        expected_action_dto = [StageActionDTO(
            stage_id="stage_1",
            action_name="action_name_1",
            logic="logic_1",
            roles=["ROLE_1", "ROLE_2"],
            function_path='ib_tasks.populate.stage_actions_logic.stage_1_action_name_1',
            button_text="button_text_1",
            button_color="button_color_1",
            action_type="NO VALIDATIONS",
            transition_template_id="transition_id"
        )]
        from ib_tasks.populate.populate_stage_actions \
            import populate_stage_actions
        path = "ib_tasks.interactors.create_or_update_or_delete_stage_actions.CreateOrUpdateOrDeleteStageActions" \
               ".create_or_update_or_delete_stage_actions"
        mock_obj = mocker.patch(path)

        # Act
        populate_stage_actions(action_dicts=actions)

        # Assert
        mock_obj.assert_called_once_with(
            action_dtos=expected_action_dto
        )
