class ServiceAdapter:
    @property
    def user_service(self):
        from ib_iam.adapters.user_service import UserService
        return UserService()

    @property
    def auth_service(self):
        from .auth_service import AuthService
        return AuthService()

    ##TODO implement elastic_service


def get_service_adapter():
    return ServiceAdapter()
