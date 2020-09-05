from typing import Dict, List, Any
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from ...constants.enum import ViewType
from ...interactors.get_permitted_template_stage_flow_to_user import GetPermittedTemplateStageFlowToUser
from ...interactors.task_dtos import SearchQueryDTO
from ...presenters.get_template_stage_flow_implementation import GetTemplateStageFlowPresenterImplementation
from ...storages.action_storage_implementation import ActionsStorageImplementation
from ...storages.storage_implementation import StagesStorageImplementation
from ...storages.task_template_storage_implementation import TaskTemplateStorageImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    project_id = kwargs['project_id']
    user_obj = kwargs['user']
    template_id = kwargs['template_id']
    stage_storage = StagesStorageImplementation()
    action_storage = ActionsStorageImplementation()
    presenter = GetTemplateStageFlowPresenterImplementation()
    template_storage = TaskTemplateStorageImplementation()
    interactor = GetPermittedTemplateStageFlowToUser(
        stage_storage=stage_storage, action_storage=action_storage,
        template_storage=template_storage
    )
    response = interactor.get_template_stage_flow_to_user_wrapper(
        user_id=user_obj.user_id, project_id=project_id,
        template_id=template_id, presenter=presenter
    )
    return response

