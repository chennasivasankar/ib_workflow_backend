from typing import List

from ib_tasks.interactors.stages_dtos import EntityTypeDTO, LogDurationDTO
from ib_utility_tools.interactors.storage_interfaces.dtos import TimerEntityDTO


class UtilityToolsService:

    @property
    def interface(self):
        from ib_utility_tools.app_interfaces.service_interface \
            import ServiceInterface
        return ServiceInterface()

    def get_log_duration_dtos(
            self, entity_dtos: List[EntityTypeDTO]
    ) -> List[LogDurationDTO]:
        timer_entity_dtos = [
            TimerEntityDTO(
                entity_id=str(entity_dto.entity_id),
                entity_type=entity_dto.entity_type
            ) for entity_dto in entity_dtos
        ]

        entity_with_timer_dtos = self.interface \
            .get_bulk_timer_details_for_given_entities(
            timer_entity_dtos=timer_entity_dtos
        )
        from datetime import timedelta
        return [
            LogDurationDTO(
                entity_id=int(entity_dto.entity_id),
                duration=timedelta(seconds=entity_dto.duration_in_seconds)
            )
            for entity_dto in entity_with_timer_dtos
        ]
