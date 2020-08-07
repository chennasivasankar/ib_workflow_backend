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
        from ib_utility_tools.interactors.get_timer_interactor import \
            GetTimerInteractor
        interactor = GetTimerInteractor(timer_storage=storage_mock)
        return interactor

    def test_given_details_has_no_timer_then_creates_and_returns_timer_details(
            self, interactor, storage_mock, presenter_mock):
        from ib_utility_tools.tests.factories.storage_dtos import \
            TimerEntityDTOFactory, TimerDetailsDTOFactory
        timer_entity_dto = TimerEntityDTOFactory()
        timer_details_dto = TimerDetailsDTOFactory(is_running=False)
        storage_mock.get_timer_id_if_exists.return_value = None
        storage_mock.create_timer.return_value = "1"
        storage_mock.get_timer_details_dto.return_value = timer_details_dto
        presenter_mock.get_success_response_with_timer_details_dto \
            .return_value = mock.Mock()

        interactor.get_timer_wrapper(timer_entity_dto=timer_entity_dto,
                                     presenter=presenter_mock)

        storage_mock.get_timer_id_if_exists.assert_called_once_with(
            timer_entity_dto=timer_entity_dto)
        storage_mock.create_timer.assert_called_once_with(
            timer_entity_dto=timer_entity_dto)
        storage_mock.get_timer_details_dto.assert_called_once_with(
            timer_entity_dto=timer_entity_dto)
        presenter_mock.get_success_response_with_timer_details_dto \
            .assert_called_once_with(timer_details_dto=timer_details_dto)

    def test_given_valid_details_and_timer_is_running_returns_timer_details(
            self, interactor, storage_mock, presenter_mock):
        from ib_utility_tools.tests.factories.storage_dtos import \
            TimerEntityDTOFactory, TimerDetailsDTOFactory
        timer_entity_dto = TimerEntityDTOFactory()
        timer_details_dto = TimerDetailsDTOFactory(is_running=False)
        storage_mock.get_timer_id_if_exists.return_value = "1"
        storage_mock.get_timer_details_dto.return_value = timer_details_dto
        presenter_mock.get_success_response_with_timer_details_dto \
            .return_value = mock.Mock()

        interactor.get_timer_wrapper(timer_entity_dto=timer_entity_dto,
                                     presenter=presenter_mock)

        storage_mock.get_timer_id_if_exists.assert_called_once_with(
            timer_entity_dto=timer_entity_dto)
        storage_mock.create_timer.assert_not_called()
        storage_mock.get_timer_details_dto.assert_called_once_with(
            timer_entity_dto=timer_entity_dto)
        presenter_mock.get_success_response_with_timer_details_dto \
            .assert_called_once_with(timer_details_dto=timer_details_dto)

    @freeze_time("2020-08-07 18:00:00")
    def test_given_valid_details_and_timer_is_not_running_returns_timer_details(
            self, interactor, storage_mock, presenter_mock):
        from ib_utility_tools.tests.factories.storage_dtos import \
            TimerEntityDTOFactory, TimerDetailsDTOFactory
        timer_entity_dto = TimerEntityDTOFactory()
        timer_details_dto = TimerDetailsDTOFactory(duration_in_seconds=100,
                                                   is_running=True)
        duration_in_seconds_from_db = 2000
        start_datetime = datetime.datetime(2020, 8, 7, 17, 0, 0, 0)
        present_datetime = datetime.datetime.now()
        storage_mock.get_timer_id_if_exists.return_value = "1"
        storage_mock.get_timer_details_dto.return_value = timer_details_dto
        storage_mock.get_start_datetime_and_duration \
            .return_value = start_datetime, duration_in_seconds_from_db
        time_delta = present_datetime - start_datetime
        duration_in_seconds = duration_in_seconds_from_db + time_delta.seconds
        timer_details_dto = TimerDetailsDTOFactory(
            duration_in_seconds=duration_in_seconds, is_running=True)
        presenter_mock.get_success_response_with_timer_details_dto \
            .return_value = mock.Mock()

        interactor.get_timer_wrapper(timer_entity_dto=timer_entity_dto,
                                     presenter=presenter_mock)

        storage_mock.get_timer_id_if_exists.assert_called_once_with(
            timer_entity_dto=timer_entity_dto)
        storage_mock.create_timer.assert_not_called()
        storage_mock.get_timer_details_dto.assert_called_once_with(
            timer_entity_dto=timer_entity_dto)
        storage_mock.get_start_datetime_and_duration.assert_called_once_with(
            timer_entity_dto=timer_entity_dto)
        storage_mock.update_start_datetime_to_present_and_duration \
            .assert_called_once_with(timer_entity_dto=timer_entity_dto,
                                     present_datetime=present_datetime,
                                     duration_in_seconds=duration_in_seconds)
        presenter_mock.get_success_response_with_timer_details_dto \
            .assert_called_once_with(timer_details_dto=timer_details_dto)
