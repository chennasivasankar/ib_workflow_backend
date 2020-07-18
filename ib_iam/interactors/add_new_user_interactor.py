from ib_iam.exceptions.exceptions import UserIsNotAdminException, InvalidNameException, InvalidEmailAddressException
from ib_iam.interactors.mixins.validation import ValidationMixin
from ib_iam.interactors.presenter_interfaces.presenter_interface \
    import PresenterInterface
from ib_iam.interactors.storage_interfaces.storage_interface \
    import StorageInterface


class AddNewUserInteractor(ValidationMixin):
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def add_new_user_wrapper(
            self, user_id: str, name: str, email: str, presenter=PresenterInterface):
        try:
            self.add_new_user(user_id=user_id, name=name, email=email)
        except UserIsNotAdminException:
            return presenter.raise_user_is_not_admin_exception()
        except InvalidNameException:
            return presenter.raise_invalid_name_exception()
        except InvalidEmailAddressException:
            return presenter.raise_invalid_email_exception()

    def add_new_user(self, user_id: str, name: str, email: str):
        self._check_and_throw_user_is_admin(user_id=user_id)
        self._validate_name_and_throw_exception(name=name)
        self._validate_email_and_throw_exception()

    def _check_and_throw_user_is_admin(self, user_id: str):
        is_admin = self.storage.validate_user_is_admin(user_id=user_id)
        is_not_admin = not is_admin
        if is_not_admin:
            raise UserIsNotAdminException()

    @staticmethod
    def _validate_email_and_throw_exception(email: str):
        email_valid_pattern = \
            r"(^[a-zA-Z]+[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]*[a-zA-Z]+$)"
        if not bool(re.match(email_valid_pattern, email)):
            raise InvalidEmailAddressException()
