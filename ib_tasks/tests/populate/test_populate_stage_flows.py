from unittest import mock


class TestCasePopulateStageFlows:

    @staticmethod
    def test_given_invalid_key_raises_exception():
        # Arrange

        valid_format = {
            "previous_stage_id": "stage_1",
            "action_name": "Submit",
            "next_stage_id": "stage_2"
        }
        import json
        import pytest
        json_valid_format = json.dumps(valid_format)
        stage_flow_dicts = [
            {
                "previous_id": "stage_1",
                "action_name": "Submit",
                "next_stage_id": "stage_2"
            }
        ]
        from ib_tasks.populate.populate_stage_flows import populate_stage_flows
        from ib_tasks.exceptions.custom_exceptions import \
            InvalidFormatException

        # Act
        with pytest.raises(InvalidFormatException) as err:
            populate_stage_flows(stage_flow_dicts=stage_flow_dicts)

        # Assert
        assert err.value.valid_format == json_valid_format

    @staticmethod
    def test_given_valid_key_creates_dtos(mocker):
        # Arrange
        stage_flow_dicts = [
            {
                "previous_stage_id": "stage_0",
                "action_name": "action_name_0",
                "next_stage_id": "stage_1"
            }
        ]
        from ib_tasks.tests.factories.interactor_dtos import CreateStageFlowDTOFactory
        CreateStageFlowDTOFactory.reset_sequence()
        stage_flow_dtos = CreateStageFlowDTOFactory.create_batch(1)
        from ib_tasks.populate.populate_stage_flows import populate_stage_flows
        path = "ib_tasks.interactors.create_stage_flow_interactor.CreateStageFlowInteractor.create_stage_flows"
        mock_obj = mocker.patch(path)

        # Act
        populate_stage_flows(stage_flow_dicts=stage_flow_dicts)

        # Assert
        mock_obj.assert_called_once_with(stage_flow_dtos=stage_flow_dtos)