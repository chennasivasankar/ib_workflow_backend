class ServiceAdapter:
    @property
    def task_service(self):
        from ib_adhoc_tasks.adapters.task_service import TaskService
        return TaskService()

    @property
    def iam_service(self):
        from ib_adhoc_tasks.adapters.iam_service import IamService
        return IamService()


def get_service_adapter():
    return ServiceAdapter()
