from typing import List
from ib_tasks.adapters.dtos import AssigneeDetailsDTO


class AssigneeDetailsService:

    @property
    def interface(self):
        from ib_iam.app_interfaces.service_interface import ServiceInterface
        return ServiceInterface()

    def get_assignees_details_dtos(
            self, assignee_ids: List[str]
    ) -> List[AssigneeDetailsDTO]:

        user_details_dtos = self.interface.get_user_details_bulk(assignee_ids)
        assignee_details_dtos = [
            AssigneeDetailsDTO(
                assignee_id=user_details_dto.user_id,
                name=user_details_dto.name,
                profile_pic_url=user_details_dto.profile_pic_url
            )
            for user_details_dto in user_details_dtos
        ]
        return assignee_details_dtos
