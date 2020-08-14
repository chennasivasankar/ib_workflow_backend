from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------

    try:
        from ib_iam.views.add_members_to_levels.request_response_mocks \
            import REQUEST_BODY_JSON
        body = REQUEST_BODY_JSON
    except ImportError:
        body = {}

    test_case = {
        "path_params": {'team_id': '179fca92-d58d-49d0-b390-00436919eb6f'},
        "query_params": {},
        "header_params": {},
        "body": body,
        "securities": [{'oauth': ['write']}]
    }

    from django_swagger_utils.drf_server.utils.server_gen.mock_response \
        import mock_response
    try:
        response = ''
        status_code = 200
        if '200' in ['201']:
            from ib_iam.views.add_members_to_levels.request_response_mocks \
                import RESPONSE_200_JSON
            response = RESPONSE_200_JSON
            status_code = 200
        elif '201' in ['201']:
            from ib_iam.views.add_members_to_levels.request_response_mocks \
                import RESPONSE_201_JSON
            response = RESPONSE_201_JSON
            status_code = 201
    except ImportError:
        response = ''
        status_code = 200
    response_tuple = mock_response(
        app_name="ib_iam", test_case=test_case,
        operation_name="add_members_to_levels",
        kwargs=kwargs, default_response_body=response,
        group_name="", status_code=status_code)
    return response_tuple