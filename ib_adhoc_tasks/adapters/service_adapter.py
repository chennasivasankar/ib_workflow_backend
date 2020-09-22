class ServiceAdapter:

    @property
    def iam_service(self):
        from ib_adhoc_tasks.adapters.iam_service import IamService
        return IamService()

    @property
    def tasks_service(self):
        from ib_adhoc_tasks.adapters.tasks_service import TasksService
        return TasksService()


def get_service_adapter():
    return ServiceAdapter()

