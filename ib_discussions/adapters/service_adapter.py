class ServiceAdapter:

    @property
    def auth_service(self):
        from ib_discussions.adapters.auth_service import AuthService
        auth_service = AuthService()
        return auth_service


def get_service_adapter():
    return ServiceAdapter()

