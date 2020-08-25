from unittest.mock import create_autospec, Mock

from ib_iam.interactors.roles_interactor import RolesInteractor
from ib_iam.interactors.storage_interfaces.roles_storage_interface \
    import RolesStorageInterface
from ib_iam.interactors.presenter_interfaces.add_roles_presenter_interface \
    import AddRolesPresenterInterface


class TestAddRolesInteractor:
    def test_given_role_ids_are_duplicate_then_raise_exception(self):
        # Arrange
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
                role_id=role["role_id"],
                name=role["role_name"],
                description=role["description"]
            )
            for role in roles
        ]
        duplicate_role_ids = ['PAYMENT_POC']
        storage = create_autospec(RolesStorageInterface)
        presenter = create_autospec(AddRolesPresenterInterface)
        interactor = RolesInteractor(storage=storage)
        presenter.raise_duplicate_role_ids_exception.return_value = \
            Mock()

        # Act
        response = interactor.add_project_roles_wrapper(
            role_dtos=role_dtos, presenter=presenter
        )

        # Assert
        call_obj = presenter.raise_duplicate_role_ids_exception.call_args

        assert call_obj[0][0].role_ids == duplicate_role_ids
        presenter.raise_duplicate_role_ids_exception.assert_called_once()

    def test_given_role_name_is_empty_then_raise_exception(self):
        # Arrange
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
        storage = create_autospec(RolesStorageInterface)
        presenter = create_autospec(AddRolesPresenterInterface)
        interactor = RolesInteractor(storage=storage)
        presenter.raise_role_name_should_not_be_empty_exception.return_value = \
            Mock()

        # Act
        interactor.add_project_roles_wrapper(
            role_dtos=role_dtos, presenter=presenter)

        # Assert
        presenter.raise_role_name_should_not_be_empty_exception.assert_called_once()

    def test_given_role_description_is_empty_then_raise_exception(self):
        # Arrange
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
        storage = create_autospec(RolesStorageInterface)
        presenter = create_autospec(AddRolesPresenterInterface)
        interactor = RolesInteractor(storage=storage)
        presenter.raise_role_description_should_not_be_empty_exception.return_value = \
            Mock()

        # Act
        interactor.add_project_roles_wrapper(role_dtos=role_dtos, presenter=presenter)

        # Assert
        presenter.raise_role_description_should_not_be_empty_exception.assert_called_once()

    def test_when_role_id_is_invalid_format_then_raise_exception(self):
        # Arrange
        roles = [{
            "role_id": "payment_poc",
            "role_name": "payment poc",
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
        storage = create_autospec(RolesStorageInterface)
        presenter = create_autospec(AddRolesPresenterInterface)
        interactor = RolesInteractor(storage=storage)
        presenter.raise_role_id_format_is_invalid_exception.return_value = Mock()

        # Act
        interactor.add_project_roles_wrapper(role_dtos=role_dtos, presenter=presenter)

        # Assert
        presenter.raise_role_id_format_is_invalid_exception.assert_called_once()

    def test_when_given_valid_details_then_create_roles(self):
        # Arrange
        roles = [{
            "role_id": "PAYMENT_POC",
            "role_name": "payment poc",
            "description": "payment poc"
        }]

        from ib_iam.tests.factories.storage_dtos import RoleDTOFactory
        role_dtos = [
            RoleDTOFactory(
                role_id=role["role_id"],
                name=role["role_name"],
                description=role["description"]
            )
            for role in roles]
        storage = create_autospec(RolesStorageInterface)
        presenter = create_autospec(AddRolesPresenterInterface)
        interactor = RolesInteractor(storage=storage)

        # Act
        interactor.add_project_roles_wrapper(role_dtos=role_dtos, presenter=presenter)

        # Assert
        storage.create_roles.assert_called_once_with(role_dtos=role_dtos)
