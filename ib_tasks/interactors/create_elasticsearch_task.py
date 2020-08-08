from ib_tasks.documents.elastic_task import ElasticTaskDTO, Task
from ib_tasks.storages.elasticsearch_storage_implementation \
    import ElasticSearchStorageImplementation


class CreateElasticSearchTask:

    def __init__(self, storage: ElasticSearchStorageImplementation):
        self.elastic_storage = storage

    def create_elastic_task(self, elastic_task_dto: ElasticTaskDTO):

       pass