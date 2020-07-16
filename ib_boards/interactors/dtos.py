from dataclasses import dataclass

@dataclass
class ColumnParametersDTO:
    board_id: str
    offset: int
    limit: int
    user_id: str
