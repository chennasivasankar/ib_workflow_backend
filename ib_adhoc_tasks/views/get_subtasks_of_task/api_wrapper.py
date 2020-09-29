from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    get_subtasks_parameter_dto = prepare_get_subtasks_parameter_dto(kwargs)
    from ib_adhoc_tasks.interactors.get_subtasks_of_task_interactor import \
        SubTasksInteractor
    interactor = SubTasksInteractor()
    from ib_adhoc_tasks.presenters.get_subtasks_presenter_implementation import \
        GetSubTasksPresenterImplementation
    response = interactor.get_subtasks_of_task_wrapper(
        get_subtasks_parameter_dto=get_subtasks_parameter_dto,
        presenter=GetSubTasksPresenterImplementation()
    )
    return response


def prepare_get_subtasks_parameter_dto(kwargs):
    from ib_adhoc_tasks.interactors.dtos.dtos import GetSubtasksParameterDTO
    user_object = kwargs["user"]
    return GetSubtasksParameterDTO(
        user_id=str(user_object.user_id),
        task_id=kwargs["request_data"]["task_id"],
        view_type=kwargs["request_data"]["view_type"]
    )
