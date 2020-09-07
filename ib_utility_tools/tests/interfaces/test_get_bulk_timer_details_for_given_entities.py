import datetime
import pytest
from freezegun import freeze_time
from ib_utility_tools.interactors.storage_interfaces.dtos import (
    EntityWithTimerDTO)


class TestGetBulkTimerDetailsForGivenEntities:

    @pytest.fixture()
    def service_interface(self):
        from ib_utility_tools.app_interfaces.service_interface import (
            ServiceInterface)
        service_interface = ServiceInterface()
        return service_interface

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
    def timer_objects(self, timers):
        from ib_utility_tools.tests.factories.models import TimerFactory
        timer_objects = [
            TimerFactory.create(
                entity_id=timer["entity_id"],
                entity_type=timer["entity_type"],
                duration_in_seconds=timer["duration_in_seconds"],
                is_running=timer["is_running"],
                start_datetime=timer["start_datetime"]
            ) for timer in timers
        ]
        return timer_objects

    @pytest.fixture
    def timer_objects_for_invalid_entities(self, timer_details):
        from ib_utility_tools.constants.enum import TimerEntityType
        timer = {
            "entity_id": "ef6d1fc6-ac3f-4d2d-a983-752c992e8331",
            "entity_type": TimerEntityType.STAGE_TASK.value,
            "duration_in_seconds": 0,
            "is_running": False,
            "start_datetime": None
        }
        from ib_utility_tools.tests.factories.models import TimerFactory
        timer_objects = [
            TimerFactory.create(
                entity_id=timer["entity_id"],
                entity_type=timer["entity_type"],
                duration_in_seconds=timer["duration_in_seconds"],
                is_running=timer["is_running"],
                start_datetime=timer["start_datetime"])
        ]
        return timer_objects

    @pytest.fixture
    def timer_entity_dtos(self, timers):
        from ib_utility_tools.tests.factories.storage_dtos import (
            TimerEntityDTOFactory)
        timer_entity_dtos = [
            TimerEntityDTOFactory(
                entity_id=timer["entity_id"],
                entity_type=timer["entity_type"]
            ) for timer in timers
        ]
        return timer_entity_dtos

    @pytest.fixture
    def expected_timers(self):
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
                "duration_in_seconds": 3600,
                "is_running": True,
                "start_datetime": datetime.datetime(2020, 8, 7, 18, 0, 0, 0)
            }
        ]
        return timers

    @pytest.fixture
    def entity_with_timer_dtos(self, expected_timers):
        entity_with_timer_dtos = [
            EntityWithTimerDTO(
                entity_id=timer["entity_id"],
                entity_type=timer["entity_type"],
                duration_in_seconds=timer["duration_in_seconds"],
                is_running=timer["is_running"]
            ) for timer in expected_timers
        ]
        return entity_with_timer_dtos

    @pytest.fixture
    def expected_timers_for_invalid_entities(self):
        from ib_utility_tools.constants.enum import TimerEntityType
        timers = [
            {
                "entity_id": "ef6d1fc6-ac3f-4d2d-a983-752c992e8331",
                "entity_type": TimerEntityType.STAGE_TASK.value,
                "duration_in_seconds": 0,
                "is_running": False
            },
            {
                "entity_id": "ef6d1fc6-ac3f-4d2d-a983-752c992e8332",
                "entity_type": TimerEntityType.STAGE_TASK.value,
                "duration_in_seconds": 0,
                "is_running": False
            }
        ]
        return timers

    @pytest.fixture
    def entity_with_timer_dtos_for_invalid_entities(
            self, expected_timers_for_invalid_entities
    ):
        entity_with_timer_dtos = [
            EntityWithTimerDTO(
                entity_id=timer["entity_id"],
                entity_type=timer["entity_type"],
                duration_in_seconds=timer["duration_in_seconds"],
                is_running=timer["is_running"]
            ) for timer in expected_timers_for_invalid_entities
        ]
        return entity_with_timer_dtos

    @pytest.mark.django_db
    def test_given_invalid_entities_returns_timers_with_0_duration_and_false_running_state_for_invalid_entities(
            self, service_interface, timer_entity_dtos,
            timer_objects_for_invalid_entities,
            entity_with_timer_dtos_for_invalid_entities
    ):
        # Arrange

        # Act
        actual_entity_with_timer_dtos = \
            service_interface.get_bulk_timer_details_for_given_entities(
                timer_entity_dtos=timer_entity_dtos)

        # Assert
        assert actual_entity_with_timer_dtos == \
               entity_with_timer_dtos_for_invalid_entities

    @pytest.mark.django_db
    @freeze_time("2020-08-07 18:00:00")
    def test_given_valid_entities_returns_timer_details_dtos(
            self, service_interface, timer_objects, timer_entity_dtos,
            entity_with_timer_dtos
    ):
        # Act
        actual_entity_with_timer_dtos = \
            service_interface.get_bulk_timer_details_for_given_entities(
                timer_entity_dtos=timer_entity_dtos)

        # Assert
        assert actual_entity_with_timer_dtos == entity_with_timer_dtos
