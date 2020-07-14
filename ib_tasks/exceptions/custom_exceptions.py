from typing import List, Dict


class InvalidStageIdsException(Exception):
    def __init__(self, stage_ids_dict: str):
        self.stage_ids_dict = stage_ids_dict

    def __str__(self):
        return self.stage_ids_dict


class InvalidRolesException(Exception):
    def __init__(self, stage_roles_dict: str):
        self.stage_roles_dict = stage_roles_dict
