import mock
import pytest


class TestStartTimerInteractor:

    @pytest.fixture()
    def storage_mock(self):
        from ib_utility_tools.interactors.storage_interfaces.timer_storage_interface import \
            TimerStorageInterface
        storage = mock.create_autospec(TimerStorageInterface)
        return storage

    @pytest.fixture()
    def presenter_mock(self):
        from ib_utility_tools.interactors.presenter_interfaces.timer_presenter_interface import \
            TimerPresenterInterface
        presenter = mock.create_autospec(TimerPresenterInterface)
        return presenter

    @pytest.fixture()
    def interactor(self, storage_mock):
        from ib_utility_tools.interactors.start_timer_interactor import \
            StartTimerInteractor
        interactor = StartTimerInteractor(timer_storage=storage_mock)
        return interactor

    def test_it_returns_timer_details_dict(
            self, interactor, storage_mock, presenter_mock):
        from ib_utility_tools.tests.factories.storage_dtos import \
            TimerEntityDTOFactory, TimerDetailsDTOFactory
        timer_entity_dto = TimerEntityDTOFactory()
        timer_details_dto = TimerDetailsDTOFactory()
        storage_mock.get_timer_details_dto.return_value = timer_details_dto
        presenter_mock.get_success_response_with_timer_details_dto \
            .return_value = mock.Mock()

        interactor.start_timer_wrapper(timer_entity_dto=timer_entity_dto,
                                       presenter=presenter_mock)

        presenter_mock.get_success_response_with_timer_details_dto \
            .assert_called_once_with(timer_details_dto=timer_details_dto)
