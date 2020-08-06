import pytest


class TestGetFilterInteractor:

    @staticmethod
    @pytest.fixture()
    def presenter():

        from ib_tasks.interactors.presenter_interfaces\
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

    def test_given_valid_user_returns_user_filters_dto(
            self, filter_storage, presenter):

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
            filter_storage=filter_storage, presenter=presenter
        )

        # Act
        interactor.get_filters_details(user_id=user_id)

        # Assert
        filter_storage.get_filters_dto_to_user\
            .assert_called_once_with(user_id=user_id)
        filter_storage.get_conditions_to_filters\
            .assert_called_once_with(filter_ids=filter_ids)
        presenter.get_response_for_get_filters_details\
            .assert_called_once_with(filter_complete_details=response)

    def test_given_valid_user_returns_empty_dtos(
            self, filter_storage, presenter):

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
            filter_storage=filter_storage, presenter=presenter
        )

        # Act
        interactor.get_filters_details(user_id=user_id)

        # Assert
        filter_storage.get_filters_dto_to_user\
            .assert_called_once_with(user_id=user_id)
        filter_storage.get_conditions_to_filters\
            .assert_called_once_with(filter_ids=filter_ids)
        presenter.get_response_for_get_filters_details\
            .assert_called_once_with(filter_complete_details=response)
