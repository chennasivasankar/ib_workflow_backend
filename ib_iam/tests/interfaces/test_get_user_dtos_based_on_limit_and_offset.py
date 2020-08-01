import pytest


class TestGetUserDTOsBasedOnLimitAndOffset:

    def test_with_invalid_offset_raise_exception(self):
        # Arrange
        offset = -1
        limit = 1
        search_query = ""

        from ib_iam.app_interfaces.service_interface import ServiceInterface
        service_interface = ServiceInterface()

        # Assert
        from ib_iam.exceptions.custom_exceptions import InvalidOffsetValue
        with pytest.raises(InvalidOffsetValue):
            service_interface.get_user_dtos_based_on_limit_and_offset(
                limit=limit, offset=offset, search_query=search_query
            )

    def test_with_invalid_limit_raise_exception(self):
        # Arrange
        offset = 1
        limit = -1
        search_query = ""

        from ib_iam.app_interfaces.service_interface import ServiceInterface
        service_interface = ServiceInterface()

        # Assert
        from ib_iam.exceptions.custom_exceptions import InvalidLimitValue
        with pytest.raises(InvalidLimitValue):
            service_interface.get_user_dtos_based_on_limit_and_offset(
                limit=limit, offset=offset, search_query=search_query
            )

    @pytest.mark.django_db
    def test_with_valid_details_return_response(self):
        # Arrange
        offset = 1
        limit = 2
        search_query = "s"

        user_details_dict = [
            {
                "user_id": "2bdb417e-4632-419a-8ddd-085ea272c6eb",
                "name": "Samuel"
            },
            {
                "user_id": "548a803c-7b48-47ba-a700-24f2ea0d1280",
                "name": "Matthew"
            },
            {
                "user_id": "4b8fb6eb-fa7d-47c1-8726-cd917901104e",
                "name": "Anthony"
            },
            {
                "user_id": "f2c02d98-f311-4ab2-8673-3daa00757002",
                "name": "Christopher"
            },
            {
                "user_id": "aa66c40f-6d93-484a-b418-984716514c7b",
                "name": "Thomas"
            },
            {
                "user_id": "c982032b-53a7-4dfa-a627-4701a5230765",
                "name": "Jonathan"
            }
        ]

        expected_user_details_dict = [
            {
                "user_id": 'f2c02d98-f311-4ab2-8673-3daa00757002',
                "name": 'Christopher'
            },
            {
                "user_id": 'aa66c40f-6d93-484a-b418-984716514c7b',
                "name": 'Thomas'
            }
        ]

        from ib_iam.tests.factories.storage_dtos import UserIdAndNameFactory
        expected_user_details_dtos = [
            UserIdAndNameFactory(
                user_id=user_details["user_id"],
                name=user_details["name"]
            )
            for user_details in expected_user_details_dict
        ]

        from ib_iam.tests.factories.models import UserDetailsFactory
        for user_details in user_details_dict:
            UserDetailsFactory(
                user_id=user_details["user_id"],
                name=user_details["name"]
            )

        from ib_iam.app_interfaces.service_interface import ServiceInterface
        service_interface = ServiceInterface()

        # Act
        response = service_interface.get_user_dtos_based_on_limit_and_offset(
            limit=limit, offset=offset, search_query=search_query
        )

        # Assert
        self._compare_user_details_dtos(response, expected_user_details_dtos)

    def _compare_user_details_dtos(
            self, user_details_dtos_list1, user_details_dtos_list2
    ):
        user_details_dtos_list1 = sorted(
            user_details_dtos_list1,
            key=lambda x: x.user_id
        )
        user_details_dtos_list2 = sorted(
            user_details_dtos_list2,
            key=lambda x: x.user_id
        )
        map_user_details_dtos_list = list(
            zip(user_details_dtos_list1, user_details_dtos_list2)
        )

        for user_details_dto1, user_details_dto2 in map_user_details_dtos_list:
            self._compare_user_details_dto(
                user_details_dto1=user_details_dto1,
                user_details_dto2=user_details_dto2
            )

    @staticmethod
    def _compare_user_details_dto(user_details_dto1, user_details_dto2):
        assert user_details_dto2 == user_details_dto1
