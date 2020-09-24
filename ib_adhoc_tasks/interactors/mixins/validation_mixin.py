class ValidationMixin:

    @staticmethod
    def _validate_project_id(project_id: str):
        from ib_adhoc_tasks.exceptions.custom_exceptions import \
            InvalidProjectId
        from ib_adhoc_tasks.adapters.service_adapter import get_service_adapter
        service_adapter = get_service_adapter()
        valid_project_ids = service_adapter.iam_service.get_valid_project_ids(
            project_ids=[project_id]
        )
        is_project_id_invalid = not valid_project_ids
        if is_project_id_invalid:
            raise InvalidProjectId

    @staticmethod
    def _validate_is_user_exists_in_project(project_id: str, user_id: str):
        from ib_adhoc_tasks.exceptions.custom_exceptions import \
            UserNotExistInProject
        from ib_adhoc_tasks.adapters.service_adapter import get_service_adapter
        service_adapter = get_service_adapter()
        is_user_exist_in_project = service_adapter.iam_service \
            .is_user_exist_in_project(user_id=user_id)
        is_not_user_exist_in_project = not is_user_exist_in_project
        if is_not_user_exist_in_project:
            raise UserNotExistInProject

    # todo invalid limit

    # todo invalid offset