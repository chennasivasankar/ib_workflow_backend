import pytest

from ib_utility_tools.models import ChecklistItem, Checklist
from ib_utility_tools.tests.factories.models import \
    ChecklistItemFactory, ChecklistFactory


class TestChecklistStorageImplementation:
    @pytest.fixture()
    def storage(self):
        from ib_utility_tools.storages.checklist_storage_implementation \
            import ChecklistStorageImplementation
        storage = ChecklistStorageImplementation()
        return storage

    @pytest.fixture
    def create_checklist_items_for_checklist_id(self):
        checklist_item_ids = ['7ee2c7b4-34c8-4d65-a83a-f87da75db24e',
                              '09b6cf6d-90ea-43ac-b0ee-3cee3c59ce5a']
        checklist_id = '2bdb417e-4632-419a-8ddd-085ea272c6eb'
        checklist_object = ChecklistFactory.create(checklist_id=checklist_id)
        from ib_utility_tools.tests.factories.models import \
            ChecklistItemFactory
        ChecklistItemFactory.reset_sequence(1)
        _ = [
            ChecklistItemFactory.create(checklist_item_id=checklist_item_id,
                                        checklist=checklist_object)
            for checklist_item_id in checklist_item_ids
        ]
        return checklist_id

    @pytest.fixture
    def expected_checklist_item_dtos(self):
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

    @pytest.fixture
    def create_checklist(self):
        checklist_id = '2bdb417e-4632-419a-8ddd-085ea272c6eb'
        ChecklistFactory.create(checklist_id=checklist_id)
        return checklist_id

    @pytest.mark.django_db
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

    @pytest.mark.django_db
    def test_get_checklist_id_if_exists_returns_checklist_id(
            self, storage):
        # todo:Can parametrize test for getting None as response too
        from ib_utility_tools.tests.factories.storage_dtos import \
            EntityDTOFactory
        checklist_id = '2bdb417e-4632-419a-8ddd-085ea272c6eb'
        entity_dto = EntityDTOFactory()
        ChecklistFactory.create(checklist_id=checklist_id,
                                entity_id=entity_dto.entity_id,
                                entity_type=entity_dto.entity_type)

        actual_checklist_id = storage.get_checklist_id_if_exists(
            entity_dto=entity_dto)

        assert actual_checklist_id == checklist_id

    @pytest.mark.django_db
    def test_create_checklist_returns_checklist_id(
            self, storage):
        from ib_utility_tools.tests.factories.storage_dtos import \
            EntityDTOFactory
        entity_dto = EntityDTOFactory()

        checklist_id = storage.create_checklist(entity_dto=entity_dto)

        checklist_object = Checklist.objects.get(checklist_id=checklist_id)

        assert checklist_object.entity_id == entity_dto.entity_id
        assert checklist_object.entity_type == entity_dto.entity_type

    @pytest.mark.django_db
    def test_update_checklist_item_updates_checklist_item(
            self, storage):
        from ib_utility_tools.tests.factories.storage_dtos import \
            ChecklistItemWithIdDTOFactory
        checklist_item_id = '2bdb417e-4632-419a-8ddd-085ea272c6eb'
        checklist_item_with_id_dto = ChecklistItemWithIdDTOFactory(
            checklist_item_id=checklist_item_id, is_checked=True)
        ChecklistItemFactory.create(checklist_item_id=checklist_item_id)

        storage.update_checklist_item(
            checklist_item_with_id_dto=checklist_item_with_id_dto)

        checklist_object = ChecklistItem.objects.get(
            checklist_item_id=checklist_item_id)

        assert checklist_object.text == checklist_item_with_id_dto.text
        assert checklist_object.is_checked == \
               checklist_item_with_id_dto.is_checked

    @pytest.mark.django_db
    @pytest.mark.parametrize("checklist_item_id_to_search, expected_value",
                             [('2bdb417e-4632-419a-8ddd-085ea272c6eb', True),
                              ('f2c02d98-f311-4ab2-8673-3daa00757002', False)])
    def test_validate_checklist_item_id_returns_true_or_false(
            self, storage, checklist_item_id_to_search, expected_value):
        checklist_item_id = '2bdb417e-4632-419a-8ddd-085ea272c6eb'
        ChecklistItemFactory.create(checklist_item_id=checklist_item_id)

        actual_value = storage.is_checklist_item_id_exists(
            checklist_item_id=checklist_item_id_to_search)

        assert actual_value == expected_value

    @pytest.mark.django_db
    def test_get_checklist_items_dto(self, storage,
                                     create_checklist_items_for_checklist_id,
                                     expected_checklist_item_dtos):
        checklist_id = create_checklist_items_for_checklist_id

        checklist_item_dtos = storage.get_checklist_item_dtos(
            checklist_id=checklist_id)

        assert checklist_item_dtos == expected_checklist_item_dtos
