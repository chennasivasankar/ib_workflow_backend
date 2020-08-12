

class ServiceInterface:

    @staticmethod
    def get_search_users(offset: int, limit: int, search_query: str):
        from ib_iam.storages.elastic_storage_implementation \
            import ElasticStorageImplementation
        elastic_storage = ElasticStorageImplementation()
        from ib_iam.interactors.get_search_results_interactor \
            import GetSearchResultsInteractor
        interactor = GetSearchResultsInteractor(elastic_storage=elastic_storage)

        return interactor.search_users_results(
            offset=offset, limit=limit, search_query=search_query
        )

    @staticmethod
    def get_search_countries(offset: int, limit: int, search_query: str):
        from ib_iam.storages.elastic_storage_implementation \
            import ElasticStorageImplementation
        elastic_storage = ElasticStorageImplementation()
        from ib_iam.interactors.get_search_results_interactor \
            import GetSearchResultsInteractor
        interactor = GetSearchResultsInteractor(elastic_storage=elastic_storage)
        return interactor.search_countries_results(
            offset=offset, limit=limit, search_query=search_query
        )

    @staticmethod
    def get_search_states(offset: int, limit: int, search_query: str):
        from ib_iam.storages.elastic_storage_implementation \
            import ElasticStorageImplementation
        elastic_storage = ElasticStorageImplementation()
        from ib_iam.interactors.get_search_results_interactor \
            import GetSearchResultsInteractor
        interactor = GetSearchResultsInteractor(elastic_storage=elastic_storage)
        return interactor.search_states_results(
            offset=offset, limit=limit, search_query=search_query
        )

    @staticmethod
    def get_search_cities(offset: int, limit: int, search_query: str):
        from ib_iam.storages.elastic_storage_implementation \
            import ElasticStorageImplementation
        elastic_storage = ElasticStorageImplementation()
        from ib_iam.interactors.get_search_results_interactor \
            import GetSearchResultsInteractor
        interactor = GetSearchResultsInteractor(elastic_storage=elastic_storage)
        return interactor.search_cities_results(
            offset=offset, limit=limit, search_query=search_query
        )
