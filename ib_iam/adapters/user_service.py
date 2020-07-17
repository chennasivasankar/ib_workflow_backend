import dataclasses
from typing import List

from ib_iam.adapters.dtos import UserProfileDTO


class UserService:
    def get_user_profile_bulk(self, user_ids: List[int]) -> List[UserProfileDTO]:
        pass