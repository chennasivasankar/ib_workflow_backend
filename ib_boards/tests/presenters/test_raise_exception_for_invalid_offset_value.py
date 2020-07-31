from ib_boards.constants.exception_messages import INVALID_OFFSET_VALUE
from ib_boards.presenters.presenter_implementation import \
    PresenterImplementation


class TestInvalidOffsetValue:

    def test_raise_exception_for_invalid_offset_value_raises_exception(self):
        # Arrange
        presenter = PresenterImplementation()
        exception_message = INVALID_OFFSET_VALUE[0]
        exception_res_status = INVALID_OFFSET_VALUE[1]

        # Act
        response_object = presenter.response_for_invalid_offset_value()

        # Assert
        import json
        response = json.loads(response_object.content)
        assert response['http_status_code'] == 400
        assert response['res_status'] == exception_res_status
        assert response['response'] == exception_message