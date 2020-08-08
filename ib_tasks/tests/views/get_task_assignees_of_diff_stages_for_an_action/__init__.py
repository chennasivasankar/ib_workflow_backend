# pylint: disable=wrong-import-position

APP_NAME = "ib_tasks"
OPERATION_NAME = "get_task_assignees_of_diff_stages_for_an_action"
REQUEST_METHOD = "get"
URL_SUFFIX = "task/{task_id}/action/{action_id}/stage_assignees/v1/"

from .test_case_01 import TestCase01GetTaskAssigneesOfDiffStagesForAnActionAPITestCase

__all__ = [
    "TestCase01GetTaskAssigneesOfDiffStagesForAnActionAPITestCase"
]
