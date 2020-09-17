from unittest.mock import create_autospec, Mock

import pytest


class TestAddRolesInteractor:

    @pytest.fixture
    def storage_mock(self):
        from ib_iam.interactors.storage_interfaces.roles_storage_interface \
            import RolesStorageInterface
        return create_autospec(RolesStorageInterface)

    @pytest.fixture
    def presenter(self):
        from ib_iam.interactors.presenter_interfaces.role_presenter_interface \
            import AddRolesPresenterInterface
        return create_autospec(AddRolesPresenterInterface)

    @pytest.fixture
    def interactor(self, storage_mock):
        from ib_iam.interactors.roles_interactor import RolesInteractor
        return RolesInteractor(storage=storage_mock)

    def test_given_role_ids_are_duplicate_then_raise_exception(
            self, interactor, storage_mock, presenter
    ):
        # Arrange
        project_id = "FA"
        roles = [
            {
                "role_id": "PAYMENT_POC",
                "role_name": "payment poc",
                "description": "payment poc"
            },
            {
                "role_id": "PAYMENT_POC",
                "role_name": "payment_poc",
                "description": "payment poc"
            },
            {
                "role_id": "PAYMENTPOC",
                "role_name": "payment_poc",
                "description": "payment poc"
            },

        ]
        from ib_iam.tests.factories.storage_dtos import RoleDTOFactory
        role_dtos = [
            RoleDTOFactory(
                role_id=role["role_id"], name=role["role_name"],
                description=role["description"]
            ) for role in roles
        ]
        duplicate_role_ids = ['PAYMENT_POC']

        presenter.response_for_duplicate_role_ids_exception.return_value = \
            Mock()

        # Act
        interactor.add_project_roles_wrapper(
            role_dtos=role_dtos, presenter=presenter, project_id=project_id
        )

        # Assert
        call_args = presenter.response_for_duplicate_role_ids_exception.call_args

        assert call_args[0][0].role_ids == duplicate_role_ids
        presenter.response_for_duplicate_role_ids_exception.assert_called_once()

    def test_given_role_name_is_empty_then_raise_exception(
            self, interactor, storage_mock, presenter
    ):
        # Arrange
        project_id = "FA"
        roles = [{
            "role_id": "PAYMENT_POC",
            "role_name": "",
            "description": "payment poc"
        }]
        from ib_iam.tests.factories.storage_dtos import RoleDTOFactory
        role_dtos = [
            RoleDTOFactory(
                role_id=role["role_id"],
                name=role["role_name"],
                description=role["description"]
            )
            for role in roles
        ]
        presenter.response_for_role_name_should_not_be_empty_exception.return_value = \
            Mock()

        # Act
        interactor.add_project_roles_wrapper(
            role_dtos=role_dtos, presenter=presenter, project_id=project_id
        )

        # Assert
        presenter.response_for_role_name_should_not_be_empty_exception.assert_called_once()

    def test_given_role_description_is_empty_then_raise_exception(
            self, interactor, storage_mock, presenter
    ):
        # Arrange
        project_id = "FA"
        roles = [{
            "role_id": "PAYMENT_POC",
            "role_name": "payment poc",
            "description": ""
        }]
        from ib_iam.tests.factories.storage_dtos import RoleDTOFactory
        role_dtos = [
            RoleDTOFactory(
                role_id=role["role_id"],
                name=role["role_name"],
                description=role["description"]
            )
            for role in roles
        ]
        presenter.response_for_role_description_should_not_be_empty_exception.return_value = \
            Mock()

        # Act
        interactor.add_project_roles_wrapper(
            role_dtos=role_dtos, presenter=presenter, project_id=project_id
        )

        # Assert
        presenter.response_for_role_description_should_not_be_empty_exception.assert_called_once()

    def test_when_role_id_is_invalid_format_then_raise_exception(
            self, interactor, storage_mock, presenter
    ):
        # Arrange
        project_id = "FA"
        roles = [{
            "role_id": "payment_poc",
            "role_name": "payment poc",
            "description": "payment poc"
        }]
        from ib_iam.tests.factories.storage_dtos import RoleDTOFactory
        role_dtos = [
            RoleDTOFactory(
                role_id=role["role_id"], name=role["role_name"],
                description=role["description"]
            ) for role in roles
        ]
        presenter.response_for_role_id_format_is_invalid_exception.return_value = Mock()

        # Act
        interactor.add_project_roles_wrapper(
            role_dtos=role_dtos, presenter=presenter, project_id=project_id
        )

        # Assert
        presenter.response_for_role_id_format_is_invalid_exception.assert_called_once()

    def test_when_given_valid_details_then_create_roles(
            self, interactor, storage_mock, presenter
    ):
        # Arrange
        project_id = "FA"
        roles = [{
            "role_id": "PAYMENT_POC",
            "role_name": "payment poc",
            "description": "payment poc"
        }]

        from ib_iam.tests.factories.storage_dtos import RoleDTOFactory
        role_dtos = [
            RoleDTOFactory(
                role_id=role["role_id"], name=role["role_name"],
                description=role["description"]
            ) for role in roles
        ]

        # Act
        interactor.add_project_roles_wrapper(
            role_dtos=role_dtos, presenter=presenter, project_id=project_id
        )

        # Assert
        storage_mock.create_roles.assert_called_once_with(
            role_dtos=role_dtos, project_id=project_id
        )
