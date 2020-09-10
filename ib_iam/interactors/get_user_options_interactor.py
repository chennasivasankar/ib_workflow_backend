from ib_iam.exceptions.custom_exceptions import UserIsNotAdmin
from ib_iam.interactors.mixins.validation import ValidationMixin
from ib_iam.interactors.presenter_interfaces.get_user_options_presenter_interface \
    import GetUserOptionsPresenterInterface
from ib_iam.interactors.storage_interfaces.user_storage_interface \
    import UserStorageInterface


class GetUserOptionsDetails(ValidationMixin):

    def __init__(self, user_storage: UserStorageInterface):
        self.user_storage = user_storage

    def get_configuration_details_wrapper(
            self, user_id: str,
            presenter: GetUserOptionsPresenterInterface):
        try:
            configuration_details_dto = self.get_configuration_details(
                user_id=user_id)
            response = presenter.get_user_options_details_response(
                configuration_details_dto)
        except UserIsNotAdmin:
            response = presenter.response_for_user_is_not_admin_exception()
        return response

    def get_configuration_details(self, user_id: str):
        self._validate_is_user_admin(user_id=user_id)
        companies = self.user_storage.get_companies()
        teams = self.user_storage.get_team_id_and_name_dtos()
        roles = self.user_storage.get_roles()
        return self._create_configuration_details_dto(
            companies=companies, teams=teams, roles=roles)

    @staticmethod
    def _create_configuration_details_dto(companies, teams, roles):
        from ib_iam.interactors.presenter_interfaces.dtos import \
            UserOptionsDetailsDTO
        configuration_details_dto = UserOptionsDetailsDTO(
            companies=companies,
            roles=roles,
            teams=teams
        )
        return configuration_details_dto
