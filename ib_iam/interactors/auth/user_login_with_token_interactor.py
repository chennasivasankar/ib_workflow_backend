from typing import Optional

from ib_iam.interactors.presenter_interfaces.auth_presenter_interface import \
    LoginWithUserTokePresenterInterface
from ib_iam.interactors.storage_interfaces.project_storage_interface import \
    ProjectStorageInterface
from ib_iam.interactors.storage_interfaces.team_storage_interface import \
    TeamStorageInterface
from ib_iam.interactors.storage_interfaces.user_storage_interface import \
    UserStorageInterface


class LoginWithTokenInteractor:

    def __init__(
            self,
            user_storage: UserStorageInterface,
            team_storage: TeamStorageInterface,
            project_storage: ProjectStorageInterface
    ):
        self.team_storage = team_storage
        self.user_storage = user_storage
        self.project_storage = project_storage

    def login_with_token_wrapper(
            self, token: str,
            presenter: LoginWithUserTokePresenterInterface,
            name: Optional[str] = None
    ):
        tokens_dto, is_admin = self.login_with_token(token=token, name=name)
        response = presenter.prepare_response_for_user_tokens_dto_and_is_admin(
            tokens_dto=tokens_dto, is_admin=is_admin
        )
        return response

    def login_with_token(self, token: str, name: Optional[str] = None):
        from django.conf import settings
        user_id = self.user_storage.get_user_id_for_given_token(token=token)
        is_user_not_exist = user_id is None
        if is_user_not_exist:
            user_id = self._create_user(token=token, name=name)
            self.add_and_assign_user_to_team(user_id=user_id)
        from ib_iam.adapters.service_adapter import ServiceAdapter
        service_adapter = ServiceAdapter()
        expiry_in_seconds = settings.USER_VERIFICATION_EMAIL_EXPIRY_IN_SECONDS
        user_tokens_dto = service_adapter.auth_service \
            .create_auth_tokens_for_user(
            user_id=user_id, expiry_in_seconds=expiry_in_seconds
        )
        is_admin = False
        return user_tokens_dto, is_admin

    def _create_user(self, token: str, name: Optional[str] = None):
        from ib_iam.adapters.service_adapter import get_service_adapter
        service_adapter = get_service_adapter()
        email = token + "@gmail.com"
        is_name_not_exist = name is None
        if is_name_not_exist:
            name = token
        user_id = service_adapter.user_service.create_user_account_with_email(
            email=email, password=email
        )
        from ib_iam.adapters.dtos import UserProfileDTO
        user_profile_dto = UserProfileDTO(
            user_id=user_id, name=name, email=email
        )
        service_adapter.user_service.create_user_profile(
            user_id=user_id, user_profile_dto=user_profile_dto
        )
        self.user_storage.create_user(
            user_id=user_id, name=name, is_admin=False
        )
        self.user_storage.create_auth_user(
            user_id=user_id, token=token)
        return user_id

    def add_and_assign_user_to_team(self, user_id: str):
        from ib_iam.constants.config import DEFAULT_TEAM_ID, DEFAULT_TEAM_NAME
        team_id = DEFAULT_TEAM_ID
        team_name = DEFAULT_TEAM_NAME
        is_created = self.team_storage.get_or_create_team_with_id_and_name(
            team_id=team_id, name=team_name
        )
        self.team_storage.add_users_to_team(
            team_id=team_id, user_ids=[user_id]
        )
        if is_created:
            from ib_iam.constants.config import PROJECT_ID
            self.project_storage.assign_teams_to_projects(
                project_id=PROJECT_ID, team_ids=[team_id]
            )

