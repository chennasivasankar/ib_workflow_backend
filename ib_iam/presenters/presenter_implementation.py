from typing import List

from django_swagger_utils.utils.http_response_mixin \
    import HTTPResponseMixin

from ib_iam.adapters.dtos import UserProfileDTO
from ib_iam.interactors.presenter_interfaces.dtos import \
    ListOfCompleteUsersDTO, UserOptionsDetails
from ib_iam.interactors.presenter_interfaces.presenter_interface \
    import PresenterInterface
from ib_iam.interactors.storage_interfaces.dtos import UserTeamDTO, \
    UserRoleDTO, UserCompanyDTO


class PresenterImplementation(PresenterInterface, HTTPResponseMixin):
    def get_user_options_details_response(
            self, configuration_details: UserOptionsDetails):
        companies = configuration_details.companies
        teams = configuration_details.teams
        roles = configuration_details.roles
        companies_details = self._get_company_details(companies)
        teams_details = self._get_team_details(teams)
        roles_details = self._get_role_details(roles)
        response_dict = {
            "companies": companies_details,
            "teams": teams_details,
            "roles": roles_details
        }
        return self.prepare_200_success_response(
            response_dict=response_dict)

    def raise_role_name_should_not_be_empty_exception(self):
        from ib_iam.constants.exception_messages \
            import ROLE_NAME_SHOULD_NOT_BE_EMPTY
        response_dict = {
            "response": ROLE_NAME_SHOULD_NOT_BE_EMPTY[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": ROLE_NAME_SHOULD_NOT_BE_EMPTY[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict)

    def raise_role_description_should_not_be_empty_exception(self):
        from ib_iam.constants.exception_messages \
            import ROLE_DESCRIPTION_SHOULD_NOT_BE_EMPTY
        response_dict = {
            "response": ROLE_DESCRIPTION_SHOULD_NOT_BE_EMPTY[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": ROLE_DESCRIPTION_SHOULD_NOT_BE_EMPTY[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict)

    def raise_role_id_format_is_invalid_exception(self):
        from ib_iam.constants.exception_messages \
            import ROLE_ID_SHOULD_NOT_BE_IN_VALID_FORMAT
        response_dict = {
            "response": ROLE_ID_SHOULD_NOT_BE_IN_VALID_FORMAT[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": ROLE_ID_SHOULD_NOT_BE_IN_VALID_FORMAT[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict)

    def raise_duplicate_role_ids_exception(self):
        from ib_iam.constants.exception_messages \
            import DUPLICATE_ROLE_IDS
        response_dict = {
            "response": DUPLICATE_ROLE_IDS[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": DUPLICATE_ROLE_IDS[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict)

    def raise_user_is_not_admin_exception(self):
        from ib_iam.constants.exception_messages import \
            USER_DOES_NOT_HAVE_PERMISSION
        response_dict = {
            "response": USER_DOES_NOT_HAVE_PERMISSION[0],
            "http_status_code": StatusCode.FORBIDDEN.value,
            "res_status": USER_DOES_NOT_HAVE_PERMISSION[1]
        }
        return self.prepare_403_forbidden_response(
            response_dict=response_dict)

    def raise_invalid_offset_value_exception(self):
        from ib_iam.constants.exception_messages import INVALID_OFFSET_VALUE
        response_dict = {
            "response": INVALID_OFFSET_VALUE[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_OFFSET_VALUE[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict)

    def raise_invalid_limit_value_exception(self):
        from ib_iam.constants.exception_messages import INVALID_LIMIT_VALUE
        response_dict = {
            "response": INVALID_LIMIT_VALUE[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_LIMIT_VALUE[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict)

    def raise_offset_value_is_greater_than_limit_value_exception(self):
        from ib_iam.constants.exception_messages import \
            OFFSET_VALUE_IS_GREATER_THAN_LIMIT
        response_dict = {
            "response": OFFSET_VALUE_IS_GREATER_THAN_LIMIT[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": OFFSET_VALUE_IS_GREATER_THAN_LIMIT[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict)

    def response_for_get_users(
            self, complete_user_details_dtos: ListOfCompleteUsersDTO):
        user_dtos = complete_user_details_dtos.users
        team_dtos = complete_user_details_dtos.teams
        role_dtos = complete_user_details_dtos.roles
        company_dtos = complete_user_details_dtos.companies
        total_no_of_users = complete_user_details_dtos.total_no_of_users
        users = self._prepare_response_for_user_details(
            user_dtos, team_dtos, role_dtos, company_dtos)
        response = {
            "users": users,
            "total": total_no_of_users
        }
        return self.prepare_200_success_response(
            response_dict=response)

    def _prepare_response_for_user_details(
            self, user_dtos, team_dtos, role_dtos, company_dtos):
        users = []
        for user_profile_dto in user_dtos:
            user_id = user_profile_dto.user_id
            user_team_dtos = self._get_user_teams(team_dtos, user_id)
            user_role_dtos = self._get_user_roles(role_dtos, user_id)
            user_company_dto = self._get_company(company_dtos, user_id)
            user_response_dict = self._convert_user_response_dict(
                user_profile_dto, user_team_dtos, user_role_dtos,
                user_company_dto)
            users.append(user_response_dict)
        return users

    def _convert_user_response_dict(
            self, user_profile_dto: UserProfileDTO,
            user_team_dtos: List[UserTeamDTO],
            user_role_dtos: List[UserRoleDTO],
            user_company_dto: UserCompanyDTO):
        user_response_dict = {
            "user_id": user_profile_dto.user_id,
            "name": user_profile_dto.name,
            "email": user_profile_dto.email,
            "teams": self._convert_to_teams_dict(user_team_dtos),
            "roles": self._convert_to_roles_dict(user_role_dtos),
            "company": {
                "company_name": user_company_dto.company_name,
                "company_id": user_company_dto.company_id
            }
        }
        return user_response_dict

    @staticmethod
    def _get_user_teams(team_dtos, user_id):
        teams = []
        for team_dto in team_dtos:
            if team_dto.user_id == user_id:
                teams.append(team_dto)
        return teams

    @staticmethod
    def _get_user_roles(role_dtos, user_id):
        roles = []
        for role_dto in role_dtos:
            if role_dto.user_id == user_id:
                roles.append(role_dto)
        return roles

    @staticmethod
    def _get_company(company_dtos, user_id):
        for company_dto in company_dtos:
            if company_dto.user_id == user_id:
                return company_dto

    @staticmethod
    def _convert_to_teams_dict(team_dtos):
        teams = []
        for team_dto in team_dtos:
            teams.append({
                "team_id": team_dto.team_id,
                "team_name": team_dto.team_name
            })
        return teams

    @staticmethod
    def _convert_to_roles_dict(role_dtos):
        roles = []
        for role_dto in role_dtos:
            roles.append({
                "role_id": role_dto.role_id,
                "role_name": role_dto.name
            })
        return roles

    def raise_invalid_name_exception(self):
        from ib_iam.constants.exception_messages import EMPTY_NAME_IS_INVALID
        response_dict = {
            "response": EMPTY_NAME_IS_INVALID[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": EMPTY_NAME_IS_INVALID[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict)

    def raise_invalid_email_exception(self):
        from ib_iam.constants.exception_messages import INVALID_EMAIL
        response_dict = {
            "response": INVALID_EMAIL[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_EMAIL[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict)

    def raise_user_account_already_exist_with_this_email_exception(self):
        from ib_iam.constants.exception_messages \
            import USER_ACCOUNT_ALREADY_EXIST_FOR_THIS_EMAIL
        response_dict = {
            "response": USER_ACCOUNT_ALREADY_EXIST_FOR_THIS_EMAIL[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": USER_ACCOUNT_ALREADY_EXIST_FOR_THIS_EMAIL[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict)

    def raise_name_should_not_contain_special_characters_exception(self):
        from ib_iam.constants.exception_messages \
            import NAME_SHOULD_NOT_CONTAINS_SPECIAL_CHARACTERS_AND_NUMBERS
        response = NAME_SHOULD_NOT_CONTAINS_SPECIAL_CHARACTERS_AND_NUMBERS[0]
        res_status = NAME_SHOULD_NOT_CONTAINS_SPECIAL_CHARACTERS_AND_NUMBERS[1]
        response_dict = {
            "response": response,
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": res_status

        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict)

    def user_created_response(self):
        from ib_iam.constants.exception_messages import \
            CREATE_USER_SUCCESSFULLY
        response_dict = {
            "response": CREATE_USER_SUCCESSFULLY[0],
            "http_status_code": StatusCode.SUCCESS_CREATE.value,
            "res_status": CREATE_USER_SUCCESSFULLY[1]

        }
        return self.prepare_201_created_response(
            response_dict=response_dict)

    def edit_user_edited_successfully(self):
        from ib_iam.constants.exception_messages import EDIT_USER_SUCCESSFULLY
        response_dict = {
            "response": EDIT_USER_SUCCESSFULLY[0],
            "http_status_code": StatusCode.SUCCESS.value,
            "res_status": EDIT_USER_SUCCESSFULLY[1]

        }
        return self.prepare_200_success_response(
            response_dict=response_dict)

    def raise_user_does_not_exist(self):
        from ib_iam.constants.exception_messages \
            import USER_DOES_NOT_EXIST
        response_dict = {
            "response": USER_DOES_NOT_EXIST[0],
            "http_status_code": StatusCode.NOT_FOUND.value,
            "res_status": USER_DOES_NOT_EXIST[1]
        }
        response = self.prepare_404_not_found_response(
            response_dict=response_dict)
        return response

    @staticmethod
    def _get_role_details(roles):
        roles_details = []
        for role in roles:
            roles_details.append({
                "role_id": role.role_id,
                "role_name": role.name
            })
        return roles_details

    @staticmethod
    def _get_team_details(teams):
        teams_details = []
        for team in teams:
            teams_details.append({
                "team_id": team.team_id,
                "team_name": team.team_name
            })
        return teams_details

    @staticmethod
    def _get_company_details(companies):
        companies_details = []
        for company in companies:
            companies_details.append({
                "company_id": company.company_id,
                "company_name": company.company_name
            })
        return companies_details

    def raise_role_ids_are_invalid(self):
        from ib_iam.constants.exception_messages import InvalidRoleIds
        response_dict = {
            "response": InvalidRoleIds[0],
            "http_status_code": StatusCode.NOT_FOUND.value,
            "res_status": InvalidRoleIds[1]
        }
        return self.prepare_404_not_found_response(
            response_dict=response_dict
        )

    def raise_company_ids_is_invalid(self):
        from ib_iam.constants.exception_messages import InvalidCompanyId
        response_dict = {
            "response": InvalidCompanyId[0],
            "http_status_code": StatusCode.NOT_FOUND.value,
            "res_status": InvalidCompanyId[1]
        }
        return self.prepare_404_not_found_response(
            response_dict=response_dict
        )

    def raise_team_ids_are_invalid(self):
        from ib_iam.constants.exception_messages import InvalidTeamIds
        response_dict = {
            "response": InvalidTeamIds[0],
            "http_status_code": StatusCode.NOT_FOUND.value,
            "res_status": InvalidTeamIds[1]
        }
        return self.prepare_404_not_found_response(
            response_dict=response_dict
        )


INVALID_EMAIL = (
    "Please send valid email",
    "INVALID_EMAIL"
)

INCORRECT_PASSWORD = (
    "Please send valid password with you registered",
    "INCORRECT_PASSWORD"
)

PASSWORD_MIN_LENGTH = (
    "Please send the password with minimum required length is {password_min_length}",
    "PASSWORD_MIN_LENGTH"
)

PASSWORD_AT_LEAST_ONE_SPECIAL_CHARACTER = (
    "Please send the password at least with one special character",
    "PASSWORD_AT_LEAST_ONE_SPECIAL_CHARACTER"
)

USER_ACCOUNT_DOES_NOT_EXIST = (
    "user account does not exist. please send valid email",
    "USER_ACCOUNT_DOES_NOT_EXIST"
)

NOT_STRONG_PASSWORD = (
    "Please send the strong password",
    "NOT_STRONG_PASSWORD"
)

TOKEN_DOES_NOT_EXIST = (
    "Please send valid token",
    "TOKEN_DOES_NOT_EXIST"
)

TOKEN_HAS_EXPIRED = (
    "Please send valid token which is not expired",
    "TOKEN_HAS_EXPIRED"
)

from django.http import HttpResponse
from ib_iam.adapters.auth_service import UserTokensDTO
from ib_iam.constants.enums import StatusCode
from ib_iam.interactors.presenter_interfaces.presenter_interface import \
    AuthPresenterInterface


class AuthPresenterImplementation(AuthPresenterInterface, HTTPResponseMixin):

    def raise_exception_for_invalid_email(self) -> HttpResponse:
        response_dict = {
            "response": INVALID_EMAIL[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_EMAIL[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict
        )

    def raise_exception_for_incorrect_password(self) -> HttpResponse:
        response_dict = {
            "response": INCORRECT_PASSWORD[0],
            "http_status_code": StatusCode.NOT_FOUND.value,
            "res_status": INCORRECT_PASSWORD[1]
        }
        return self.prepare_404_not_found_response(response_dict=response_dict)

    def prepare_response_for_user_tokens_dto_and_is_admin(
            self, tokens_dto: UserTokensDTO, is_admin: int
    ) -> HttpResponse:
        response_dict = {
            "access_token": tokens_dto.access_token,
            "refresh_token": tokens_dto.refresh_token,
            "expires_in_seconds": tokens_dto.expires_in_seconds,
            "is_admin": is_admin
        }
        return self.prepare_200_success_response(
            response_dict=response_dict
        )

    def raise_exception_for_user_account_does_not_exists(self) -> HttpResponse:
        response_dict = {
            "response": USER_ACCOUNT_DOES_NOT_EXIST[0],
            "http_status_code": StatusCode.NOT_FOUND.value,
            "res_status": USER_ACCOUNT_DOES_NOT_EXIST[1]
        }
        return self.prepare_404_not_found_response(response_dict=response_dict)

    def raise_exception_for_password_min_length_required(self) -> HttpResponse:
        from ib_iam.constants.config import REQUIRED_PASSWORD_MIN_LENGTH
        min_required_length_for_password = REQUIRED_PASSWORD_MIN_LENGTH
        response_dict = {
            "response": PASSWORD_MIN_LENGTH[0].format(
                password_min_length=min_required_length_for_password
            ),
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": PASSWORD_MIN_LENGTH[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict
        )

    def raise_exception_for_password_at_least_one_special_character_required(
            self
    ) -> HttpResponse:
        response_dict = {
            "response": PASSWORD_AT_LEAST_ONE_SPECIAL_CHARACTER[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": PASSWORD_AT_LEAST_ONE_SPECIAL_CHARACTER[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict
        )

    def raise_exception_for_user_account_does_not_exist(self):
        response_dict = {
            "response": USER_ACCOUNT_DOES_NOT_EXIST[0],
            "http_status_code": StatusCode.NOT_FOUND.value,
            "res_status": USER_ACCOUNT_DOES_NOT_EXIST[1]
        }
        return self.prepare_404_not_found_response(response_dict=response_dict)

    def raise_exception_for_token_does_not_exists(self):
        response_dict = {
            "response": TOKEN_DOES_NOT_EXIST[0],
            "http_status_code": StatusCode.NOT_FOUND.value,
            "res_status": TOKEN_DOES_NOT_EXIST[1]
        }
        return self.prepare_404_not_found_response(response_dict=response_dict)

    def raise_exception_for_token_has_expired(self):
        response_dict = {
            "response": TOKEN_HAS_EXPIRED[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": TOKEN_HAS_EXPIRED[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict
        )

    def get_update_user_password_success_response(self):
        return self.prepare_200_success_response(response_dict={})

    def get_success_response_for_reset_password_link_to_user_email(self) \
            -> HttpResponse:
        return self.prepare_200_success_response(response_dict={})
