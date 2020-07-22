from typing import List
from ib_tasks.interactors.storage_interfaces.task_storage_interface \
    import TaskStorageInterface
from ib_tasks.interactors.dtos import GoFsWithTemplateIdDTO, \
    GoFWithOrderAndAddAnotherDTO


class AddGoFsToTaskTemplateInteractor:
    def __init__(self, task_storage: TaskStorageInterface):
        self.task_storage = task_storage

    def add_gofs_to_task_template_wrapper(
            self, gofs_with_template_id_dto: GoFsWithTemplateIdDTO):
        self.add_gofs_to_task_template(
            gofs_with_template_id_dto=gofs_with_template_id_dto
        )

    def add_gofs_to_task_template(
            self, gofs_with_template_id_dto: GoFsWithTemplateIdDTO):
        self._make_validations(
            gofs_with_template_id_dto=gofs_with_template_id_dto
        )
        template_id = gofs_with_template_id_dto.template_id
        gof_dtos = gofs_with_template_id_dto.gof_dtos

        existing_gof_ids_of_template = self.task_storage.\
            get_existing_gof_ids_of_template(template_id=template_id)
        existing_gof_ids_not_in_given_data = \
            self._get_existing_gof_ids_that_are_not_in_given_data(
                existing_gof_ids=existing_gof_ids_of_template,
                gof_dtos=gof_dtos
            )
        self._add_gofs_to_task_template_in_db(
                template_id=template_id, gof_dtos=gof_dtos,
                existing_gof_ids_of_template=existing_gof_ids_of_template
        )
        from ib_tasks.exceptions.custom_exceptions import \
            ExistingGoFsNotInGivenData
        from ib_tasks.constants.exception_messages import \
            EXISTING_GOFS_NOT_IN_GIVEN_DATA
        if existing_gof_ids_not_in_given_data:
            message = EXISTING_GOFS_NOT_IN_GIVEN_DATA.format(
                existing_gof_ids_not_in_given_data
            )
            raise ExistingGoFsNotInGivenData(message)

    def _add_gofs_to_task_template_in_db(
            self, template_id: str,
            gof_dtos: List[GoFWithOrderAndAddAnotherDTO],
            existing_gof_ids_of_template: List[str]):

        gof_dtos_to_add, gof_dtos_to_update = \
            self._filter_gof_dtos_to_create_and_update(
                gof_dtos=gof_dtos,
                existing_gof_ids_of_template=existing_gof_ids_of_template
            )

        self.task_storage.add_gofs_to_template(
            template_id=template_id, gof_dtos=gof_dtos_to_add
        )
        self.task_storage.update_gofs_to_template(
            template_id=template_id, gof_dtos=gof_dtos_to_update
        )

    def _make_validations(
            self, gofs_with_template_id_dto: GoFsWithTemplateIdDTO):
        self._make_field_values_validations(
            gofs_with_template_id_dto=gofs_with_template_id_dto
        )

        gof_ids = \
            self._get_gof_ids(gof_dtos=gofs_with_template_id_dto.gof_dtos)
        self._validate_uniqueness_in_gof_ids(gof_ids=gof_ids)

        orders_of_gofs = [
            gof_dto.order
            for gof_dto in gofs_with_template_id_dto.gof_dtos
        ]
        self._validate_uniqueness_in_orders_of_gofs(
            orders_of_gofs=orders_of_gofs
        )
        self._make_database_validations(
            gofs_with_template_id_dto=gofs_with_template_id_dto
        )

    def _make_database_validations(
            self, gofs_with_template_id_dto: GoFsWithTemplateIdDTO):
        template_id = gofs_with_template_id_dto.template_id
        is_template_exists = self.task_storage.check_is_template_exists(
            template_id=template_id
        )
        is_template_does_not_exists = not is_template_exists
        from ib_tasks.exceptions.custom_exceptions import \
            TemplateDoesNotExists
        from ib_tasks.constants.exception_messages import \
            TEMPLATE_DOES_NOT_EXISTS
        if is_template_does_not_exists:
            raise TemplateDoesNotExists(
                TEMPLATE_DOES_NOT_EXISTS.format(template_id)
            )

        given_gof_ids = \
            self._get_gof_ids(gof_dtos=gofs_with_template_id_dto.gof_dtos)
        valid_gof_ids = self.task_storage.\
            get_valid_gof_ids_in_given_gof_ids(gof_ids=given_gof_ids)

        invalid_gof_ids = [
            gof_id for gof_id in given_gof_ids if gof_id not in valid_gof_ids
        ]
        from ib_tasks.exceptions.custom_exceptions import GofsDoesNotExist
        from ib_tasks.constants.exception_messages import GOFS_DOES_NOT_EXIST
        if invalid_gof_ids:
            message = GOFS_DOES_NOT_EXIST.format(invalid_gof_ids)
            raise GofsDoesNotExist(message)

    def _make_field_values_validations(
            self, gofs_with_template_id_dto: GoFsWithTemplateIdDTO):

        template_id = gofs_with_template_id_dto.template_id
        self._validate_template_id(template_id=template_id)

        invalid_gof_ids = self._get_invalid_gof_ids(
            gof_dtos=gofs_with_template_id_dto.gof_dtos
        )
        from ib_tasks.exceptions.custom_exceptions import \
            InvalidValueForField
        from ib_tasks.constants.exception_messages import \
            INVALID_VALUE_FOR_GOF_IDS
        if invalid_gof_ids:
            raise InvalidValueForField(INVALID_VALUE_FOR_GOF_IDS)

        gof_ids_of_invalid_orders = self._get_gof_ids_of_invalid_orders(
            gof_dtos=gofs_with_template_id_dto.gof_dtos
        )
        from ib_tasks.exceptions.custom_exceptions import InvalidOrdersForGoFs
        from ib_tasks.constants.exception_messages import \
            INVALID_ORDERS_FOR_GOFS
        if gof_ids_of_invalid_orders:
            raise InvalidOrdersForGoFs(
                INVALID_ORDERS_FOR_GOFS.format(gof_ids_of_invalid_orders)
            )

    def _get_existing_gof_ids_that_are_not_in_given_data(
            self, existing_gof_ids: List[str],
            gof_dtos: List[GoFWithOrderAndAddAnotherDTO]):
        given_gof_ids = self._get_gof_ids(gof_dtos=gof_dtos)

        existing_gof_ids_not_in_given_data = [
            gof_id
            for gof_id in existing_gof_ids
            if gof_id not in given_gof_ids
        ]
        return existing_gof_ids_not_in_given_data

    @staticmethod
    def _validate_template_id(template_id: str):
        from ib_tasks.exceptions.custom_exceptions import InvalidValueForField
        from ib_tasks.constants.exception_messages import \
            INVALID_VALUE_FOR_TEMPLATE_ID

        template_id_after_strip = template_id.strip()
        is_empty_template_id = not template_id_after_strip
        if is_empty_template_id:
            raise InvalidValueForField(INVALID_VALUE_FOR_TEMPLATE_ID)

    @staticmethod
    def _get_gof_ids_of_invalid_orders(
            gof_dtos: List[GoFWithOrderAndAddAnotherDTO]) -> List[str]:
        gof_ids_of_invalid_orders = []
        for gof_dto in gof_dtos:
            is_invalid_order = gof_dto.order < -1
            if is_invalid_order:
                gof_ids_of_invalid_orders.append(
                    gof_dto.gof_id
                )
        return gof_ids_of_invalid_orders

    @staticmethod
    def _get_invalid_gof_ids(
            gof_dtos: List[GoFWithOrderAndAddAnotherDTO]) -> List[str]:
        invalid_gof_ids = []
        for gof_dto in gof_dtos:
            gof_id = gof_dto.gof_id
            gof_id_after_strip = gof_id.strip()
            is_empty_gof_id = not gof_id_after_strip
            if is_empty_gof_id:
                invalid_gof_ids.append(gof_id)
        return invalid_gof_ids

    @staticmethod
    def _get_gof_ids(gof_dtos: List[GoFWithOrderAndAddAnotherDTO]):
        gof_ids = [
            gof_dto.gof_id for gof_dto in gof_dtos
        ]
        return gof_ids

    @staticmethod
    def _filter_gof_dtos_to_create_and_update(
            gof_dtos: List[GoFWithOrderAndAddAnotherDTO],
            existing_gof_ids_of_template: List[str]):
        gof_dtos_to_create = []
        gof_dtos_to_update = []

        for gof_dto in gof_dtos:
            is_gof_already_exists = \
                gof_dto.gof_id in existing_gof_ids_of_template
            if is_gof_already_exists:
                gof_dtos_to_update.append(gof_dto)
            else:
                gof_dtos_to_create.append(gof_dto)
        return gof_dtos_to_create, gof_dtos_to_update

    @staticmethod
    def _validate_uniqueness_in_gof_ids(gof_ids: List[str]):
        from collections import Counter
        gof_ids_counter = Counter(gof_ids)

        duplicate_gof_ids = []
        for gof_id, count in gof_ids_counter.items():
            is_duplicate_gof_id = count > 1
            if is_duplicate_gof_id:
                duplicate_gof_ids.append(gof_id)

        from ib_tasks.exceptions.custom_exceptions \
            import DuplicateGoFIds
        from ib_tasks.constants.exception_messages import \
            DUPLICATE_GOF_IDS
        if duplicate_gof_ids:
            message = DUPLICATE_GOF_IDS.format(duplicate_gof_ids)
            raise DuplicateGoFIds(message)

    @staticmethod
    def _validate_uniqueness_in_orders_of_gofs(orders_of_gofs: List[int]):
        from collections import Counter
        orders_of_gofs_counter = Counter(orders_of_gofs)

        duplicate_orders_of_gofs = []
        for order_value, count in orders_of_gofs_counter.items():
            is_duplicate_order_value = count > 1
            if is_duplicate_order_value:
                duplicate_orders_of_gofs.append(order_value)

        from ib_tasks.exceptions.custom_exceptions \
            import DuplicateOrderValuesForGoFs
        from ib_tasks.constants.exception_messages import \
            DUPLICATE_ORDER_VALUES_FOR_GOFS
        if duplicate_orders_of_gofs:
            message = DUPLICATE_ORDER_VALUES_FOR_GOFS.format(
                duplicate_orders_of_gofs
            )
            raise DuplicateOrderValuesForGoFs(message)
