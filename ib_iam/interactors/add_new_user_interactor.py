from ib_iam.exceptions.exceptions import UserIsNotAdminException, GivenNameIsEmptyException, \
    InvalidEmailAddressException, \
    UserAccountAlreadyExistWithThisEmail, NameShouldNotContainsNumbersSpecCharactersException
from ib_iam.interactors.mixins.validation import ValidationMixin
from ib_iam.interactors.presenter_interfaces.presenter_interface \
    import PresenterInterface
from ib_iam.interactors.storage_interfaces.storage_interface \
    import StorageInterface


class AddNewUserInteractor(ValidationMixin):
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def add_new_user_wrapper(
            self, user_id: str, name: str, email: str, presenter: PresenterInterface):
        try:
            self.add_new_user(user_id=user_id, name=name, email=email)
        except UserIsNotAdminException:
            return presenter.raise_user_is_not_admin_exception()
        except GivenNameIsEmptyException:
            return presenter.raise_invalid_name_exception()
        except InvalidEmailAddressException:
            return presenter.raise_invalid_email_exception()
        except UserAccountAlreadyExistWithThisEmail:
            return presenter.\
                raise_user_account_already_exist_with_this_email_exception()
        except NameShouldNotContainsNumbersSpecCharactersException:
            return presenter.\
                raise_name_should_not_contain_special_characters_exception()

    def add_new_user(self, user_id: str, name: str, email: str):
        self._check_and_throw_user_is_admin(user_id=user_id)
        self._validate_name_and_throw_exception(name=name)
        self._validate_email_and_throw_exception(email=email)
        new_user_id = self._create_user_account_with_email(
            name=name, email=email)
        self._create_user_profile(user_id=new_user_id, email=email, name=name)
        self.storage.add_new_user(user_id=user_id, is_admin=False)

    def _check_and_throw_user_is_admin(self, user_id: str):
        is_admin = self.storage.validate_user_is_admin(user_id=user_id)
        is_not_admin = not is_admin
        if is_not_admin:
            raise UserIsNotAdminException()

    @staticmethod
    def _validate_email_and_throw_exception(email: str):
        import re
        email_valid_pattern = \
            r"(^[a-zA-Z]+[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]*[a-zA-Z]+$)"
        if not bool(re.match(email_valid_pattern, email)):
            raise InvalidEmailAddressException()

    @staticmethod
    def _create_user_account_with_email(name: str, email: str):
        from ib_iam.adapters.service_adapter import get_service_adapter
        service_adapter = get_service_adapter()
        user_id = service_adapter.user_service. \
            create_user_account_with_email(email=email)
        return user_id

    def _create_user_profile(self, user_id: str, email: str, name: str):
        from ib_iam.adapters.service_adapter import get_service_adapter
        service_adapter = get_service_adapter()
        user_profile_dto = self._create_user_profile_dto(
            name=name, email=email, user_id=user_id)
        service_adapter.user_service.create_user_profile(
            user_id=user_id, user_profile_dto=user_profile_dto)

    @staticmethod
    def _create_user_profile_dto(name, email, user_id):
        from ib_iam.adapters.dtos import UserProfileDTO
        user_profile_dto = UserProfileDTO(
            name=name,
            email=email,
            user_id=user_id
        )
        return user_profile_dto
