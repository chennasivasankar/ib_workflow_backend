from dataclasses import dataclass

from ib_tasks.constants.enum import Searchable


@dataclass
class SearchableFieldTypeDTO:
    searchable_type: Searchable
    limit: int
    offset: int
    search_query: str


@dataclass
class SearchableFieldDetailDTO:
    id: str
    name: str


@dataclass
class FieldIdWithTaskGoFIdDTO:
    field_id: str
    task_gof_id: int
