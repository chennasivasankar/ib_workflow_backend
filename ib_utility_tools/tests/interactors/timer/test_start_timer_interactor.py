import datetime

import mock
import pytest
from freezegun import freeze_time

from ib_utility_tools.tests.factories.storage_dtos import \
    TimerEntityDTOFactory, TimerDetailsDTOFactory


class TestStartTimerInteractor:

    @pytest.fixture()
    def storage_mock(self):
        from ib_utility_tools.interactors.storage_interfaces \
            .timer_storage_interface import TimerStorageInterface
        return mock.create_autospec(TimerStorageInterface)

    @pytest.fixture()
    def presenter_mock(self):
        from ib_utility_tools.interactors.presenter_interfaces \
            .timer_presenter_interface import TimerPresenterInterface
        return mock.create_autospec(TimerPresenterInterface)

    @pytest.fixture()
    def interactor(self, storage_mock):
        from ib_utility_tools.interactors.start_timer_interactor import \
            StartTimerInteractor
        return StartTimerInteractor(timer_storage=storage_mock)

    def test_timer_is_already_running_raises_timer_already_running_exception(
            self, interactor, storage_mock, presenter_mock
    ):
        # Arrange
        timer_entity_dto = TimerEntityDTOFactory()
        timer_details_dto = TimerDetailsDTOFactory(is_running=True)
        storage_mock.get_timer_details_dto.return_value = timer_details_dto
        presenter_mock.get_response_for_timer_is_already_running_exception \
            .return_value = mock.Mock()

        # Act
        interactor.start_timer_wrapper(timer_entity_dto=timer_entity_dto,
                                       presenter=presenter_mock)

        # Assert
        storage_mock.get_timer_details_dto.assert_called_once_with(
            timer_entity_dto=timer_entity_dto)
        presenter_mock.get_response_for_timer_is_already_running_exception \
            .assert_called_once()

    @freeze_time("2020-08-07 18:00:00")
    def test_it_returns_timer_details_dict(
            self, interactor, storage_mock, presenter_mock
    ):
        # Arrange
        timer_entity_dto = TimerEntityDTOFactory()
        timer_details_dto = TimerDetailsDTOFactory()
        storage_mock.get_timer_details_dto.return_value = timer_details_dto
        presenter_mock.get_response_for_get_timer_details \
            .return_value = mock.Mock()

        # Act
        interactor.start_timer_wrapper(timer_entity_dto=timer_entity_dto,
                                       presenter=presenter_mock)

        # Assert
        timer_details_dto.start_datetime = datetime.datetime.now()
        timer_details_dto.is_running = True
        storage_mock.get_timer_details_dto.assert_called_once_with(
            timer_entity_dto=timer_entity_dto)
        storage_mock.update_timer(timer_entity_dto=timer_entity_dto,
                                  timer_details_dto=timer_details_dto)
        presenter_mock.get_response_for_get_timer_details \
            .assert_called_once_with(timer_details_dto=timer_details_dto)
