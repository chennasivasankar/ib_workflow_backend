class ServiceAdapter:

    @property
    def iam_service(self):
        from ib_adhoc_tasks.adapters.iam_service import IamService
        iam_service = IamService()
        return iam_service

    @property
    def task_service(self):
        from ib_adhoc_tasks.adapters.task_interface import TaskService
        task_service = TaskService()
        return task_service


def get_service_adapter():
    return ServiceAdapter()
