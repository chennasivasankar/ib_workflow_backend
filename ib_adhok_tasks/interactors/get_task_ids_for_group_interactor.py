from dataclasses import dataclass
from typing import List

from ib_adhok_tasks.adapters import service
from ib_adhok_tasks.constants.enum import GroupByType


@dataclass
class GroupByDTO:
    key: GroupByType
    value: str


@dataclass
class ApplyGroupDTO:
    project_id: str
    template_id: str
    user_id: str
    groupby_dtos: List[GroupByDTO]
    value: str


class GetTaskIdsForGroupInteractor:

    def get_task_ids_for_groups(self, apply_group_dto: ApplyGroupDTO):
        # TODO :
        # input: project_id, template_id, user_id,
        # groupby_dto : (groupby_field, groupby_value) ex:stage_id, assignee_id
        # group1_id : key, value
        # group2_id: key, value
        # if g1 and g2 are in [FIELD or STAGE] filter on field then stage then limit and offset
        # if g1 is in [FIELD or STAGE] and g2 is assignee then filter on g1 then filter with assignee
        # if g2 is in [FIELD or STAGE] and g1 is assignee then filter on g2 then filter with assignee
        user_roles = service.get_user_role_ids_based_on_project(
            user_id=apply_group_dto.user_id,
            project_id=apply_group_dto.project_id
        )
        stage_ids = service.get_stage_ids_based_on_user_roles(
            user_roles=user_roles
        )

        pass
