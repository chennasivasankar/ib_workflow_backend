import json

import pytest

from ib_discussions.constants.enum import StatusCode


class TestGetDiscussionsPresenterImplementation:

    @pytest.fixture()
    def presenter(self):
        from ib_discussions.presenters.get_discussion_presenter_implementation import \
            GetDiscussionPresenterImplementation
        presenter = GetDiscussionPresenterImplementation()
        return presenter

    def test_raise_exception_for_entity_id_not_found(self, presenter):
        # Arrange
        from ib_discussions.presenters.get_discussion_presenter_implementation import \
            ENTITY_ID_NOT_FOUND
        expected_response = ENTITY_ID_NOT_FOUND[0]
        expected_http_status_code = StatusCode.NOT_FOUND.value
        expected_res_status = ENTITY_ID_NOT_FOUND[1]

        # Act
        response_obj = presenter.raise_exception_for_entity_id_not_found()

        # Assert
        response_data = json.loads(response_obj.content)

        assert response_data["response"] == expected_response
        assert response_data["http_status_code"] == expected_http_status_code
        assert response_data["res_status"] == expected_res_status

    def test_raise_exception_for_discussion_set_not_found(self, presenter):
        # Arrange
        from ib_discussions.presenters.get_discussion_presenter_implementation import \
            DISCUSSION_SET_NOT_FOUND
        expected_response = DISCUSSION_SET_NOT_FOUND[0]
        expected_http_status_code = StatusCode.NOT_FOUND.value
        expected_res_status = DISCUSSION_SET_NOT_FOUND[1]

        # Act
        response_obj = presenter.raise_exception_for_discussion_set_not_found()

        # Assert
        response_data = json.loads(response_obj.content)

        assert response_data["response"] == expected_response
        assert response_data["http_status_code"] == expected_http_status_code
        assert response_data["res_status"] == expected_res_status

    def test_raise_exception_for_invalid_entity_type_for_entity_id(self,
                                                                   presenter):
        # Arrange
        from ib_discussions.presenters.get_discussion_presenter_implementation import \
            INVALID_ENTITY_TYPE_FOR_ENTITY_ID
        expected_response = INVALID_ENTITY_TYPE_FOR_ENTITY_ID[0]
        expected_http_status_code = StatusCode.BAD_REQUEST.value
        expected_res_status = INVALID_ENTITY_TYPE_FOR_ENTITY_ID[1]

        # Act
        response_obj \
            = presenter.raise_exception_for_invalid_entity_type_for_entity_id()

        # Assert
        response_data = json.loads(response_obj.content)

        assert response_data["response"] == expected_response
        assert response_data["http_status_code"] == expected_http_status_code
        assert response_data["res_status"] == expected_res_status

    def test_raise_exception_for_invalid_user_id(self,
                                                 presenter):
        # Arrange
        from ib_discussions.presenters.get_discussion_presenter_implementation import \
            INVALID_USER_ID
        expected_response = INVALID_USER_ID[0]
        expected_http_status_code = StatusCode.BAD_REQUEST.value
        expected_res_status = INVALID_USER_ID[1]

        # Act
        response_obj \
            = presenter.raise_exception_for_invalid_user_id()

        # Assert
        response_data = json.loads(response_obj.content)

        assert response_data["response"] == expected_response
        assert response_data["http_status_code"] == expected_http_status_code
        assert response_data["res_status"] == expected_res_status

    def test_raise_exception_for_invalid_offset(self, presenter):
        # Arrange
        from ib_discussions.presenters.create_discussion_presenter_implementation import \
            INVALID_OFFSET
        expected_response = INVALID_OFFSET[0]
        expected_http_status_code = StatusCode.BAD_REQUEST.value
        expected_res_status = INVALID_OFFSET[1]

        # Act
        response_obj = presenter.raise_exception_for_invalid_offset()

        # Assert
        response_data = json.loads(response_obj.content)

        assert response_data["response"] == expected_response
        assert response_data["http_status_code"] == expected_http_status_code
        assert response_data["res_status"] == expected_res_status

    def test_raise_exception_for_invalid_limit(self, presenter):
        # Arrange
        from ib_discussions.presenters.create_discussion_presenter_implementation import \
            INVALID_LIMIT
        expected_response = INVALID_LIMIT[0]
        expected_http_status_code = StatusCode.BAD_REQUEST.value
        expected_res_status = INVALID_LIMIT[1]

        # Act
        response_obj = presenter.raise_exception_for_invalid_limit()

        # Assert
        response_data = json.loads(response_obj.content)

        assert response_data["response"] == expected_response
        assert response_data["http_status_code"] == expected_http_status_code
        assert response_data["res_status"] == expected_res_status

    @pytest.fixture()
    def get_discussions_details_dto(self):
        discussion_set_id = "e892e8db-6064-4d8f-9ce2-7c9032dbd8a5"
        from ib_discussions.tests.factories.adapter_dtos import \
            UserProfileFactory
        user_ids = [
            'fc4c3c81-ebc3-4957-8c62-e1cbb6238b27',
            '458813d7-9954-44fd-a014-a9faafce5948',
            '06b0bdc4-76ac-4a01-a4da-68156f0527f5'
        ]
        user_profile_dtos = [
            UserProfileFactory.create(user_id=user_id)
            for user_id in user_ids
        ]
        discussion_ids = [
            'c5a444ea-589a-4e8f-b006-cfac3c1c0b78',
            '5ce6581b-86ce-4246-8551-2c8a8ed4df87',
            'ed10c17c-8995-4d84-9807-189a54a2049d'
        ]
        from ib_discussions.tests.factories.storage_dtos import \
            CompleteDiscussionFactory
        complete_discussion_dtos = [
            CompleteDiscussionFactory(
                discussion_set_id=discussion_set_id,
                user_id=user_profile_dtos[i].user_id,
                discussion_id=discussion_ids[i]
            )
            for i in range(0, 3)
        ]
        from ib_discussions.interactors.presenter_interfaces.dtos import \
            DiscussionsDetailsDTO
        discussions_details_dto = DiscussionsDetailsDTO(
            complete_discussion_dtos=complete_discussion_dtos,
            user_profile_dtos=user_profile_dtos,
            total_count=len(complete_discussion_dtos)
        )
        return discussions_details_dto

    def test_prepare_response_for_discussions_details_dto(
            self, presenter, get_discussions_details_dto
    ):
        # Act
        response_object = presenter.prepare_response_for_discussions_details_dto(
            get_discussions_details_dto)
        expected_discussion_details_response = {
            'discussions': [{
                'discussion_id': 'c5a444ea-589a-4e8f-b006-cfac3c1c0b78',
                'description': 'Description of discussion id is c5a444ea-589a-4e8f-b006-cfac3c1c0b78',
                'title': 'Title of discussion id is c5a444ea-589a-4e8f-b006-cfac3c1c0b78',
                'created_at': '01-01-2008,00:00:1199125800.000000',
                'author': {
                    'user_id': 'fc4c3c81-ebc3-4957-8c62-e1cbb6238b27',
                    'name': 'name of user_id is fc4c3c81-ebc3-4957-8c62-e1cbb6238b27',
                    'profile_pic_url': 'https://graph.ib_users.com/fc4c3c81-ebc3-4957-8c62-e1cbb6238b27/picture'
                },
                "is_clarified": True
            }, {
                'discussion_id': '5ce6581b-86ce-4246-8551-2c8a8ed4df87',
                'description': 'Description of discussion id is 5ce6581b-86ce-4246-8551-2c8a8ed4df87',
                'title': 'Title of discussion id is 5ce6581b-86ce-4246-8551-2c8a8ed4df87',
                'created_at': '01-01-2008,00:00:1199125800.000000',
                'author': {
                    'user_id': '458813d7-9954-44fd-a014-a9faafce5948',
                    'name': 'name of user_id is 458813d7-9954-44fd-a014-a9faafce5948',
                    'profile_pic_url': 'https://graph.ib_users.com/458813d7-9954-44fd-a014-a9faafce5948/picture'
                },
                "is_clarified": False
            }, {
                'discussion_id': 'ed10c17c-8995-4d84-9807-189a54a2049d',
                'description': 'Description of discussion id is ed10c17c-8995-4d84-9807-189a54a2049d',
                'title': 'Title of discussion id is ed10c17c-8995-4d84-9807-189a54a2049d',
                'created_at': '01-01-2008,00:00:1199125800.000000',
                'author': {
                    'user_id': '06b0bdc4-76ac-4a01-a4da-68156f0527f5',
                    'name': 'name of user_id is 06b0bdc4-76ac-4a01-a4da-68156f0527f5',
                    'profile_pic_url': 'https://graph.ib_users.com/06b0bdc4-76ac-4a01-a4da-68156f0527f5/picture'
                },
                "is_clarified": True
            }],
            'total_count': 3
        }

        # Assert
        response_dict = json.loads(response_object.content)

        self._compare_two_discussions_list(
            expected_discussion_details_response["discussions"],
            response_dict["discussions"]
        )
        assert expected_discussion_details_response["total_count"] \
               == response_dict["total_count"]

    def _compare_two_discussions_list(self, discussion_list1, discussion_list2):
        discussion_list1 = sorted(
            discussion_list1,
            key=lambda x: x['discussion_id']
        )
        discussion_list2 = sorted(
            discussion_list2,
            key=lambda x: x['discussion_id']
        )
        map_of_two_discussion_lists = list(zip(
            discussion_list1, discussion_list2
        ))

        for discussion_dict1, discussion_dict2 in map_of_two_discussion_lists:
            self._compare_two_discussion_dict(discussion_dict1,
                                              discussion_dict2)

    @staticmethod
    def _compare_two_discussion_dict(discussion_dict1, discussion_dict2):
        assert discussion_dict1 == discussion_dict2
