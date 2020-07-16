class ServiceAdapter:
    @property
    def task_service(self):
        from .tasks_service import TaskService
        return TaskService()


def get_service_adapter():
    return ServiceAdapter()

