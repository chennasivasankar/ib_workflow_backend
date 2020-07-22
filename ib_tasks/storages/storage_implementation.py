

from ib_tasks.interactors.storage_interfaces.storage_interface \
    import StorageInterface
from ib_tasks.models import *


class StorageImplementation(StorageInterface):

    def validate_task_id(self, task_id: str):

        return Task.objects.filter(id=task_id).exists()
