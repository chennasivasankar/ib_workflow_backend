import datetime
import pytest
from ib_utility_tools.models import Timer
from ib_utility_tools.tests.factories.models import TimerFactory
from ib_utility_tools.tests.factories.storage_dtos import (
    TimerEntityDTOFactory, TimerDetailsDTOFactory,
    CompleteTimerDetailsDTOFactory
)


class TestTimerStorageImplementation:
    @pytest.fixture()
    def storage(self):
        from ib_utility_tools.storages.timer_storage_implementation import (
            TimerStorageImplementation
        )
        storage = TimerStorageImplementation()
        return storage

    @pytest.fixture
    def timers(self):
        from ib_utility_tools.constants.enum import TimerEntityType
        timers = [
            {
                "entity_id": "ef6d1fc6-ac3f-4d2d-a983-752c992e8331",
                "entity_type": TimerEntityType.STAGE_TASK.value,
                "duration_in_seconds": 0,
                "is_running": False,
                "start_datetime": None
            },
            {
                "entity_id": "ef6d1fc6-ac3f-4d2d-a983-752c992e8332",
                "entity_type": TimerEntityType.STAGE_TASK.value,
                "duration_in_seconds": 0,
                "is_running": True,
                "start_datetime": datetime.datetime(2020, 8, 7, 17, 0, 0, 0)
            }
        ]
        return timers

    @pytest.fixture
    def timer_entity_dtos(self, timers):
        timer_entity_dtos = [
            TimerEntityDTOFactory(
                entity_id=timer["entity_id"], entity_type=timer["entity_type"]
            ) for timer in timers
        ]
        return timer_entity_dtos

    @pytest.fixture
    def timer_objects(self, timers):
        timer_objects = [
            TimerFactory.create(
                entity_id=timer["entity_id"], entity_type=timer["entity_type"],
                duration_in_seconds=timer["duration_in_seconds"],
                is_running=timer["is_running"],
                start_datetime=timer["start_datetime"]
            ) for timer in timers
        ]
        return timer_objects

    @pytest.fixture
    def timer_details_dtos(self, timers):
        timer_details_dtos = [
            CompleteTimerDetailsDTOFactory(
                entity_id=timer["entity_id"], entity_type=timer["entity_type"],
                duration_in_seconds=timer["duration_in_seconds"],
                is_running=timer["is_running"],
                start_datetime=timer["start_datetime"]
            ) for timer in timers
        ]
        return timer_details_dtos

    @pytest.mark.django_db
    def test_get_timer_id_if_exists_returns_timer_id_or_none(self, storage):
        # Arrange
        # todo:Can parametrize test for getting None as response too
        from ib_utility_tools.tests.factories.storage_dtos import (
            TimerEntityDTOFactory
        )
        timer_id = '2bdb417e-4632-419a-8ddd-085ea272c6eb'
        timer_entity_dto = TimerEntityDTOFactory()
        TimerFactory.create(
            timer_id=timer_id, entity_id=timer_entity_dto.entity_id,
            entity_type=timer_entity_dto.entity_type
        )

        # Act
        actual_timer_id = storage.get_timer_id_if_exists(
            timer_entity_dto=timer_entity_dto
        )

        # Assert
        assert actual_timer_id == timer_id

    @pytest.mark.django_db
    def test_create_timer_returns_timer_id(self, storage):
        # Arrange
        from ib_utility_tools.tests.factories.storage_dtos import (
            TimerEntityDTOFactory
        )
        timer_entity_dto = TimerEntityDTOFactory()

        # Act
        timer_id = storage.create_timer(timer_entity_dto=timer_entity_dto)

        # Assert
        timer_object = Timer.objects.get(timer_id=timer_id)

        assert timer_object.entity_id == timer_entity_dto.entity_id
        assert timer_object.entity_type == timer_entity_dto.entity_type

    @pytest.mark.django_db
    def test_get_timer_details_dto_returns_timer_details_dto(self, storage):
        # Arrange
        timer_entity_dto = TimerEntityDTOFactory()
        timer_object = TimerFactory.create(
            entity_id=timer_entity_dto.entity_id,
            entity_type=timer_entity_dto.entity_type
        )
        expected_duration_in_seconds = timer_object.duration_in_seconds
        expected_is_running = timer_object.is_running
        expected_start_datetime = timer_object.start_datetime

        # Act
        storage.get_timer_details_dto(timer_entity_dto=timer_entity_dto)

        # Assert
        timer_object = Timer.objects.get(
            entity_id=timer_entity_dto.entity_id,
            entity_type=timer_entity_dto.entity_type
        )

        assert timer_object.duration_in_seconds == expected_duration_in_seconds
        assert timer_object.is_running == expected_is_running
        assert timer_object.start_datetime == expected_start_datetime

    @pytest.mark.django_db
    def test_update_start_datetime_to_present_and_duration(self, storage):
        # Arrange
        timer_entity_dto = TimerEntityDTOFactory()
        timer_object = TimerFactory.create(
            entity_id=timer_entity_dto.entity_id,
            entity_type=timer_entity_dto.entity_type
        )
        expected_start_datetime = datetime.datetime(2020, 8, 7, 18)
        expected_is_running = timer_object.is_running
        expected_duration_in_seconds = timer_object.duration_in_seconds
        timer_detail_dto = TimerDetailsDTOFactory(
            start_datetime=expected_start_datetime,
            is_running=expected_is_running,
            duration_in_seconds=expected_duration_in_seconds
        )

        # Act
        storage.update_timer(
            timer_entity_dto=timer_entity_dto,
            timer_details_dto=timer_detail_dto
        )

        # Assert
        timer_object = Timer.objects.get(
            entity_id=timer_entity_dto.entity_id,
            entity_type=timer_entity_dto.entity_type
        )

        assert timer_object.start_datetime == expected_start_datetime
        assert timer_object.is_running == expected_is_running
        assert timer_object.duration_in_seconds == expected_duration_in_seconds

    @pytest.mark.django_db
    def test_get_complete_timer_details_dtos_for_given_entities_returns_dtos(
            self, timer_entity_dtos, timer_objects, timer_details_dtos,
            storage
    ):
        # Act
        actual_timer_details_dtos = storage.get_timer_details_dtos(
            timer_entity_dtos=timer_entity_dtos
        )

        # Assert
        assert actual_timer_details_dtos == timer_details_dtos
