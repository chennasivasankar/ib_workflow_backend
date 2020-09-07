from typing import List

from django.db import transaction

from ib_iam.populate.add_project_roles_details import ProjectRoleDetails
from ib_tasks.constants.constants import ROLES_SUB_SHEET
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
from ib_tasks.populate.populate_projects_for_task_templates import \
    PopulateProjectsForTaskTemplates


@transaction.atomic()
def populate_projects_for_task_templates(spread_sheet_name: str):
    projects_for_task_templates = PopulateProjectsForTaskTemplates()
    projects_for_task_templates.populate_projects_for_task_template(
        spread_sheet_name=spread_sheet_name)


@transaction.atomic()
def populate_project_roles(spread_sheet_name: str):
    project_roles = ProjectRoleDetails()
    project_roles.add_project_roles_details_to_database(
        spread_sheet_name=spread_sheet_name, sub_sheet_name=ROLES_SUB_SHEET)


@transaction.atomic()
def populate_data(spread_sheet_name: str):

    task_template = PopulateTaskTemplates()
    task_template.populate_task_templates(spread_sheet_name=spread_sheet_name)

    gofs = PopulateGoFs()
    gofs.create_or_update_gofs(spread_sheet_name=spread_sheet_name)

    template_gofs = PopulateGoFsToTaskTemplate()
    template_gofs.populate_gofs_to_task_template(
        spread_sheet_name=spread_sheet_name)

    transition_template = PopulateTransitionTemplates()
    transition_template.populate_transition_templates(
        spread_sheet_name=spread_sheet_name)

    gofs_to_transition_template = PopulateGoFsToTransitionTemplate()
    gofs_to_transition_template.populate_gofs_to_transition_templates(
        spread_sheet_name=spread_sheet_name)

    fields = PopulateFields()
    fields.create_or_update_fields(spread_sheet_name=spread_sheet_name)

    global_constants = PopulateGlobalConstantsToTemplate()
    global_constants.populate_global_constants_to_template(
        spread_sheet_name=spread_sheet_name)

    status_variables = GetSheetDataForStatusVariables()
    status_variables.get_data_from_status_variables_sub_sheet(
        spread_sheet_name=spread_sheet_name)

    stage_values = GetSheetDataForStages()
    stage_values.get_data_from_stage_id_and_values_sub_sheet(
        spread_sheet_name=spread_sheet_name)

    stage_actions = GetSheetDataForStageActions()
    stage_actions.get_data_from_stages_and_actions_sub_sheet(
        spread_sheet_name=spread_sheet_name)

    task_creation_config = GetSheetDataForTaskCreationConfig()
    task_creation_config.get_data_from_task_creation_config_sub_sheet(
        spread_sheet_name=spread_sheet_name)


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


def create_tasks_in_elasticsearch_data(task_ids=None):
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
    if task_ids is None:
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


def delete_task_template_gofs_with_gof_fields(template_ids: List[str]):
    from ib_tasks.models.task_template_gofs import TaskTemplateGoFs, GoF
    gof_ids = TaskTemplateGoFs.objects.filter(
        task_template_id__in=template_ids).values_list('gof_id', flat=True)
    GoF.objects.filter(gof_id__in=gof_ids).delete()


def create_task_index_with_mapping():
    pass
