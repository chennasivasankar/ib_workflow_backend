from typing import List

from ib_discussions.exceptions.custom_exceptions import InvalidUserId


class InvalidProjectId(Exception):
    pass


class InvalidUserForProject(Exception):
    pass


class IamService:

    @property
    def interface(self):
        from ib_iam.app_interfaces.service_interface import ServiceInterface
        service_interface = ServiceInterface()
        return service_interface

    def get_subordinate_user_ids(self, project_id: str, user_id: str) -> List[
        str]:
        member_id_with_subordinate_member_ids_dto = \
            self.interface.get_user_id_with_subordinate_user_ids_dto(
                user_id=user_id,
                project_id=project_id
            )
        user_ids = member_id_with_subordinate_member_ids_dto.subordinate_member_ids
        user_ids.append(member_id_with_subordinate_member_ids_dto.member_id)
        return user_ids

    def validate_user_id_for_given_project(
            self, user_id: str, project_id: str
    ):
        try:
            is_invalid_user_id_for_given_project = \
                not self.interface.is_valid_user_id_for_given_project(
                    user_id=user_id, project_id=project_id
                )
        except InvalidUserId:
            raise InvalidUserId
        except InvalidProjectId:
            raise InvalidProjectId

        if is_invalid_user_id_for_given_project:
            raise InvalidUserForProject
