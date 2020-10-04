from collections import Counter
from typing import List, Tuple

from ib_iam.adapters.dtos import UserProfileDTO
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

        for auth_user_dto in auth_user_dtos:
            self._update_empty_values_auth_user_dto(
                auth_user_dto=auth_user_dto
            )
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
                auth_user_dtos=valid_auth_user_dtos
            )
        exceptions_and_valid_dtos_dict.update(exceptions)
        print(exceptions_and_valid_dtos_dict)
        valid_auth_user_dtos = \
            exceptions_and_valid_dtos_dict["valid_auth_user_dtos"]
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
        valid_auth_user_dtos_to_populate, exceptions_dict_with_valid_auth_user_dtos = \
            self._validate_duplicates_in_given_auth_user_dtos(
                auth_user_dtos=valid_auth_user_dtos
            )
        exceptions_dict_with_valid_auth_user_dtos.update(
            {
                "duplicate_invitation_codes": duplicate_invitation_codes,
                "duplicate_auth_tokens": duplicate_auth_tokens,
                "duplicate_auth_token_user_ids": duplicate_auth_token_user_ids,
                "valid_auth_user_dtos": valid_auth_user_dtos_to_populate
            }
        )
        return exceptions_dict_with_valid_auth_user_dtos

    # @staticmethod
    # def _validate_duplicates_in_given_auth_user_dtos(
    #         auth_user_dtos: List[AuthUserDTO]
    # ):
    #     valid_auth_user_dtos = []
    #     invitation_codes = [
    #         auth_user_dto.invitation_code
    #         for auth_user_dto in auth_user_dtos
    #     ]
    #     auth_tokens = [
    #         auth_user_dto.token
    #         for auth_user_dto in auth_user_dtos
    #     ]
    #     auth_token_user_ids = [
    #         auth_user_dto.auth_token_user_id
    #         for auth_user_dto in auth_user_dtos
    #     ]
    #     already_existing_invitation_codes = []
    #     already_existing_auth_tokens = []
    #     already_existing_auth_token_user_ids = []
    #     for auth_user_dto in auth_user_dtos:
    #         is_invitation_code_already_exists = \
    #             invitation_codes.count(auth_user_dto.invitation_code) > 1
    #         is_auth_token_already_exists = \
    #             auth_tokens.count(auth_user_dto.token) > 1
    #         is_auth_token_user_id_exists = \
    #             auth_token_user_ids.count(auth_user_dto.auth_token_user_id) > 1
    #         if is_invitation_code_already_exists:
    #             already_existing_invitation_codes.append(auth_user_dto)
    #         elif is_auth_token_already_exists:
    #             already_existing_auth_tokens.append(auth_user_dto)
    #         elif is_auth_token_user_id_exists:
    #             already_existing_auth_token_user_ids.append(auth_user_dto)
    #         else:
    #             valid_auth_user_dtos.append(auth_user_dto)
    #     exceptions_dict = {
    #         "already_existing_invitation_codes": already_existing_invitation_codes,
    #         "already_existing_auth_tokens": already_existing_auth_tokens,
    #         "already_existing_auth_token_user_ids": already_existing_auth_token_user_ids
    #     }
    #     return valid_auth_user_dtos, exceptions_dict


    def main(self, auth_user_dtos: List[AuthUserDTO]):
        invalid_auth_user_dtos = []
        valid_auth_user_dtos = []

        invitation_codes_from_db = []
        auth_tokens_from_db = []
        user_ids_from_db = []
        for auth_token_user_dto in auth_user_dtos:
            invitation_codes_from_db.append(
                auth_token_user_dto.invitation_code)
            auth_tokens_from_db.append(auth_token_user_dto.token)
            user_ids_from_db.append(
                auth_token_user_dto.auth_token_user_id)

        duplicate_user_ids, passed_dtos = \
            self._validate_duplicate_user_ids(dtos=auth_user_dtos)

        duplicate_auth_tokens, passed_dtos = \
            self._validate_duplicate_auth_tokens(dtos=passed_dtos)

        duplicate_invitation_codes, passed_dtos = \
            self._validate_duplicate_invitation_code(dtos=auth_user_dtos)

        already_existing_invitation_codes, passed_dtos = \
            self._validate_already_existing_invitation_code(
                dtos=auth_user_dtos,
                invitation_codes_from_db=invitation_codes_from_db
            )

        already_existing_auth_tokens, passed_dtos = \
            self._validate_already_existing_auth_tokens(
                dtos=auth_user_dtos,
                auth_tokens_from_db=auth_tokens_from_db
            )

        already_existing_user_ids, passed_dtos = \
            self._validate_already_existing_user_ids(
                dtos=auth_user_dtos,
                user_ids_from_db=user_ids_from_db
            )

        exceptions = {
            "already_existing_invitation_codes": already_existing_invitation_codes,
            "already_existing_auth_tokens": already_existing_auth_tokens,
            "already_existing_user_ids": already_existing_user_ids,
            "duplicate_invitation_codes": duplicate_invitation_codes,
            "duplicate_auth_tokens": duplicate_auth_tokens,
            "duplicate_user_ids": duplicate_user_ids,
            "already_email_exists": [],
            "duplicate_emails": [],
            "already_phone_number_exists": [],
            "duplicate_phone_numbers": []
        }
        return passed_dtos, exceptions





    def _validate_duplicate_user_ids(self, dtos):
        user_ids = [dto.user_id for dto in dtos]

        from collections import Counter
        user_id_count_dict = Counter(user_ids)

        failed_dtos = []
        passed_dtos = []
        for dto in dtos:
            if user_id_count_dict[dto.user_id] > 1:
                failed_dtos.append(dto)
            else:
                passed_dtos.append(dto)

        return failed_dtos, passed_dtos

    def _validate_duplicate_auth_tokens(self, dtos):
        tokens = [dto.user_id for dto in dtos]

        from collections import Counter
        token_count_dict = Counter(tokens)

        failed_dtos = []
        passed_dtos = []
        for dto in dtos:
            if token_count_dict[dto.token] > 1:
                failed_dtos.append(dto)
            else:
                passed_dtos.append(dto)
        return failed_dtos, passed_dtos

    def _validate_duplicate_invitation_code(self, dtos):
        invitation_codes = [dto.user_id for dto in dtos]

        from collections import Counter
        invitation_code_count_dict = Counter(invitation_codes)

        failed_dtos = []
        passed_dtos = []
        for dto in dtos:
            if invitation_code_count_dict[dto.invitation_code] > 1:
                failed_dtos.append(dto)
            else:
                passed_dtos.append(dto)
        return failed_dtos, passed_dtos

    def _validate_already_existing_invitation_code(
            self, dtos, invitation_codes_from_db: List[str]
    ):
        failed_dtos = []
        passed_dtos = []
        for dto in dtos:
            if dto.invitation_code in invitation_codes_from_db:
                failed_dtos.append(dto)
            else:
                passed_dtos.append(dto)
        return failed_dtos, passed_dtos

    def _validate_already_existing_auth_tokens(
            self, dtos, auth_tokens_from_db: List[str]
    ):
        failed_dtos = []
        passed_dtos = []
        for dto in dtos:
            if dto.token in auth_tokens_from_db:
                failed_dtos.append(dto)
            else:
                passed_dtos.append(dto)
        return failed_dtos, passed_dtos

    def _validate_already_existing_user_ids(
            self, dtos, user_ids_from_db: List[str]
    ):
        failed_dtos = []
        passed_dtos = []
        for dto in dtos:
            if dto.auth_token_user_id in user_ids_from_db:
                failed_dtos.append(dto)
            else:
                passed_dtos.append(dto)
        return failed_dtos, passed_dtos

    @staticmethod
    def _validate_already_email_exists(
            auth_user_dtos: List[AuthUserDTO], user_profile_dtos: List[UserProfileDTO]
    ) -> Tuple[List[AuthUserDTO], List[AuthUserDTO]]:
        existing_emails = [
            user_profile_dto.email
            for user_profile_dto in user_profile_dtos
        ]

        failed_dtos = []
        passed_dtos = []
        for auth_user_dto in auth_user_dtos:
            if auth_user_dto.email in existing_emails:
                failed_dtos.append(auth_user_dto)
            else:
                passed_dtos.append(auth_user_dto)
        return failed_dtos, passed_dtos

    @staticmethod
    def _validate_duplicate_emails(
            auth_user_dtos: List[AuthUserDTO]
    ) -> Tuple[List[AuthUserDTO], List[AuthUserDTO]]:
        emails = [auth_user_dto.email for auth_user_dto in auth_user_dtos]
        emails_count_dict = Counter(emails)

        failed_dtos = []
        passed_dtos = []
        for auth_user_dto in auth_user_dtos:
            if emails_count_dict[auth_user_dto.email] > 1:
                failed_dtos.append(auth_user_dto)
            else:
                passed_dtos.append(auth_user_dto)
        return failed_dtos, passed_dtos

    @staticmethod
    def _validate_already_phone_number_exists(
            auth_user_dtos: List[AuthUserDTO],
            user_profile_dtos: List[UserProfileDTO]
    ) -> Tuple[List[AuthUserDTO], List[AuthUserDTO]]:
        existing_phone_numbers = [
            user_profile_dto.phone_number
            for user_profile_dto in user_profile_dtos
        ]

        failed_dtos = []
        passed_dtos = []
        for auth_user_dto in auth_user_dtos:
            if auth_user_dto.phone_number in existing_phone_numbers:
                failed_dtos.append(auth_user_dto)
            else:
                passed_dtos.append(auth_user_dto)
        return failed_dtos, passed_dtos

    @staticmethod
    def _validate_duplicate_phone_numbers(
            auth_user_dtos: List[AuthUserDTO]
    ) -> Tuple[List[AuthUserDTO], List[AuthUserDTO]]:
        phone_numbers = [
            auth_user_dto.phone_number for auth_user_dto in auth_user_dtos]
        phone_numbers_count_dict = Counter(phone_numbers)

        failed_dtos = []
        passed_dtos = []
        for auth_user_dto in auth_user_dtos:
            if phone_numbers_count_dict[auth_user_dto.phone_number] > 1:
                failed_dtos.append(auth_user_dto)
            else:
                passed_dtos.append(auth_user_dto)
        return failed_dtos, passed_dtos

    def _update_empty_values_auth_user_dto(self, auth_user_dto: AuthUserDTO):
        is_auth_token_empty = not auth_user_dto.token
        if is_auth_token_empty:
            auth_user_dto.token = self._generate_uuid4()
        is_auth_token_user_id_empty = not auth_user_dto.auth_token_user_id
        if is_auth_token_user_id_empty:
            auth_user_dto.auth_token_user_id = self._generate_uuid4()
        is_country_code_empty = not auth_user_dto.country_code
        if is_country_code_empty:
            auth_user_dto.country_code = "91"
        is_phone_number_empty = not auth_user_dto.phone_number
        if is_phone_number_empty:
            auth_user_dto.phone_number = None
            auth_user_dto.country_code = None
        is_email_empty = not auth_user_dto.email
        if is_email_empty:
            auth_user_dto.email = auth_user_dto.token + "@gmail.com"


    @staticmethod
    def _generate_uuid4():
        import uuid
        return str(uuid.uuid4())

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
