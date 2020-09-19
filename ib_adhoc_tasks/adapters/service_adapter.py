class ServiceAdapter:

    @property
    def iam_service(self):
        from ib_adhok_tasks.adapters.iam_service import IamService
        iam_service = IamService()
        return iam_service


def get_service_adapter():
    return ServiceAdapter()

