from dataclasses import dataclass


@dataclass
class GroupByResponseDTO:
    group_by_id: int
    group_by_display_name: str
    order: int
