import mock
import pytest


class TestGetChecklistInteractor:

    @pytest.fixture()
    def storage_mock(self):
        from ib_utility_tools.interactors.storage_interfaces \
            .checklist_storage_interface import ChecklistStorageInterface
        storage = mock.create_autospec(ChecklistStorageInterface)
        return storage

    @pytest.fixture()
    def presenter_mock(self):
        from ib_utility_tools.interactors.presenter_interfaces \
            .get_checklist_presenter_interface import \
            GetChecklistPresenterInterface
        presenter = mock.create_autospec(GetChecklistPresenterInterface)
        return presenter

    @pytest.fixture()
    def interactor(self, storage_mock):
        from ib_utility_tools.interactors.get_checklist_interactor \
            import GetChecklistInteractor
        interactor = GetChecklistInteractor(checklist_storage=storage_mock)
        return interactor

    @pytest.fixture()
    def checklist_item_dtos(self):
        from ib_utility_tools.tests.factories.storage_dtos import \
            ChecklistItemWithIdDTOFactory
        checklist_item_dtos = ChecklistItemWithIdDTOFactory.create_batch(
            size=3)
        return checklist_item_dtos

    def test_given_entity_details_has_checklist_returns_checklist_response(
            self, storage_mock, presenter_mock, interactor,
            checklist_item_dtos):
        from ib_utility_tools.tests.factories.storage_dtos import \
            EntityDTOFactory
        entity_dto = EntityDTOFactory()
        checklist_id = "checklist_id1"
        storage_mock.get_checklist_id_if_exists.return_value = checklist_id
        storage_mock.get_checklist_item_dtos.return_value = checklist_item_dtos
        presenter_mock.get_response_for_get_checklist \
            .return_value = mock.Mock()

        interactor.get_checklist_wrapper(entity_dto=entity_dto,
                                         presenter=presenter_mock)

        storage_mock.get_checklist_id_if_exists.assert_called_once_with(
            entity_dto=entity_dto)
        storage_mock.get_checklist_item_dtos.assert_called_once_with(
            checklist_id=checklist_id)
        presenter_mock.get_response_for_get_checklist \
            .assert_called_once_with(
            checklist_item_dtos=checklist_item_dtos)

    def test_given_entity_details_has_no_checklist_returns_checklist_response(
            self, storage_mock, presenter_mock, interactor):
        from ib_utility_tools.tests.factories.storage_dtos import \
            EntityDTOFactory
        entity_dto = EntityDTOFactory()
        storage_mock.get_checklist_id_if_exists.return_value = None
        presenter_mock.get_response_for_get_checklist \
            .return_value = mock.Mock()

        interactor.get_checklist_wrapper(entity_dto=entity_dto,
                                         presenter=presenter_mock)

        storage_mock.get_checklist_id_if_exists.assert_called_once_with(
            entity_dto=entity_dto)
        presenter_mock.get_response_for_get_checklist \
            .assert_called_once_with(checklist_item_dtos=[])
