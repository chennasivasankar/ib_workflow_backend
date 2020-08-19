import datetime

import pytest
from freezegun import freeze_time


class TestGetBulkTimerDetailsForGivenEntities:

    @pytest.fixture()
    def service_interface(self):
        from ib_utility_tools.app_interfaces.service_interface import \
            ServiceInterface
        service_interface = ServiceInterface()
        return service_interface

    @pytest.fixture
    def timer_details(self):
        from ib_utility_tools.constants.enum import TimerEntityType
        timer_details = [
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
        return timer_details

    @pytest.fixture
    def timer_objects(self, timer_details):
        from ib_utility_tools.tests.factories.models import TimerFactory
        timer_objects = [
            TimerFactory.create(
                entity_id=timer["entity_id"],
                entity_type=timer["entity_type"],
                duration_in_seconds=timer["duration_in_seconds"],
                is_running=timer["is_running"],
                start_datetime=timer["start_datetime"]
            ) for timer in timer_details
        ]
        return timer_objects

    @pytest.fixture
    def timer_entity_dtos(self, timer_details):
        from ib_utility_tools.tests.factories.storage_dtos import \
            TimerEntityDTOFactory
        timer_entity_dtos = [
            TimerEntityDTOFactory(
                entity_id=timer["entity_id"],
                entity_type=timer["entity_type"]
            ) for timer in timer_details
        ]
        return timer_entity_dtos

    @pytest.fixture
    def expected_timer_details(self):
        from ib_utility_tools.constants.enum import TimerEntityType
        timer_details = [
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
        return timer_details

    @pytest.fixture
    def timer_details_dtos(self, expected_timer_details):
        from ib_utility_tools.tests.factories.storage_dtos import \
            TimerDetailsDTOFactory
        timer_details_dtos = [
            TimerDetailsDTOFactory(
                entity_id=timer["entity_id"],
                entity_type=timer["entity_type"],
                duration_in_seconds=timer["duration_in_seconds"],
                is_running=timer["is_running"],
                start_datetime=timer["start_datetime"]
            ) for timer in expected_timer_details
        ]
        return timer_details_dtos

    @pytest.mark.django_db
    def test_given_invalid_entities_raises_invalid_entities_exception(
            self, service_interface, timer_objects, timer_entity_dtos):
        # Arrange
        from ib_utility_tools.tests.factories.storage_dtos import \
            TimerEntityDTOFactory
        invalid_timer_entity_dto = TimerEntityDTOFactory()
        timer_entity_dtos.append(invalid_timer_entity_dto)

        # Assert
        from ib_utility_tools.exceptions.custom_exceptions import \
            InvalidEntities
        with pytest.raises(InvalidEntities):
            service_interface.get_bulk_timer_details_for_given_entities(
                timer_entity_dtos=timer_entity_dtos)

    @pytest.mark.django_db
    @freeze_time("2020-08-07 18:00:00")
    def test_given_valid_entities_returns_timer_details_dtos(
            self, service_interface, timer_objects, timer_entity_dtos,
            timer_details_dtos):
        # Arrange

        # Assert
        actual_timer_details_dtos = \
            service_interface.get_bulk_timer_details_for_given_entities(
                timer_entity_dtos=timer_entity_dtos)

        assert actual_timer_details_dtos == timer_details_dtos
