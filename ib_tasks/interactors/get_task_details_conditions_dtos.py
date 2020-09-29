"""
Created on: 29/09/20
Author: Pavankumar Pamuru

"""
from dataclasses import dataclass
from typing import List

from ib_tasks.constants.enum import Operators
from ib_tasks.interactors.mixins.validation_mixin import ValidationMixin


@dataclass
class TaskFilterDTO:
    field_id: str
    operator: Operators
    value: str


class GetConditionsForTaskDetails(ValidationMixin):
    def __init__(self):
        pass

    def get_conditions_for_the_task_details(
            self, project_id: str, user_id: str) -> List[TaskFilterDTO]:
        self.validate_given_project_ids(project_ids=[project_id])
        self.validate_if_user_is_in_project(
            project_id=project_id, user_id=user_id
        )
        from ib_tasks.adapters.service_adapter import get_service_adapter
        service_adapter = get_service_adapter()

        is_user_in_least_level = service_adapter.auth_service.check_user_in_least_level(
            project_id=project_id,
            user_id=user_id
        )
        if is_user_in_least_level:
            task_condition_dtos = [
                TaskFilterDTO(
                    field_id="created_by",
                    operator=Operators.EQ.value,
                    value=user_id
                )
            ]
            return task_condition_dtos

        user_ids = service_adapter.auth_service.get_user_ids_based_on_user_level(
            project_id=project_id,
            user_id=user_id
        )
        return [
            TaskFilterDTO(
                field_id="created_by",
                operator=Operators.EQ.value,
                value=user_id
            )
            for user_id in user_ids
        ]
