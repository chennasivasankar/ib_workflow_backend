import datetime

import pytest

from ib_utility_tools.models import Timer
from ib_utility_tools.tests.factories.models import TimerFactory
from ib_utility_tools.tests.factories.storage_dtos import \
    TimerEntityDTOFactory, TimerDetailsDTOFactory


class TestTimerStorageImplementation:
    @pytest.fixture()
    def storage(self):
        from ib_utility_tools.storages.timer_storage_implementation import \
            TimerStorageImplementation
        storage = TimerStorageImplementation()
        return storage

    @pytest.mark.django_db
    def test_get_timer_id_if_exists_returns_timer_id_or_none(self, storage):
        # todo:Can parametrize test for getting None as response too
        from ib_utility_tools.tests.factories.storage_dtos import \
            TimerEntityDTOFactory
        timer_id = '2bdb417e-4632-419a-8ddd-085ea272c6eb'
        timer_entity_dto = TimerEntityDTOFactory()
        TimerFactory.create(timer_id=timer_id,
                            entity_id=timer_entity_dto.entity_id,
                            entity_type=timer_entity_dto.entity_type)

        actual_timer_id = storage.get_timer_id_if_exists(
            timer_entity_dto=timer_entity_dto)

        assert actual_timer_id == timer_id

    @pytest.mark.django_db
    def test_create_timer_returns_timer_id(self, storage):
        from ib_utility_tools.tests.factories.storage_dtos import \
            TimerEntityDTOFactory
        timer_entity_dto = TimerEntityDTOFactory()

        timer_id = storage.create_timer(timer_entity_dto=timer_entity_dto)

        timer_object = Timer.objects.get(timer_id=timer_id)

        assert timer_object.entity_id == timer_entity_dto.entity_id
        assert timer_object.entity_type == timer_entity_dto.entity_type

    @pytest.mark.django_db
    def test_get_timer_details_dto_returns_timer_details_dto(self, storage):
        timer_entity_dto = TimerEntityDTOFactory()
        factory_timer_object = TimerFactory.create(
            entity_id=timer_entity_dto.entity_id,
            entity_type=timer_entity_dto.entity_type)
        expected_duration_in_seconds = factory_timer_object.duration_in_seconds
        expected_is_running = factory_timer_object.is_running
        expected_start_datetime = factory_timer_object.start_datetime

        storage.get_timer_details_dto(timer_entity_dto=timer_entity_dto)

        timer_object = Timer.objects.get(
            entity_id=timer_entity_dto.entity_id,
            entity_type=timer_entity_dto.entity_type)
        assert timer_object.duration_in_seconds == expected_duration_in_seconds
        assert timer_object.is_running == expected_is_running
        assert timer_object.start_datetime == expected_start_datetime

    @pytest.mark.django_db
    def test_update_start_datetime_to_present_and_duration(self, storage):
        timer_entity_dto = TimerEntityDTOFactory()
        factory_timer_object = TimerFactory.create(
            entity_id=timer_entity_dto.entity_id,
            entity_type=timer_entity_dto.entity_type)
        expected_start_datetime = datetime.datetime(2020, 8, 7, 18)
        expected_is_running = factory_timer_object.is_running
        expected_duration_in_seconds = factory_timer_object.duration_in_seconds
        timer_detail_dto = TimerDetailsDTOFactory(
            start_datetime=expected_start_datetime,
            is_running=expected_is_running,
            duration_in_seconds=expected_duration_in_seconds)

        storage.update_timer(timer_entity_dto=timer_entity_dto,
                             timer_details_dto=timer_detail_dto)

        timer_object = Timer.objects.get(
            entity_id=timer_entity_dto.entity_id,
            entity_type=timer_entity_dto.entity_type)
        assert timer_object.start_datetime == expected_start_datetime
        assert timer_object.is_running == expected_is_running
        assert timer_object.duration_in_seconds == expected_duration_in_seconds
