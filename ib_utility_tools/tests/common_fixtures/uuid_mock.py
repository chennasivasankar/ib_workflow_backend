def prepare_uuid_mock(mocker):
    mock = mocker.patch("uuid.uuid4")
    return mock
