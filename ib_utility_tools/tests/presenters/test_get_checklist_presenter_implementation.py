import json

import pytest

from ib_utility_tools.presenters \
    .get_checklist_presenter_implementation import \
    GetChecklistPresenterImplementation


class TestGetChecklistPresenterImplementation:

    @pytest.fixture
    def checklist_item_dtos(self):
        checklist_item_ids = ['7ee2c7b4-34c8-4d65-a83a-f87da75db24e',
                              '09b6cf6d-90ea-43ac-b0ee-3cee3c59ce5a']
        from ib_utility_tools.tests.factories.storage_dtos import \
            ChecklistItemWithIdDTOFactory
        ChecklistItemWithIdDTOFactory.reset_sequence(1)
        checklist_item_dtos = [
            ChecklistItemWithIdDTOFactory(checklist_item_id=checklist_item_id)
            for checklist_item_id in checklist_item_ids
        ]
        return checklist_item_dtos

    def test_whether_it_returns_checklist_items_and_entity_http_response(
            self, checklist_item_dtos, snapshot):
        json_presenter = GetChecklistPresenterImplementation()
        from ib_utility_tools.tests.factories.storage_dtos import \
            EntityDTOFactory
        entity_dto = EntityDTOFactory(
            entity_id='bb3e538e-a18a-4268-b2d6-0b6dba669ba0')

        http_response = json_presenter.get_success_response_for_get_checklist(
            entity_dto=entity_dto, checklist_item_dtos=checklist_item_dtos)

        response = json.loads(http_response.content)

        snapshot.assert_match(response, "response")
