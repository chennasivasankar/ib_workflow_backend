# pylint: disable=wrong-import-position

APP_NAME = "ib_tasks"
OPERATION_NAME = "get_next_stages_random_assignees_of_a_task"
REQUEST_METHOD = "get"
URL_SUFFIX = "task/{task_id}/action/{action_id}/stage_assignees/v1/"

from .test_case_01 import TestCase01GetNextStagesRandomAssigneesOfATaskAPITestCase

__all__ = [
    "TestCase01GetNextStagesRandomAssigneesOfATaskAPITestCase"
]
