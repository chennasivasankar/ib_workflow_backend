from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    request_data = kwargs["request_data"]
    timer_entity_dto = _prepare_timer_entity_dto(request_data=request_data)

    from ib_utility_tools.storages.timer_storage_implementation import \
        TimerStorageImplementation
    from ib_utility_tools.presenters.timer_presenter_implementation import \
        TimerPresenterImplementation
    timer_storage = TimerStorageImplementation()
    presenter = TimerPresenterImplementation()
    from ib_utility_tools.interactors.stop_timer_interactor import \
        StopTimerInteractor
    interactor = StopTimerInteractor(timer_storage=timer_storage)

    response_data = interactor.stop_timer_wrapper(
        timer_entity_dto=timer_entity_dto, presenter=presenter)
    return response_data


def _prepare_timer_entity_dto(request_data):
    from ib_utility_tools.interactors.storage_interfaces.dtos import \
        TimerEntityDTO
    timer_entity_dto = TimerEntityDTO(
        entity_id=request_data["entity_id"],
        entity_type=request_data["entity_type"])
    return timer_entity_dto
