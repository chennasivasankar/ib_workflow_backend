class TestAddNewUserStorage:
    def test_add_new_user_create_user_object(self):
        # Arrange
        user_id = "user1"
        email = "user@email.com"
        is_admin = False
        from ib_iam.storages.storage_implementation \
            import StorageImplementation
        storage = StorageImplementation()
        # Act
        storage.add_new_user(user_id=user_id, email=email, is_admin=is_admin)

        # Assert
