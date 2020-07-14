class UserLogoutInteractor:
    def user_logout_wrapper(self, user_id: int):
        self.user_logout_from_a_device(user_id=user_id)

    @staticmethod
    def user_logout_from_a_device(user_id: int):
        from ib_iam.adapters.service_adapter import ServiceAdapter
        service_adapter = ServiceAdapter()
        service_adapter.auth_service.user_log_out_from_a_device(
            user_id=user_id
        )
        return
