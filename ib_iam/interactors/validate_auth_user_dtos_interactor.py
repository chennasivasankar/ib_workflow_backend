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
        user_profile_dtos = self._get_all_user_profile_dtos(
            auth_user_dtos=auth_user_dtos
        )
        auth_tokens_from_db, invitation_codes_from_db, user_ids_from_db = \
            self._get_user_auth_related_data_from_db()

        already_email_exists, passed_dtos = self._validate_already_email_exists(
            auth_user_dtos=auth_user_dtos, user_profile_dtos=user_profile_dtos
        )
        duplicate_emails, passed_dtos = self._validate_duplicate_emails(
            auth_user_dtos=passed_dtos
        )
        already_phone_number_exists, passed_dtos = \
            self._validate_already_phone_number_exists(
                auth_user_dtos=passed_dtos, user_profile_dtos=user_profile_dtos
            )
        duplicate_phone_numbers, passed_dtos = \
            self._validate_duplicate_phone_numbers(auth_user_dtos=passed_dtos)
        duplicate_user_ids, passed_dtos = \
            self._validate_duplicate_user_ids(dtos=passed_dtos)

        duplicate_auth_tokens, passed_dtos = \
            self._validate_duplicate_auth_tokens(dtos=passed_dtos)

        duplicate_invitation_codes, passed_dtos = \
            self._validate_duplicate_invitation_code(dtos=passed_dtos)

        already_existing_invitation_codes, passed_dtos = \
            self._validate_already_existing_invitation_code(
                dtos=passed_dtos,
                invitation_codes_from_db=invitation_codes_from_db
            )
        already_existing_auth_tokens, passed_dtos = \
            self._validate_already_existing_auth_tokens(
                dtos=passed_dtos,
                auth_tokens_from_db=auth_tokens_from_db
            )

        already_existing_user_ids, passed_dtos = \
            self._validate_already_existing_user_ids(
                dtos=passed_dtos,
                user_ids_from_db=user_ids_from_db
            )
        either_email_or_phone_number_exists, passed_dtos = \
            self._validate_either_email_or_phone_number_exists(
                dtos=passed_dtos
            )
        empty_invitation_codes_exists, passed_dtos = \
            self._validate_empty_invitation_codes_exists(
                dtos=passed_dtos
            )

        exceptions = {
            "already_existing_invitation_codes": already_existing_invitation_codes,
            "already_existing_auth_tokens": already_existing_auth_tokens,
            "already_existing_user_ids": already_existing_user_ids,
            "duplicate_invitation_codes": duplicate_invitation_codes,
            "duplicate_auth_tokens": duplicate_auth_tokens,
            "duplicate_user_ids": duplicate_user_ids,
            "already_email_exists": already_email_exists,
            "duplicate_emails": duplicate_emails,
            "already_phone_number_exists": already_phone_number_exists,
            "duplicate_phone_numbers": duplicate_phone_numbers,
            "either_email_or_phone_number_exists": either_email_or_phone_number_exists,
            "empty_invitation_codes_exists": empty_invitation_codes_exists
        }
        return passed_dtos, exceptions

    def _get_user_auth_related_data_from_db(self):
        invitation_codes_from_db = []
        auth_tokens_from_db = []
        user_ids_from_db = []
        auth_token_user_dtos = self.user_storage.get_all_auth_token_user_dtos()
        for auth_token_user_dto in auth_token_user_dtos:
            invitation_codes_from_db.append(
                auth_token_user_dto.invitation_code)
            auth_tokens_from_db.append(auth_token_user_dto.token)
            user_ids_from_db.append(
                auth_token_user_dto.auth_token_user_id)
        return auth_tokens_from_db, invitation_codes_from_db, user_ids_from_db

    def _get_all_user_profile_dtos(self, auth_user_dtos: List[AuthUserDTO]):
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
        return user_profile_dtos

    def _validate_duplicate_user_ids(self, dtos):
        user_ids = [dto.auth_token_user_id for dto in dtos]

        from collections import Counter
        user_id_count_dict = Counter(user_ids)

        failed_dtos = []
        passed_dtos = []
        for dto in dtos:
            if user_id_count_dict[dto.auth_token_user_id] > 1:
                failed_dtos.append(dto)
            else:
                passed_dtos.append(dto)

        return failed_dtos, passed_dtos

    def _validate_duplicate_auth_tokens(self, dtos):
        tokens = [dto.token for dto in dtos]

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
        invitation_codes = [dto.invitation_code for dto in dtos]

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
            auth_user_dtos: List[AuthUserDTO],
            user_profile_dtos: List[UserProfileDTO]
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

    @staticmethod
    def _validate_either_email_or_phone_number_exists(
            dtos: List[AuthUserDTO]
    ):
        failed_dtos = []
        passed_dtos = []
        for dto in dtos:
            is_no_email_exists = not dto.email
            is_no_phone_number_exists = not dto.phone_number
            if is_no_email_exists and is_no_phone_number_exists:
                failed_dtos.append(dto)
            else:
                passed_dtos.append(dto)
        return failed_dtos, passed_dtos

    @staticmethod
    def _validate_empty_invitation_codes_exists(
            dtos: List[AuthUserDTO]
    ):
        failed_dtos = []
        passed_dtos = []
        for dto in dtos:
            is_no_invitation_exists = not dto.invitation_code
            if is_no_invitation_exists:
                failed_dtos.append(dto)
            else:
                passed_dtos.append(dto)
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
