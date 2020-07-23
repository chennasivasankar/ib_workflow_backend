class ServiceAdapter:
    @property
    def task_service(self):
        from .task_service import TaskService
        return TaskService()

    @property
    def iam_service(self):
        from .iam_service import IamService
        return IamService()

    @property
    def user_service(self):
        from ib_boards.adapters.iam_service import IAMService
        return IAMService()


def get_service_adapter():
    return ServiceAdapter()
