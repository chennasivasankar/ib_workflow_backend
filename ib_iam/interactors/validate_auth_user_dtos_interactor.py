from typing import List

from ib_iam.interactors.dtos.dtos import AuthUserDTO
from ib_iam.interactors.storage_interfaces.user_storage_interface import \
    UserStorageInterface


class ValidateAuthUserDTOsInteractor:

    def __init__(
            self,
            user_storage: UserStorageInterface
    ):
        self.user_storage = user_storage

    def validate_auth_user_dtos(self, auth_user_dtos: List[AuthUserDTO]):
        self._validate_user_auth_details(auth_user_dtos=auth_user_dtos)

    def _validate_user_auth_details(self, auth_user_dtos: List[AuthUserDTO]):
        valid_auth_user_dtos = []
        invitation_codes_from_db = []
        auth_tokens_from_db = []
        auth_token_user_ids_from_db = []
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
            "duplicate_emails": [],
            "duplicate_phone_numbers": [],
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
