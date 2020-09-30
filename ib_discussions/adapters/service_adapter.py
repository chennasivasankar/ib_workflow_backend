class ServiceAdapter:

    @property
    def auth_service(self):
        from ib_discussions.adapters.auth_service import AuthService

        auth_service = AuthService()
        return auth_service

    @property
    def iam_service(self):
        from ib_discussions.adapters.iam_service import IamService
        iam_service = IamService()
        return iam_service


def get_service_adapter():
    return ServiceAdapter()
