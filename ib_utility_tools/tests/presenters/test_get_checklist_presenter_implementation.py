import json
import pytest


class TestGetChecklistPresenterImplementation:
    @pytest.fixture
    def presenter(self):
        from ib_utility_tools.presenters.get_checklist_presenter_implementation import (
            GetChecklistPresenterImplementation
        )
        presenter = GetChecklistPresenterImplementation()
        return presenter

    @pytest.fixture
    def checklist_item_dtos(self):
        checklist_item_ids = [
            '7ee2c7b4-34c8-4d65-a83a-f87da75db24e',
            '09b6cf6d-90ea-43ac-b0ee-3cee3c59ce5a'
        ]
        from ib_utility_tools.tests.factories.storage_dtos import (
            ChecklistItemWithIdDTOFactory
        )
        ChecklistItemWithIdDTOFactory.reset_sequence(0)
        checklist_item_dtos = [
            ChecklistItemWithIdDTOFactory(checklist_item_id=checklist_item_id)
            for checklist_item_id in checklist_item_ids
        ]
        return checklist_item_dtos

    def test_with_valid_details_then_returns_response(
            self, checklist_item_dtos, presenter, snapshot
    ):
        # Act
        http_response = presenter.get_response_for_get_checklist(
            checklist_item_dtos=checklist_item_dtos
        )

        # Assert
        response = json.loads(http_response.content)
        snapshot.assert_match(response, "response")
