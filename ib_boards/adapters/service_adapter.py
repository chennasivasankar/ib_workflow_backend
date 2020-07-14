class ServiceAdapter:
    pass

    @property
    def task_service(self):
        from ib_boards.adapters.task_service import TaskService
        return TaskService()


def get_service_adapter():
    return ServiceAdapter()

