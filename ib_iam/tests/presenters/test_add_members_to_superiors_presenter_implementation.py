import pytest

from ib_iam.constants.enums import StatusCode


class TestAddMembersToSuperiorsPresenterImplementation:

    @pytest.fixture()
    def presenter(self):
        from ib_iam.presenters.add_members_to_superiors_presenter_implementation import \
            AddMembersToSuperiorsPresenterImplementation
        presenter = AddMembersToSuperiorsPresenterImplementation()
        return presenter

    def test_prepare_success_response_for_add_members_superiors(
            self, presenter):
        # Act
        response_object = presenter. \
            prepare_success_response_for_add_members_superiors()

        # Assert
        assert response_object.status_code == StatusCode.SUCCESS_CREATE.value
