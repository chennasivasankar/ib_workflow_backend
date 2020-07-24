from ib_iam.exceptions.custom_exceptions import UserIsNotAdmin
from ib_iam.interactors.presenter_interfaces.get_user_options_presenter_interface \
    import GetUserOptionsPresenterInterface
from ib_iam.interactors.storage_interfaces.get_user_options_storage_interface \
    import GetUserOptionsStorageInterface


class GetUserOptionsDetails:

    def __init__(self, storage: GetUserOptionsStorageInterface):
        self.storage = storage

    def get_configuration_details_wrapper(
            self, user_id: str,
            presenter: GetUserOptionsPresenterInterface):
        try:
            configuration_details_dto = self.get_configuration_details(
                user_id=user_id)
            response = presenter.get_user_options_details_response(
                configuration_details_dto)
        except UserIsNotAdmin:
            response = presenter.raise_user_is_not_admin_exception()
        return response

    def get_configuration_details(self, user_id: str):
        self._check_and_throw_user_is_admin(user_id=user_id)
        companies = self.storage.get_companies()
        teams = self.storage.get_teams()
        roles = self.storage.get_roles()
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

    def _check_and_throw_user_is_admin(self, user_id: str):
        is_admin = self.storage.check_is_admin_user(user_id=user_id)
        is_not_admin = not is_admin
        if is_not_admin:
            raise UserIsNotAdmin()
