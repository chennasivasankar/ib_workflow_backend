"""
Created on: 21/08/20
Author: Pavankumar Pamuru

"""
from ib_tasks.interactors.storage_interfaces.create_or_update_task_storage_interface import \
    CreateOrUpdateTaskStorageInterface
from ib_tasks.interactors.storage_interfaces.elastic_storage_interface import \
    ElasticSearchStorageInterface
from ib_tasks.interactors.storage_interfaces.fields_storage_interface import \
    FieldsStorageInterface
from ib_tasks.interactors.storage_interfaces.stages_storage_interface import \
    StageStorageInterface
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface


class CreateOrUpdateDataIntoElasticsearchInteractor:
    def __init__(self, storage: CreateOrUpdateTaskStorageInterface,
                 stage_storage: StageStorageInterface,
                 field_storage: FieldsStorageInterface,
                 task_storage: TaskStorageInterface,
                 elasticsearch_storage: ElasticSearchStorageInterface):
        self.elasticsearch_storage = elasticsearch_storage
        self.field_storage = field_storage
        self.task_storage = task_storage
        self.storage = storage
        self.stage_storage = stage_storage

    def create_or_update_task_in_elasticsearch_storage(self, task_id: int):

        from ib_tasks.interactors.get_task_base_interactor import \
            GetTaskBaseInteractor
        task_interactor = GetTaskBaseInteractor(
            storage=self.storage
        )
        task_dto = task_interactor.get_task(task_id=task_id)
        stage_ids = self.stage_storage.get_task_current_stages(
            task_id=task_id
        )
        from ib_tasks.interactors.create_or_update_data_in_elasticsearch_interactor import \
            CreateOrUpdateDataInElasticSearchInteractor
        elasticsearch_interactor = CreateOrUpdateDataInElasticSearchInteractor(
            elasticsearch_storage=self.elasticsearch_storage,
            field_storage=self.field_storage,
            task_storage=self.task_storage
        )
        elasticsearch_interactor.create_or_update_task_in_elasticsearch(
            task_dto=task_dto, task_id=task_id, stage_ids=stage_ids
        )
