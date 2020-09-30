"""
# TODO: fixing
"""
import factory
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from ib_boards.interactors.dtos import TaskCompleteDetailsDTO
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from ...factories.interactor_dtos import ColumnTaskIdsDTOFactory, \
    StageAssigneesDTOFactory, FieldDetailsDTOFactory


class TestCase01GetColumnTasksAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read', 'write']}}

    @pytest.fixture()
    def setup(self, mocker):
        from ib_boards.tests.factories.models import BoardFactory
        from ib_boards.tests.factories.models import ColumnFactory
        from ib_boards.tests.factories.models import ColumnPermissionFactory

        roles = "USER"
        from ib_boards.tests.common_fixtures.adapters.iam_service import \
            adapter_mock_to_get_user_role
        adapter_mock_to_get_user_role(mocker, roles)
        from ib_boards.tests.common_fixtures.adapters.task_service import \
            task_ids_mock
        ColumnTaskIdsDTOFactory.reset_sequence()
        dtos = ColumnTaskIdsDTOFactory.create_batch(10)
        task_ids_mock(mocker, dtos)

        StageAssigneesDTOFactory.reset_sequence()
        dtos = StageAssigneesDTOFactory.create_batch(3)
        from ib_boards.tests.common_fixtures.adapters.iam_service import \
            get_tasks_assignees_details_mock
        get_tasks_assignees_details_mock(mocker, dtos)
        from ib_boards.tests.common_fixtures.adapters.task_service import \
            task_details_mock
        task_details_mock(mocker, self.task_complete_details_dto())
        BoardFactory.reset_sequence()
        BoardFactory.create_batch(size=10)

        board = BoardFactory()
        ColumnFactory.reset_sequence()
        ColumnPermissionFactory.reset_sequence()
        columns = ColumnFactory.create_batch(size=4, board=board)
        ColumnPermissionFactory.create_batch(size=2, column=columns[0])
        ColumnPermissionFactory.create_batch(size=2, column=columns[1])
        ColumnPermissionFactory.create_batch(size=2, column=columns[2])
        ColumnPermissionFactory.create_batch(size=2, column=columns[3])

    @staticmethod
    def task_complete_details_dto():
        from ib_boards.tests.factories.storage_dtos import \
            TaskActionsDTOFactory
        return [
            TaskCompleteDetailsDTO(
                task_id=1,
                stage_id='STAGE_ID_1',
                stage_color="blue",
                field_dtos=FieldDetailsDTOFactory.create_batch(
                    2, field_id=factory.Iterator(
                        ['field_id_0', 'field_id_1']
                    )
                ),
                action_dtos=TaskActionsDTOFactory.create_batch(2)
            )
        ]

    @pytest.mark.django_db
    def test_case(self, snapshot, setup):
        body = {"view_type": "LIST"}
        path_params = {"column_id": "COLUMN_ID_1"}
        query_params = {'limit': 10, 'offset': 0}
        headers = {}
        response = self.make_api_call(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )
