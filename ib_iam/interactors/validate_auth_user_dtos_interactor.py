from typing import List

from ib_iam.interactors.dtos.dtos import AuthUserDTO
from ib_iam.interactors.storage_interfaces.user_storage_interface import \
    UserStorageInterface


class ValidateAuthUserDTOsInteractor:

    def __init__(
            self, user_storage: UserStorageInterface
    ):
        self.user_storage = user_storage

    def validate_auth_users_dtos(self, auth_user_dtos: List[AuthUserDTO]):
        existing_user_ids = self.user_storage.get_all_user_ids()

        from ib_iam.adapters.service_adapter import get_service_adapter
        service_adapter = get_service_adapter()
        user_profile_dtos = service_adapter.user_service.get_user_profile_bulk(
            user_ids=existing_user_ids
        )

        existing_phone_numbers = []
        existing_emails = []
        for user_profile_dto in user_profile_dtos:
            existing_phone_numbers.append(user_profile_dto.phone_number)
            existing_emails.append(user_profile_dto.email)

        phone_numbers = []
        emails = []
        for auth_user_dto in auth_user_dtos:
            phone_numbers.append(auth_user_dto.phone_number)
            emails.append(auth_user_dto.email)

        exceptions = {
            "already_email_exists": [],
            "duplicate_emails": [],
            "already_phone_number_exists": [],
            "duplicate_phone_numbers": []
        }
        valid_auth_user_dtos = []

        from collections import Counter
        emails_count_dict = Counter(emails)
        phone_numbers_count_dict = Counter(phone_numbers)

        for auth_user_dto in auth_user_dtos:
            if auth_user_dto.email in existing_emails:
                exceptions["already_email_exists"].append(auth_user_dto)
            elif auth_user_dto.phone_number in existing_phone_numbers:
                exceptions["already_phone_number_exists"].append(auth_user_dto)
            elif emails_count_dict[auth_user_dto.email] > 1:
                exceptions["duplicate_emails"].append(auth_user_dto)
            elif phone_numbers_count_dict[auth_user_dto.phone_number] > 1:
                exceptions["duplicate_phone_numbers"].append(auth_user_dto)
            else:
                valid_auth_user_dtos.append(auth_user_dto)
        print(exceptions)
        return valid_auth_user_dtos
