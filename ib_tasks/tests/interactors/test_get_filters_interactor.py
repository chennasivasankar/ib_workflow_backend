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

    def test_given_valid_user_returns_user_filters_dto(
            self, filter_storage, presenter, field_storage):
        # Arrange
        user_id = '1'
        from ib_tasks.tests.factories.storage_dtos import FilterDTOFactory
        FilterDTOFactory.reset_sequence(1)
        filters = FilterDTOFactory.create_batch(2, user_id="1")
        from ib_tasks.tests.factories.storage_dtos import ConditionDTOFactory
        ConditionDTOFactory.reset_sequence(1)
        conditions = ConditionDTOFactory.create_batch(2)
        from ib_tasks.interactors.filter_dtos import FilterCompleteDetailsDTO
        response = FilterCompleteDetailsDTO(
            filters_dto=filters, conditions_dto=conditions
        )
        filter_storage.get_filters_dto_to_user.return_value = filters
        filter_ids = [1, 2]
        filter_storage.get_conditions_to_filters.return_value = conditions
        from ib_tasks.interactors.filter_interactor import FilterInteractor
        interactor = FilterInteractor(
            filter_storage=filter_storage, presenter=presenter,
            field_storage=field_storage
        )

        # Act
        interactor.get_filters_details(user_id=user_id)

        # Assert
        filter_storage.get_filters_dto_to_user \
            .assert_called_once_with(user_id=user_id)
        filter_storage.get_conditions_to_filters \
            .assert_called_once_with(filter_ids=filter_ids)
        presenter.get_response_for_get_filters_details \
            .assert_called_once_with(filter_complete_details=response)

    def test_given_valid_user_returns_empty_dtos(
            self, filter_storage, presenter, field_storage):
        # Arrange
        user_id = '1'
        from ib_tasks.interactors.filter_dtos import FilterCompleteDetailsDTO
        response = FilterCompleteDetailsDTO(
            filters_dto=[], conditions_dto=[]
        )
        filter_storage.get_filters_dto_to_user.return_value = []
        filter_ids = []
        filter_storage.get_conditions_to_filters.return_value = []
        from ib_tasks.interactors.filter_interactor import FilterInteractor
        interactor = FilterInteractor(
            filter_storage=filter_storage, presenter=presenter,
            field_storage=field_storage
        )

        # Act
        interactor.get_filters_details(user_id=user_id)

        # Assert
        filter_storage.get_filters_dto_to_user \
            .assert_called_once_with(user_id=user_id)
        filter_storage.get_conditions_to_filters \
            .assert_called_once_with(filter_ids=filter_ids)
        presenter.get_response_for_get_filters_details \
            .assert_called_once_with(filter_complete_details=response)

    def test_update_filter_status_raises_invalid_filter_exception(
            self, filter_storage, presenter, field_storage):
        # Arrange
        from ib_tasks.interactors.filter_interactor import FilterInteractor
        interactor = FilterInteractor(
            filter_storage=filter_storage, presenter=presenter, field_storage=field_storage
        )
        from ib_tasks.exceptions.filter_exceptions import InvalidFilterId
        filter_storage.validate_filter_id.side_effect = InvalidFilterId()
        user_id = "1"
        filter_id = 1
        from ib_tasks.constants.enum import Status
        is_selected = Status.ENABLED.value

        # Act
        interactor.update_filter_select_status_wrapper(
            user_id=user_id, filter_id=filter_id, is_selected=is_selected
        )

        # Assert
        presenter.get_response_for_invalid_filter_id.assert_called_once()

    def test_raises_invalid_user_permission(
            self, filter_storage, presenter, field_storage):
        # Arrange
        from ib_tasks.interactors.filter_interactor import FilterInteractor
        interactor = FilterInteractor(
            filter_storage=filter_storage, presenter=presenter, field_storage=field_storage
        )
        from ib_tasks.exceptions.filter_exceptions import UserNotHaveAccessToFilter
        filter_storage.validate_user_with_filter_id \
            .side_effect = UserNotHaveAccessToFilter()
        user_id = "1"
        filter_id = 1
        from ib_tasks.constants.enum import Status
        is_selected = Status.ENABLED.value

        # Act
        interactor.update_filter_select_status_wrapper(
            user_id=user_id, filter_id=filter_id, is_selected=is_selected
        )

        # Assert
        presenter.get_response_for_invalid_user_to_update_filter_status \
            .assert_called_once()

    def test_returns_update_status(
            self, filter_storage, presenter, field_storage):
        # Arrange
        from ib_tasks.interactors.filter_interactor import FilterInteractor
        interactor = FilterInteractor(
            filter_storage=filter_storage, presenter=presenter,
            field_storage=field_storage
        )
        from ib_tasks.constants.enum import Status
        boolean_field = Status.ENABLED.value
        filter_storage.update_filter_status.return_value = boolean_field
        user_id = "1"
        filter_id = 1

        is_selected = Status.ENABLED.value

        # Act
        interactor.update_filter_select_status_wrapper(
            user_id=user_id, filter_id=filter_id, is_selected=is_selected
        )

        # Assert
        presenter.get_response_for_update_filter_status \
            .assert_called_once_with(filter_id=filter_id, is_selected=is_selected)

    def test_returns_disabled_update_status(
            self, filter_storage, presenter, field_storage):
        # Arrange
        from ib_tasks.interactors.filter_interactor import FilterInteractor
        interactor = FilterInteractor(
            filter_storage=filter_storage, presenter=presenter, field_storage=field_storage
        )
        from ib_tasks.constants.enum import Status
        boolean_field = Status.DISABLED.value
        filter_storage.update_filter_status.return_value = boolean_field
        user_id = "1"
        filter_id = 1

        is_selected = Status.DISABLED.value

        # Act
        interactor.update_filter_select_status_wrapper(
            user_id=user_id, filter_id=filter_id, is_selected=is_selected
        )

        # Assert
        presenter.get_response_for_update_filter_status \
            .assert_called_once_with(filter_id=filter_id, is_selected=is_selected)
