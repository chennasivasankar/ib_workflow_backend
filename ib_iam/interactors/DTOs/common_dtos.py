from dataclasses import dataclass
from typing import List


@dataclass
class UserIdWithRoleIdsDTO:
    user_id: str
    role_ids: List[str]
