"""
Created on: 03/09/20
Author: Pavankumar Pamuru

"""
from unittest.mock import create_autospec

import pytest


class TestGetFilterInteractor:

    @staticmethod
    @pytest.fixture()
    def presenter():
        from ib_tasks.interactors.presenter_interfaces \
            .filter_presenter_interface import FilterPresenterInterface
        from unittest.mock import create_autospec
        presenter = create_autospec(FilterPresenterInterface)
        return presenter

    @staticmethod
    @pytest.fixture()
    def filter_storage():
        from ib_tasks.interactors.storage_interfaces.filter_storage_interface \
            import FilterStorageInterface
        from unittest.mock import create_autospec
        filter_storage = create_autospec(FilterStorageInterface)
        return filter_storage

    @pytest.fixture
    def field_storage(self):
        from ib_tasks.interactors.storage_interfaces.fields_storage_interface \
            import FieldsStorageInterface
        return create_autospec(FieldsStorageInterface)

    @pytest.fixture()
    def project_ids_mock(self, mocker):
        path = 'ib_tasks.adapters.auth_service.AuthService.validate_project_ids'
        mock_obj = mocker.patch(path)
        return mock_obj

    @pytest.fixture()
    def user_project_mock(self, mocker):
        path = 'ib_tasks.adapters.auth_service.AuthService.validate_if_user_is_in_project'
        mock_obj = mocker.patch(path)
        return mock_obj

    def test_update_filter_status_raises_invalid_filter_exception(
            self, filter_storage, presenter, field_storage):
        # Arrange
        from ib_tasks.interactors.filters.update_filter_status import \
            UpdateFilerStatusInteractor
        interactor = UpdateFilerStatusInteractor(
            filter_storage=filter_storage, presenter=presenter
        )
        from ib_tasks.exceptions.filter_exceptions import InvalidFilterId
        filter_storage.validate_filter_id.side_effect = InvalidFilterId()
        user_id = "1"
        filter_id = 1
        from ib_tasks.constants.enum import Status
        filter_status = Status.ENABLED.value

        # Act
        interactor.update_filter_select_status_wrapper(
            user_id=user_id, filter_id=filter_id, filter_status=filter_status
        )

        # Assert
        presenter.get_response_for_invalid_filter_id.assert_called_once()

    def test_raises_invalid_user_permission(
            self, filter_storage, presenter, field_storage):
        # Arrange
        from ib_tasks.interactors.filters.update_filter_status import \
            UpdateFilerStatusInteractor
        interactor = UpdateFilerStatusInteractor(
            filter_storage=filter_storage, presenter=presenter
        )
        from ib_tasks.exceptions.filter_exceptions import UserNotHaveAccessToFilter
        filter_storage.validate_user_with_filter_id \
            .side_effect = UserNotHaveAccessToFilter()
        user_id = "1"
        filter_id = 1
        from ib_tasks.constants.enum import Status
        filter_status = Status.ENABLED.value

        # Act
        interactor.update_filter_select_status_wrapper(
            user_id=user_id, filter_id=filter_id, filter_status=filter_status
        )

        # Assert
        presenter.get_response_for_invalid_user_to_update_filter_status \
            .assert_called_once()

    def test_returns_update_status(
            self, filter_storage, presenter, field_storage):
        # Arrange
        from ib_tasks.interactors.filters.update_filter_status import \
            UpdateFilerStatusInteractor
        interactor = UpdateFilerStatusInteractor(
            filter_storage=filter_storage, presenter=presenter
        )
        from ib_tasks.constants.enum import Status
        boolean_field = Status.ENABLED.value
        filter_storage.update_filter_status.return_value = boolean_field
        user_id = "1"
        filter_id = 1

        filter_status = Status.ENABLED.value

        # Act
        interactor.update_filter_select_status_wrapper(
            user_id=user_id, filter_id=filter_id, filter_status=filter_status
        )

        # Assert
        presenter.get_response_for_update_filter_status \
            .assert_called_once_with(filter_id=filter_id, filter_status=filter_status)

    def test_returns_disabled_update_status(
            self, filter_storage, presenter, field_storage):
        # Arrange
        from ib_tasks.interactors.filters.update_filter_status import \
            UpdateFilerStatusInteractor
        interactor = UpdateFilerStatusInteractor(
            filter_storage=filter_storage, presenter=presenter
        )
        from ib_tasks.constants.enum import Status
        boolean_field = Status.DISABLED.value
        filter_storage.update_filter_status.return_value = boolean_field
        user_id = "1"
        filter_id = 1

        filter_status = Status.DISABLED.value

        # Act
        interactor.update_filter_select_status_wrapper(
            user_id=user_id, filter_id=filter_id, filter_status=filter_status
        )

        # Assert
        presenter.get_response_for_update_filter_status \
            .assert_called_once_with(filter_id=filter_id, filter_status=filter_status)
