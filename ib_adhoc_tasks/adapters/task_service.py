from dataclasses import dataclass
from typing import List, Optional

from ib_adhoc_tasks.exceptions.custom_exceptions import InvalidTaskTemplateId


class InvalidGroupById(Exception):
    pass


class InvalidRoleIdsException(Exception):
    def __init__(self, role_ids: List[str]):
        self.role_ids = role_ids


@dataclass
class StageIdAndNameDTO:
    stage_id: str
    name: str


class TaskService:

    @property
    def interface(self):
        from ib_tasks.app_interfaces.service_interface import ServiceInterface
        return ServiceInterface()

    def validate_task_template_id(self, task_template_id: str) -> \
            Optional[InvalidTaskTemplateId]:
        valid_task_template_ids = self.interface.validate_task_template_ids(
            task_template_ids=[task_template_id]
        )
        is_invalid_task_template_id = not valid_task_template_ids
        if is_invalid_task_template_id:
            raise InvalidTaskTemplateId
        return

    def get_user_permitted_stage_ids(self, user_role_ids: List[str]):
        try:
            stage_ids = self.interface.get_user_permitted_stage_ids(
                user_roles=user_role_ids
            )
        except InvalidRoleIdsException:
            raise InvalidRoleIdsException
        return stage_ids

    def get_stage_details(self, stage_ids: List[str]):
        stage_details_dtos = self.interface.get_stage_details(
            stage_ids=stage_ids
        )
        stage_id_and_name_dtos = [
            StageIdAndNameDTO(
                stage_id=stage_details_dto.stage_id,
                name=stage_details_dto.name
            )
            for stage_details_dto in stage_details_dtos
        ]
        return stage_id_and_name_dtos
