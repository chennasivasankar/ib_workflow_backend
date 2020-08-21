from typing import List

from django.db import transaction

from ib_tasks.populate.get_sheet_data_for_creating_or_updating_stages import \
    GetSheetDataForStages
from ib_tasks.populate.get_sheet_data_for_stage_actions import \
    GetSheetDataForStageActions
from ib_tasks.populate.get_sheet_data_for_task_creation_config import \
    GetSheetDataForTaskCreationConfig
from ib_tasks.populate.get_sheet_data_for_task_status_variables import \
    GetSheetDataForStatusVariables
from ib_tasks.populate.global_constants import \
    PopulateGlobalConstantsToTemplate
from ib_tasks.populate.populate_fields import PopulateFields
from ib_tasks.populate.populate_gofs import PopulateGoFs
from ib_tasks.populate.populate_gofs_to_task_templates import \
    PopulateGoFsToTaskTemplate
from ib_tasks.populate.populate_gofs_to_transition_templates import \
    PopulateGoFsToTransitionTemplate
from ib_tasks.populate.task_templates import PopulateTaskTemplates
from ib_tasks.populate.transition_template import PopulateTransitionTemplates


@transaction.atomic()
def populate_data():
    task_template = PopulateTaskTemplates()
    task_template.populate_task_templates()

    # roles = RoleDetails()
    # roles.add_roles_details_to_database(
    #     GOOGLE_SHEET_NAME, ROLES_SUB_SHEET)

    gofs = PopulateGoFs()
    gofs.create_or_update_gofs()

    template_gofs = PopulateGoFsToTaskTemplate()
    template_gofs.populate_gofs_to_task_template()

    transition_template = PopulateTransitionTemplates()
    transition_template.populate_transition_templates()

    gofs_to_transition_template = PopulateGoFsToTransitionTemplate()
    gofs_to_transition_template.populate_gofs_to_transition_templates()

    fields = PopulateFields()
    fields.create_fields()

    global_constants = PopulateGlobalConstantsToTemplate()
    global_constants.populate_global_constants_to_template()

    status_variables = GetSheetDataForStatusVariables()
    status_variables.get_data_from_status_variables_sub_sheet()

    stage_values = GetSheetDataForStages()
    stage_values.get_data_from_stage_id_and_values_sub_sheet()

    stage_actions = GetSheetDataForStageActions()
    stage_actions.get_data_from_stages_and_actions_sub_sheet()

    task_creation_config = GetSheetDataForTaskCreationConfig()
    task_creation_config.get_data_from_task_creation_config_sub_sheet()


def delete_elastic_search_data():
    from elasticsearch_dsl import connections
    from django.conf import settings
    from ib_tasks.documents.elastic_task import TASK_INDEX_NAME
    connections.create_connection(
        hosts=[settings.ELASTICSEARCH_ENDPOINT], timeout=20
    )
    from elasticsearch import Elasticsearch
    es = Elasticsearch(hosts=[settings.ELASTICSEARCH_ENDPOINT])
    indices = [
        TASK_INDEX_NAME
    ]
    es.delete_by_query(index=indices, body={"query": {"match_all": {}}})


def create_tasks_in_elasticsearch_data(task_ids: List[int]):
    from ib_tasks.storages.elasticsearch_storage_implementation import \
        ElasticSearchStorageImplementation
    elasticsearch_storage = ElasticSearchStorageImplementation()
    from ib_tasks.storages.fields_storage_implementation import \
        FieldsStorageImplementation
    field_storage = FieldsStorageImplementation()
    from ib_tasks.storages.tasks_storage_implementation import \
        TasksStorageImplementation
    task_storage = TasksStorageImplementation()
    from ib_tasks.storages.create_or_update_task_storage_implementation import \
        CreateOrUpdateTaskStorageImplementation
    storage = CreateOrUpdateTaskStorageImplementation()
    from ib_tasks.storages.storage_implementation import \
        StagesStorageImplementation
    stage_storage = StagesStorageImplementation()
    task_ids = storage.get_task_ids()
    from ib_tasks.interactors.create_tasks_into_elasticsearch_interactor import \
        CreateDataIntoElasticsearchInteractor
    interactor = CreateDataIntoElasticsearchInteractor(
        elasticsearch_storage=elasticsearch_storage,
        storage=storage,
        task_storage=task_storage,
        stage_storage=stage_storage,
        field_storage=field_storage
    )
    for task_id in task_ids:
        interactor.create_task_in_elasticsearch_storage(
            task_id=task_id
        )
