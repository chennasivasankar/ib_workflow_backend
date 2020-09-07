import mock
import pytest

from ib_utility_tools.tests.factories.storage_dtos import \
    ChecklistItemWithEntityDTOFactory


class TestCreateChecklistItemInteractor:

    @pytest.fixture()
    def storage_mock(self):
        from ib_utility_tools.interactors.storage_interfaces \
            .checklist_storage_interface import ChecklistStorageInterface
        storage = mock.create_autospec(ChecklistStorageInterface)
        return storage

    @pytest.fixture()
    def presenter_mock(self):
        from ib_utility_tools.interactors.presenter_interfaces \
            .create_checklist_item_presenter_interface import \
            CreateChecklistItemPresenterInterface
        presenter = mock.create_autospec(CreateChecklistItemPresenterInterface)
        return presenter

    @pytest.fixture()
    def interactor(self, storage_mock):
        from ib_utility_tools.interactors.create_checklist_item_interactor \
            import CreateChecklistItemInteractor
        interactor = CreateChecklistItemInteractor(
            checklist_storage=storage_mock)
        return interactor

    def test_given_item_text_is_empty_returns_empty_text_exception_response(
            self, interactor, storage_mock, presenter_mock):
        checklist_item_with_entity_dto = ChecklistItemWithEntityDTOFactory(
            text="")
        presenter_mock.response_for_empty_checklist_item_text_exception = \
            mock.Mock()

        interactor.create_checklist_item_wrapper(
            checklist_item_with_entity_dto=checklist_item_with_entity_dto,
            presenter=presenter_mock)

        presenter_mock.response_for_empty_checklist_item_text_exception \
            .assert_called_once()

    def test_item_text_has_only_spaces_returns_empty_text_exception_response(
            self, interactor, storage_mock, presenter_mock):
        checklist_item_with_entity_dto = ChecklistItemWithEntityDTOFactory(
            text="")
        presenter_mock.response_for_empty_checklist_item_text_exception = \
            mock.Mock()

        interactor.create_checklist_item_wrapper(
            checklist_item_with_entity_dto=checklist_item_with_entity_dto,
            presenter=presenter_mock)

        presenter_mock.response_for_empty_checklist_item_text_exception \
            .assert_called_once()

    def test_given_details_already_has_checklist_returns_success_response(
            self, interactor, storage_mock, presenter_mock):
        from ib_utility_tools.tests.factories.storage_dtos import \
            ChecklistItemWithChecklistIdDTOFactory, EntityDTOFactory
        entity_id = "entity1"
        checklist_id = "checklist_id1"
        checklist_item_id = "checklist_item_id1"
        text_for_checklist_item = "text_for_item"
        checklist_item_with_entity_dto = ChecklistItemWithEntityDTOFactory(
            text=text_for_checklist_item, entity_id=entity_id)
        entity_dto = EntityDTOFactory(entity_id=entity_id)
        checklist_item_with_checklist_id_dto = \
            ChecklistItemWithChecklistIdDTOFactory(
                checklist_id=checklist_id, text=text_for_checklist_item)
        storage_mock.get_checklist_id_if_exists.return_value = checklist_id
        storage_mock.create_checklist_item.return_value = checklist_item_id
        presenter_mock.get_success_response_for_create_checklist_item = mock.Mock()

        interactor.create_checklist_item_wrapper(
            checklist_item_with_entity_dto=checklist_item_with_entity_dto,
            presenter=presenter_mock)

        storage_mock.get_checklist_id_if_exists.assert_called_once_with(
            entity_dto=entity_dto)
        storage_mock.create_checklist_item.assert_called_once_with(
            checklist_item_with_checklist_id_dto=
            checklist_item_with_checklist_id_dto)
        presenter_mock.get_success_response_for_create_checklist_item \
            .assert_called_once()

    def test_given_details_has_no_checklist_before_returns_success_response(
            self, interactor, storage_mock, presenter_mock):
        from ib_utility_tools.tests.factories.storage_dtos import \
            ChecklistItemWithChecklistIdDTOFactory, EntityDTOFactory
        entity_id = "entity1"
        checklist_id = "checklist_id1"
        checklist_item_id = "checklist_item_id1"
        text_for_checklist_item = "text_for_item"
        checklist_item_with_entity_dto = ChecklistItemWithEntityDTOFactory(
            text=text_for_checklist_item, entity_id=entity_id)
        entity_dto = EntityDTOFactory(entity_id=entity_id)
        checklist_item_with_checklist_id_dto = \
            ChecklistItemWithChecklistIdDTOFactory(
                checklist_id=checklist_id, text=text_for_checklist_item)
        storage_mock.get_checklist_id_if_exists.return_value = None
        storage_mock.create_checklist.return_value = checklist_id
        storage_mock.create_checklist_item.return_value = checklist_item_id
        presenter_mock.get_success_response_for_create_checklist_item = mock.Mock()

        interactor.create_checklist_item_wrapper(
            checklist_item_with_entity_dto=checklist_item_with_entity_dto,
            presenter=presenter_mock)

        storage_mock.create_checklist.assert_called_once_with(
            entity_dto=entity_dto)
        storage_mock.create_checklist_item.assert_called_once_with(
            checklist_item_with_checklist_id_dto=
            checklist_item_with_checklist_id_dto)
        presenter_mock.get_success_response_for_create_checklist_item \
            .assert_called_once()
