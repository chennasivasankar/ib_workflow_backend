from typing import List


class InvalidRolesException(Exception):
    def __init__(self, stage_roles_dict: str):
        self.stage_roles_dict = stage_roles_dict

    def __str__(self):
        return self.stage_roles_dict


class InvalidReadPermissionRoles(Exception):

    def __init__(self, invalid_read_permission_roles: List[str]):
        self.read_permission_roles = invalid_read_permission_roles


class InvalidWritePermissionRoles(Exception):

    def __init__(self, invalid_write_permission_roles: List[str]):
        self.write_permission_roles = invalid_write_permission_roles


class EmptyValueForPermissions(Exception):

    def __init__(self, message: str):
        self.message = message


class InvalidStageRolesException(Exception):

    def __init__(self, invalid_roles_ids: List[str]):
        self.invalid_roles_ids = invalid_roles_ids


class InvalidRoleIdsException(Exception):
    def __init__(self, role_ids: List[str]):
        self.role_ids = role_ids
