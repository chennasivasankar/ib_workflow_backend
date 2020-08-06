from uuid import UUID

import mock
import pytest

from ib_utility_tools.models import ChecklistItem


@pytest.mark.django_db
class TestChecklistStorageImplementation:
    @pytest.fixture()
    def storage(self):
        from ib_utility_tools.storages.checklist_storage_implementation \
            import ChecklistStorageImplementation
        storage = ChecklistStorageImplementation()
        return storage

    @pytest.fixture
    def create_checklists(self):
        checklist_ids = ['2bdb417e-4632-419a-8ddd-085ea272c6eb',
                         '548a803c-7b48-47ba-a700-24f2ea0d1280',
                         '4b8fb6eb-fa7d-47c1-8726-cd917901104e']
        from ib_utility_tools.tests.factories.models import ChecklistFactory
        checklist_objects = [
            ChecklistFactory.create(checklist_id=checklist_id)
            for checklist_id in checklist_ids
        ]
        return checklist_objects

    @pytest.fixture
    def create_checklist_items(self):
        checklist_item_ids = ['7ee2c7b4-34c8-4d65-a83a-f87da75db24e',
                              '09b6cf6d-90ea-43ac-b0ee-3cee3c59ce5a',
                              '8bcf545d-4573-4bc2-b037-16c856d37287',
                              "f2c02d98-f311-4ab2-8673-3daa00757002",
                              "155f3fa1-e4eb-4bfa-89e7-ca80edd23a6e"]
        from ib_utility_tools.tests.factories.models import \
            ChecklistItemFactory
        checklist_item_objects = [
            ChecklistItemFactory.create(checklist_item_id=checklist_item_id)
            for checklist_item_id in checklist_item_ids
        ]
        return checklist_item_objects

    @pytest.fixture
    def create_checklist(self):
        checklist_id = '2bdb417e-4632-419a-8ddd-085ea272c6eb'
        from ib_utility_tools.tests.factories.models import ChecklistFactory
        ChecklistFactory.create(checklist_id=checklist_id)
        return checklist_id

    def test_create_checklist_item_returns_checklist_item_id(
            self, storage, create_checklist):
        checklist_id = create_checklist
        from ib_utility_tools.tests.factories.storage_dtos import \
            ChecklistItemWithChecklistIdDTOFactory
        checklist_item_with_checklist_id_dto = \
            ChecklistItemWithChecklistIdDTOFactory(checklist_id=checklist_id)
        expected_text = checklist_item_with_checklist_id_dto.text
        expected_is_checked = checklist_item_with_checklist_id_dto.is_checked

        checklist_item_id = storage.create_checklist_item(
            checklist_item_with_checklist_id_dto=
            checklist_item_with_checklist_id_dto)

        checklist_item_object = ChecklistItem.objects.get(
            checklist_item_id=checklist_item_id)
        assert checklist_item_object.text == expected_text
        assert checklist_item_object.is_checked == expected_is_checked

    def test_get_checklist_id_if_exists_returns_checklist_id(
            self, storage, create_checklist):
        from ib_utility_tools.tests.factories.models import ChecklistFactory
        from ib_utility_tools.tests.factories.storage_dtos import \
            EntityDTOFactory
        checklist_id = '2bdb417e-4632-419a-8ddd-085ea272c6eb'
        checklist_object = ChecklistFactory.create(checklist_id=checklist_id)
        entity_dto = EntityDTOFactory(entity_id=checklist_object.entity_id,
                                      entity_type=checklist_object.entity_type)

        checklist_id = storage.create_checklist(
            entity_dto=entity_dto)

        checklist_item_object = ChecklistItem.objects.get(
            checklist_item_id=checklist_item_id)
        assert checklist_item_object.text == expected_text
        assert checklist_item_object.is_checked == expected_is_checked
