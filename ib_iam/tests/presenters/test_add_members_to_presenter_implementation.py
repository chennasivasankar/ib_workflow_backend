import pytest

from ib_iam.constants.enums import StatusCode


class TestAddMembersToLevelPresenterImplementation:

    @pytest.fixture()
    def presenter(self):
        from ib_iam.presenters.add_members_to_presenter_implementation import \
            AddMembersToLevelPresenterImplementation
        presenter = AddMembersToLevelPresenterImplementation()
        return presenter

    def test_prepare_success_response_for_add_members_to_levels(
            self, presenter):
        # Act
        response_object = presenter. \
            prepare_success_response_for_add_members_to_levels()

        # Assert
        assert response_object.status_code == StatusCode.SUCCESS_CREATE.value
