import json

import pytest


class TestCreateChecklistItemPresenterImplementation:
    @pytest.fixture
    def presenter(self):
        from ib_utility_tools.presenters.create_checklist_item_presenter_implementation import (
            CreateChecklistItemPresenterImplementation
        )
        return CreateChecklistItemPresenterImplementation()

    def test_with_valid_details_then_returns_checklist_id_response(self,
                                                                   presenter):
        # Arrange
        checklist_item_id = "checklist_item_id"
        expected_response = {"checklist_item_id": checklist_item_id}

        # Act
        result = presenter.get_response_for_create_checklist_item(
            checklist_item_id=checklist_item_id
        )

        # Assert
        actual_response = json.loads(result.content)
        assert actual_response == expected_response
