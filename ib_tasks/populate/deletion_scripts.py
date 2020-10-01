def delete_task_template(task_template_id):
    from ib_tasks.models import Stage, TaskTemplate, GoF, TaskTemplateGoFs

    Stage.objects.filter(task_template_id=task_template_id).delete()
    GoF.objects.filter(
        gof_id__in=list(
            TaskTemplateGoFs.objects.filter(
                task_template_id=task_template_id
            ).values_list('gof_id', flat=True)
        )
    ).delete()
    TaskTemplate.objects.filter(template_id=task_template_id).delete()

    # Board.objects.filter(
    #     project_id="project_835cadf5da3248748dd714ceade89447").delete()

    delete_task_template_tasks_from_elastic_search(task_template_id)


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


def delete_task_template_tasks_from_elastic_search(task_template_id):
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
    es.delete_by_query(
        index=indices,
        body={"query": {
            "match": {"template_id": task_template_id}}})
