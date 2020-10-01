class ValidationMixin:

    @staticmethod
    def _validate_project_id(project_id: str):
        from ib_adhoc_tasks.exceptions.custom_exceptions import \
            InvalidProjectId
        from ib_adhoc_tasks.adapters.service_adapter import get_service_adapter
        service = get_service_adapter()
        valid_project_ids = service.iam_service.get_valid_project_ids(
            project_ids=[project_id]
        )
        is_project_id_invalid = not valid_project_ids
        if is_project_id_invalid:
            raise InvalidProjectId

    @staticmethod
    def _validate_is_user_exists_in_project(project_id: str, user_id: str):
        from ib_adhoc_tasks.adapters.service_adapter import get_service_adapter
        service_adapter = get_service_adapter()
        service_adapter.iam_service.validate_user_id_for_given_project(
            user_id=user_id, project_id=project_id
        )

    @staticmethod
    def _validate_user_project_and_user_existence_in_project(
            project_id: str, user_id: str
    ):
        from ib_adhoc_tasks.adapters.service_adapter import get_service_adapter
        service = get_service_adapter()
        service.iam_service.validate_user_id_for_given_project(
            project_id=project_id, user_id=user_id
        )

    @staticmethod
    def _validate_limit_offset_values(limit: int, offset: int):
        from ib_adhoc_tasks.exceptions.custom_exceptions import \
            InvalidGroupLimitValue, InvalidGroupOffsetValue
        if limit < 0:
            raise InvalidGroupLimitValue
        if offset < 0:
            raise InvalidGroupOffsetValue
