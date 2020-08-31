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

    @pytest.fixture
    def timer_entity_dtos(self):
        from ib_utility_tools.constants.enum import TimerEntityType
        timer_entity_details = [
            {"entity_id": "f2c02d98-f311-4ab2-8673-3daa00757002",
             "entity_type": TimerEntityType.STAGE_TASK.value},
            {"entity_id": "f2c02d98-f311-4ab2-8673-3daa00757003",
             "entity_type": TimerEntityType.STAGE_TASK.value}
        ]
        from ib_utility_tools.tests.factories.storage_dtos import \
            TimerEntityDTOFactory
        timer_entity_dtos = [TimerEntityDTOFactory.create(
            entity_id=entity["entity_id"], entity_type=entity["entity_type"])
            for entity in timer_entity_details]
        return timer_entity_dtos

    @pytest.fixture
    def entity_with_timer_dtos_when_invalid_entities_given(self):
        from ib_utility_tools.interactors.storage_interfaces.dtos import \
            EntityWithTimerDTO

        from ib_utility_tools.constants.enum import TimerEntityType
        entity_with_timer_dtos = [
            EntityWithTimerDTO(
                entity_id='f2c02d98-f311-4ab2-8673-3daa00757002',
                entity_type=TimerEntityType.STAGE_TASK.value,
                duration_in_seconds=100,
                is_running=False),
            EntityWithTimerDTO(
                entity_id='f2c02d98-f311-4ab2-8673-3daa00757004',
                entity_type=TimerEntityType.STAGE_TASK.value,
                duration_in_seconds=0,
                is_running=False)]
        return entity_with_timer_dtos

    @pytest.fixture
    def complete_timer_details_when_no_timers_in_running_state(self):
        from ib_utility_tools.tests.factories.storage_dtos import \
            CompleteTimerDetailsDTOFactory
        from ib_utility_tools.constants.enum import TimerEntityType
        timer_entity_details = [
            {"entity_id": "f2c02d98-f311-4ab2-8673-3daa00757002",
             "entity_type": TimerEntityType.STAGE_TASK.value},
            {"entity_id": "f2c02d98-f311-4ab2-8673-3daa00757003",
             "entity_type": TimerEntityType.STAGE_TASK.value}
        ]
        complete_timer_details_dtos = [
            CompleteTimerDetailsDTOFactory(
                entity_id=timer_entity["entity_id"],
                entity_type=timer_entity["entity_type"],
                duration_in_seconds=100
            ) for timer_entity in timer_entity_details
        ]
        return complete_timer_details_dtos

    @pytest.fixture
    def entity_with_timer_dtos_when_no_timers_in_running_state(self):
        from ib_utility_tools.constants.enum import TimerEntityType
        timer_entity_details = [
            {"entity_id": "f2c02d98-f311-4ab2-8673-3daa00757002",
             "entity_type": TimerEntityType.STAGE_TASK.value},
            {"entity_id": "f2c02d98-f311-4ab2-8673-3daa00757003",
             "entity_type": TimerEntityType.STAGE_TASK.value}
        ]
        from ib_utility_tools.interactors.storage_interfaces.dtos import \
            EntityWithTimerDTO
        entity_with_timer_dtos = [
            EntityWithTimerDTO(
                entity_id=timer_entity["entity_id"],
                entity_type=timer_entity["entity_type"],
                duration_in_seconds=100,
                is_running=False)
            for timer_entity in timer_entity_details]
        return entity_with_timer_dtos

    def test_given_invalid_entities_returns_timer_dtos_with_0_duration_and_is_running_false(
            self, interactor, storage_mock, timer_entity_dtos,
            entity_with_timer_dtos_when_invalid_entities_given):
        from ib_utility_tools.tests.factories.storage_dtos import \
            CompleteTimerDetailsDTOFactory
        complete_timer_details_dtos = [CompleteTimerDetailsDTOFactory.create(
            entity_id="f2c02d98-f311-4ab2-8673-3daa00757002",
            entity_type="STAGE_TASK",
            duration_in_seconds=100)]
        storage_mock.get_timer_details_dtos_for_given_entities \
            .return_value = complete_timer_details_dtos
        from ib_utility_tools.tests.factories.storage_dtos import \
            TimerEntityDTOFactory
        timer_entity_dtos = [
            TimerEntityDTOFactory(
                entity_id="f2c02d98-f311-4ab2-8673-3daa00757002"),
            TimerEntityDTOFactory(
                entity_id="f2c02d98-f311-4ab2-8673-3daa00757004")
        ]
        expected_entity_with_timer_dtos = \
            entity_with_timer_dtos_when_invalid_entities_given

        actual_entity_with_timer_dtos = interactor.get_timers_bulk(
            timer_entity_dtos=timer_entity_dtos)

        storage_mock.get_timer_details_dtos_for_given_entities \
            .assert_called_once_with(timer_entity_dtos=timer_entity_dtos)
        assert actual_entity_with_timer_dtos == expected_entity_with_timer_dtos

    def test_given_valid_entities_and_no_timers_running_returns_timer_details_dtos(
            self, interactor, storage_mock, timer_entity_dtos,
            complete_timer_details_when_no_timers_in_running_state,
            entity_with_timer_dtos_when_no_timers_in_running_state):
        storage_mock.get_timer_details_dtos_for_given_entities.return_value = \
            complete_timer_details_when_no_timers_in_running_state
        expected_entity_with_timer_dtos = \
            entity_with_timer_dtos_when_no_timers_in_running_state

        actual_entity_with_timer_dtos = interactor.get_timers_bulk(
            timer_entity_dtos=timer_entity_dtos)

        storage_mock.get_timer_details_dtos_for_given_entities \
            .assert_called_once_with(timer_entity_dtos=timer_entity_dtos)
        assert actual_entity_with_timer_dtos == expected_entity_with_timer_dtos

    @freeze_time("2020-08-07 18:00:00")
    def test_given_valid_entities_and_timers_running_returns_timer_details_dtos(
            self, interactor, storage_mock):
        from ib_utility_tools.tests.factories.storage_dtos import \
            TimerEntityDTOFactory, CompleteTimerDetailsDTOFactory
        entity_id = 'ef6d1fc6-ac3f-4d2d-a983-752c992e8331'
        timer_entity_dtos = TimerEntityDTOFactory.create_batch(
            size=1, entity_id=entity_id)
        start_datetime = datetime.datetime(2020, 8, 7, 17, 0, 0, 0)
        complete_timer_details_dto = CompleteTimerDetailsDTOFactory.create(
            entity_id=entity_id, is_running=True,
            start_datetime=start_datetime)
        storage_mock.get_timer_details_dtos_for_given_entities \
            .return_value = [complete_timer_details_dto]
        present_datetime = datetime.datetime.now()
        time_delta = \
            present_datetime - complete_timer_details_dto.start_datetime
        duration_in_seconds = (complete_timer_details_dto.duration_in_seconds
                               + time_delta.seconds)
        from ib_utility_tools.interactors.storage_interfaces.dtos import \
            EntityWithTimerDTO
        entity_with_timer_dtos = [EntityWithTimerDTO(
            entity_id=complete_timer_details_dto.entity_id,
            entity_type=complete_timer_details_dto.entity_type,
            duration_in_seconds=duration_in_seconds,
            is_running=True)]

        actual_entity_with_timer_dtos = interactor.get_timers_bulk(
            timer_entity_dtos=timer_entity_dtos)

        storage_mock.get_timer_details_dtos_for_given_entities \
            .assert_called_once_with(timer_entity_dtos=timer_entity_dtos)
        assert actual_entity_with_timer_dtos == entity_with_timer_dtos
