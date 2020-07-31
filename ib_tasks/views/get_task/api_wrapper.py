from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from ib_tasks.storages.create_or_update_task_storage_implementation \
        import CreateOrUpdateTaskStorageImplementation
from ib_tasks.interactors.get_task_interactor \
    import GetTaskInteractor
from ib_tasks.presenters.get_task_presenter_implementation \
    import GetTaskPresenterImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user_obj = kwargs['user']
    user_id = user_obj.id
    query_parameter_dict = kwargs['request_query_params'].__dict__
    task_id = query_parameter_dict['task_id']
    storage = CreateOrUpdateTaskStorageImplementation()
    presenter = GetTaskPresenterImplementation()
    interactor = GetTaskInteractor(storage=storage)
    response = interactor.get_task_details_wrapper(
       user_id=user_id, task_id=task_id, presenter=presenter
    )
    return response
