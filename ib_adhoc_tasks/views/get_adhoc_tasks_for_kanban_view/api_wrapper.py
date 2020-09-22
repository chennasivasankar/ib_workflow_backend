from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------

    try:
        from ib_adhoc_tasks.views.get_adhoc_tasks_for_kanban_view.request_response_mocks \
            import REQUEST_BODY_JSON
        body = REQUEST_BODY_JSON
    except ImportError:
        body = {}

    test_case = {
        "path_params": {},
        "query_params": {'project_id': 'string', 'limit': 772, 'offset': 564, 'group1_limit': 10, 'group1_offset': 198, 'group2_limit': 10, 'group2_offset': 215},
        "header_params": {},
        "body": body,
        "securities": [{'oauth': ['read']}]
    }

    from django_swagger_utils.drf_server.utils.server_gen.mock_response \
        import mock_response
    try:
        response = ''
        status_code = 200
        if '200' in ['200']:
            from ib_adhoc_tasks.views.get_adhoc_tasks_for_kanban_view.request_response_mocks \
                import RESPONSE_200_JSON
            response = RESPONSE_200_JSON
            status_code = 200
        elif '201' in ['200']:
            from ib_adhoc_tasks.views.get_adhoc_tasks_for_kanban_view.request_response_mocks \
                import RESPONSE_201_JSON
            response = RESPONSE_201_JSON
            status_code = 201
    except ImportError:
        response = ''
        status_code = 200
    response_tuple = mock_response(
        app_name="ib_adhoc_tasks", test_case=test_case,
        operation_name="get_adhoc_tasks_for_kanban_view",
        kwargs=kwargs, default_response_body=response,
        group_name="", status_code=status_code)
    return response_tuple