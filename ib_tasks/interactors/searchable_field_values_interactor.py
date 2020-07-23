from ib_tasks.interactors.field_dtos import SearchableFieldTypeDTO


class SearchableFieldValuesInteractor:

    def __init__(self, storage):
        self.storage = storage

    def searchable_field_values_wrapper(self):
        pass

    def searchable_field_values_based_on_query(self,searchable_field_type_dto:SearchableFieldTypeDTO):
        searchable_type=searchable_field_type_dto.searchable_type