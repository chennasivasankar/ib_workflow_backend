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
    def interactor(self, storage_mock):
        from ib_utility_tools.interactors.get_timers_bulk_interactor import \
            GetTimersBulkInteractor
        interactor = GetTimersBulkInteractor(timer_storage=storage_mock)
        return interactor

    def test_given_invalid_entities_raises_invalid_entities(
            self, interactor, storage_mock):
        from ib_utility_tools.tests.factories.storage_dtos import \
            TimerEntityDTOFactory, TimerDetailsDTOFactory
        timer_entity_dtos = TimerEntityDTOFactory.create_batch(size=2)
        timer_details_dtos = TimerDetailsDTOFactory.create_batch(size=1)
        storage_mock.get_timer_details_dtos_for_given_entities \
            .return_value = timer_details_dtos

        from ib_utility_tools.exceptions.custom_exceptions import \
            InvalidEntities
        with pytest.raises(InvalidEntities):
            interactor.get_timers_bulk(timer_entity_dtos=timer_entity_dtos)

        storage_mock.get_timer_details_dtos_for_given_entities \
            .assert_called_once_with(timer_entity_dtos=timer_entity_dtos)

    def test_given_valid_entities_and_no_timers_running_returns_timer_details_dtos(
            self, interactor, storage_mock):
        from ib_utility_tools.tests.factories.storage_dtos import \
            TimerEntityDTOFactory, TimerDetailsDTOFactory
        timer_entity_dtos = TimerEntityDTOFactory.create_batch(size=2)
        timer_details_dtos = TimerDetailsDTOFactory.create_batch(size=2)
        storage_mock.get_timer_details_dtos_for_given_entities \
            .return_value = timer_details_dtos

        interactor.get_timers_bulk(timer_entity_dtos=timer_entity_dtos)

        storage_mock.get_timer_details_dtos_for_given_entities \
            .assert_called_once_with(timer_entity_dtos=timer_entity_dtos)
        storage_mock.update_timers_bulk.assert_not_called()

    @freeze_time("2020-08-07 18:00:00")
    def test_given_valid_entities_and_a_timer_is_running_returns_timer_details_dtos(
            self, interactor, storage_mock):
        from ib_utility_tools.tests.factories.storage_dtos import \
            TimerEntityDTOFactory, TimerDetailsDTOFactory
        entity_id = 'ef6d1fc6-ac3f-4d2d-a983-752c992e8331'
        timer_entity_dtos = TimerEntityDTOFactory.create_batch(
            size=1, entity_id=entity_id)
        start_datetime = datetime.datetime(2020, 8, 7, 17, 0, 0, 0)
        timer_details_dto = TimerDetailsDTOFactory.create(
            entity_id=entity_id, is_running=True,
            start_datetime=start_datetime)
        timer_details_dtos = [timer_details_dto]
        storage_mock.get_timer_details_dtos_for_given_entities \
            .return_value = timer_details_dtos
        present_datetime = datetime.datetime.now()
        time_delta = \
            present_datetime - timer_details_dto.start_datetime
        duration_in_seconds = \
            timer_details_dto.duration_in_seconds + time_delta.seconds
        timer_details_dto.duration_in_seconds = duration_in_seconds
        timer_details_dto.start_datetime = present_datetime

        interactor.get_timers_bulk(timer_entity_dtos=timer_entity_dtos)

        storage_mock.get_timer_details_dtos_for_given_entities \
            .assert_called_once_with(timer_entity_dtos=timer_entity_dtos)
        storage_mock.update_timers_bulk.assert_called_once_with(
            timer_details_dtos=timer_details_dtos)
