import mock
import pytest

from ib_utility_tools.tests.factories.storage_dtos import (
    ChecklistItemWithIdDTOFactory
)


class TestUpdateChecklistItemInteractor:

    @pytest.fixture()
    def storage_mock(self):
        from ib_utility_tools.interactors.storage_interfaces.checklist_storage_interface import (
            ChecklistStorageInterface
        )
        storage = mock.create_autospec(ChecklistStorageInterface)
        return storage

    @pytest.fixture()
    def presenter_mock(self):
        from ib_utility_tools.interactors.presenter_interfaces.checklist_presenter_interface import (
            UpdateChecklistItemPresenterInterface
        )
        presenter = mock.create_autospec(UpdateChecklistItemPresenterInterface)
        return presenter

    @pytest.fixture()
    def interactor(self, storage_mock):
        from ib_utility_tools.interactors.update_checklist_item_interactor import (
            UpdateChecklistItemInteractor
        )
        interactor = UpdateChecklistItemInteractor(
            checklist_storage=storage_mock
        )
        return interactor

    def test_given_item_text_is_empty_returns_empty_text_exception_response(
            self, interactor, storage_mock, presenter_mock
    ):
        # Arrange
        checklist_item_with_id_dto = ChecklistItemWithIdDTOFactory(text="")
        presenter_mock.response_for_empty_checklist_item_text_exception = mock.Mock()

        # Act
        interactor.update_checklist_item_wrapper(
            checklist_item_with_id_dto=checklist_item_with_id_dto,
            presenter=presenter_mock
        )

        # Assert
        presenter_mock.response_for_empty_checklist_item_text_exception.assert_called_once()

    def test_item_text_has_only_spaces_returns_empty_text_exception_response(
            self, interactor, storage_mock, presenter_mock
    ):
        # Arrange
        checklist_item_with_id_dto = ChecklistItemWithIdDTOFactory(text="   ")
        presenter_mock.response_for_empty_checklist_item_text_exception = mock.Mock()

        # Act
        interactor.update_checklist_item_wrapper(
            checklist_item_with_id_dto=checklist_item_with_id_dto,
            presenter=presenter_mock)

        # Assert
        presenter_mock.response_for_empty_checklist_item_text_exception \
            .assert_called_once()

    def test_given_invalid_checklist_item_id_returns_checklist_item_id_not_found_exception_response(
            self, interactor, storage_mock, presenter_mock
    ):
        # Arrange
        checklist_item_with_id_dto = ChecklistItemWithIdDTOFactory()
        storage_mock.is_checklist_item_id_exists.return_value = False
        presenter_mock.get_checklist_item_id_not_found_response = mock.Mock()

        # Act
        interactor.update_checklist_item_wrapper(
            checklist_item_with_id_dto=checklist_item_with_id_dto,
            presenter=presenter_mock
        )

        # Assert
        storage_mock.is_checklist_item_id_exists.assert_called_once_with(
            checklist_item_id=checklist_item_with_id_dto.checklist_item_id
        )
        presenter_mock.get_checklist_item_id_not_found_response.assert_called_once()

    def test_given_valid_details_returns_success_response(
            self, interactor, storage_mock, presenter_mock
    ):
        # Arrange
        checklist_item_with_id_dto = ChecklistItemWithIdDTOFactory()
        presenter_mock.get_checklist_item_id_not_found_response = mock.Mock()

        # Act
        interactor.update_checklist_item_wrapper(
            checklist_item_with_id_dto=checklist_item_with_id_dto,
            presenter=presenter_mock
        )

        # Assert
        storage_mock.is_checklist_item_id_exists.assert_called_once_with(
            checklist_item_id=checklist_item_with_id_dto.checklist_item_id
        )
        storage_mock.update_checklist_item.assert_called_once_with(
            checklist_item_with_id_dto=checklist_item_with_id_dto
        )
        presenter_mock.get_success_response_for_update_checklist_item.assert_called_once()
