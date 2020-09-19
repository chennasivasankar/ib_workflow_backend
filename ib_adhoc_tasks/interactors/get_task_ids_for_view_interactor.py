from ib_adhok_tasks.interactors.dtos.dtos import GroupByDTO


class GetTaskIdsForViewInteractor:

    def get_task_ids_for_view(
            self, user_id: str, project_id: str, adhoc_template_id: str,
            group_by_dto: GroupByDTO
    ):
        '''
        # TODO:
        validate user id
        validate project id
        validate adhoc template id
        validate group by dto
        '''

        from ib_adhok_tasks.adapters.service_adapter import get_service_adapter
        service_adapter = get_service_adapter()
        user_role_ids = service_adapter.iam_service.get_user_role_ids(
            user_id=user_id
        )
        # stage_ids_having_actions = self.service_adapter.