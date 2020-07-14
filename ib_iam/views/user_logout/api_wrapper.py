from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user_obj = kwargs["user"]
    user_id = user_obj.id

    from ib_iam.interactors.user_logout_interactor import \
        UserLogoutInteractor
    interactor = UserLogoutInteractor()
    interactor.user_logout_wrapper(user_id=user_id)
    from django.http import HttpResponse
    return HttpResponse(status=200)
