# pylint: disable=wrong-import-position

APP_NAME = "ib_tasks"
OPERATION_NAME = "update_assignees_of_diff_stages_for_a_task"
REQUEST_METHOD = "put"
URL_SUFFIX = "task/{task_id}/stage_assignees/update/v1/"

from .test_case_01 import TestCase01UpdateAssigneesOfDiffStagesForATaskAPITestCase

__all__ = [
    "TestCase01UpdateAssigneesOfDiffStagesForATaskAPITestCase"
]
