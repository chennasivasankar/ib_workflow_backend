import abc
from dataclasses import dataclass
from typing import List

from ib_tasks.interactors.storage_interfaces.actions_dtos import \
    ActionWithStageIdDTO
from ib_tasks.interactors.storage_interfaces.fields_dtos import \
    FieldPermissionDTO
from ib_tasks.interactors.storage_interfaces.gof_dtos import GoFDTO, \
    GoFToTaskTemplateDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import \
    StageIdWithTemplateIdDTO
from ib_tasks.interactors.storage_interfaces.task_templates_dtos import \
    TemplateDTO, ProjectIdWithTaskTemplateIdDTO


@dataclass
class CompleteTaskTemplatesDTO:
    task_template_dtos: List[TemplateDTO]
    project_id_with_task_template_id_dtos: \
        List[ProjectIdWithTaskTemplateIdDTO]
    stage_id_with_template_id_dtos: List[StageIdWithTemplateIdDTO]
    action_with_stage_id_dtos: List[ActionWithStageIdDTO]
    gof_dtos: List[GoFDTO]
    gofs_of_task_templates_dtos: List[GoFToTaskTemplateDTO]
    field_with_permissions_dtos: List[FieldPermissionDTO]


class GetTaskTemplatesPresenterInterface(abc.ABC):
    @abc.abstractmethod
    def raise_task_templates_does_not_exists_exception(self):
        pass

    @abc.abstractmethod
    def get_task_templates_response(
            self, complete_task_templates_dto: CompleteTaskTemplatesDTO):
        pass
