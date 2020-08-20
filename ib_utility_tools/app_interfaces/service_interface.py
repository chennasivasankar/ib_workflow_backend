from typing import List

from ib_utility_tools.interactors.storage_interfaces.dtos import \
    TimerEntityDTO, CompleteTimerDetailsDTO


class ServiceInterface:

    @staticmethod
    def get_bulk_timer_details_for_given_entities(
            timer_entity_dtos: List[TimerEntityDTO]) -> \
            List[CompleteTimerDetailsDTO]:
        from ib_utility_tools.storages.timer_storage_implementation import \
            TimerStorageImplementation
        timer_storage = TimerStorageImplementation()

        from ib_utility_tools.interactors.get_timers_bulk_interactor import \
            GetTimersBulkInteractor
        interactor = GetTimersBulkInteractor(timer_storage=timer_storage)
        complete_timer_details_dtos = interactor.get_timers_bulk(
            timer_entity_dtos=timer_entity_dtos)
        return complete_timer_details_dtos
