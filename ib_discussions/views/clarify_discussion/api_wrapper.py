from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user = kwargs["user"]
    user_id = user.user_id
    path_params = kwargs["path_params"]
    discussion_id = path_params["discussion_id"]

    from ib_discussions.storages.storage_implementation import \
        StorageImplementation
    storage = StorageImplementation()

    from ib_discussions.presenters.mark_discussion_clarified_presenter_implementation import \
        MarkDiscussionClarifiedPresenterImplementation
    presenter = MarkDiscussionClarifiedPresenterImplementation()

    from ib_discussions.interactors.mark_discussion_clarified_interactor import \
        MarkDiscussionClarifiedInteractor
    interactor = MarkDiscussionClarifiedInteractor(storage=storage)

    response = interactor.mark_discussion_clarified_wrapper(
        user_id=user_id, discussion_id=discussion_id, presenter=presenter
    )
    return response
