from typing import List


class InvalidRolesException(Exception):
    def __init__(self, stage_roles_dict: str):
        self.stage_roles_dict = stage_roles_dict


class InvalidReadPermissionRoles(Exception):

    def __init__(self, invalid_read_permission_roles: List[str]):
        self.read_permission_roles = invalid_read_permission_roles


class InvalidWritePermissionRoles(Exception):

    def __init__(self, invalid_write_permission_roles: List[str]):
        self.write_permission_roles = invalid_write_permission_roles


class EmptyValueForPermissions(Exception):

    def __init__(self, message: str):
        self.message = message
