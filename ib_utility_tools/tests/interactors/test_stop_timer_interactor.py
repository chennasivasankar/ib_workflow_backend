import datetime

import mock
import pytest
from freezegun import freeze_time


class TestStopTimerInteractor:

    @pytest.fixture()
    def storage_mock(self):
        from ib_utility_tools.interactors.storage_interfaces \
            .timer_storage_interface import TimerStorageInterface
        storage = mock.create_autospec(TimerStorageInterface)
        return storage

    @pytest.fixture()
    def presenter_mock(self):
        from ib_utility_tools.interactors.presenter_interfaces \
            .timer_presenter_interface import TimerPresenterInterface
        presenter = mock.create_autospec(TimerPresenterInterface)
        return presenter

    @pytest.fixture()
    def interactor(self, storage_mock):
        from ib_utility_tools.interactors.stop_timer_interactor import \
            StopTimerInteractor
        interactor = StopTimerInteractor(timer_storage=storage_mock)
        return interactor

    def test_timer_already_stopped_raises_timer_is_already_stopped_exception(
            self, interactor, storage_mock, presenter_mock):
        from ib_utility_tools.tests.factories.storage_dtos import \
            TimerEntityDTOFactory, TimerDetailsDTOFactory
        timer_entity_dto = TimerEntityDTOFactory()
        timer_details_dto = TimerDetailsDTOFactory(is_running=False)
        storage_mock.get_timer_details_dto.return_value = timer_details_dto
        presenter_mock.raise_timer_is_already_stopped_exception \
            .return_value = mock.Mock()

        interactor.stop_timer_wrapper(timer_entity_dto=timer_entity_dto,
                                      presenter=presenter_mock)

        storage_mock.get_timer_details_dto.assert_called_once_with(
            timer_entity_dto=timer_entity_dto)
        presenter_mock.raise_timer_is_already_stopped_exception \
            .assert_called_once()

    @freeze_time("2020-08-07 18:00:00")
    def test_given_valid_details_it_returns_timer_details(
            self, interactor, storage_mock, presenter_mock):
        from ib_utility_tools.tests.factories.storage_dtos import \
            TimerEntityDTOFactory, TimerDetailsDTOFactory
        timer_entity_dto = TimerEntityDTOFactory()
        start_datetime = datetime.datetime(2020, 8, 7, 17, 0, 0, 0)
        duration_in_seconds_from_db = 2000
        timer_details_dto_from_storage = TimerDetailsDTOFactory(
            is_running=True, start_datetime=start_datetime,
            duration_in_seconds=duration_in_seconds_from_db)
        storage_mock.get_timer_details_dto \
            .return_value = timer_details_dto_from_storage
        stop_datetime = datetime.datetime.now()
        time_delta = stop_datetime - start_datetime
        duration_in_seconds = duration_in_seconds_from_db + time_delta.seconds
        timer_details_dto_for_presenter = TimerDetailsDTOFactory(
            duration_in_seconds=duration_in_seconds, is_running=False)

        presenter_mock.get_success_response_with_timer_details_dto \
            .return_value = mock.Mock()

        interactor.stop_timer_wrapper(timer_entity_dto=timer_entity_dto,
                                      presenter=presenter_mock)

        storage_mock.get_timer_details_dto.assert_called_once_with(
            timer_entity_dto=timer_entity_dto)
        storage_mock.update_timer.assert_called_once_with(
            timer_entity_dto=timer_entity_dto,
            timer_details_dto=timer_details_dto_for_presenter)
        presenter_mock.get_success_response_with_timer_details_dto \
            .assert_called_once_with(
            timer_details_dto=timer_details_dto_for_presenter)
