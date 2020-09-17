from dataclasses import dataclass
from typing import List, Union

from ib_tasks.constants.enum import Searchable


@dataclass()
class ColumnDTO:
    column_id: str
    board_id: str
    name: str


@dataclass()
class ColumnFieldDTO:
    column_id: str
    field_ids: List[str]


@dataclass()
class ColumnStageDTO:
    column_id: str
    stage_id: str


@dataclass()
class BoardDTO:
    board_id: str
    name: str


@dataclass()
class TaskBoardsDetailsDTO:
    board_dto: BoardDTO
    column_stage_dtos: List[ColumnStageDTO]
    columns_dtos: List[ColumnDTO]


@dataclass
class UserDTO:
    user_id: str
    name: str


@dataclass
class AssigneeDetailsDTO:
    assignee_id: str
    name: str
    profile_pic_url: str


@dataclass
class TeamInfoDTO:
    team_id: str
    team_name: str


@dataclass
class UserDetailsDTO:
    user_id: str
    user_name: str
    profile_pic_url: str


@dataclass
class SearchableDetailsDTO:
    search_type: Searchable
    id: Union[int, str]
    value: str


@dataclass
class TeamDetailsDTO:
    team_id: str
    name: str


@dataclass
class UserIdWIthTeamDetailsDTOs:
    user_id: str
    team_details: List[TeamDetailsDTO]


@dataclass
class UserIdWIthTeamDetailsDTO:
    user_id: str
    team_details: TeamDetailsDTO


@dataclass
class ProjectDetailsDTO:
    project_id: str
    name: str
    logo_url: str


@dataclass
class UserIdWithTeamIdDTO:
    user_id: str
    team_id: str


@dataclass
class ProjectRolesDTO:
    project_id: str
    roles: List[str]


@dataclass
class TeamDetailsWithUserIdDTO(TeamDetailsDTO):
    user_id: str


@dataclass
class ProjectTeamUserIdsDTO:
    project_id: str
    user_id_with_team_id_dtos: List[UserIdWithTeamIdDTO]


@dataclass
class UserProjectStatusDTO:
    user_id: str
    project_id: str
    is_exists: bool