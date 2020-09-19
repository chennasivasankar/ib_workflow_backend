class TestCasePopulateTasks:

    @staticmethod
    def test_given_invalid_key_raises_exception():

        # Arrange
        valid_format = {
            "task_template_id": "task_template_1",
            "stage_id": "stage_1",
            "action_logic": "logic_1",
            "action_name": "action_name_1",
            "roles": "ROLE_1",
            "button_text": "button_text_1",
            "button_color": "button_color_1",
            "action_type": "NO VALIDATIONS",
            "transition_template_id": "transition_id"
        }
        import json
        import pytest
        json_valid_format = json.dumps(valid_format)
        tasks = [
            {
                "task_template_": "task_template_1",
                "stage": "stage_1",
                "action_": "logic_1",
                "action_name": "action_name_1",
                "roles": "ROLE_1",
                "button_text": "button_text_1",
                "button_color": "button_color_1",
                "action_type": "NO VALIDATIONS",
                "transition_template_id": "transition_id"
            }
        ]
        from ib_tasks.populate.populate_task_initial_stage_actions_logic \
            import populate_tasks
        from ib_tasks.exceptions.custom_exceptions import \
            InvalidFormatException

        # Act
        with pytest.raises(InvalidFormatException) as err:
            populate_tasks(tasks=tasks)

        # Assert
        assert err.value.valid_format == json_valid_format

    @staticmethod
    def test_given_invalid_python_code_in_action_logic_raises_exception():
        # Arrange
        tasks = [
            {
                "task_template_id": "task_template_1",
                "stage_id": "stage_1",
                "action_logic": "\tif : c=9",
                "action_name": "action_name_1",
                "roles": "ROLE_1",
                "button_text": "button_text_1",
                "button_color": "button_color_1",
                "action_type": "NO VALIDATIONS",
                "transition_template_id": "transition_id"
            }
        ]
        import pytest
        from ib_tasks.populate.populate_task_initial_stage_actions_logic \
            import populate_tasks
        from ib_tasks.exceptions.custom_exceptions \
            import InvalidPythonCodeException

        # Act
        with pytest.raises(InvalidPythonCodeException):
            populate_tasks(tasks=tasks)

    @staticmethod
    def test_given_valid_key_creates_dtos(mocker):
        # Arrange
        tasks = [
            {
                "task_template_id": "task_template_1",
                "stage_id": "stage_1",
                "action_logic": "logic_1",
                "action_name": "action_name_1",
                "roles": "ROLE_1",
                "button_text": "button_text_1",
                "button_color": "button_color_1",
                "action_type": "NO VALIDATIONS",
                "transition_template_id": "transition_id"
            }
        ]
        from ib_tasks.interactors.stages_dtos import TaskTemplateStageActionDTO
        expected_action_dto = [TaskTemplateStageActionDTO(
            task_template_id="task_template_1",
            stage_id="stage_1",
            action_name="action_name_1",
            logic="logic_1",
            roles=["ROLE_1"],
            function_path='ib_tasks.populate.stage_actions_logic.stage_1_action_name_1',
            button_text="button_text_1",
            button_color="button_color_1",
            action_type="NO VALIDATIONS",
            transition_template_id="transition_id"
        )]
        from ib_tasks.populate.populate_task_initial_stage_actions_logic \
            import populate_tasks
        path = "ib_tasks.interactors.configure_initial_task_template_stage_actions" \
               ".ConfigureInitialTaskTemplateStageActions.create_update_delete_stage_actions_to_task_template"
        mock_obj = mocker.patch(path)

        # Act
        populate_tasks(tasks=tasks)

        # Assert
        mock_obj.called_once()
