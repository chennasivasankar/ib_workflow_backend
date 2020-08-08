from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user_object = kwargs["user"]
    user_id = user_object.user_id

    path_params = kwargs["path_params"]
    discussion_id = path_params["discussion_id"]

    from ib_discussions.presenters.delete_discussion_presenter_implementation import \
        DeleteDiscussionPresenterImplementation
    presenter = DeleteDiscussionPresenterImplementation()

    from ib_discussions.storages.storage_implementation import \
        StorageImplementation
    storage = StorageImplementation()

    from ib_discussions.interactors.discussion_interactor import \
        DiscussionInteractor
    interactor = DiscussionInteractor(storage=storage)

    response = interactor.delete_discussion_wrapper(
        discussion_id=discussion_id, user_id=user_id, presenter=presenter
    )

    return response
