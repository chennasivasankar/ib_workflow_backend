from dataclasses import dataclass
from typing import List

from ib_iam.interactors.dtos.dtos import AuthUserDTO
from ib_iam.interactors.storage_interfaces.user_storage_interface import \
    UserStorageInterface


@dataclass
class AuthTokenUserDetailsDTO:
    user_id: str
    auth_token_user_id: str
    token: str
    invitation_code: str


class ValidateAuthUserDTOsInteractor:

    def __init__(
            self,
            user_storage: UserStorageInterface
    ):
        self.user_storage = user_storage

    def validate_auth_user_dtos(self, auth_user_dtos: List[AuthUserDTO]):
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
        exceptions_and_valid_dtos_dict = \
            self._validate_user_auth_details(
                auth_user_dtos=valid_auth_user_dtos)
        exceptions_and_valid_dtos_dict.update(exceptions)
        print(exceptions_and_valid_dtos_dict)
        valid_auth_user_dtos = exceptions_and_valid_dtos_dict[
            "valid_auth_user_dtos"]
        return valid_auth_user_dtos

    def _validate_user_auth_details(self, auth_user_dtos: List[AuthUserDTO]):
        auth_token_user_dtos = self.user_storage.get_all_auth_token_user_dtos()
        valid_auth_user_dtos = []
        invitation_codes_from_db = []
        auth_tokens_from_db = []
        auth_token_user_ids_from_db = []
        for auth_token_user_dto in auth_token_user_dtos:
            invitation_codes_from_db.append(
                auth_token_user_dto.invitation_code)
            auth_tokens_from_db.append(auth_token_user_dto.token)
            auth_token_user_ids_from_db.append(
                auth_token_user_dto.auth_token_user_id)
        duplicate_invitation_codes = []
        duplicate_auth_tokens = []
        duplicate_auth_token_user_ids = []
        for auth_user_dto in auth_user_dtos:
            is_invitation_code_already_exists = \
                auth_user_dto.invitation_code in invitation_codes_from_db
            is_token_already_exists = \
                auth_user_dto.token in auth_tokens_from_db
            is_auth_token_user_id_already_exists = \
                auth_user_dto.auth_token_user_id in auth_token_user_ids_from_db
            if is_invitation_code_already_exists:
                duplicate_invitation_codes.append(auth_user_dto)
            elif is_token_already_exists:
                duplicate_auth_tokens.append(auth_user_dto)
            elif is_auth_token_user_id_already_exists:
                duplicate_auth_token_user_ids.append(auth_user_dto)
            else:
                valid_auth_user_dtos.append(auth_user_dto)
        valid_auth_user_dtos_to_populate = \
            self._validate_duplicates_in_given_auth_user_dtos(
                auth_user_dtos=valid_auth_user_dtos,
                duplicate_invitation_codes=duplicate_invitation_codes
            )

        return {
            "duplicate_invitation_codes": duplicate_invitation_codes,
            "duplicate_auth_tokens": duplicate_auth_tokens,
            "duplicate_auth_token_user_ids": duplicate_auth_token_user_ids,
            "valid_auth_user_dtos": valid_auth_user_dtos_to_populate
        }

    def _validate_duplicates_in_given_auth_user_dtos(
            self, auth_user_dtos: List[AuthUserDTO],
            duplicate_invitation_codes, duplicate_auth_tokens,
            duplicate_auth_token_user_ids
    ):
        valid_auth_user_dtos = []
        invitation_codes = [
            auth_user_dto.invitation_code
            for auth_user_dto in auth_user_dtos
        ]
        auth_tokens = [
            auth_user_dto.token
            for auth_user_dto in auth_user_dtos
        ]
        auth_token_user_ids = [
            auth_user_dto.auth_token_user_id
            for auth_user_dto in auth_user_dtos
        ]
        for auth_user_dto in auth_user_dtos:
            is_invitation_code_already_exists = \
                invitation_codes.count(auth_user_dto.invitation_code) > 1
            is_auth_token_already_exists = \
                auth_tokens.count(auth_user_dto.token) > 1
            is_auth_token_user_id_exists = \
                auth_token_user_ids.count(auth_user_dto.auth_token_user_id) > 1
            if is_invitation_code_already_exists:
                duplicate_invitation_codes.append(auth_user_dto)
            elif is_auth_token_already_exists:
                duplicate_auth_tokens.append(auth_user_dto)
            elif is_auth_token_user_id_exists:
                duplicate_auth_token_user_ids.append(auth_user_dto)
            else:
                valid_auth_user_dtos.append(auth_user_dto)
        return valid_auth_user_dtos

# # TODO invitation code not empty
# # invitation code not be a  duplicate, check in given dtos and database too
# # Can duplicate auth tokens exists, check in given dtos and database too
# # Can duplicate auth token user_id exists, check in given dtos and database too
#
#
# # either of email or phone number should exists
# # duplicate email exists, check in given dtos and database too
# # Can duplicate phone_number exists, check in given dtos and database too
#
# {
#     "field": "",
#     "cause": ""
#              "auth_user_dict"
# }
