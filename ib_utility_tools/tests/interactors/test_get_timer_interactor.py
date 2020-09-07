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
        timer_details_dto = TimerDetailsDTOFactory(duration_in_seconds=0)
        storage_mock.get_timer_id_if_exists.return_value = None
        storage_mock.create_timer.return_value = "1"
        presenter_mock.get_response_for_get_timer_details \
            .return_value = mock.Mock()

        interactor.get_timer_wrapper(timer_entity_dto=timer_entity_dto,
                                     presenter=presenter_mock)

        storage_mock.get_timer_id_if_exists.assert_called_once_with(
            timer_entity_dto=timer_entity_dto)
        storage_mock.create_timer.assert_called_once_with(
            timer_entity_dto=timer_entity_dto)
        presenter_mock.get_response_for_get_timer_details \
            .assert_called_once_with(timer_details_dto=timer_details_dto)

    def test_given_valid_details_and_timer_is_not_running_returns_timer_details(
            self, interactor, storage_mock, presenter_mock):
        from ib_utility_tools.tests.factories.storage_dtos import \
            TimerEntityDTOFactory, TimerDetailsDTOFactory
        timer_entity_dto = TimerEntityDTOFactory()
        timer_details_dto = TimerDetailsDTOFactory(is_running=False)
        storage_mock.get_timer_id_if_exists.return_value = "1"
        storage_mock.get_timer_details_dto.return_value = timer_details_dto
        presenter_mock.get_response_for_get_timer_details \
            .return_value = mock.Mock()

        interactor.get_timer_wrapper(timer_entity_dto=timer_entity_dto,
                                     presenter=presenter_mock)

        storage_mock.get_timer_id_if_exists.assert_called_once_with(
            timer_entity_dto=timer_entity_dto)
        storage_mock.create_timer.assert_not_called()
        storage_mock.get_timer_details_dto.assert_called_once_with(
            timer_entity_dto=timer_entity_dto)
        presenter_mock.get_response_for_get_timer_details \
            .assert_called_once_with(timer_details_dto=timer_details_dto)

    @freeze_time("2020-08-07 18:00:00")
    def test_given_valid_details_and_timer_is_running_returns_timer_details(
            self, interactor, storage_mock, presenter_mock):
        from ib_utility_tools.tests.factories.storage_dtos import \
            TimerEntityDTOFactory, TimerDetailsDTOFactory
        timer_entity_dto = TimerEntityDTOFactory()
        storage_mock.get_timer_id_if_exists.return_value = "1"
        duration_in_seconds_from_db = 2000
        start_datetime = datetime.datetime(2020, 8, 7, 17, 0, 0, 0)
        timer_details_dto_from_storage = TimerDetailsDTOFactory(
            duration_in_seconds=duration_in_seconds_from_db,
            start_datetime=start_datetime,
            is_running=True)
        storage_mock.get_timer_details_dto \
            .return_value = timer_details_dto_from_storage
        present_datetime = datetime.datetime.now()
        time_delta = \
            present_datetime - timer_details_dto_from_storage.start_datetime
        duration_in_seconds = duration_in_seconds_from_db + time_delta.seconds
        timer_details_dto_for_response = TimerDetailsDTOFactory(
            duration_in_seconds=duration_in_seconds, is_running=True,
            start_datetime=present_datetime)
        presenter_mock.get_response_for_get_timer_details \
            .return_value = mock.Mock()

        interactor.get_timer_wrapper(timer_entity_dto=timer_entity_dto,
                                     presenter=presenter_mock)

        storage_mock.get_timer_id_if_exists.assert_called_once_with(
            timer_entity_dto=timer_entity_dto)
        storage_mock.create_timer.assert_not_called()
        storage_mock.get_timer_details_dto.assert_called_once_with(
            timer_entity_dto=timer_entity_dto)
        storage_mock.update_timer \
            .assert_called_once_with(
            timer_entity_dto=timer_entity_dto,
            timer_details_dto=timer_details_dto_for_response)
        presenter_mock.get_response_for_get_timer_details \
            .assert_called_once_with(
            timer_details_dto=timer_details_dto_for_response)
