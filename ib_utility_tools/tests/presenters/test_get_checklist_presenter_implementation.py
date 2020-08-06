import json

import pytest

from ib_utility_tools.presenters \
    .get_checklist_presenter_implementation import \
    GetChecklistPresenterImplementation


class TestGetChecklistPresenterImplementation:

    @pytest.fixture()
    def checklist_item_dtos(self):
        from ib_utility_tools.tests.factories.storage_dtos import \
            ChecklistItemWithIdDTOFactory
        checklist_item_dtos = ChecklistItemWithIdDTOFactory.create_batch(
            size=3)
        return checklist_item_dtos

    def test_whether_it_returns_checklist_items_and_entity_http_response(
            self, checklist_item_dtos, snapshot):
        json_presenter = GetChecklistPresenterImplementation()
        from ib_utility_tools.tests.factories.storage_dtos import \
            EntityDTOFactory
        entity_dto = EntityDTOFactory()

        http_response = json_presenter.get_success_response_for_get_checklist(
            entity_dto=entity_dto, checklist_item_dtos=checklist_item_dtos)

        response = json.loads(http_response.content)

        snapshot.assert_match(response, "response")
