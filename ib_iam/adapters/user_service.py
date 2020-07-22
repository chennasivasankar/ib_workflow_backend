import dataclasses
from typing import List

from ib_iam.adapters.dtos import UserProfileDTO


class UserService:
    def get_user_profile_bulk(
            self, user_ids: List[str]) -> List[UserProfileDTO]:
        pass

    def create_user_account_with_email(self, email: str) -> str:
        pass

    def create_user_profile(
            self, user_id, user_profile_dto: UserProfileDTO):
        pass
