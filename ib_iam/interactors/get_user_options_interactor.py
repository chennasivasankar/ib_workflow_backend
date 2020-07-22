from ib_iam.exceptions.exceptions import UserIsNotAdmin
from ib_iam.interactors.presenter_interfaces.presenter_interface \
    import PresenterInterface
from ib_iam.interactors.storage_interfaces.storage_interface \
    import StorageInterface


class GetUserOptionsDetails:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_configuration_details_wrapper(self, user_id: str,
                                          presenter: PresenterInterface):
        try:
            configuration_details_dto = self.get_configuration_details(
                user_id=user_id)
            return presenter.get_user_options_details_response(
                configuration_details_dto)
        except UserIsNotAdmin:
            presenter.raise_user_is_not_admin_exception()

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
            UserOptionsDetails
        configuration_details_dto = UserOptionsDetails(
            companies=companies,
            roles=roles,
            teams=teams
        )
        return configuration_details_dto

    def _check_and_throw_user_is_admin(self, user_id: str):
        is_admin = self.storage.is_admin_user(user_id=user_id)
        is_not_admin = not is_admin
        if is_not_admin:
            raise UserIsNotAdmin()
